from time import sleep
from types import NoneType
from requests_html import HTMLSession

SLEEPINTERVAL = 3


def getInfoData(r):
    # 40個の行を解析。Noneが帰ってきたら終了
    specData = []
    endFlag = False

    for i in range(40):
        # Noneかどうか壁撃ち
        processorName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]', first=True)

        # print(r.html.xpath(
        #     f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text)

        if processorName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProcessorName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]/text()[1]', first=True),
                "ReleaseDate": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[8]', first=True).text,
                "Frequency": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[10]', first=True).text,
                "Socket": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[11]', first=True).text,
                "Price": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[2]/ul/li[1]/a', first=True).text,
                "CPUCores": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[12]', first=True).text.replace("コア", ""),
                "CPUThreads": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[13]', first=True).text,
            })

        else:
            endFlag = True
            break

    return endFlag, specData


def crawling():
    # ページ送り
    session = HTMLSession()
    allData = []

    for i in range(1, 10):
        url = f"https://kakaku.com/pc/cpu/itemlist.aspx?pdf_so=d2&pdf_pg={i}"
        r = session.get(url)
        endFlag, specData = getInfoData(r)

        if endFlag == False:
            allData.extend(specData)
            sleep(SLEEPINTERVAL)
        else:
            allData.extend(specData)
            break

    return allData


allData = crawling()
print(allData)
