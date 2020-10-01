# -*- coding: utf-8 -*-

import scrapy
import logging


base_url = "https://b-ok.asia"


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['b-ok.asia']
    user_input = input('What do you want to scrape ?\n')
    start_urls = [f'https://b-ok.asia/s/{user_input}']

    def parse(self, response):

        books = response.xpath("//td/h3/a")
        for book in books:
            name = book.xpath(".//text()").get()
            self.book_name = name
            link = book.xpath(".//@href").get()
            self.links = link
            yield response.follow(url=link, callback=self.parse_country, meta=({'title': name}))

    def parse_country(self, response):
        logging.info(response.url)
        title = response.request.meta['title']
        links_toDownload = response.xpath(
            '/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div[1]/div[1]/div/a')
        for links in links_toDownload:
            dwnld_links = links.xpath('.//@href').get()
            self.download_links = dwnld_links
            yield {
                'title': title,
                'link': base_url+dwnld_links
            }
