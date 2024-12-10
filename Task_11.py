# Task_11.py
# Import necessary libraries for web automation using Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Action Chains class
from selenium.webdriver.common.action_chains import ActionChains

# Class for URL and basic data
class Data:
   url = "https://jqueryui.com/droppable/"

# Class for web-elements locator
class Locators:
    source_id = "draggable"
    target_id = "droppable"

class DragAndDrop(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Set an explicit wait to wait for elements to become interactable (up to 10 seconds)
        self.wait = WebDriverWait(self.driver, 20)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def validate_iframe(self):
        try:
            # Wait and validate the iframe presence
            iframe = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
            if iframe:
                print("Iframe is present on the page.")
                return True
            else:
                print("Iframe not found.")
                return False
        except Exception as e:
            print("Error while validating iframe:", e)
            return False

    def drag_drop(self):
        try:
            # Switch to the iframe containing the draggable and droppable elements
            iframe =  self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
            self.driver.switch_to.frame(iframe)

            # Now that we are inside the iframe, locate the elements
            source = self.wait.until(EC.visibility_of_element_located((By.ID, self.source_id)))
            target = self.wait.until(EC.visibility_of_element_located((By.ID, self.target_id)))

            # Perform the drag-and-drop action
            self.action.drag_and_drop(source, target).perform()
            target_text = target.text
            print(target_text)

            # Switch back to the main content
            self.driver.switch_to.default_content()
            return target_text

        # Return any exceptions encountered
        except Exception as error:
            print("Error during execution:",error)
            return error

    def close_driver(self):
        """Close the browser after extraction"""
        self.driver.quit()