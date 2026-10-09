# Selenium with Python — Quick Revision Notes

## 1. Setup & Launching Browser
```python
from selenium import webdriver

driver = webdriver.Chrome()      # auto uses Selenium Manager (Selenium 4+)
driver.get("https://example.com")
driver.maximize_window()
driver.implicitly_wait(10)       # implicit wait (seconds)

driver.quit()    # closes browser + ends session
driver.close()   # closes current tab only
```

---

## 2. Locators (Finding Elements)
```python
from selenium.webdriver.common.by import By

driver.find_element(By.ID, "username")
driver.find_element(By.NAME, "email")
driver.find_element(By.CLASS_NAME, "btn-primary")
driver.find_element(By.TAG_NAME, "input")
driver.find_element(By.LINK_TEXT, "Sign Up")
driver.find_element(By.PARTIAL_LINK_TEXT, "Sign")
driver.find_element(By.CSS_SELECTOR, "#login > button")
driver.find_element(By.XPATH, "//input[@type='submit']")

# multiple elements
driver.find_elements(By.CLASS_NAME, "product-item")
```
**Priority order (fastest → slowest):** ID > NAME > CSS_SELECTOR > XPATH

id - unique
name - tied closer to id speed native broswer dom
css- selector -DOM TraversalForward/Downward only
xpath -> DOM Traversal Bidirectional (Parent \(\leftrightarrow \) Child, Ancestors, Siblings)
---

## 3. WebElement Basics
```python
elem = driver.find_element(By.ID, "username")
elem.send_keys("karthik")     # type text
elem.clear()                   # clear field
elem.click()                   # click
elem.submit()                  # submit form
elem.is_displayed()            # visible? True/False
elem.is_enabled()              # enabled? True/False
elem.is_selected()             # checkbox/radio selected?
```

---

## 4. Getting Attribute & Text
```python
elem.text                              # visible text of element
elem.get_attribute("value")            # input field value
elem.get_attribute("href")             # link URL
elem.get_attribute("class")            # class name
elem.tag_name                          # tag name e.g. 'input'
```

---

## 5. Waits (Synchronization)

### Implicit Wait
```python
driver.implicitly_wait(10)   # applies globally to all find_element calls
```

### Explicit Wait
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
elem = wait.until(EC.presence_of_element_located((By.ID, "username")))
elem = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
elem = wait.until(EC.visibility_of_element_located((By.ID, "msg")))
wait.until(EC.invisibility_of_element_located((By.ID, "loader")))
wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "Success"))
```

### Fluent Wait (custom polling)
```python
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(driver, 20, poll_frequency=2,
                      ignored_exceptions=[NoSuchElementException])
wait.until(EC.presence_of_element_located((By.ID, "username")))
```
**Rule:** Never mix implicit + explicit wait — causes inconsistent delays.

---

## 6. Dropdowns (Select Class)
```python
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("India")
dropdown.select_by_value("IN")
dropdown.select_by_index(2)
dropdown.all_selected_options
```

---

## 7. Mouse & Keyboard Interactions (Action Chains)
```python
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

actions = ActionChains(driver)
actions.move_to_element(elem).perform()         # hover
actions.click_and_hold(elem).perform()
actions.double_click(elem).perform()
actions.context_click(elem).perform()           # right click
actions.drag_and_drop(source, target).perform()

elem.send_keys(Keys.ENTER)
elem.send_keys(Keys.CONTROL, "a")               # select all
```

---

## 8. File Upload
```python
# Simple upload (input type=file) - no dialog needed
upload = driver.find_element(By.ID, "fileUpload")
upload.send_keys("/home/user/documents/sample.pdf")

# Multiple files
upload.send_keys("/path/file1.jpg\n/path/file2.jpg")
```
> For OS-level upload dialogs (non-input based), use `pyautogui` or `AutoIT` since Selenium can't control OS windows.

---

## 9. Alerts & Popups
```python
alert = driver.switch_to.alert
alert.accept()          # click OK
alert.dismiss()         # click Cancel
alert.send_keys("text") # for prompt boxes
alert.text               # read alert message
```

---

## 10. Frames & Windows
```python
# iframe
driver.switch_to.frame("frameName")     # or index / WebElement
driver.switch_to.default_content()      # back to main page

# multiple windows/tabs
main_window = driver.current_window_handle
for handle in driver.window_handles:
    driver.switch_to.window(handle)
driver.switch_to.window(main_window)
```

---

## 11. Cookies
```python
driver.get_cookies()                          # all cookies
driver.get_cookie("session_id")               # specific cookie
driver.add_cookie({"name":"key","value":"123"})
driver.delete_cookie("session_id")
driver.delete_all_cookies()
```

---

## 12. JavaScript Executor
```python
driver.execute_script("arguments[0].click();", elem)                 # JS click
driver.execute_script("arguments[0].scrollIntoView();", elem)        # scroll to elem
driver.execute_script("window.scrollBy(0,500);")                     # scroll page
driver.execute_script("document.getElementById('id').value='abc';")  # set value
value = driver.execute_script("return arguments[0].innerText;", elem) # get value
```

---

## 13. Screenshots
```python
driver.save_screenshot("page.png")             # full page screenshot
elem.screenshot("element.png")                  # single element screenshot
```

---

## 14. Exceptions in Selenium
```python
from selenium.common.exceptions import (
    NoSuchElementException,      # locator didn't match any element
    TimeoutException,            # explicit wait timed out
    ElementNotInteractableException,  # element found but not clickable/typeable
    StaleElementReferenceException,   # element no longer attached to DOM (page refreshed)
    ElementClickInterceptedException, # another element is blocking the click
    WebDriverException           # generic driver/browser level error
)

try:
    driver.find_element(By.ID, "wrong").click()
except NoSuchElementException:
    print("Element not found")
except TimeoutException:
    print("Wait timed out")
finally:
    print("Continue execution")
```

---

## 15. Handling Stale Elements (Retry Pattern)
```python
from selenium.common.exceptions import StaleElementReferenceException

def safe_click(driver, by, value):
    for _ in range(3):
        try:
            driver.find_element(by, value).click()
            break
        except StaleElementReferenceException:
            continue
```

---

## 16. Debugging Tips
```python
# 1. Print page source to check what's loaded
print(driver.page_source)

# 2. Highlight an element (visual debug)
driver.execute_script("arguments[0].style.border='3px solid red'", elem)

# 3. Check current URL / title
print(driver.current_url, driver.title)

# 4. Use browser console logs (Chrome only)
logs = driver.get_log("browser")

# 5. Add small explicit wait + screenshot on failure
try:
    elem.click()
except Exception as e:
    driver.save_screenshot("error.png")
    print("Failed:", e)

# 6. Run in non-headless mode first to visually see the issue
options = webdriver.ChromeOptions()
# options.add_argument("--headless")   # keep commented while debugging
driver = webdriver.Chrome(options=options)
```

---

## 17. Browser Options (Headless, etc.)
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
```

---

## 18. Sample Test Script (End-to-End)
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com/login")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("karthik")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "loginBtn").click()

wait.until(EC.presence_of_element_located((By.ID, "welcomeMsg")))
assert "Welcome" in driver.find_element(By.ID, "welcomeMsg").text

driver.save_screenshot("login_success.png")
driver.quit()
```

---

## 19. Pytest Integration (Bonus)
```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

def test_title(driver):
    driver.get("https://example.com")
    assert "Example" in driver.title
```
