import asyncio
import re
from bs4 import BeautifulSoup
from request.request import get


# only accept date format as YYYY-MM-DD
def isValidDateFormat(date: str):
    if(len(date) != 10):
        return False

    regex = r"^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$"
    test_str = date
    matches = re.findall(regex, test_str)
    if(len(matches) != 1):
        return False
    return True


def extractDataFromRow(row):
    tds = row.findChildren("td")
    if(len(tds) != 12):
        print("error: 12 columns not found. -> ", tds)
        return

    return {
        "id" : tds[0].get_text().strip(),
        "date" : tds[1].get_text().strip(),
        "trading_code" : tds[2].get_text().strip(),
        "ltp" : float(tds[3].get_text().strip().replace(",","")),
        "high" : float(tds[4].get_text().strip().replace(",","")),
        "low" : float(tds[5].get_text().strip().replace(",","")),
        "openp" : float(tds[6].get_text().strip().replace(",","")),
        "closep" : float(tds[7].get_text().strip().replace(",","")),
        "ycp" : float(tds[8].get_text().strip().replace(",","")),
        "trade" : float(tds[9].get_text().strip().replace(",","")),
        "value" : float(tds[10].get_text().strip().replace(",","")),
        "volume" : float(tds[11].get_text().strip().replace(",",""))
    }

def scrapArchive(startDate: str, endDate: str, companyName: str = "All Instrument"):
    if(not(isValidDateFormat(startDate) and isValidDateFormat(endDate))):
        raise ValueError("Date must be in yyyy-mm-dd format")
    
    url = "https://www.dsebd.org/day_end_archive.php?startDate=" + startDate + "&endDate=" + endDate + "&inst=" + companyName + "&archive=data"
    print("Scraping data from - ", url)
    response = asyncio.run(get(url))
    soup = BeautifulSoup(response, "lxml")
    tableDiv = soup.find( "table", {"class" : "shares-table"})
    tbody = tableDiv.findChild("tbody")
    trs = tbody.findChildren("tr")
    datas = []
    for tr in trs:
        datas.append(extractDataFromRow(tr))
    return datas
    