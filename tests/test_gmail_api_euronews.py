from steps.euronews_main_page_steps import EuronewsMainPageSteps
from steps.news_letters_page_steps import NewsLettersPageSteps

euronews_steps = EuronewsMainPageSteps()
news_letters_page_steps = NewsLettersPageSteps()


def test_gmail_api_euronews(browser):
    euronews_steps.open_main_page()
    euronews_steps.click_news_letters_link()
    news_letters_page_steps.choose_random_newsletter_subscription_plan()
