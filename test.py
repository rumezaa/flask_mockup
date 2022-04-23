import requests
import scrapy
from scrapy import FormRequest
from scrapy.crawler import CrawlerProcess
from scrapy.http import FormRequest
import re


class Auth(scrapy.Spider):
    name = 'auth'

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
        cookies = {'cookie-key': 'csrftoken=ZT83UOSuhrUCyxH3OeOGiErEiXd8Agqc; _ga=GA1.2.763447300.1650640946; _gid=GA1.2.479302257.1650640946; _gcl_au=1.1.1955578836.1650640947; G_ENABLED_IDPS=google; _scid=822486c8-34f7-404e-858f-e6538cc00231; _fbp=fb.1.1650640947565.875495067; ebGAClientId=763447300.1650640946; _pin_unauth=dWlkPU5UaG1OVFk1T1RJdFlqSXlZeTAwWm1JMUxXRTFaREl0TWpObU9UWTNPV1ZsTmpnMA; _sctr=1|1650607200000; _dd_s=rum=0&expire=1650643838291'}
        yield scrapy.Request(
            url='https://www.eventbrite.com/signin/',
            method='GET',
            headers=headers,
            cookies=cookies,
            callback=self.login,
        )


    def _get_xcsrf_token(self, response):
        cookies = response.headers.getlist('Set-Cookie')
        cookie, = [c for c in cookies if 'csrftoken' in str(c)]
        self.token = re.search(r'csrftoken=(\w+)', str(cookie)).groups()[0]
        return self.token

    def login(self, response):
        yield scrapy.FormRequest(
            url='https://www.eventbrite.com/signin/',
            formdata={
                'email': 'rumeza06@gmail.com',
                'password': 'pwd',
                'forward':'',
                'referrer': '/?internal_ref=login&internal_ref=login',
                'pckg': '',
                'stld': ''
            },
            callback=self.parse,
            headers={'X-CSRFToken': self._get_xcsrf_token(response),'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        )

    def parse(self, response):
        print("logged in")

    def parse_after_login(self, response):
        pass

if __name__ == "__main__":
  process = CrawlerProcess()
  process.crawl(Auth)
  process.start()