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
file_path = 'C:\\Users\\Hamza Yasin\\Downloads\\what\\sample.txt'  # Replace 'your_file.txt' with your actual file path
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove newline characters from each string
group_names = [line.strip() for line in lines]
# Function to generate the message
def message():
    msg = ("Dear Student,"+"\n\nHope you are doing well."+"\n\nWe hope your learning is going well, if you would like to schedule a session, please let us know. If you would like assistance in any other area, please feel free to get in touch with us."+ "\n\nWe're available for you from Monday to Saturday 10:00 am - 5:00 pm. Our trainer's support has also been extended for Sunday 9 am to 5 pm, Due to limited Slots you have to book a session on Saturday before 5pm."
+"\n\nBest Regards"+'\nFuture Connect Training & Recruitment Ltd.')
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
    time.sleep(7)

# Consider manually logging out if needed, or simply close the browser.
# Wait for a while before closing the browser
time.sleep(60)  # Adjust this timing based on your need
driver.quit()
