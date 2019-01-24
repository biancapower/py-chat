### Client-server chat application built using PyQt ###
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

# counter for number of clicks
button_clicks = 0

# Create a GUI application
app = QApplication([])

# Create our root window
window = QWidget()

# Create a vertical layout and embed it in the root window
layout = QVBoxLayout()
window.setLayout(layout)

# Create a text display
label = QLabel('Hello, Cyber')

# Make it visible
# label.show()

# Create a button
button = QPushButton('Click me!')

def on_button_clicked():
    global button_clicks
    button_clicks += 1

    label.setText("Button was clicked " + str(button_clicks) + " times")

button.clicked.connect(on_button_clicked)

# Add widgets to the layout
layout.addWidget(label)
layout.addWidget(button)

window.show()

# Enter the application's main loop
# This method call doesn't end until the main window is closed
app.exec_()

print("Application was closed")

