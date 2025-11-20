from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QPushButton,
    QCheckBox,
    QLabel,
)
from PyQt6.QtCore import Qt, QPoint
from ai_engine import ask_dora
from actions import type_in_editor
from voice import speak


class DoraOverlay(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Dora Overlay")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.resize(400, 350)

        # For dragging
        self._drag_pos: QPoint | None = None

        # Main container with rounded corners
        container = QWidget()
        container.setObjectName("container")

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(container)

        layout = QVBoxLayout(container)

        title = QLabel("Dora - Windows Assistant")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        credit = QLabel("Design By :- Chetan Wagh")
        credit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        credit.setStyleSheet("font-size: 10px; color: #bbbbbb;")

        self.input = QTextEdit()
        self.input.setPlaceholderText(
            "Ask Dora anything… (e.g. 'Write Python code for a login screen')"
        )
        self.input.setFixedHeight(90)

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        btn_row = QHBoxLayout()
        self.ask_button = QPushButton("Ask Dora")
        self.ask_button.clicked.connect(self.on_ask_clicked)

        self.type_checkbox = QCheckBox("Auto-type in editor")
        btn_row.addWidget(self.ask_button)
        btn_row.addWidget(self.type_checkbox)

        layout.addWidget(title)
        layout.addWidget(self.input)
        layout.addLayout(btn_row)
        layout.addWidget(self.output)
        layout.addWidget(credit)

        # Styling
        self.setStyleSheet(
            """
            QWidget#container {
                background-color: rgba(20, 20, 20, 230);
                border-radius: 16px;
            }
            QLabel {
                color: white;
                font-size: 14px;
            }
            QTextEdit {
                background-color: #222;
                color: #eee;
                border-radius: 8px;
                border: 1px solid #444;
            }
            QPushButton {
                background-color: #3b82f6;
                border-radius: 8px;
                padding: 6px 12px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
            QCheckBox {
                color: #dddddd;
            }
            """
        )

    # ---------- Mouse drag to move window ----------
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self._drag_pos is not None:
            diff = event.globalPosition().toPoint() - self._drag_pos
            self.move(self.pos() + diff)
            self._drag_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self._drag_pos = None

    # ---------- Button logic ----------
    def on_ask_clicked(self):
        question = self.input.toPlainText().strip()
        if not question:
            return

        self.output.setPlainText("Thinking...")
        self.ask_button.setEnabled(False)

        answer = ask_dora(question)
        self.output.setPlainText(answer)
        self.ask_button.setEnabled(True)

        # Dora speaks the answer
        speak(answer)

        # If checkbox checked → type into editor
        if self.type_checkbox.isChecked():
            type_in_editor(answer)
