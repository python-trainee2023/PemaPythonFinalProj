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
        # time.sleep(5)  # Sleep for 5 seconds
        self.driver.quit()


class Testlogin(BaseTest):
    def test_login(self):
        try:
            wait = WebDriverWait(self.driver, 30) #configure the wait time here. no need to set it everytime
        # Wait for the "Login/Register" button to be clickable
            login_btn_xpath = "//div[@class='my-auto pb-1']//button[contains(text(),'Login/Register')]"
            login_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, login_btn_xpath))
            )
            login_btn.click()


            # Find the input fields for username/email and password
            username_input_xpath = "//input[@id='username']"
            password_input_xpath = "//input[@id='Password']"
            username_input = wait.until(
                EC.presence_of_element_located((By.XPATH, username_input_xpath))
            )
            password_input = wait.until(
                EC.presence_of_element_located((By.XPATH, password_input_xpath))
            )

            # Enter the login credentials
            username_input.send_keys("kulchan.pema@gmail.com")
            password_input.send_keys("Pema123")
            # time.sleep(10)

            # Find and click the login button
            # login_button_xpath = "//button[contains(text(), 'Login')]" #xpath format needs changing. used the correct xpath in the lines below
            login=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))) #you can remove the login= and just apply a wait here

            # login = self.driver.find_element_by_xpath("//button[text()='Login']") #better to use this while looking for an element to be interacted with
            login.click()

            # Wait for an element on the homepage to ensure the page has loaded
            # homepage_element_xpath = "//a[contains(text(), 'Categories')]" #this xpath not found
            homepage_element_xpath='//div[@class="categories container mx-auto"]' #waits until the bar with the categories is visible
            wait.until(
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
    test = Testlogin()
    test.setup()
    test.test_login()
    test.teardown()
