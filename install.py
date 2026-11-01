"""Install the Mayday-themed pets for Codex."""

import argparse
import json
import os
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
NAMES = ("ashin", "masa", "monster", "stone", "ming")
FILES = ("pet.json", "spritesheet.webp")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--codex-home", type=Path,
        default=Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")),
        help="Codex data directory (default: CODEX_HOME or ~/.codex)",
    )
    destination = parser.parse_args().codex_home.expanduser() / "pets"

    # Preflight every file before writing; preserve existing customized packs.
    for name in NAMES:
        source = ROOT / "pets" / f"mayday-{name}"
        manifest = json.loads((source / "pet.json").read_text(encoding="utf-8"))
        if manifest["id"] != source.name:
            raise SystemExit(f"Unexpected pet id in {source / 'pet.json'}")
        for filename in FILES:
            data = (source / filename).read_bytes()
            target = destination / source.name / filename
            if target.exists() and target.read_bytes() != data:
                raise SystemExit(f"Refusing to overwrite existing, different file: {target}")

    for name in NAMES:
        source = ROOT / "pets" / f"mayday-{name}"
        target = destination / source.name
        target.mkdir(parents=True, exist_ok=True)
        for filename in FILES:
            shutil.copy2(source / filename, target / filename)
        print(f"Installed {name}: {target}")


if __name__ == "__main__":
    main()
