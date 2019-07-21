import daiquiri
import logging
import click
import click_completion
from git import Repo

click_completion.init()
daiquiri.setup()
log = logging.getLogger(__name__)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--debug/--no-debug', help="debug logging", default=False)
@click.pass_context
def cli(ctx, debug):
    """A git submodules wrapper command"""
    ctx.obj = {}
    ctx.obj['repo'] = Repo()

    if debug:
        log.setLevel(logging.DEBUG)
        log.debug("Activating DEBUG logging")


@cli.command()
@click.pass_context
def list(ctx):
    """-- list submodules"""
    submodules = ["'%s' url:%s sha:%s" % (submodule.name,
                                          submodule.url,
                                          submodule.hexsha)
                  for submodule in ctx.obj['repo'].submodules]
    print("\n".join(submodules))
