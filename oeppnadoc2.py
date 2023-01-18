from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
pycurlimport 

def finns_fil(url):
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopts(c.NOBODY, 1)
    c.perform()
    status_code = c.getinfo(c.REPSONSE_CODE)
    c.close

    if status code == 200:
        return True
    else:
        return False



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


WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

driver.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[2]').click()

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

driver.find_element_by_xpath('//*[@id="app-content-files"]/div[1]/div[2]/a').click()

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

driver.find_element_by_xpath('//*[@id="app-content-files"]/table/tbody/tr[3]').click()


fil_url = "https://samarbeta-qa.sgit.se/index.php/apps/files/?dir=/&fileid=14463"

if finns_fil(fil_url):
    print ("Filen finns")
else:
    print ("Filen finns inte")

input("Press Enter to close the browser...")

driver.close()
