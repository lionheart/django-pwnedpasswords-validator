#!/usr/bin/env/python
# -*- coding: utf-8 -*-

# Copyright 2018 Lionheart Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from distutils.cmd import Command
import os
import re
import unittest
import runpy

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

metadata_filename = "django_pwnedpasswords_validator/metadata.py"
metadata = runpy.run_path(metadata_filename)

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as file:
    long_description = file.read()

    id_regex = re.compile(r"<\#([\w-]+)>")
    link_regex = re.compile(r"<(\w+)>")
    link_alternate_regex = re.compile(r"   :target: (\w+)")

    long_description = id_regex.sub(r"<https://github.com/lionheart/django-pwnedpasswords-validator#\1>", long_description)
    long_description = link_regex.sub(r"<https://github.com/lionheart/django-pwnedpasswords-validator/blob/master/\1>", long_description)
    long_description = link_regex.sub(r"<https://github.com/lionheart/django-pwnedpasswords-validator/blob/master/\1>", long_description)
    long_description = link_alternate_regex.sub(r"   :target: https://github.com/lionheart/django-pwnedpasswords-validator/blob/master/\1", long_description)

    long_description = long_description.replace("`__", "`_")

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
]

setup(
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    classifiers=classifiers,
    description="A Django app that validates user passwords against the Pwned Passwords v2 API.",
    install_requires=["pwnedpasswords"],
    keywords="passwords security",
    license=metadata['__license__'],
    long_description=long_description,
    name='django-pwnedpasswords-validator',
    package_data={'': ['LICENSE', 'README.rst']},
    packages=['django_pwnedpasswords_validator'],
    url="https://github.com/lionheart/django-pwnedpasswords-validator/tarball",
    download_url="https://github.com/lionheart/django-pwnedpasswords-validator/tarball/{}".format(metadata['__version__']),
    version=metadata['__version__'],
)
