import json
from urllib.parse import urljoin
from datetime import datetime


def parseDate(s):
    mon_s, day_s, year_s = s.split('/')
    return datetime(int(year_s), int(mon_s), int(day_s))

if __name__ == '__main__':
    pass
    # parseDate('08/27/2019')

    # start_urls = []
    # url = 'https://nvd.nist.gov/vuln/detail/'
    # with open('cvvid.json', 'r') as f:
    #     for cnt, line in enumerate(f):
    #         try:
    #             line = line.strip('\n').strip(',')
    #             json_obj = json.loads(line)
    #             cvvid = json_obj['cvvID']
    #             url = urljoin(url, cvvid)
    #             start_urls.append(url)
    #         except Exception as e:
    #             print(e)
    #             continue
    # print(start_urls)


# with open("urls.txt", "rt") as f:
#     start_urls = [url.strip() for url in f.readlines()]
#
#     start_urls = [json.loads(line.strip('\n').strip(','))['cvvID'] for (cnt,line) in enumerate(f)]