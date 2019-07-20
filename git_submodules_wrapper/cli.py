import daiquiri
import logging
import click
import click_completion

click_completion.init()
daiquiri.setup()
log = logging.getLogger(__name__)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--debug/--no-debug', help="debug logging", default=False)
def cli(debug):
    """A git submodules wrapper command"""

    if debug:
        log.setLevel(logging.DEBUG)
        log.debug("Activating DEBUG logging")
