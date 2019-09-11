
if __name__ == '__main__':
    import os
    file = "all.log"
    if os.path.exists(file):
        os.remove(file)
    from scrapy import cmdline
    # cmdline.execute("scrapy crawl agentSpider".split())
    # cmdline.execute("scrapy crawl idSpider".split())
    # cmdline.execute("scrapy crawl idSpider -o cvvid.json".split())
    cmdline.execute("scrapy crawl detailSpider".split())