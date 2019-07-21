# git-submodules-wrapper

[![Build Status](https://dev.azure.com/kiniou/kiniou/_apis/build/status/kiniou.git-submodules-wrapper?branchName=master)](https://dev.azure.com/kiniou/kiniou/_build/latest?definitionId=2&branchName=master)
[![WTFPL License](https://img.shields.io/github/license/kiniou/git-submodules-wrapper.svg?style=flat&color=337&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAOCAYAAADNGCeJAAAACXBIWXMAAAsTAAALEwEAmpwYAAACHUlEQVQ4jY2TsUtbYRTFf9971SE0TiqtLqWlpCDt1ERxKVleIVYX/4QOTh0d/Asc2ymlpZ0EQdeAGcKLJrSIOpin4BAc2sUtICgmxHpPB33pK9HSA5cLl+8e7v3OPY5+PAbeAE+BLhAB34BXwHPgHtAESsDPW/oBSANfgEtAibBEJOtdoAikYgJ3k+8DIZD1PM8FQUA2m6XT6VCpVGg0GuRyOfL5PAMDA2xvb1OtVpGkm6lfA+2Y9BOgsbEx7ezsyMwUw8x0cHDQV6vVahoZGYmnfB8TPQIufd/X7u6uzEwLCwsqFAoql8tKYm1tTYVCQYuLizIzbW5uyjknoAM8AHgHaHZ2Vmam4+Pj3r9EUaRSqaTl5WWFYagwDAXI9321Wi2ZmfL5fPz+rQc8A5iensY5x9HREQCe55HJZFhfX2dpaYmNjQ0mJiYAuLq6otls4pxjamoq3jDj3SWtcw7nHN1uF6CX/wHXW3Nubk5mppOTEw0ODgrQ/Py80um0AI2OjmpmZkaAhoaGdHZ21rfmXwLs7e3JzFQsFnuE4+PjWllZ0fDwsAClUimtrq5Kkra2tpICPIxH/Bw3xoq2Wi1FUaSLiwsdHh7q/PxcjUZDp6enMjPV6/XkaXzo7cn10VaBl77vuyAIyOVytNttKpUK+/v7TE5O9h2tmQn4DgQkjhau7fQV+MX/2ekS+MgtdkriCXcb/QXg88foP5KNvwEfDF4ZJ9xGOQAAAABJRU5ErkJggg==)](http://www.wtfpl.net/)

Just a small wrapper CLI that extends `git submodule`.

## Prerequisites

- Python 3.7+
- Git

## Installing

Directly from this repository:
```shell
$ pip3 install git+https://github.com/kiniou/git-submodules-wrapper
```

## Running the tests

Install `tox`:
```shell
$ pip install tox
```

Then run the full test suite:
```shell
$ tox
```

## Build With

* [GitPython](https://github.com/gitpython-developers/GitPython)
* [click](https://click.palletsprojects.com)
* [daiquiri](https://github.com/jd/daiquiri)
