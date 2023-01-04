import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from request_manager import send_message
from session_logging import timestamp, log_response, get_timestamp

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

        self.textPrimaryEdit = QTextEdit()
        self.textAlphaEdit = QTextEdit()
        self.textBetaEdit = QTextEdit()

        self.textEdits = (self.textPrimaryEdit, self.textAlphaEdit, self.textBetaEdit)

        self.textOutput = QTextEdit()
        self.buttonPrimary = QPushButton("Send Primary Text")
        self.buttonAlpha = QPushButton("Send Text A")
        self.buttonBeta = QPushButton("Send Text B")
        self.buttonOutput = QPushButton("Clear Output")


        # Set sizes
        self.textPrimaryEdit.setMinimumHeight(64)
        self.textAlphaEdit.setMinimumHeight(200)
        self.textBetaEdit.setMinimumHeight(200)
        self.textOutput.setMinimumHeight(600)
        self.textOutput.setReadOnly(True)

        # Connect signals
        self.buttonPrimary.clicked.connect(lambda: self.sendText(self.textEdit1))
        self.buttonAlpha.clicked.connect(lambda: self.sendText(self.textEdit2))
        self.buttonBeta.clicked.connect(lambda: self.sendText(self.textEdit3))
        self.buttonOutput.clicked.connect(lambda: self.textOutput.clear())

        for textEdit in (self.textPrimaryEdit, self.textAlphaEdit, self.textBetaEdit):
            textEdit.installEventFilter(self)

        # Create layouts and widgets
        layoutPrimary = QVBoxLayout()
        layoutAlpha = QVBoxLayout()
        layoutBeta = QVBoxLayout()
        layoutOutput = QVBoxLayout()

        widgetPrimary = QWidget()
        widgetAlpha = QWidget()
        widgetBeta = QWidget()
        widgetRight = QWidget()
        widgetPrimary.setMaximumHeight(128)

        for layout, text, button in (
                (layoutOutput, self.textOutput, self.buttonOutput),
                (layoutPrimary, self.textPrimaryEdit, self.buttonPrimary),
                (layoutAlpha, self.textAlphaEdit, self.buttonAlpha),
                (layoutBeta, self.textBetaEdit, self.buttonBeta)
            ):
            layout.addWidget(text)
            layout.addWidget(button)

        for widget, layout in (
                (widgetPrimary, layoutPrimary),
                (widgetAlpha, layoutAlpha),
                (widgetBeta, layoutBeta),
                (widgetRight, layoutOutput)
            ):
            widget.setLayout(layout)

        for widget in (widgetPrimary, widgetAlpha, widgetBeta):
            self.splitterLeft.addWidget(widget)

        # Add widgets to splitter
        self.splitterMain.addWidget(self.splitterLeft)
        self.splitterMain.addWidget(widgetRight)
        self.setCentralWidget(self.splitterMain)


    def log(self, text):
        log_response(text, self.chat_log)

    def appendText(self, text, which):
        this_timestamp = get_timestamp(which)
        timestamped = f'{this_timestamp}\n{text.strip()}'
        self.log(timestamped)
        self.textOutput.append(timestamped)
        self.textOutput.moveCursor(QTextCursor.MoveOperation.End)
        self.update()
        QApplication.processEvents()
        return True

    def sendText(self, object):
        message = object.toPlainText()
        self.appendText(message, 'Sent')
        response, output = send_message(self.model_id, self.api_key, message)
        completed = f'{get_timestamp("Completion")}\n{output}'
        result = self.appendText(response, 'Received')
        self.log(completed)
        return result

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
