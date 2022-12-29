import argparse
from scraper.scraper import scrapArchive
from file_writer.file_writer_factory import writeFile

def main():

    parser = argparse.ArgumentParser(description='Scraper Usage')
    parser.add_argument('--start', dest='startDate', type=str, help='Start date')
    parser.add_argument('--end', dest='endDate', type=str, help='End date')
    parser.add_argument('--company', dest='company', type=str, help='Company name that you want to scrap for.')
    parser.add_argument('--output', dest='output', type=int, help='Output format, 1 means csv 2 means json')
    args = parser.parse_args()
    
    # print(args.startDate)
    scrapData(args.startDate, args.endDate, args.company, args.output)


def scrapData(startDate: str, endDate: str, company: str, output: int):
    datas : list= scrapArchive(startDate=startDate, endDate=endDate, companyName=company)
    print("Data scraped: ", len(datas))
    writeFile(data=datas, path= "Stock data {}-{}-{}.csv".format(company, startDate, endDate),type=output)
    
    
    # allInstrument = "All Instrument"
    # startDate = "2022-07-01"
    # endDate = "2022-07-01"

    # print("Data scraped: ", len(datas))
    

    # writeFile(data=datas, path= "Stock data {}-{}-{}.json".format(allInstrument, startDate, endDate),type=2)

main()