from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the absolute path to chromedriver
chromedriver_path = os.path.join(current_dir, "chromedriver")

# Start browser with ChromeDriver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open local file
    driver.get("http://localhost:8000/index.html")

    # Find task input field and add button
    task_input = driver.find_element(By.ID, "taskInput")
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Task']")

    # Add new task
    task_input.send_keys("Buy groceries")
    add_button.click()

    # Wait for the task to be added
    wait = WebDriverWait(driver, 5)
    task_list = wait.until(EC.presence_of_element_located((By.ID, "taskList")))

    # Check whether the task was added by retrieving the task list elements
    tasks = task_list.find_elements(By.TAG_NAME, "li")
    assert any("Buy groceries" in task.text for task in tasks), "Task was not added!"

    # Print success message
    print("Test Success: Task was added successfully!")
    screenshot_success_path = os.path.join(current_dir, "test_success.png")
    driver.save_screenshot(screenshot_success_path)  # Save screenshot

except Exception as e:
    print("Test Failed:", str(e))
    screenshot_failure_path = os.path.join(current_dir, "test_failure.png")
    driver.save_screenshot(screenshot_failure_path)  # Save screenshot

finally:
    time.sleep(2)  # Wait a few seconds
    driver.quit()  # Close browser
