from time import sleep
from requests_html import HTMLSession
import conf_params


def crawling(category: str):
    # ページ送り
    session = HTMLSession()
    allData = []

    scraping = conf_params.scrapingfunc(category)

    for i in range(1, conf_params.maxpage()):
        # ページ繰り
        url = conf_params.geturl(category, i)
        r = session.get(url)
        endFlag, specData = scraping(r)

        if endFlag == False:
            allData.extend(specData)
            sleep(conf_params.sleepinterval())
        else:
            allData.extend(specData)
            break

    return allData
