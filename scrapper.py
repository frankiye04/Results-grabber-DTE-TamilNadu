from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import os

driver_path = "C:/chromedriver/chromedriver.exe" #Keep Your Chrome Driver here (Chrome Driver version must be same as the Chrome Browser).

results_dir = r"" #Directory to Save your Results.

if not os.path.exists(results_dir):
    os.makedirs(results_dir)

chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1920,1080")

service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://dte.tn.gov.in/diploma-results") #Paste your Results Website here.

start_number = 00000000 #Register Numbers Starting From.
end_number = 00000000 #Register Numbers Ending.
numbers = range(start_number, end_number + 1)

for number in numbers:
    try:
        register_number_input = driver.find_element(By.XPATH, '//*[@id="register_number"]') #This is the XPATH for Register number field (you can change this by lookuing up on your website)
        register_number_input.clear()
        register_number_input.send_keys(str(number))
        submit_button = driver.find_element(By.XPATH, '//*[@id="submitbtn"]') #This is the XPATH for Submit Button (you can change this by lookuing up on your website)
        actions = ActionChains(driver)
        actions.move_to_element(submit_button).click().perform()
        time.sleep(0.5)
        screenshot_path = os.path.join(results_dir, f"{number}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Result saved as image: {screenshot_path}")

    except Exception as e:
        print(f"Error processing {number}: {e}")
driver.quit()
