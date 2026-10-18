"""Development-only deterministic packaging. Never installs, uploads or deletes anything."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MOD = 'B47ANCEDActiveHours'
FILES = ('common/.keep', 'thumbnail.png', '42/mod.info', '42/icon.png', '42/poster.png',
         '42/media/lua/shared/B47ANCEDActiveHours.lua',
         '42/media/lua/shared/B47ANCEDActiveHours/Compatibility.lua')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    if not out.is_relative_to((ROOT / 'dist').resolve()) or out.exists():
        raise SystemExit('Output must be a fresh directory beneath repository dist; nothing overwritten.')
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    source = ROOT / 'src' / MOD
    actual = {p.relative_to(source).as_posix() for p in source.rglob('*') if p.is_file()}
    if actual != set(FILES) or any(p.is_symlink() for p in source.rglob('*')):
        raise SystemExit('Unexpected/symlinked source files; inspect before packaging.')
    metadata = dict(line.split('=', 1) for line in (source / '42/mod.info').read_text(encoding='utf-8').splitlines() if '=' in line)
    if metadata['id'] != MOD or metadata['modversion'] != version or metadata.get('require'):
        raise SystemExit('Source metadata/version mismatch')
    commit = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
    dirty = subprocess.check_output(['git', '-C', str(ROOT), 'status', '--porcelain'], text=True)
    if dirty:
        raise SystemExit('Commit intended source before generating release provenance.')
    if metadata['id'] != 'B47ANCEDActiveHours' or (ROOT/'WORKSHOP_ID.txt').read_text(encoding='utf-8').strip() != '3820693462':
        raise SystemExit('Unexpected existing item identity')
    out.mkdir(parents=True)
    records = {}
    archive = out / f'B47ANCEDActiveHours-{version}.zip'
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for relative in sorted(FILES):
            data = (source / relative).read_bytes()
            member = f'mods/{MOD}/{relative}'
            target = out / 'Contents' / member
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            info = zipfile.ZipInfo(member, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data, compresslevel=9)
            records[member] = hashlib.sha256(data).hexdigest()
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        assert len(names) == len(set(names)) == len({n.lower() for n in names}) == len(FILES)
        assert set(names) == set(records) and z.testzip() is None
        for name in names:
            assert '..' not in Path(name).parts and not name.startswith(('/', '\\'))
            assert hashlib.sha256(z.read(name)).hexdigest() == records[name]
    manifest = {'projectVersion': version, 'sourceCommit': commit, 'modId': MOD,
                'targetBuild': '42.21', 'workshopId': (ROOT / 'WORKSHOP_ID.txt').read_text(encoding='utf-8').strip(), 'itemIntent': 'authorized existing-item MP test update',
                'package': archive.name, 'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
                'files': records, 'validation': 'offline only; dedicated multiplayer NOT TESTED',
                'gates': {'G2': 'BLOCKED', 'G6': 'NOT TESTED', 'G7': 'BLOCKED / NOT TESTED', 'G8': 'BLOCKED'}}
    (out / 'release-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'output': str(out), 'files': len(FILES), 'sha256': manifest['sha256']}))


if __name__ == '__main__':
    main()
