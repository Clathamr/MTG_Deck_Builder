import sys
from app.services.mtg_api import get_card_by_name
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MTG App")

        self.label = QLabel()

        self.button = QPushButton("Fetch Card")

        self.input = QLineEdit()

        self.button.clicked.connect(self.on_fetch_card)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def on_fetch_card(self):
        name = self.input.text()
        card = get_card_by_name(name)

        if card:
            self.label.setText(card.name)
        else:
            self.label.setText("Card not found")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
