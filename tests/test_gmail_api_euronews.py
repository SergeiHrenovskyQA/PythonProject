from steps.euronews_steps import EuronewsSteps


def test_gmail_api_euronews(browser):
    EuronewsSteps().open_main_page()
