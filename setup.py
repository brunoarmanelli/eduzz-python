#!/usr/bin/env python
from setuptools import setup
from io import open

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

setup(name='eduzz-python',
      version='0.1',
      description='Eduzz requests made easy',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      author='Bruno Armanelli',
      author_email='brunoarmanelli@me.com',
      url='https://github.com/brunoarmanelli/eduzz-python',
      packages=['eduzz'],
      keywords='eduzz',
      install_requires=['requests', 'six']
     )