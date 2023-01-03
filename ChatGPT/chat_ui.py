import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
# from PyQt6 import QtCore, QtGui

class MainWindow(QMainWindow):
    def __init__(self, data_dir, api_key, model_id, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("OpenAI ChatGPT")

        # Create widgets
        self.splitter = QSplitter()
        self.textEdit1 = QTextEdit()
        self.textEdit2 = QTextEdit()
        self.textOutput = QTextEdit()
        self.button1 = QPushButton("Send Text 1")
        self.button2 = QPushButton("Send Text 2")
        self.button3 = QPushButton("Clear Output")


        # Set sizes
        self.textEdit1.setMinimumHeight(200)
        self.textEdit2.setMinimumHeight(200)
        self.textOutput.setMinimumHeight(400)
        self.textOutput.setReadOnly(True)

        # Connect signals
        self.button1.clicked.connect(lambda: self.sendText(self.textEdit1))
        self.button2.clicked.connect(lambda: self.sendText(self.textEdit2))
        self.button3.clicked.connect(lambda: self.textOutput.clear())
        self.textEdit1.installEventFilter(self)
        self.textEdit2.installEventFilter(self)

        # Create layouts
        layout1 = QVBoxLayout()
        layout1.addWidget(self.textEdit1)
        layout1.addWidget(self.button1)
        layout1.addWidget(self.textEdit2)
        layout1.addWidget(self.button2)

        layout2 = QVBoxLayout()
        layout2.addWidget(self.textOutput)
        layout2.addWidget(self.button3)

        widget1 = QWidget()
        widget1.setLayout(layout1)

        widget2 = QWidget()
        widget2.setLayout(layout2)

        # Add widgets to splitter
        self.splitter.addWidget(widget1)
        self.splitter.addWidget(widget2)
        self.setCentralWidget(self.splitter)


    def appendText(self, text):
        self.textOutput.append(text)
        self.textOutput.moveCursor(QTextCursor.MoveOperation.End)
        return True

    def sendText(self, object):
        return self.appendText(object.toPlainText())

    def eventFilter(self, object, event):
        event_type=str(event.type())
        if event_type == "Type.KeyPress" and object in (self.textEdit1, self.textEdit2):
            modifier=str(event.modifiers())
            if modifier == "KeyboardModifier.ControlModifier":
                key = event.key()
                if key == Qt.Key.Key_Return:
                    return self.sendText(object)
                if key == ord('X'):
                    object.cut();
                if key == ord('C'):
                    object.copy();
                if key == ord('V'):
                    object.paste();
                return True
        return False

def main(data_dir, api_key, model_id):
    app = QApplication(sys.argv)
    window = MainWindow(data_dir, api_key, model_id)
    window.show()
    sys.exit(app.exec())
