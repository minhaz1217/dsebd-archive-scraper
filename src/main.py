import argparse
import asyncio
from request.request import get
from scraper.scraper import scrapArchive
from file_writer.file_writer_factory import writeFile

def parseArgs():
    parser = argparse.ArgumentParser(description='Personal information')
    parser.add_argument('--name', dest='name', type=str, help='Name of the candidate')
    parser.add_argument('--surname', dest='surname', type=str, help='Surname of the candidate')
    parser.add_argument('--age', dest='age', type=int, help='Age of the candidate')

    args = parser.parse_args()
    print(args.name)
    print(args.surname)
    print(args.age)

def getResponse():
    allInstrument = "All Instrument"
    startDate = "2022-12-27"
    endDate = "2022-12-27"

    datas : list= scrapArchive(startDate=startDate, endDate=endDate, companyName=allInstrument)
    print("Data scraped: ", len(datas))
    writeFile(data=datas, path= "Stock data {}-{}-{}".format(allInstrument, startDate, endDate),type=1)

    
    # for data in datas:
    #     print(data)

getResponse()