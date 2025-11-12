import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context()
        # Открываем новую страницу в рамках контекста
        page = context.new_page()

        # Переходим на страницу входа
        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )

        # Заполняем поле email
        email_input = page.get_by_test_id("registration-form-email-input").locator(
            "input"
        )
        email_input.fill("user.name@gmail.com")

        # Заполняем поле юзернэйм
        user_name_input = page.get_by_test_id(
            "registration-form-username-input"
        ).locator("input")
        user_name_input.fill("username")

        # Заполняем поле пароль
        password_input = page.get_by_test_id(
            "registration-form-password-input"
        ).locator("input")
        password_input.fill("password")

        # Нажимаем на кнопку Login
        login_button = page.get_by_test_id("registration-page-registration-button")
        login_button.click()

        dashboard_toolbar = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_toolbar).to_be_visible()
        expect(dashboard_toolbar).to_have_text("Dashboard")

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page = context.new_page()
        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
        )

        cources_toolbar = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(cources_toolbar).to_be_visible()
        expect(cources_toolbar).to_have_text("Courses")

        cources_empty_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(cources_empty_icon).to_be_visible()

        courses_title_text_empty = page.get_by_test_id(
            "courses-list-empty-view-title-text"
        )
        expect(courses_title_text_empty).to_be_visible()
        expect(courses_title_text_empty).to_have_text("There is no results")

        courses_list_description_text = page.get_by_test_id(
            "courses-list-empty-view-description-text"
        )
        expect(courses_list_description_text).to_be_visible()
        expect(courses_list_description_text).to_have_text(
            "Results from the load test pipeline will be displayed here"
        )
