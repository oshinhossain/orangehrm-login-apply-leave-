# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_experimental_option("detach", True)  # Keeps the browser open after script ends
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
# print("Login attempted. Current title:", driver.title)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Navigate to the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Wait for the login fields to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # Enter login credentials
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys("Admin")
    password_input.send_keys("admin123")

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Wait for the dashboard to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Leave']"))
    )

    # Navigate to the Apply Leave page
    leave_menu = driver.find_element(By.XPATH, "//span[text()='Leave']")
    leave_menu.click()

    apply_leave_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/web/index.php/leave/applyLeave']"))
    )
    apply_leave_option.click()

    # Wait for the Apply Leave form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Apply Leave']"))
    )

    # Select Leave Type
    leave_type_dropdown = driver.find_element(By.XPATH, "//label[text()='Leave Type']/following::div[1]")
    leave_type_dropdown.click()
    leave_type_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']//span[text()='CAN - Bereavement']"))
    )
    leave_type_option.click()

    # Enter From Date
    from_date_input = driver.find_element(By.XPATH, "//label[text()='From Date']/following::input[1]")
    from_date_input.clear()
    from_date_input.send_keys("2025-08-20")
    from_date_input.send_keys(Keys.RETURN)

    # Enter To Date
    to_date_input = driver.find_element(By.XPATH, "//label[text()='To Date']/following::input[1]")
    to_date_input.clear()
    to_date_input.send_keys("2025-08-22")
    to_date_input.send_keys(Keys.RETURN)

    # Enter Comment
    comment_input = driver.find_element(By.XPATH, "//label[text()='Comment']/following::textarea[1]")
    comment_input.send_keys("Applying for bereavement leave.")

    # Click Apply button
    apply_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    apply_button.click()

    # Wait for confirmation (e.g., a success message or redirection)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Successfully Applied')]"))
    )

    print("Leave application submitted successfully.")

finally:
    # Close the browser after a short delay
    time.sleep(5)
    driver.quit()


