""" git-submodules-wrapper - extends 'git submodule' command """
# pylint: disable=unused-import
from .cli import cli
from . import (
    upstream,
)
__appname__ = "git-sm"
__version__ = "0.0.0"
