from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time

# Setup
options = UiAutomator2Options()
options.set_capability("platformName", "Android")
options.set_capability("deviceName", "Android Device")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("appPackage", "in.amazon.mShop.android.shopping")
options.set_capability("appActivity", "com.amazon.mShop.home.HomeActivity")
options.set_capability("noReset", True)

driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(10)

#Open Amazon App: task f
start_a = time.time()
amazon_app = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("Amazon")' )
amazon_app.click()
end_a = time.time()
print(f"Amazon app opening time: {end_a - start_a:.2f}s")


start_b = time.time()

#  Search for headphones: task a
driver.find_element(AppiumBy.ID, "in.amazon.mShop.android.shopping:id/chrome_action_bar_search_icon").click()
driver.find_element(AppiumBy.ID, "in.amazon.mShop.android.shopping:id/rs_search_src_text").send_keys("wireless headphones")
driver.press_keycode(66)

time.sleep(4)
end_b = time.time()
print(f"Response time for searching for item: {end_b - start_b:.2f}s")

start_c = time.time()

# Sort from Low to High: task b
filters_btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("s-all-filters")')
filters_btn.click()

for attempt in range(5):
     driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollForward()'
            )
     attempt+1

sort_by = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Sort by")'
        )
sort_by.click()

center_x = (624 + 1004) // 2
center_y = (518 + 611) // 2
driver.tap([(center_x, center_y)], 100)

time.sleep(2)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textStartsWith("Show")').click()
time.sleep(3)

product_views = driver.find_elements(
            AppiumBy.XPATH,
            "//android.view.View[@clickable='true' and @content-desc]"
        )
title_view = product_views[4] 
title_text = title_view.get_attribute("content-desc")
print(f"Product title is: {title_text}")

all_text_elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
price_elements = []
for elem in all_text_elements:
    text = elem.text
    if "₹" in text or "$" in text:
                price_elements.append(elem)
        
if price_elements:
        print(f"Price is: {price_elements[2].text}")
end_c = time.time()
print(f"Sort low to high Response time: {end_c - start_c:.2f}s")


# Sort by Average Customer Review : task c
start_d = time.time()
filters_btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("s-all-filters")')
filters_btn.click()


for attempt in range(3):
     driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollForward()'
            )
     attempt+1

sort_by = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Sort by")'
        )
sort_by.click()

center_x = (379 + 826) // 2
center_y = (743 + 836) // 2
driver.tap([(center_x, center_y)], 100)

time.sleep(2)

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textStartsWith("Show")').click()

time.sleep(3)
product_views = driver.find_elements(
            AppiumBy.XPATH,
            "//android.view.View[@clickable='true' and @content-desc]"
        )
title_view = product_views[4]  
title_text = title_view.get_attribute("content-desc")
print(f"Product Title is: {title_text}")

all_text_elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
price_elements = []
for elem in all_text_elements:
    text = elem.text
    if "₹" in text or "$" in text:
                price_elements.append(elem)
        
if price_elements:
            print(f"Price is: {price_elements[2].text}")
end_d = time.time()
print(f"Sort avg. customer reviews response time: {end_d - start_d:.2f}s")

# Adding to cart: task d
start_e = time.time()
add_to_cart_button = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Add to cart").instance(0)'
    )
add_to_cart_button.click()
end_e = time.time()
print(f"Add to Cart Response time: {end_e - start_e:.2f}s")

driver.quit()
