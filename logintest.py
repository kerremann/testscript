from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

# Nextcloud credentials
username = "erikadmin"
password = "x2djnasudjnap3"

# Open Microsoft Edge
driver = webdriver.Chrome("chromedriver")

# Navigate to the login page
driver.get('http://192.168.50.226/index.php/login')
time.sleep(3)
# find username/email field and send the username itself to the input field
driver.find_element("id", "user").send_keys(username)
# find password input field and insert password as well
driver.find_element("id", "password").send_keys(password)
# click login button
driver.find_element("class", "button-vue button-vue--icon-and-text button-vue--vue-primary button-vue--wide").click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

# Pause the script and wait for the user to press the Enter key
input("Press Enter to close the browser...")

# Close the browser
driver.close()
