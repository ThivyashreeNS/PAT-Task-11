# Drag-and-Drop Automation Using Python Selenium

## Overview:
This project demonstrates a web automation task using Selenium to perform a drag-and-drop action on the jQuery UI's draggable and droppable demo page. The task is wrapped in a class that interacts with a browser to automate the drag-and-drop action and verify its successful completion. The solution is divided into methods for validating the iframe and performing the drag-and-drop operation,

## Table of Contents:
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Code Explanation](#Code-Explanation)
- [Running the test](#Running-the-test)

## Prerequisites
- Python 3.x
- Required libraries:
  - `selenium`
  - `pytest`
  - `webdriver-manager`

 ## Installation:
To successfully set up and run the Selenium Automation Testing Project, follow these steps:

1. Ensure that you have Python 3.x installed on your machine. You can download it from  [python.org](https://www.python.org/).

2. Familiarity with command-line interface (CLI) tools is recommended for executing commands.

3. Set Up a Virtual Environment (Optional but Recommended):
   - It's best practice to create a virtual environment to manage dependencies for your project:
     
     - Verify Python Virtual Environment: `Virtualenv --version`
       
     - Create Virtual Environment:  `virtualenv cd`
       
     - Activate Virtual Environment:  `Scripts\Activate`
       
     - Deactivate Virtual Environment: `Scripts\Deactivate`
       
4.  Install Required Libraries:
    - Install the necessary Python libraries using pip. The required libraries for this project include:
      - __Selenium :__ For web browser automation.
        Install Python Selenium Module: `pip install selenium`
        
      - __Pytest :__ For running test cases and managing test execution.
        `pip install pytest`
         Pytest Report: `pip install pytest-html`
        
      - __Webdriver-manager :__ To automatically manage browser drivers.
          Install WebDriver Manager Module: `pip install webdriver-manager`

## Project Structure
```python
PAT Task 11/
│
├── Task_11.py                        # Contains the main logic for automating the drag-and-drop task using Selenium.
│   ├── class Data:                   # Contains the URL of the page to automate.
│   ├── class Locators:               # Contains locators for the draggable and droppable elements.
│   └── class DragAndDrop             # Main class to automate the drag-and-drop action.
│       ├── def validate_iframe()     # Method to validate the iframe presence on the page.
│       └── def drag_drop():          # Method to perform the drag-and-drop action.
│  
├── test_DragAndDrop.py               # Contains the test cases using pytest to verify the drag-and-drop functionality.
│    ├── def test_validate_iframe()   # Test to validate the iframe presence.
│    └── def test_drag_drop()         # Test to perform the drag-and-drop and verify success.
│  
├── drag_drop.html                    # Pytest html report
└── README.md                         # This README file
```

## Code Explanation
### Task_11.py
This script contains the main logic for automating the drag-and-drop task using Selenium.

- __Data class:__ This class contains the URL of the web page to automate.

- __Locators class:__ This class contains the locators for the draggable and droppable elements.

- __DragAndDrop Class:__ Contains the logic to perform the drag-and-drop action and interact with the web page.

### Methods in `DragAndDrop` class:
- __validate_iframe():__
    - This method checks if the iframe is present on the page.

    - It waits for the iframe element and returns True if it is found, otherwise False.

- __drag_drop():__
    - Open the URL (https://jqueryui.com/droppable/), which contains draggable and droppable elements inside an iframe.

    - Switch to the iframe containing the draggable and droppable elements.

    - Perform a drag-and-drop action from the source element (draggable) to the target element (droppable).

    - Verify if the drop was successful by checking if the target element's text changes to "Dropped!".

    - Handles exceptions if anything goes wrong during the drag-and-drop action.
 
- __close_driver():__
    - Closes the browser after the operation is complete.

### test_DragAndDrop.py

- __test_validate_iframe():__

    - A test case that calls the validate_iframe() method to ensure the iframe is present.

- __test_drag_drop():__
    - Instantiate the DragAndDrop class.

    - Call the drag_drop method to perform the drag-and-drop action.

    - Validate that the target element's text is "Dropped!", which signifies that the drag-and-drop operation was successful.
   
    - Close the browser after the test is complete.
 
## Running the test:
- The project uses pytest to test the drag-and-drop functionality. To run the tests:
  
  - Make sure the project and dependencies are properly set up.

  - Run the following command to execute the test cases:
    ```
     pytest -v -s --capture=sys --html=Reports\drag_drop.html test_DragAndDrop.py
    ```







    
