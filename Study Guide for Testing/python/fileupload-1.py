from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#river=webdriver.chrome()
#driver.get
#upload=driver.(By.ID,"fileInput")
#upload.send_keys("/home/dev078/Pictures/Screenshots")


try:
    driver=webdriver.Chrome()
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    driver.get("https://practice.expandtesting.com/upload")
    #title=driver.title
    title=driver.title
    
    if title=='Files Upload page for Automation Testing Practice':
        upload=wait.until(EC.presence_of_element_located((By.ID,'fileInput')))
        upload.send_keys("/home/dev078/Pictures/Screenshots/Screenshot from 2026-09-10 15-07-04.png")
        click_button = wait.until(EC.element_to_be_clickable((By.ID, "fileSubmit")))

        click_button.click()
        
        text_message=wait.until(EC.visibility_of_element_located((By.ID,"uploaded-files")))
        print(text_message.text)
    else:
        print("page is not opening")

    
    #text_message=EC.presence_of_all_elements_located(driver.find_element(By.ID,"uploaded-files"))
    
    #print(text_message.text)

except Exception as E:
    print(E)
    raise