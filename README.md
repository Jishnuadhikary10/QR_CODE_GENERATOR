# Function to generate the README file content
def generate_readme():
    readme_content = '''# QR Code Generator

This is a simple Python application that generates QR codes based on student details. It provides a graphical user interface (GUI) built using the Tkinter library.

## Features

- Generate QR codes with student details, including Student ID, Name, Department, and Stream.
- Clear the input fields and QR code display.
- Display success and error messages.

## Installation

1. Clone the repository:

   shell
   git clone https://github.com/Jishnuadhikary10/QR_CODE_GENERATOR.git
2. Change to the project directory:

    shell
    cd QR_CODE_GENERATOR

3. Install the required dependencies:
   shell
   pip install qrcode Pillow

4. Usage
    Run the application by executing the following command:
   shell
    python qr_code_generator.py

5.Dependencies
    The following packages are required to run the application:

    qrcode
    Pillow

These packages can be installed using the pip package manager. The requirements.txt file is provided with the project, which includes the necessary dependencies. You can install them by running the following command:
pip install -r requirements.txt

                                     
          
![image](https://github.com/Jishnuadhikary10/QR_CODE_GENERATOR/assets/89401869/a68e94b7-0fbe-4461-8e19-3a61bef934cf)

# The algorithm of how the code works in points:

1. `from re import I`: Imports the `I` constant from the `re` module. However, the `I` constant is not used in the code provided.

2. `from tkinter import *`: Imports all classes, functions, and variables from the `tkinter` module. This allows you to use Tkinter's GUI components and features.

3. `import qrcode`: Imports the `qrcode` module, which provides functionality for generating QR codes.

4. `from PIL import Image, ImageTk`: Imports classes `Image` and `ImageTk` from the `PIL` module. These classes are used for image processing and displaying images in Tkinter.

5. `from resizeimage import resizeimage`: Imports the `resizeimage` module, which is used to resize images.

6. `class Qr_Generator`: Defines a class named `Qr_Generator` for the QR code generator application.

7. `def __init__(self, root)`: Initializes the `Qr_Generator` class with the `root` parameter, which represents the Tkinter root window.

8. `self.root`: Stores the reference to the Tkinter root window.

9. GUI Setup:
   - Sets the window geometry, title, and prevents resizing.
   - Creates a title label at the top of the window.

10. Variables:
    - `self.var_emp_code`, `self.var_name`, `self.var_department`, `self.var_stream`: Tkinter `StringVar` variables used to store the values entered by the user in the student details section.

11. Student Details Window:
    - Creates a frame for entering student details.
    - Adds labels and entry fields for student ID, name, department, and stream.
    - Provides buttons to generate the QR code and clear the fields.
    - Displays a label for status messages.

12. Student QR Code Window:
    - Creates a frame for displaying the generated QR code.
    - Adds a label to show the "No QR Available" message initially.

13. `clear(self)`: Clears the input fields and resets the status message and QR code label.

14. `generate(self)`: Generates the QR code based on the entered student details.
    - Checks if all fields are filled. If any field is empty, it shows an error message.
    - Creates the QR code data using the entered student details.
    - Generates the QR code using the `qrcode` module.
    - Resizes the QR code image.
    - Saves the QR code image with a unique name based on the student ID.
    - Updates the QR code label with the generated image.
    - Displays a success message.

15. `root=Tk()`: Creates an instance of the Tkinter `Tk` class to create the main window.

16. `obj=Qr_Generator(root)`: Creates an instance of the `Qr_Generator` class, passing the root window as a parameter.

17. `root.mainloop()`: Starts the Tkinter event loop to handle user interactions and display the GUI.

This code creates a GUI application for generating QR codes based on student details. It uses Tkinter for the GUI components, the `qrcode` library to generate QR codes, and the `PIL` library for image processing. The code organizes the GUI elements into frames and provides functionality to generate and display QR codes based on the entered student details.
