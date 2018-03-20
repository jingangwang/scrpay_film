import scrapy


class FilmSpider(scrapy.Spider):
    name = 'filmspider'

    def start_requests(self):
        yield scrapy.Request("https://www.dy2018.com/html/gndy/dyzz/index.html", self.parse)

    def parse(self, response):
        # 分析下一页的链接并跟踪
        next_page_url = response.xpath('//a[contains(.,"\u4e0b\u4e00\u9875")]/@href').extract_first()
        self.log(">>>>> 下一页的地址：%s" % next_page_url)
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)

        # 分析当前页面的所有链接并提取到item
        film_urls = response.xpath('//a[@class="ulink"]/@href').extract()
        for film_url in film_urls:
            yield response.follow(film_url, callback=self.parse_film)

    def parse_film(self, response):
        film_name = response.xpath('//div[@class="title_all"]/h1/text()').extract_first()
        film_score = response.xpath('//strong[@class="rank"]/text()').extract_first()
        film_download_urls = response.xpath('//div[@id="Zoom"]//a[re:test(@href,"^ftp:|^magnet:")]/@href').extract()
        self.log(">>>>>>>电影名称：%s,电影评分：%s,下载地址：%s" % (film_name, film_score, film_download_urls))

