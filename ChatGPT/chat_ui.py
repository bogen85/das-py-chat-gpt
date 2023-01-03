import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from request_manager import send_message
from response_logger import timestamp, log_response

class MainWindow(QMainWindow):
    def __init__(self, data_dir, api_key, model_id, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("OpenAI ChatGPT")

        # Chat overhead
        self.data_dir = data_dir
        self.api_key = api_key
        self.model_id = model_id
        self.chat_log = f'{data_dir}/chat.log'

        # Create widgets
        self.splitterMain = QSplitter()
        self.splitterMain.setOrientation(Qt.Orientation.Horizontal)
        self.splitterLeft = QSplitter()
        self.splitterLeft.setOrientation(Qt.Orientation.Vertical)

        self.textEdit1 = QTextEdit()
        self.textEdit2 = QTextEdit()
        self.textEdit3 = QTextEdit()

        self.textEdits = (self.textEdit1, self.textEdit2, self.textEdit3)

        self.textOutput = QTextEdit()
        self.button1 = QPushButton("Send Text 1")
        self.button2 = QPushButton("Send Text 2")
        self.button3 = QPushButton("Send Text 3")
        self.buttonOutput = QPushButton("Clear Output")


        # Set sizes
        self.textEdit1.setMinimumHeight(20)
        self.textEdit2.setMinimumHeight(200)
        self.textEdit3.setMinimumHeight(200)
        self.textOutput.setMinimumHeight(600)
        self.textOutput.setReadOnly(True)

        # Connect signals
        self.button1.clicked.connect(lambda: self.sendText(self.textEdit1))
        self.button2.clicked.connect(lambda: self.sendText(self.textEdit2))
        self.button3.clicked.connect(lambda: self.sendText(self.textEdit3))
        self.buttonOutput.clicked.connect(lambda: self.textOutput.clear())
        self.textEdit1.installEventFilter(self)
        self.textEdit2.installEventFilter(self)
        self.textEdit3.installEventFilter(self)

        # Create layouts
        layout1 = QVBoxLayout()
        layout1.addWidget(self.textEdit1)
        layout1.addWidget(self.button1)

        layout2 = QVBoxLayout()
        layout2.addWidget(self.textEdit2)
        layout2.addWidget(self.button2)

        layout3 = QVBoxLayout()
        layout3.addWidget(self.textEdit3)
        layout3.addWidget(self.button3)

        layoutRight = QVBoxLayout()
        layoutRight.addWidget(self.textOutput)
        layoutRight.addWidget(self.buttonOutput)

        widget1 = QWidget()
        widget1.setLayout(layout1)
        widget1.setMaximumHeight(128)

        widget2 = QWidget()
        widget2.setLayout(layout2)

        widget3 = QWidget()
        widget3.setLayout(layout3)

        widgetRight = QWidget()
        widgetRight.setLayout(layoutRight)

        self.splitterLeft.addWidget(widget1)
        self.splitterLeft.addWidget(widget2)
        self.splitterLeft.addWidget(widget3)

        # Add widgets to splitter
        self.splitterMain.addWidget(self.splitterLeft)
        self.splitterMain.addWidget(widgetRight)
        self.setCentralWidget(self.splitterMain)


    def appendText(self, text, which):
        timestamped = f'{timestamp()}: {which}\n{text.strip()}'
        log_response(timestamped, self.chat_log)
        self.textOutput.append(timestamped)
        self.textOutput.moveCursor(QTextCursor.MoveOperation.End)
        self.update()
        QApplication.processEvents()
        return True

    def sendText(self, object):
        message = object.toPlainText()
        self.appendText(message, 'Sent')
        response = send_message(self.model_id, self.api_key, message)
        return self.appendText(response, 'Received')

    def eventFilter(self, object, event):
        event_type=str(event.type())
        if event_type == "Type.KeyPress" and object in (self.textEdits):
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
