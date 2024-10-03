from pages.login_page import LoginPage

def test_facebook_login(browser):
    login_page = LoginPage(browser)

    # Load the login page
    login_page.load()

    # Enter login credentials
    login_page.enter_email("email")
    login_page.enter_password("password")

    # Click the login button
    login_page.click_login()

    # Verify the login by checking the page title
    assert "Facebook" in browser.title
