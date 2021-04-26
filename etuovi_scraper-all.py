import scrapy
# raapija, joka kerää etuovi.com:sta ilmoituksien tiedoista
# asuntotyypin, osoitteen, hinnan, valmistuvuoden ja pinta-alan.
# (Kyseessä Tampereen omakotitalot)
class EtuoviScraperSpider(scrapy.Spider):
    name = 'etuovi_scraper'
    allowed_domains = ['etuovi.com']
    # assing a page url below
    start_urls = \
    ['https://www.etuovi.com/myytavat-asunnot?haku=M1645676469&sivu=0']

  # Funkito parse(self, response) käy läpi aloitusosoitteesta eteenpäin
  # sivuja, joilta dataa kerätään. Parse kutsuu parse_page-funktiota, jossa
  # on määritelty varsinainen kerättävä tieto.
  # max 5 sivua tässä esimerkissä
    def parse(self, response):
        for i in range(1, 301):
            url=response.request.url[:-1]+str(i)
            yield scrapy.Request(url, callback=self.parse_page)
        
    
    def parse_page(self, response):
        description_texts = response.css(\
          '[class="flexboxgrid__col-xs-12__1I1LS"] *::text').extract()
        size_text = response.css(\
          '[class="flexboxgrid__col-xs__26GXk flexboxgrid__col-md-4__2DYW-"] > span::text').extract()
        year_text = response.css(\
          '[class="flexboxgrid__col-xs-3__3Kf8r flexboxgrid__col-md-4__2DYW-"] > span::text'\
          ).extract()
        price_text = response.css(\
          '[class="flexboxgrid__col-xs-4__p2Lev flexboxgrid__col-md-4__2DYW-"] > span::text'\
          ).extract()

        for i in range(len(price_text)):
            yield {
                'house_type' : description_texts[2*i],
                'address': description_texts[2*i+1],
                'price': price_text[i],
                'year': year_text[i],
                'size': size_text[i]
            }