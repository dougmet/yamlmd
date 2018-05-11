# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:54:09 2017

@author: dashton
"""

from yamlmd import write_yamlmd
import ruamel.yaml
from ruamel.yaml import YAML
import os
import pytest

base_path = os.path.dirname(os.path.realpath(__file__))

# %% write test


def test_write(tmpdir):
    """Check that the main write function works"""
    test_header = ruamel.yaml.comments.CommentedMap({"a": 1})
    test_md = ["\n", "the first thing\n"]

    tmp_file = tmpdir.mkdir("md").join("test.md").strpath

    write_yamlmd([test_header, test_md], tmp_file)

    with open(tmp_file) as f:
        tmp_lines = f.readlines()

    assert tmp_lines[0] == "---\n"
    assert len(tmp_lines) == 5


# %% Header only


def test_write_header(tmpdir):
    """Check you can write just the yaml"""
    test_header = ruamel.yaml.comments.CommentedMap({"a": 1})
    test_md = ["\n", "the first thing\n"]
    test_yamlmd = [test_header, test_md]

    tmp_file = tmpdir.mkdir("md").join("test.yml").strpath

    write_yaml(test_yamlmd, tmp_file)

    yaml = YAML(typ='rt')
    with open(tmp_file, encoding="UTF-8") as f:
        meta = next(yaml.load_all(f))

    assert 'a' in meta
    assert meta['a'] == 1

# %% md only


def test_write_md(tmpdir):
    """Check you can write just the yaml"""
    test_header = ruamel.yaml.comments.CommentedMap({"a": 1})
    test_md = ["\n", "the first thing\n"]
    test_yamlmd = [test_header, test_md]

    tmp_file = tmpdir.mkdir("md").join("test.yml").strpath

    write_md(test_yamlmd, tmp_file)

    with open(tmp_file) as f:
        tmp_lines = f.readlines()

    assert tmp_lines[0] == "\n"
    assert len(tmp_lines) == 2
