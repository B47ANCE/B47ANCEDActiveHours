"""Read-only standalone bundle integrity/provenance check; never uploads or installs."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile
from build_standalone_test_package import ROOT, MOD, FILES


def verify(bundle):
    manifest = json.loads((bundle/'release-manifest.json').read_text(encoding='utf-8'))
    version = (ROOT/'VERSION').read_text().strip()
    if (manifest['projectVersion'], manifest['modId'], manifest['workshopId']) != (version, MOD, '3820693462'):
        raise ValueError('Version/mod/item identity differs')
    package = manifest['package']
    if not isinstance(package, str) or Path(package).name != package or package != f'B47ANCEDActiveHours-{version}.zip':
        raise ValueError('Unexpected package filename')
    if subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',manifest['sourceCommit'],'HEAD'],
                      capture_output=True).returncode:
        raise ValueError('Unverified source ancestry')
    expected = {f'mods/{MOD}/{name}':ROOT/'src'/MOD/name for name in FILES}
    if set(manifest['files']) != set(expected):
        raise ValueError('Manifest inventory differs')
    archive = bundle/package
    if hashlib.sha256(archive.read_bytes()).hexdigest() != manifest['sha256']:
        raise ValueError('Package SHA-256 differs')
    actual = {p.relative_to(bundle/'Contents').as_posix() for p in (bundle/'Contents').rglob('*') if p.is_file()}
    if actual != set(expected) or any(p.is_symlink() for p in (bundle/'Contents').rglob('*')):
        raise ValueError('Staging inventory differs/contains links')
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        if set(names) != set(expected) or len(names) != len(set(n.casefold() for n in names)):
            raise ValueError('ZIP inventory or case collision')
        if any(n.startswith('/') or ':' in n or '\\' in n or '..' in n.split('/') for n in names) or z.testzip():
            raise ValueError('ZIP path or CRC failure')
        for name, source in expected.items():
            original = source.read_bytes()
            if z.read(name) != original or (bundle/'Contents'/name).read_bytes() != original:
                raise ValueError('Source/ZIP/staging differs: '+name)
            if hashlib.sha256(original).hexdigest() != manifest['files'][name]:
                raise ValueError('Manifest hash differs: '+name)
    info = dict(line.split('=',1) for line in expected[f'mods/{MOD}/42/mod.info'].read_text().splitlines() if '=' in line)
    if info.get('require') or info['id'] != MOD or info['modversion'] != version:
        raise ValueError('Incorrect independent metadata')
    print(f'PASS: {len(expected)} exact files; source/ZIP/stage hashes, ancestry, CRC, paths, case, version, item; runtime NOT TESTED')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle', type=Path)
    verify(parser.parse_args().bundle.resolve())
