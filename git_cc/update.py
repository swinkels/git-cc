"""Update the git repository with Clearcase manually, ignoring history"""

from __future__ import print_function

from .common import *
from . import reset
from . import sync

ARGS = {
    'subdir': 'Syncs to the given Git sub directory',
}


def main(message, subdir=None):
    setGlobalsForSubdir(subdir)
    cc_exec(['update', '.'], errors=False)
    if sync.main(subdir=subdir):
        git_exec(['add', '.'])
        git_exec(['commit', '-m', message])
        reset.main('HEAD')
    else:
        print("No files have changed, nothing to commit.")
