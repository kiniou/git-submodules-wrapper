""" git-submodules-wrapper - extends 'git submodule' command """
# pylint: disable=unused-import
from . import (
    cli,
)
__appname__ = "git-sm"
__version__ = "0.0.0"


def main():
    """main module entrypoint"""
    return cli.cli.main(prog_name=__appname__)
