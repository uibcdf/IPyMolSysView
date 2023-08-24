// Copyright (c) Diego Prada
// Distributed under the terms of the Modified BSD License.

import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import { MODULE_NAME, MODULE_VERSION } from './version';

// Import the CSS
import '../css/widget.css';

export class MolSysModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: MolSysModel.model_name,
      _model_module: MolSysModel.model_module,
      _model_module_version: MolSysModel.model_module_version,
      _view_name: MolSysModel.view_name,
      _view_module: MolSysModel.view_module,
      _view_module_version: MolSysModel.view_module_version,
      _molsysmt_version: 'x.x.x',
    };
  }

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
    // Add any extra serializers here
  };

  static model_name = 'MolSysModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'MolSysView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class MolSysView extends DOMWidgetView {
  render() {
    this.el.classList.add('custom-widget');

    // before display

    //this.molsysmt_version_changed();
    //this.model.on('change:_molsysmt_version', this.molsysmt_version_changed, this);

  }

  molsysmt_version_changed() {
    this.el.textContent = this.model.get('_molsysmt_version');
  }
}
