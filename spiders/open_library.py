# -*- coding: utf-8 -*-
import json
import os

import scrapy


class OpenLibrarySpider(scrapy.Spider):
    name = 'open_library'
    allowed_domains = ['ia800301.us.archive.org']
    storage_path = os.environ['STORAGE_PATH']
    cookies = json.loads(os.environ['cookies'])
    total_images = int(os.environ['total_images'])
    fstring_formatted_url = os.environ['FSTRING_FORMATTED_URL']

    def start_requests(self):
        # this url is an example to
        for i in range(1, self.total_images + 1):
            yield scrapy.Request(
                url=self.fstring_formatted_url.format(i),
                callback=self.parse,
                cookies=self.cookies,
                meta={
                    'img_id': str(i)
                }
            )

    def parse(self, response):
        with open(os.path.join(self.storage_path, f"{response.meta['img_id']}.jpg"), 'wb') as f:
            f.write(response.body)
