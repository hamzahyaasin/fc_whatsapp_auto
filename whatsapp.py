import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()

# Define the target names (list of groups)
file_path = 'C:\\Users\\Hamza Yasin\\Downloads\\what\\groups.txt'  # Replace 'your_file.txt' with your actual file path
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove newline characters from each string
group_names = [line.strip() for line in lines]
# Function to generate the message
def message():
    msg = ('''Hey fellow students! Heard about our awesome referral program? As currently enrolled student, you can earn a cool £50 internal referral bonus for each new student you refer to our company. Spread the word, bring in your friends and family, and let's build something amazing together! Don't miss out on this opportunity to earn rewards while helping our community grow.
''')
    return msg

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Wait for the user to log in manually
input("Press enter after you login.")

for name in group_names:
    # Use WebDriverWait to wait for the search box to be visible and clickable
    search_box_xpath = '//*[@id="side"]/div[1]/div/div[2]/button'
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, search_box_xpath))).click()

    # After opening search, find the input and type the name
    search_input_xpath = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, search_input_xpath))).send_keys(name + Keys.ENTER)

    # Wait a bit to ensure the group chat is opened
    time.sleep(2)

    # Wait for the message box to be visible and interactable
    message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    try:
        message_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, message_box_xpath)))
        message_box.send_keys(message())

        # Find and click the send button
        send_button_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'
        send_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, send_button_xpath)))
        send_button.click()

    except Exception as e:
        print(f"Error sending message to {name}: {e}")

    
    # Optional: Add a delay between sending messages to different groups
    time.sleep(3)

# Consider manually logging out if needed, or simply close the browser.
# Wait for a while before closing the browser
time.sleep(60)  # Adjust this timing based on your need
driver.quit()
