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

        self.fetch_card_button = QPushButton("Fetch Card")
        self.write_to_db_button = QPushButton("Add to 'My Cards'")
        # self.sourced_card = QPushButton("Sourced Card")

        self.input = QLineEdit()

        self.fetch_card_button.clicked.connect(self.on_fetch_card)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        # layout.addWidget(self.label)
        layout.addWidget(self.fetch_card_button)
        layout.addWidget(self.write_to_db_button)
        # layout.addWidget(self.sourced_card)

        # sourced_card = QWidget()
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def on_fetch_card(self):
        name = self.input.text()
        card = get_card_by_name(name)

        if card:
            self.write_to_db_button.setText(f"Add: {card.name} to 'My Cards'")
        else:
            self.write_to_db_button.setText("Card not found")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
