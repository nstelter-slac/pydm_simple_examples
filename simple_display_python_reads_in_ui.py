#!/usr/bin/env python3
from pydm import Display
from pydm.widgets import PyDMLineEdit, PyDMLabel
from qtpy.QtWidgets import QLabel
from qtpy.QtCore import QTimer


class SimpleDisplay(Display):
    def __init__(self, parent=None, args=None):
        super().__init__(parent=parent, args=args) # ui_filename="simple_display.ui"

        # find widgets in the loaded UI
        self.update_time_edit = self.findChild(PyDMLineEdit, "PyDMLineEdit")
        self.float_edit = self.findChild(PyDMLineEdit, "PyDMLineEdit_2")
        self.label_update_time = self.findChild(QLabel, "label")
        self.label_float = self.findChild(QLabel, "label_2")

        # ex: change PV channels
        # self.update_time_edit.channel = "ca://MTEST:Float2"

        # ex: change label text
        self.label_update_time.setText("New text!!")
        self.label_float.setText("Also new text!!")

        # add label to display processed result
        self.processed_label = QLabel(self)
        self.processed_label.setGeometry(20, 80, 200, 20)
        self.processed_label.setText("processed val: n/a")
        self.processed_label.show()

        # set up timer to process the value continuously
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.process_input)
        self.timer.start(200) # ms

    def process_input(self):
        """
        read val from PyDMLineEdit and do some processing.
        for example: scale by 2 and square.
        """
        try:
            val = float(self.float_edit.text())
            doubled = val * 2
            squared = val ** 2
            self.processed_label.setText(f"doubled: {doubled:.2f}, squared: {squared:.2f}")
        except ValueError:
            # handle non-numeric input
            self.processed_label.setText("processed Value: n/a")

    def ui_filename(self):
        return "simple_display.ui"
