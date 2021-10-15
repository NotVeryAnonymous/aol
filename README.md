## Age of Learning assessment

### To run the test:
1. Execute `source venv/bin/activate` from this directory
2. Execute `pytest`
### Notes:
1. Instead of reinventing the wheel for this assignment by making methods to interact with the elements, I used the 
library called SeleniumBase that I am actively using in my current company that does a lot of abstraction for us such as
WebDriverWaits. I still made some classes in pages/locators.py to store the selectors, and config/config.ini to store 
the configs.
Reference: https://seleniumbase.io

2. Note that this test won't actually pass right now. The elements to be located are all within multiple layers of a
shadow DOM that, while possible to traverse, looks quite cumbersome given the scope of the assignment. The elements
can't even be selected via entering an XPath/selector in the browser console because of the shadow DOM.

3. The site blocks access for being a bot after the first time running the test, this also was cumbersome and out
of the scope of this assignment to try and work around. 

4. The instructions do not have the updated URL for registration, I've used the updated URL in my config.ini

### To run the sort:
1. Execute `python sort.py`