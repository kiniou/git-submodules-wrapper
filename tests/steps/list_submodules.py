# pylint: skip-file
from behave import given, when, then, step
import git
from subprocess import run, PIPE
import shlex
import logging
from pprint import pformat
from pathlib import Path
import re
from environment import cd

log = logging.getLogger(__name__)
sha_re = re.compile("\b[0-9a-f]{5,40}\b")


@given('a git repository "{repo_name}"')
def step_impl(context, repo_name):
    repo = git.Repo.init(repo_name)
    commit = repo.index.commit('Initial commit for "{}"'.format(repo_name))
    context.sha[repo_name] = str(commit)
    log.info("created %s with commit %s", repo_name, commit)
    repo.close()


@given('"{submod_name}" is a submodule of "{repo_name}"')
def step_impl(context, submod_name, repo_name):
    repo = git.Repo(repo_name)
    submod_repo = str(git.Repo(submod_name).commit(rev="HEAD"))
    log.info("get submod repository HEAD: %s", submod_repo)
    assert git.Repo.re_hexsha_only.match(submod_repo) is not None, \
        "%s sha : %s" % (submod_name, submod_repo)
    with cd(repo_name):
        submod = repo.create_submodule(name=submod_name,
                                       path=submod_name,
                                       url="../%s" % submod_name)
    repo_sha = context.sha[submod_name]
    submod_sha = str(submod.hexsha)
    assert repo_sha == submod_sha, \
        "%s != %s" % (repo_sha, submod_sha)


@when('I execute "{command}" in "{repo_name}" repository')
def step_impl(context, command, repo_name):
    result = run(shlex.split(command), stdout=PIPE, stderr=PIPE, cwd=repo_name)
    context.command_stdout[command] = {
        'stdout': result.stdout.decode().splitlines(),
        'stderr': result.stderr.decode().splitlines()
    }
    log.info(
        "command '%s' output:\nstdout:%s\nstderr:%s",
        command,
        "\n".join(context.command_stdout[command]['stdout']),
        "\n".join(context.command_stdout[command]['stderr']),
    )
    assert result.returncode == 0, \
        "execution of '{}' returned code={}".format(result.returncode, command)


@then('the submodule "{submod}" must be found in the "{command}" {pipe}')
def step_impl(context, submod, command, pipe):
    submod_sha = context.sha[submod]
    expected_line = context.text.format(submod_sha=submod_sha)
    pipe = context.command_stdout[command][pipe]
    log.info("submod_sha: %s", submod_sha)
    log.info("expected_line: %s", expected_line)
    log.info("pipe: %s", pipe)
    assert expected_line in pipe, \
        "\n%s not found in %r" % (expected_line, pipe)
