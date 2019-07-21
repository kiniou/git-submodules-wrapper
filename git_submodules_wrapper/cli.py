"""cli - Console Line Interface to git-submodules-wrapper module """
import logging
import daiquiri
import click
import click_completion
from git import Repo

click_completion.init()
daiquiri.setup()
log = logging.getLogger(__name__)

context_settings = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=context_settings)
@click.option('-d', '--debug/--no-debug', help="debug logging", default=False)
@click.pass_context
def cli(ctx, debug):
    """A git submodules wrapper command"""
    ctx.obj = {}
    ctx.obj['repo'] = Repo()

    if debug:
        log.setLevel(logging.DEBUG)
        log.debug("Activating DEBUG logging")


@cli.command("list")
@click.pass_context
def list_submodules(ctx):
    """-- list submodules"""
    submodules = ["'%s' url:%s sha:%s" % (submodule.name,
                                          submodule.url,
                                          submodule.hexsha)
                  for submodule in ctx.obj['repo'].submodules]
    print("\n".join(submodules))
