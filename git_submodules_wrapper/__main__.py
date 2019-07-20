from .cli import cli
from . import __appname__

if __name__ == '__main__':
    cli.main(prog_name=__appname__)  # pylint: disable=no-value-for-parameter
