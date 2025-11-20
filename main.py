import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class DoraWindow(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Dora - Windows Assistant")
        self.resize(500, 300)

        layout = QVBoxLayout()
        title = QLabel("Dora - Windows Assistant (Starter Project)")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        credit = QLabel("Design By :- Chetan Wagh")
        credit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(credit)

        self.setLayout(layout)

if _name_ == "_main_":
    app = QApplication(sys.argv)
    win = DoraWindow()
    win.show()
    sys.exit(app.exec())
