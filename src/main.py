import sys

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from src.utils import check_user_in_group


class LoginThread(QThread):
    success = Signal(str)
    fail = Signal(str)

    def __init__(self, parent, userid):
        super().__init__(parent)
        self.userid = userid

    def run(self):
        # Example usage
        if check_user_in_group(self.userid):
            self.success.emit("✅ User is in the group!")
        else:
            self.success.emit("❌ User is NOT in the group.")

class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login use Telegram")
        self.resize(300, 100)

        layout = QVBoxLayout()

        self.userid_label = QLabel("userid:")
        self.userid_input = QLineEdit()
        layout.addWidget(self.userid_label)
        layout.addWidget(self.userid_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def handle_login(self):
        userid = self.userid_input.text()
        print(userid)

        thread = LoginThread(self, userid)
        thread.success.connect(lambda val: QMessageBox.information(self, '', val))
        thread.fail.connect(lambda val: QMessageBox.warning(self, '', val))
        thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec())
