from selenium import webdriver


TEST_URL = "https://practicetestautomation.com/practice-test-login/"
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"
SUCCESS_CONFIRMATION = "//p[@class='has-text-align-center']/strong[contains(text(), 'You successfully logged in!')]"

# Setup #
drv = webdriver.Chrome(executable_path="C:/Webdrivers/chromedriver.exe")
drv.implicitly_wait(5000)
drv.maximize_window()

# Login Page #
print('TEST: User login using valid credentials')
drv.get(TEST_URL)
drv.find_element_by_xpath("//input[@id='username']").send_keys(VALID_USERNAME)
drv.find_element_by_xpath("//input[@id='password']").send_keys(VALID_PASSWORD)
drv.find_element_by_xpath("//button[@id='submit']").click()

# Successful Logged in #
drv.implicitly_wait(5000)
msgLoginSuccess = drv.find_element_by_xpath(SUCCESS_CONFIRMATION)

if msgLoginSuccess.is_displayed():
    print('PASSED.')

else:
    print('FAILED!')

# Close Page #
drv.quit()