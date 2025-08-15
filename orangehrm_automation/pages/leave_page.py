# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# def apply_leave(driver, leave_type="CAN - Bereavement", from_date="2025-08-20", to_date="2025-08-22", comment="Automated leave"):
#     driver.find_element(By.XPATH, "//span[text()='Leave']").click()
#     WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'applyLeave')]"))
#     ).click()
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//h6[text()='Apply Leave']"))
#     )
#
#     # Select leave type
#     driver.find_element(By.XPATH, "//label[text()='Leave Type']/following::div[1]").click()
#     WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[text()='{leave_type}']"))
#     ).click()
#
#     # Set dates
#     from_input = driver.find_element(By.XPATH, "//label[text()='From Date']/following::input[1]")
#     to_input = driver.find_element(By.XPATH, "//label[text()='To Date']/following::input[1]")
#     from_input.clear()
#     from_input.send_keys(from_date)
#     to_input.clear()
#     to_input.send_keys(to_date)
#
#     # Add comment and submit
#     driver.find_element(By.XPATH, "//label[text()='Comment']/following::textarea[1]").send_keys(comment)
#     driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Successfully') or contains(text(),'Applied')]"))
#     )
#     print("Leave applied successfully.")
