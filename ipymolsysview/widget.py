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
from molsysmt import __version__ as __molsysmt_version__

class Widget(DOMWidget):

    _model_name = Unicode('MolSysModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('MolSysView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    #_molsysmt_version = Unicode(__molsysmt_version__).tag(sync=True)
    #n_atoms = Int(0).tag(sync=True)

    def __init__(self, molecular_system, selection='all', structure_indices='all', syntax='MolSysMT'):

        self.molecular_system = molecular_system
        self.selection = selection
        self.syntax = syntax
        self.atom_indices = None
        self.structure_indices = structure_indices
        self.coordinates = None

        from molsysmt import get, select

        self.atom_indices = select(self.molecular_system, selection=self.selection,
                syntax=self.syntax)

        self.coordinates = get(self.molecular_system, selection=self.atom_indices,
                structure_indices=self.structure_indices, coordinates=True)

        self.n_atoms = len(self.atom_indices)



