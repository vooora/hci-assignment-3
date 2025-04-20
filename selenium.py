from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
start_time = time.time()
driver.get("https://www.amazon.in")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "field-keywords"))
)

end_time = time.time()
load_time = end_time - start_time
print(f"Page load time: {load_time:.2f} seconds\n")

#search for headphones
start_time = time.time()
text_box = driver.find_element(By.NAME, "field-keywords")
text_box.send_keys("wireless headphones")
search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

end_time = time.time()
load_time = end_time - start_time
print(f"Search time: {load_time:.2f} seconds\n")

#loading
time.sleep(3)

#select price low to high
start_time = time.time()
sort_dropdown = driver.find_element(by=By.ID, value="s-result-sort-select")
sort_select = Select(sort_dropdown)
sort_select.select_by_index(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2 span")))

end_time = time.time()
load_time = end_time - start_time
print(f"Sort low to high time: {load_time:.2f} seconds\n")

#loading
time.sleep(5)

names = driver.find_elements(By.CSS_SELECTOR, "h2 span")

product_names = [name.text.strip() for name in names if name.text.strip()]

print("Name:", product_names[2])

prices = driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")
price = f"₹{prices[3].text}"
print("Price:", price)

#select highest rated
start_time = time.time()
sort_dropdown = driver.find_element(by=By.ID, value="s-result-sort-select")
sort_select = Select(sort_dropdown)
sort_select.select_by_index(3)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2 span")))

end_time = time.time()
load_time = end_time - start_time
print(f"\nSort by customer review time: {load_time:.2f} seconds\n")

#loading
time.sleep(5)

names = driver.find_elements(By.CSS_SELECTOR, "h2 span")

product_names = [name.text.strip() for name in names if name.text.strip()]

print("Name:", product_names[2])

prices = driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")
price = f"₹{prices[3].text}"
print("Price:", price)

#add to cart
start_time = time.time()
cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@name='submit.addToCart']"))
)
cart_button.click()

end_time = time.time()
load_time = end_time - start_time
print(f"\nAdd to cart time: {load_time:.2f} seconds\n")

time.sleep(5)
