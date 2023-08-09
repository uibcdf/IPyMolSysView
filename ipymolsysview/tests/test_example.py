#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Diego Prada.
# Distributed under the terms of the Modified BSD License.

import pytest

from ..widget import MolSysWidget


def test_example_creation_blank():
    w = MolSysWidget()
    assert w.value == 'Hello World'
