# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:43:17 2017

@author: dashton
"""

import yaml

# %% The yaml header part


def write_yaml_header(x):
    yaml_lines = yaml.safe_dump(x, default_flow_style=False)
    header_lines = ["---\n", yaml_lines, "---\n"]

    return header_lines

# %% Combine


def write_yamlmd(yamlmd, fname):
    """Doug docstrings!"""
    header_lines = write_yaml_header(yamlmd[0])

    output = header_lines + yamlmd[1]
    with open(fname, 'w') as f:
        f.writelines(output)
