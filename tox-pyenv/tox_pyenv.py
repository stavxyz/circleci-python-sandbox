
import subprocess

from tox import hookimpl


class ToxPyenvException(Exception):

    """Base class for exceptions from this plugin."""


class PyenvMissing(ToxPyenvException, RuntimeError):

    """The pyenv program is not installed."""


class PyenvWhichFailed(ToxPyenvException):

    """Calling `pyenv which` failed."""


@hookimpl
def tox_get_python_executable(envconfig):
    try:
        pipe = subprocess.Popen(
            ['pyenv', 'which', envconfig.basepython],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = pipe.communicate()
    except OSError:
        raise PyenvMissing(
            "Pyenv doesn't seem to be installed, you probably "
            "don't want this tox-pyenv plugin.")
    if pipe.poll() != 0:
        raise PyenvWhichFailed(err)
    return out.strip()
