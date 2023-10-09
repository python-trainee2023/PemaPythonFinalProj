import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.gyapu.com/")

    def teardown(self):
        time.sleep(5)  # Sleep for 5 seconds
        self.driver.quit()


class Test_login(BaseTest):
    def test_login(self):
        try:
            # Wait for the "Login/Register" button to be clickable
            login_btn_xpath = "//div[@class='my-auto pb-1']//button[contains(text(),'Login/Register')]"
            login_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, login_btn_xpath))
            )
            login_btn.click()

            time.sleep(2)

            # Find the input fields for username/email and password
            username_input_xpath = "//input[@id='username']"
            password_input_xpath = "//input[@id='Password']"
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, username_input_xpath))
            )
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, password_input_xpath))
            )

            # Enter the login credentials
            username_input.send_keys("kulchan.pema@gmail.com")
            password_input.send_keys("Pema123")

            # Find and click the login button
            login_button_xpath = "//button[contains(text(), 'Login')]"
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, login_button_xpath))
            )
            login_button.click()

            # Wait for an element on the homepage to ensure the page has loaded
            homepage_element_xpath = "//a[contains(text(), 'Categories')]"
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, homepage_element_xpath))
            )

            # Verify (check the current URL)
            homepage_url = "https://www.gyapu.com/"
            if homepage_url in self.driver.current_url:
                print("Logged in and on the homepage.")
            else:
                print("Not on the homepage after login. Current URL:", self.driver.current_url)

        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    test = Test_login()
    test.setup()
    test.test_login()
    test.teardown()
