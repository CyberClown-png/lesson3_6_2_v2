
def test_guest_should_see_button_add(browser):

    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//")
    browser.implicitly_wait(5)
    assert browser.find_elements_by_class_name("btn-add-to-basket") != [], "button not found"
