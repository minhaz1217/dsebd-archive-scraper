import argparse
import asyncio
import aiohttp

def parseArgs():
    parser = argparse.ArgumentParser(description='Personal information')
    parser.add_argument('--name', dest='name', type=str, help='Name of the candidate')
    parser.add_argument('--surname', dest='surname', type=str, help='Surname of the candidate')
    parser.add_argument('--age', dest='age', type=int, help='Age of the candidate')

    args = parser.parse_args()
    print(args.name)
    print(args.surname)
    print(args.age)

async def getUrlFromText(url: str):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        return await response.text()

def getResponse():
    allInstrument = "All Instrument"
    startDate = "2022-12-27"
    endDate = "2022-12-27"
    url = "https://www.dsebd.org/day_end_archive.php?startDate=" + startDate + "&endDate=" + endDate + "&inst=" + allInstrument + "&archive=data"
    print(url)
    html_text = asyncio.run(getUrlFromText(url))
    print(len(html_text))



getResponse()