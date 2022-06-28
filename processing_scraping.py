import conf_params
from requests_html import HTMLSession


def crawlingDetails(urls: list):
    # 詳細ページを一括取得
    session = HTMLSession()

    allRes = []
    for url in urls:
        r = session.get(url)
        # sleep(conf_params.sleepinterval())
        allRes.append(r)
    return allRes


def getInfoData_CPU(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "ProcessorName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]/text()[1]', first=True),
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
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            # print(specData)
        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_CPUCOOLER(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "IntelSocket": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]', first=True).text,
                "AMDSocket": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[10]', first=True).text,
                "Type": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[11]', first=True).text,
                "Price": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[2]/ul/li[1]/a', first=True).text,
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            # print(specData)
        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_GPU(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            # specData.append({
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "Interface": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]/text()[1]', first=True),
                "Chip": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[10]', first=True).text,
                "GMemory": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[11]', first=True).text,
                "Price": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[2]/ul/li[1]/a', first=True).text,
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            # print(specData)

        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_HDD(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "Size": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]/text()[1]', first=True),
                "RPM": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[11]', first=True).text,
                "Price": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[2]/ul/li[1]/a', first=True).text,
                "Interface": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[13]', first=True).text,
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            # print(specData)

        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_MOTHERBOARD(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "FormFactor": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]/span/a/text()', first=True),
                "Socket": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[10]', first=True).text,
                "Chipset": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[11]', first=True).text,
                "Price": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[2]/ul/li[1]/a', first=True).text,
                "RAMType": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[12]', first=True).text,
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            # print(specData)
        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_RAM(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "Size1piece": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]/text()[1]', first=True),
                "Pieces": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[10]', first=True).text,
                "Type": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[11]', first=True).text,
                "Price": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[2]/ul/li[1]/a', first=True).text,
                "Interface": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[12]', first=True).text,
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            # print(specData)

        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_SSD_M2(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "Size": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]', first=True).text.replace("GB", ""),
                "Price": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[2]/ul/li[1]/a', first=True).text,
                "Interface": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[13]/span/a', first=True).text,
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            # print(specData)

        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_SSD_SATA(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "Size": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]', first=True).text.replace("GB", ""),
                "Price": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[2]/ul/li[1]/a', first=True).text,
                "Interface": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[13]/span/a', first=True).text,
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            # print(specData)

        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_POWERSUPPLY(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "Capacity": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]', first=True).text.replace("W", ""),
                "Price": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[2]/ul/li[1]/a', first=True).text,
                "Revisions": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[10]', first=True).text,
                "RankOf80plus": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 6}]/td/div/span[3]/a/text()', first=True) or "NoData",
                "Plugin": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 6}]/td/div/span[5]/a/text()', first=True) or "",
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            # print(specData)

        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_CASE(r):

    specData = []
    endFlag = False

    for i in range(conf_params.onepage()):
        # Noneかどうか壁撃ち
        productName = r.html.xpath(
            f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]', first=True)

        if productName != None:
            specData.append({
                "Brand": r.html.xpath(
                    f'// *[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]/table/tr/td[1]/a/span', first=True).text,
                "ProductName": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 4}]/td[2]/table/tr/td[1]/a/text()[1]', first=True),
                "FormFactor": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[9]/text()', first=False),
                "Link": list(r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{i * 3 + 4}]/td[2]', first=True).absolute_links)[0],
                "Img": r.html.xpath(
                    f'//*[@id="compTblList"]/tbody/tr[{ i * 3 + 5}]/td[1]/a/img', first=True).attrs['src'],
            })
            print(specData)
        else:
            endFlag = True
            break

    return endFlag, specData


def getInfoData_OS(r):
    items = r.html.find('.ckitanker', first=False)
    print(len(items))

    specData = []

    # 終了フラグ確認
    if(len(items) != conf_params.onepage()):
        endFlag = True
    else:
        endFlag = False

    # URL配列取得
    specURLs = []
    for i in range(len(items)):
        specURLs.append(list(items[i].absolute_links)[0])

    allcontents = crawlingDetails(specURLs)

    for content in allcontents:
        specData.append({
            "Brand": content.html.xpath(
                f'//*[@id="relateList"]/li[1]/a/text()', first=True) or "",
            "Series": content.html.xpath(
                f'//*[@id="relateList"]/li[2]/a/text()', first=True) or "",
            "ProductName": content.html.xpath(
                f'//*[@id="titleBox"]/div[1]/h2/text()', first=True) or "",
            "Link": content.html.base_url,
            "Price": content.html.xpath(
                f'//*[@id="priceBox"]/div[1]/div/p/span/text()', first=True) or "",
        })

    # print(specData)
    return endFlag, specData
