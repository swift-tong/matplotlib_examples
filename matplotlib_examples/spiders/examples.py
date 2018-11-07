# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy import Request
from matplotlib_examples.items import MatplotlibExamplesItem
import sys


class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        le=LinkExtractor(restrict_css='div.toctree-wrapper.compound',deny='/index.html$')
        links=le.extract_links(response)
        print(len(links))
        print(links)
        for link in links:
            yield Request(link.url,callback=self.parse_example)


    def parse_example(self,response):
        href = response.css('a.reference.external::attr(href)').extract_first()
        print(href)
        url = response.urljoin(href)
        print(url)
        example = MatplotlibExamplesItem()
        example['file_urls'] = [url]
        return example

