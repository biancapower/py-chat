from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSpacerItem
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QPalette


# NAMING CONVENTION we will use for PyQt widgets
# txt_ is a multi line text box
# inp_ is an input box
# btn_ is a button
# lbl_ is a label





class ChatUI():
    """This class encapsulates out application"""
    # constructor
    def __init__(self):

        # counter for number of clicks
        self.button_clicks = 0

        # Create a GUI application
        app = QApplication([])

        # Style app
        app.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.red)
        app.setPalette(palette)

        # Create our root window
        window = QMainWindow()

        self.create_connection_pane()
        self.create_chat_pane()

        # Initially display the connection pane
        window.setCentralWidget(self.connection_pane)

        # Everything has been set up, create the window
        window.show()

        # Store the things we will need later in attributes
        self.app = app
        self.window = window

    def run(self):
        # Enter the application's main loop
        # This method call doesn't end until the main window is closed
        self.app.exec_()

        print("Application was closed")

    def create_connection_pane(self):
        # Create the pane that allows the user to initiate a connection
        connection_pane = QWidget()

        # Create a layout for the connection pane
        connection_layout = QVBoxLayout()
        connection_pane.setLayout(connection_layout)

        # for the user to type an IP address and connect to it
        lbl_connect_address = QLabel('IP address')
        inp_connect_address = QLineEdit()

        btn_connect = QPushButton('Connect')
        btn_connect.clicked.connect(self.btn_connect_clicked)

        # for the user to listen for an incoming connection
        btn_listen = QPushButton('Wait for connection')
        btn_listen.clicked.connect(self.btn_listen_clicked)


        # Add all these widgets to the connection pane layout
        connection_layout.addWidget(lbl_connect_address)
        connection_layout.addWidget(inp_connect_address)
        connection_layout.addWidget(btn_connect)

        # Create space between the client options and server options
        connection_layout.addSpacing(30)

        connection_layout.addWidget(btn_listen)

        self.connection_layout = connection_layout
        self.connection_pane = connection_pane

    def create_chat_pane(self):
        # Create the pane that allows the user to chat
        chat_pane = QWidget()

        # Create a layout for the chat pane
        chat_layout = QVBoxLayout()

        # Create the chat history box
        txt_history = QTextEdit()
        txt_history.setPlainText('')
        txt_history.setReadOnly(True)

        # Create a text display
        lbl_message = QLabel('Type your message:')

        # Create an input box
        inp_message = QLineEdit()

        inp_message.returnPressed.connect(self.send)


        # Add widgets to the chat pane layout
        chat_layout.addWidget(txt_history)

        chat_layout.addWidget(lbl_message)
        chat_layout.addWidget(inp_message)

        chat_pane.setLayout(chat_layout)


        self.inp_message = inp_message
        self.txt_history = txt_history


        self.chat_layout = chat_layout
        self.chat_pane = chat_pane



    def btn_connect_clicked(self):
        pass

    def btn_listen_clicked(self):
        # Currently when listen button is clicked, show the chat pane
        self.window.setCentralWidget(self.chat_pane)



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
