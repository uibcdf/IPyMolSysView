#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Diego Prada.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget
from traitlets import Unicode
from ._frontend import module_name, module_version


class Widget(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('MolSysModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('MolSysView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    value = Unicode('Hello IPyMolSysView!').tag(sync=True)
