"""Tag a particular commit as gitcc start point"""

from .common import *
import common

def main(commit):
    tag(common.CI_TAG, commit)
