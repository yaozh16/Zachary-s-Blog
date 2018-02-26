# 2018-2-26 selenium&Python Element Locating
### universal:find_element(s)
```
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
``` 
By 可选有
* ID = "id"
* XPATH = "xpath"
* LINK_TEXT = "link text"
* PARTIAL_LINK_TEXT = "partial link text"
* NAME = "name"
* TAG_NAME = "tag name"
* CLASS_NAME = "class name"
* CSS_SELECTOR = "css selector"


### preset API
#### return first-found
* find_element_by_id
* find_element_by_name
* find_element_by_xpath
* find_element_by_link_text
* find_element_by_partial_link_text
* find_element_by_tag_name
* find_element_by_class_name
* find_element_by_css_selector
#### return a list
* find_elements_by_name
* find_elements_by_xpath
* find_elements_by_link_text
* find_elements_by_partial_link_text
* find_elements_by_tag_name
* find_elements_by_class_name
* find_elements_by_css_selector
### Xpath
//标识任意位置
