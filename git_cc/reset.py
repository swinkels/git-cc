"""Reset hard to a specific changeset"""

from .common import *
import common

def main(commit):
    git_exec(['branch', '-f', CC_TAG, commit])
    tag(common.CI_TAG, commit)
