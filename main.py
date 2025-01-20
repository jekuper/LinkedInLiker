from Automation.Configuration import Configuration
from Automation.Automation import Automation
from Automation.Logger import set_step_pause
from Automation.driver import initialize_driver

import json


def main():
    config = Configuration("config/config.json")
    set_step_pause(config.manual)
    
    driver = initialize_driver()
    
    linkedin = Automation(driver, config.username, config.password, config.post_count, config.pause_time)
    linkedin.Login()
    linkedin.Interact_with_posts()
    
    driver.quit()

if __name__ == "__main__":
    main()