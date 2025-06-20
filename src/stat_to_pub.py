import pathlib as pl
from decorators import type_check

PUBLIC = "/home/ldv/workspace/github.com/lawrence-de-varga/ssgen/public/"
STATIC = "/home/ldv/workspace/github.com/lawrence-de-varga/ssgen/static/"


public = pl.Path(PUBLIC)
static = pl.Path(STATIC)

if not public.exists():
    raise ValueError(f"Error: '{public}' path does not exist.")

if not static.exists():
    raise ValueError(f"Error: '{static}' path does not exist.")

@type_check(pl.Path)
def delete_all_files(directory):
    
