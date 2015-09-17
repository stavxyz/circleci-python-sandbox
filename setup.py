#!/usr/bin/env python

import os
from setuptools import setup, find_packages


INSTALL_REQUIRES = [
    'requests',
]


TESTS_REQUIRE = [
    'nosetests>=1.3.7',
]

package_attributes = {
    'author': 'Sam Stavionha',
    'author_email': 'smlstvnh@gmail.com',
    
    'name': 'circleci_sandbox',
    'description': 'See what circleci will do.',
    'install_requires': INSTALL_REQUIRES,
    'py_modules': ['hi'],
    'scripts': ['hi.py', 'test_hi.py'],
    'tests_require': TESTS_REQUIRE,
    'url': 'https://github.com/samstav/circleci-sandbox',
    'version': '1.0.0',
}


setup(**package_attributes)
