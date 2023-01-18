from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(command_executor='http://sadburanextc0.sfa.se:4444/wd/hub', DesiredCapabilities.EDGE())

username = "admintest"
password = "Majsmajs123!"

driver.get('https://samarbeta-qa.sgit.se/index.php/login?redirect_url=&direct=1')
#driver.get_screenshot_as_file('test.png')

driver.find_element("id", "user").send_keys(username)
driver.find_element("id", "password").send_keys(password)
driver.find_element_by_xpath('//*[@id="body-login"]/div[1]/div/main/div/div/div[1]/div/form/fieldset/button').click()

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."

errors = driver.find_elements("css selector", ".flash-error")

if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

input("Press Enter to close the browser...")

driver.close()
