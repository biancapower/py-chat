### Client-server chat application built using PyQt ###
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

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

# Add widgets to the layout
layout.addWidget(label)
layout.addWidget(button)

window.show()

# Enter the application's main loop
# This method call doesn't end until the main window is closed
app.exec_()

print("Application was closed")

