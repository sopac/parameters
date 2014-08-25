# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'parameters'
__filename = 'numeric_parameter_widget'
__date__ = '8/21/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from PyQt4.QtGui import QLabel, QSizePolicy,QWidget, QComboBox
from PyQt4.QtCore import Qt

from qt_widgets.generic_parameter_widget import GenericParameterWidget


class NumericParameterWidget(GenericParameterWidget):
    """Widget class for Numeric parameter."""
    def __init__(self, parameter, parent=None):
        """Constructor

        .. versionadded:: 2.2

        :param parameter: A NumericParameter object.
        :type parameter: NumericParameter

        """
        super(NumericParameterWidget, self).__init__(parameter, parent)

        self._input = QWidget()

        self._unit_widget = QLabel()
        self.set_unit()

        # Size policy
        self._spin_box_size_policy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed)

        label_policy = QSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Fixed)
        self._unit_widget.setSizePolicy(label_policy)

    def get_parameter(self):
        """Obtain boolean parameter object from the current widget state.

        :returns: A BooleanParameter from the current state of widget

        """
        self._parameter.value = self._input.value()
        return self._parameter

    def set_unit(self):
        """Set up label or combo box for unit."""
        if len(self._parameter.allowed_units) == 1:
            self._unit_widget = QLabel(self._parameter.unit.name)
            self._unit_widget.setToolTip(self._parameter.unit.help_text)
        elif len(self._parameter.allowed_units) > 1:
            self._unit_widget = QComboBox()
            index = -1
            current_index = -1
            for allowed_unit in self._parameter.allowed_units:
                name = allowed_unit.name
                tooltip = allowed_unit.help_text
                index += 1
                if allowed_unit.guid == self._parameter.unit.guid:
                    current_index = index
                self._unit_widget.addItem(name)
                self._unit_widget.setItemData(index, tooltip, Qt.ToolTipRole)
            self._unit_widget.setCurrentIndex(current_index)
            self._unit_widget.setToolTip('Select your preferred unit')
