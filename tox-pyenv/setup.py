

from setuptools import setup

if __name__ == "__main__":
    setup(
        name='tox-pyenv',
        description=('Prefer `pyenv which` for '
                     'finding the python executable'),
        license="MIT license",
        version='0.1',
        py_modules=['tox_pyenv'],
        entry_points={'tox': ['pyenv = tox_pyenv']},
        install_requires=['tox>=2.0'],
    )
