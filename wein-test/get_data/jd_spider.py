import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import etree

from get_data.jd_db_helper import *


db = get_connection()
cursor = get_cursor(db)

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 5)
KEYWORD = '充电宝'


def get_page():
    url = 'http://www.jd.com/'
    browser.get(url)
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
    input.clear()
    input.send_keys(KEYWORD)

    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search button.button')))
    button.click()

    time.sleep(3)

    # 先滑动到底部，再向上自动滚动
    str_js = 'var scrollHeight = document.body.scrollHeight;window.scrollTo(0, scrollHeight);'
    browser.execute_script(str_js)

    for i in range(16, 0, -1):
        str_js = 'var scrollHeight = document.body.scrollHeight;window.scrollTo(0, (%d * scrollHeight) / 16);' % i
        time.sleep(2)
        browser.execute_script(str_js)

    html = browser.page_source

    return html


def parse_page(html):
    ehtml = etree.HTML(html)
    gl_items = ehtml.xpath('//div[@id="J_goodsList"]//li[@class="gl-item"]')
    count = 0
    result_list = []
    for gl_item in gl_items:
        # 获取商品信息
        img_url = 'http:' + ''.join(gl_item.xpath('.//div[@class="p-img"]/a/img/@src'))

        # 保存图片到本地
        save_img(img_url)

        title = ''.join(gl_item.xpath('.//div[@class="p-name p-name-type-2"]//em//text()'))
        price = ''.join(gl_item.xpath('.//div[@class="p-price"]/strong/i/text()'))
        detail = ''.join(gl_item.xpath('.//div[@class="p-name p-name-type-2"]/a/i/text()'))
        print(img_url)
        count += 1
        print(count)

        # 存储商品信息
        result_dict = {}
        result_dict['title'] = title
        result_dict['img_url'] = img_url
        result_dict['price'] = price
        result_dict['detail'] = detail

        result_list.append(result_dict)

    # 将商品信息存入数据库
    for item in result_list:
        insert_record(db, cursor, item)


def save_img(img_url):
    response = requests.get(img_url)
    result = response.content
    img_name = img_url.split('/')[-1]
    with open('../static/images/%s' % img_name, 'wb')as f:
        f.write(result)


def main():
    html = get_page()
    parse_page(html)


if __name__ == '__main__':
    main()
