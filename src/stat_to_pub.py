from decorators import type_check
from pathlib import Path

PUBLIC = "/home/ldv/workspace/github.com/lawrence-de-varga/ssgen/public/"
STATIC = "/home/ldv/workspace/github.com/lawrence-de-varga/ssgen/static/"


public = Path(PUBLIC)
static = Path(STATIC)

if not public.exists():
    raise ValueError(f"Error: '{public}' path does not exist.")

if not static.exists():
    raise ValueError(f"Error: '{static}' path does not exist.")


@type_check(pl.Path)
def delete_all_files(directory: Path):
    if not directory.exists():
        raise ValueError(f"Error: '{directory}' does not exist.")
    if not directory.is_dir():
        raise ValueError(f"Error: '{directory}' is not a directory.")

    items = directory.iter
