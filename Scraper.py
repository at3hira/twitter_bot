# coding:utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime,timedelta
import twitter

def get_driver():
    # chromedriverの設定
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

def news_list(driver):
    # ページOPEN
    driver.get("https://football-tribe.com/japan/news/")
    contents = {}
    # ニュース一覧ページからurlとテキストを取得
    for element in driver.find_elements_by_class_name('tribe-thumbnails-wrapper'):
        result = element.find_element_by_tag_name('a')
        url = result.get_attribute("href")
        # ニュースの配信日時を取得
        # 日付フォーマットを変換(2019.09.26. 10:59 am　形式)
        post_date = element.find_element_by_class_name('post-date').text
        post = post_date.replace("Posted on: ", "")
        post_time = datetime.strptime(post, '%Y.%m.%d. %I:%M %p')
        # 1時間前のタイムスタンプを取得
        last_date = datetime.now() + timedelta(hours=-1)

        # 直近１時間以内に配信されたニュースのみツイート
        if last_date.timestamp() < post_time.timestamp():
            twitter.tweet(url)
        else:
            continue

    return contents
driver = get_driver()
news_list(driver)
