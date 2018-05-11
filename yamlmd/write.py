# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:43:17 2017

@author: dashton
"""

from ruamel.yaml import YAML
import io

# %% The yaml header part


def write_yaml_header(x):
    """Write yaml part of the header to a string"""
    # Need a string as a file to write to
    strio = io.StringIO()
    # Set the yaml object for pretty printing
    yaml = YAML(typ='rt')
    yaml.default_flow_style = False
    # Write out
    yaml.dump(x, strio)
    yaml_lines = strio.getvalue()
    strio.close()

    header_lines = ["---\n", yaml_lines, "---\n"]

    return yaml_lines

# %% Combine


def write_yamlmd(yamlmd, fname):
    """Combine head and content and write to a markdown file"""
    yaml_lines = write_yaml_header(yamlmd[0])

    output = ["---\n", yaml_lines, "---\n"] + yamlmd[1]
    with open(fname, 'w', encoding='UTF-8') as f:
        f.writelines(output)

# %% One on its own
        
def write_yaml(yamlmd, fname):
    """Only write the yaml component to a file"""
    output = write_yaml_header(yamlmd[0])

    with open(fname, 'w', encoding='UTF-8') as f:
        f.writelines(output)
        
def write_md(yamlmd, fname):
    """Only write the content component to a file"""
    output = yamlmd[1]
    
    with open(fname, 'w', encoding='UTF-8') as f:
        f.writelines(output)

    
    