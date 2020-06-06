#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
	name='git_backup',
	packages=find_packages(),
	entry_points={'console_scripts': ['git-backup = git_backup.backup:main']}
)