# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:30:57 2017

@author: dashton
"""
# %% Imports

import yaml

# %% Yaml header


def read_yaml_header(fname):
    """Do the docstring"""
    with open(fname, encoding="UTF-8") as stream:
        meta = next(yaml.safe_load_all(stream))
    return meta

# %% Markdown


def read_markdown(fname):
    """Do the docstring"""
    with open(fname) as f:
        content = f.readlines()
    yaml_delim = [i for i, x in enumerate(content) if x.startswith("---")]
    assert len(yaml_delim) > 1

    start_line = yaml_delim[1]+1

    return content[start_line:]

# %% Read everything


def read_yamlmd(fname):
    """Doug do the docstring"""
    return (read_yaml_header(fname), read_markdown(fname))
