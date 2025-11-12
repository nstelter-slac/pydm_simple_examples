import sys
from pydm import Display
# import Qt widgets from qtpy (instead of the Qt Python wrapper directly),
# this should let ur code run on PyQt5 and Pyside6.
from qtpy.QtWidgets import QVBoxLayout, QLabel
from pydm.widgets import PyDMLabel, PyDMLineEdit


class SimpleDisplay(Display): # must subclass pydm's `Display`
    def __init__(self, parent=None, args=None):
        super().__init__(parent=parent, args=args, ui_filename=None)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("pv read:"))

        pv = "ca://MTEST:Float"

        pv_label = PyDMLabel()
        pv_label.channel = pv
        layout.addWidget(pv_label)

        layout.addWidget(QLabel("pv write:"))
        pv_edit = PyDMLineEdit()
        pv_edit.channel = pv
        layout.addWidget(pv_edit)
