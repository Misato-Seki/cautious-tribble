from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import os
import platform

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# 実行環境を確認
system_platform = platform.system()

# macOS用かUbuntu用のchromedriverを選択
if system_platform == "Darwin":  # macOS
    chromedriver_path = os.path.join(os.path.dirname(__file__), "chromedriver_mac")
elif system_platform == "Linux":  # Ubuntu (Linux)
    chromedriver_path = os.path.join(os.path.dirname(__file__), "chromedriver_ubuntu")
else:
    raise Exception("Unsupported platform")

# WebDriverのサービスを作成
service = Service(executable_path=chromedriver_path)

# Chromeドライバーを起動
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
