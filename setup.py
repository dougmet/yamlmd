# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='yamlmd',
      version='0.1.1',
      description='Read and write to Markdown files with yaml headers',
      url='https://github.com/dougmet/yamlmd',
      author='Doug Ashton',
      author_email='dashton@mango-solutions.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      zip_safe=False,
      install_requires=['pyyaml>3'])
