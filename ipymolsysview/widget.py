#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Diego Prada.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget
from traitlets import Unicode
from traittypes import Empty, Array
from ._frontend import module_name, module_version

from molsysmt import __version__ as __molsysmt_version__

class Widget(DOMWidget):

    _model_name = Unicode('MolSysModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('MolSysView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    _molsysmt_version = Unicode(__molsysmt_version__).tag(sync=True)

    coordinates = Array(default_value=Empty, dtype=float).tag(sync=True)

    def __init__(self, molecular_system, selection='all', structure_indices='all', syntax='MolSysMT'):

        super(Widget, self).__init__()

        from molsysmt.basic import get

        self.molecular_system = molecular_system
        self.selection = selection
        self.syntax = syntax
        self.structure_indices = structure_indices

        self.n_atoms = get(self.molecular_system, element='atom', selection=selection,
                syntax=syntax, n_atoms=True)

        coordinates = get(self.molecular_system, element='atom', selection=selection,
                syntax=syntax, coordinates=True)

        self.coordinates = Array(puw.get_value(coordinates))

