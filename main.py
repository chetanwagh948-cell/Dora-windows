import sys
from PyQt6.QtWidgets import QApplication
from overlay import DoraOverlay


def main():
    app = QApplication(sys.argv)
    window = DoraOverlay()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
