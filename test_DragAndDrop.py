"""test_DragAndDrop.py"""

import pytest
from Task_11 import DragAndDrop

# Initialize the DragAndDrop instance
def test_validate_iframe():
    obj = DragAndDrop()
    # Validate if the iframe is present
    iframe_valid = obj.validate_iframe()
    assert iframe_valid, "Iframe validation failed."

# Validate if the source element is now inside the target element
# The target element should have the "dropped" text after the drag-and-drop operation
def test_drag_drop():
    # Initialize the DragAndDrop instance
    obj = DragAndDrop()
    target_text = obj.drag_drop()
    assert target_text == "Dropped!", f"Expected 'Dropped!' but got {target_text}"
    obj.close_driver()