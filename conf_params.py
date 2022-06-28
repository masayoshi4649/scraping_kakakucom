import processing_scraping


def sleepinterval():
    # 3秒猶予
    return 3


def onepage():
    # 1ページ
    return 40


def maxpage():
    # 最大ページ
    return 500


def scrapingfunc(category: str):
    if(category == "CPU"):
        return processing_scraping.getInfoData_CPU

    if(category == "CPUCOOLER"):
        return processing_scraping.getInfoData_CPUCOOLER

    if(category == "GPU"):
        return processing_scraping.getInfoData_GPU

    if(category == "RAM"):
        return processing_scraping.getInfoData_RAM

    if(category == "SSD_M2"):
        return processing_scraping.getInfoData_SSD_M2

    if(category == "SSD_SATA"):
        return processing_scraping.getInfoData_SSD_SATA

    if(category == "HDD"):
        return processing_scraping.getInfoData_HDD

    if(category == "MOTHERBOARD"):
        return processing_scraping.getInfoData_MOTHERBOARD

    if(category == "POWERSUPPLY"):
        return processing_scraping.getInfoData_POWERSUPPLY

    if(category == "CASE"):
        return processing_scraping.getInfoData_CASE

    if(category == "OS"):
        return processing_scraping.getInfoData_OS


def geturl(category: str, pagenum: int):
    if(category == "CPU"):
        return f"https://kakaku.com/pc/cpu/itemlist.aspx?pdf_so=d2&pdf_pg={pagenum}"

    if(category == "CPUCOOLER"):
        return f"https://kakaku.com/pc/cpu-cooler/itemlist.aspx?pdf_so=e2&pdf_pg={pagenum}"

    if(category == "GPU"):
        # nVidia+AMD
        return f"https://kakaku.com/pc/videocard/itemlist.aspx?pdf_Spec101=1,11&pdf_so=e2&pdf_pg={pagenum}"

    if(category == "RAM"):
        return f"https://kakaku.com/pc/pc-memory/itemlist.aspx?pdf_so=e2&pdf_pg={pagenum}"

    if(category == "SSD_M2"):
        # 内蔵 / M.2 (Type2280) / NVMe
        return f"https://kakaku.com/pc/ssd/itemlist.aspx?pdf_Spec001=1&pdf_Spec102=8&pdf_Spec104=1&pdf_so=e2&pdf_pg={pagenum}"

    if(category == "SSD_SATA"):
        # 内蔵 / 2.5インチ
        return f"https://kakaku.com/pc/ssd/itemlist.aspx?pdf_Spec102=2&pdf_Spec104=1&pdf_so=e2&pdf_pg={pagenum}"

    if(category == "HDD"):
        return f"https://kakaku.com/pc/hdd-35inch/itemlist.aspx?pdf_so=e2&pdf_pg={pagenum}"

    if(category == "MOTHERBOARD"):
        return f"https://kakaku.com/pc/motherboard/itemlist.aspx?pdf_so=e2&pdf_pg={pagenum}"

    if(category == "POWERSUPPLY"):
        return f"https://kakaku.com/pc/power-supply/itemlist.aspx?pdf_so=e2&pdf_pg={pagenum}"

    if(category == "CASE"):
        return f"https://kakaku.com/pc/pc-case/itemlist.aspx?pdf_so=e2&pdf_pg={pagenum}"

    if(category == "OS"):
        return f"https://kakaku.com/pc/os-soft/itemlist.aspx?pdf_so=e2&pdf_pg={pagenum}"
