from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

class ChatUI():
    """This class encapsulates out application"""
    # constructor
    def __init__(self):

        # counter for number of clicks
        self.button_clicks = 0

        # Create a GUI application
        app = QApplication([])

        # Create our root window
        window = QWidget()

        # Create a vertical layout and embed it in the root window
        layout = QVBoxLayout()
        window.setLayout(layout)

        # Create a text display
        label = QLabel('Hello, Cyber')

        # Create a button
        button = QPushButton('Click me!')

        
        button.clicked.connect(self.button_clicked)

        # Add widgets to the layout
        layout.addWidget(label)
        layout.addWidget(button)

        window.show()

        self.app = app
        self.window = window
        self.layout = layout
        self.label = label
        self.button = button

    def run(self):
        # Enter the application's main loop
        # This method call doesn't end until the main window is closed
        self.app.exec_()

        print("Application was closed")

    def button_clicked(self):
        self.button_clicks += 1

        # alternative: label.setText(f"Button was clicked {button_clicks} times")
        self.label.setText("Button was clicked " + str(self.button_clicks) + " times")
