from scrapy.spider import Spider
from scrapy.selector import Selector

class TeamSpider(Spider):
    name="Teams"
    allowed_domains="mlb.com"
    start_urls = ["http://mlb.mlb.com/team/index.jsp"]
    def parse(sel, response):
        sel = Selector(response)
        mlbteams = sel.xpath('//*[@id="section_navigation_links"]/li[3]/ul/li')
        for team in mlbteams:
            print team.xpath('a/text()').extract()