# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:54:09 2017

@author: dashton
"""

from yamlmd import read_yamlmd
import os
import pytest

base_path = os.path.dirname(os.path.realpath(__file__))


def test_read():
    """Check that the main read function works"""
    lorum_file = os.path.join(base_path, "data", "lorum.md")
    lorum = read_yamlmd(lorum_file)
    data_types = [type(x) for x in lorum]
    expect(
        (len(lorum) == 2, "Returned tuple must be length 2"),
        (data_types[0] == "dict", "First element must be dict"),
        (data_types[1] == "list", "Second element must be list")
    )

    report_failures(error=False, display=True, clear=clear)
