import pytest
from playwright.sync_api import sync_playwright, expect
import allure

@allure.title("Forgot Password - Invalid Username")
def test_forgotpassword_invalid_username():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://canvas-preuat.muzaini.com/login")
        page.wait_for_timeout(5000)

        page.get_by_text("Forgot Password?").click()
        page.wait_for_timeout(5000)

        page.get_by_placeholder("Enter CIVIL ID Number").fill("301103030789")
        page.wait_for_timeout(5000)

        page.get_by_placeholder("Enter Username").fill("france200")
        page.wait_for_timeout(5000)

        page.get_by_role("button", name="Confirm").first.click()
        page.wait_for_timeout(5000)

        expect(page.get_by_text("Invalid username")).to_be_visible()
        page.wait_for_timeout(5000)

        browser.close()
