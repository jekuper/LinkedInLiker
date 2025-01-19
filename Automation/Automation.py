import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Automation.LLMCommunicator import LLMCommunicator
from Automation.Logger import log_info, log_error , get_logger, log_warning


AVAILABLE_REACTIONS = [
    {
        "label": "React Like",
        "reaction": "Like"
    },
    {
        "label": "React Celebrate",
        "reaction": "Celebrate"
    },
    {
        "label": "React Support",
        "reaction": "Support"
    },
    {
        "label": "React Love",
        "reaction": "Love"
    },
    {
        "label": "React Insightful",
        "reaction": "Insightful"
    },
    {
        "label": "React Funny",
        "reaction": "Funny"
    },
]


class Automation:
    def __init__(self, driver, email, password, post_count):
        self.communicator = LLMCommunicator()
        self.email = email
        self.password = password
        self.driver = driver
        self.post_count = post_count

    def Login(self):
        """Log in to LinkedIn."""
        self.driver.get("https://www.linkedin.com/login")
        log_info("Opened LinkedIn Login Page")

        email_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        remember_me = self.driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/label')

        remember_me.click()

        email_field.send_keys(self.email)
        password_field.send_keys(self.password)

        log_info("Entered email and password")

        password_field.send_keys(Keys.RETURN)
        log_info("Logged in to LinkedIn")
        input("Pass Capctcha")

    def Interact_with_posts(self):
        for i in range(1, self.post_count + 1):
            self.Process_post(i)

    def Process_post(self, post_number):
        try:
            # Locate the post using a dynamic XPath based on post_number
            post_xpath = f"//h2[contains(text(), 'Feed post number {post_number}')]/.."
            
            # Wait for the element to be visible
            post_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, post_xpath))
            )

            post_element = post_element.find_element(By.XPATH, "./following-sibling::*")

            log_info(f"Located post #{post_number}")

            # Locate children of the post element
            children = post_element.find_elements(By.XPATH, "./*")

            # Check if the post has exactly 5 children
            if len(children) != 5:
                log_error("Error: The post does not have exactly 5 children.")
                return
            
            log_info(f"All 5 parts of the post found.")

            # Select the second child and call it text_item
            text_item = children[1]

            # Search for a span with text "...more" within text_item
            more_span = text_item.find_element(By.XPATH, ".//span[text()='…more']")

            if more_span:
                log_info("'More' button found on this post. Pressing...")
                # Navigate up one level to get the parent button
                button = more_span.find_element(By.XPATH, "./..")

                # Press the button
                button.click()
                time.sleep(1)

            # Scroll the text_item into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", text_item)

            # Wait for 30 seconds + random time between 0 and 20 seconds
            wait_time = 30 + random.randint(0, 20)

            log_info(f"Post scrolled into view. Now waiting for {wait_time}")
            time.sleep(wait_time)

            # Get and print the innerText of the text_item
            inner_text = text_item.get_attribute("innerText")
            print(inner_text)            

            buttons = []
            for reaction in AVAILABLE_REACTIONS:
                label = reaction["label"]
                try:
                    button = post_element.find_element(By.XPATH, f".//button[@aria-label='{label}']")
                    buttons.append(button)
                except Exception:
                    log_error(f"Button with aria-label '{label}' not found.")
                    return

            if len(buttons) != 6:
                log_error(f"Not all required buttons were found. Found {len(buttons)}")
                return

            selected_button = self.communicator.Get_reaction(inner_text, AVAILABLE_REACTIONS)

            self.driver.execute_script("arguments[0].click();", selected_button)

            log_info(f"Successfully clicked on button: {selected_button.get_attribute('aria-label')}")


        except Exception as e:
            log_error(f"Error locating or parsing post number {post_number}: {e}")
            return