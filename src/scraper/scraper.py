import asyncio
import re
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

def scrapArchive(startDate: str, endDate: str, companyName: str = "All Instrument"):
    if(not(isValidDateFormat(startDate) and isValidDateFormat(endDate))):
        raise ValueError("Date must be in yyyy-mm-dd format")
    
    print("scrapArchive")
    url = "https://www.dsebd.org/day_end_archive.php?startDate=" + startDate + "&endDate=" + endDate + "&inst=" + companyName + "&archive=data"
    print("Scraping data from - ", url)
    html_text = asyncio.run(get(url))
    print(len(html_text))