import pytest
from playwright.sync_api import  expect, Page


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):

    chromium_page_with_state.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    cources_toolbar = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(cources_toolbar).to_be_visible()
    expect(cources_toolbar).to_have_text("Courses")

    cources_empty_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(cources_empty_icon).to_be_visible()

    courses_title_text_empty = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-title-text"
    )
    expect(courses_title_text_empty).to_be_visible()
    expect(courses_title_text_empty).to_have_text("There is no results")

    courses_list_description_text = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-description-text"
    )
    expect(courses_list_description_text).to_be_visible()
    expect(courses_list_description_text).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )
