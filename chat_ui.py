from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QPalette

class ChatUI():
    """This class encapsulates out application"""
    # constructor
    def __init__(self):

        # counter for number of clicks
        self.button_clicks = 0


        initial_history = """Welcome to Hackchat

Batman: Hi there
You: What's up?
Batman: Crime"""

        # Create a GUI application
        app = QApplication([])

        # Style app
        app.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.red)
        app.setPalette(palette)

        # Create our root window
        window = QWidget()

        # Create a vertical layout and embed it in the root window
        layout = QVBoxLayout()
        window.setLayout(layout)

        



        # NAMING CONVETION
        # txt_ is a multi line text box
        # inp_ is an input box
        # btn_ is a button
        # lbl_ is a label

        txt_history = QTextEdit()
        txt_history.setPlainText(initial_history)
        txt_history.setReadOnly(True)

        # Create a text display
        lbl_message = QLabel('Type your message:')

        # Create an input box
        inp_message = QLineEdit()

        inp_message.returnPressed.connect(self.send)
        

        # Create a button
        #button = QPushButton('Click me!')
        #button.clicked.connect(self.button_clicked)

        # Add widgets to the layout
        #layout.addWidget(button)
        layout.addWidget(txt_history)

        layout.addWidget(lbl_message)
        layout.addWidget(inp_message)


        window.show()

        self.app = app
        self.window = window
        self.layout = layout
        self.inp_message = inp_message
        self.txt_history = txt_history
        #self.button = button

    def run(self):
        # Enter the application's main loop
        # This method call doesn't end until the main window is closed
        self.app.exec_()

        print("Application was closed")

    def send(self):
        user_typed = self.inp_message.text()

        # add "You: " and put it in display window
        display = "You: " + user_typed
        self.txt_history.append(display)

        # make the input box blank again
        self.inp_message.setText(None)

    def button_clicked(self):
        self.button_clicks += 1

        # alternative: label.setText(f"Button was clicked {button_clicks} times")
        self.label.setText("Button was clicked " + str(self.button_clicks) + " times")
