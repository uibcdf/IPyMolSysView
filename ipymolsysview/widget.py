#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Diego Prada.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipymolsysview import pyunitwizard as puw
from ipywidgets import DOMWidget
from traitlets import Unicode, Int
from ._frontend import module_name, module_version

class Widget(DOMWidget):

    _model_name = Unicode('MolSysModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('MolSysView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    n_atoms = Int(0).tag(sync=True)

    def __init__(self, molecular_system, selection='all', structure_indices='all', syntax='MolSysMT'):

        .self.molecular_system = molecular_system
        .self.selection = selection
        .self.syntax = syntax
        .self.structure_indices = structure_indices

        from molsysmt import get

        coordinates = get(self.molecular_system, selection=self.selection,
                structure_indices=self.structure_indices, syntax=self.syntax)

        coordinates_value = puw.get_value(coordinates, standard=True)
        coordinates_value = coordinates_value[0]

        
