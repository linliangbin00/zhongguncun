import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from zhongguancun.items import ZhongguancunItem


class MyzhongSpider(CrawlSpider):
    name = 'myzhongguancun'
    allowed_demains = ['mobile.zol.com.cn','detail.zol.com.cn']
    start_urls = ['http://detail.zol.com.cn/cell_phone/index1182632.shtml']

    rules = [Rule(LinkExtractor(allow=('/cell_phone/(.*)')),callback="get_parse",follow=True)]


    def get_parse(self, response):

        try:
            # 手机名
            photoName = response.xpath('//h1[@class="product-model__name"]//text()').extract()[0]
            # 副标题
            subheads = response.xpath('//div[@class="product-model__subtitle"]//text()').extract()
            # 手机参考价格
            originalPrice = response.xpath('/html/body/div[13]/div[2]/div[2]/div/span[1]/b[2]//text()').extract()[0]
            # 手机商家报价
            shopPrice = response.xpath('//*[@id="_j_local_price"]/a[1]//text()').extract()[0]
            # 手机主图
            mainPhoto = response.xpath('/html/body/div[13]/div[1]/div[1]/a/img/@src').extract()[0]
            # 手机小图
            photos = response.xpath('/html/body/div[13]/div[1]/div[2]/ul//img/@src').extract()
            # 规格名称
            baseConfigurations = response.xpath('/html/body/div[14]/div[1]/div[3]/div[2]/ul//p//text()').extract()
            # 手机类型
            phoneType = response.xpath('//h2[@class="product-model__alias"]//text()').extract()[0]
            # 评论
            comments = response.xpath('//div[@class="comment-list-content"]//text()').extract()

            subhead = ''
            photo = ';'
            baseConfiguration = ''
            item = ZhongguancunItem()
            for s in subheads:
                subhead += s

            for i,p in enumerate(photos):
                if i == 1:
                    pass
                else:
                    p += ';'
                photo += p

            for i,b in enumerate(baseConfigurations):
                b.strip().replace('\n', '').replace('\r','')
                baseConfiguration += b


            commentTemp = ''
            reRule = '[^ \']+'
            for c in comments:
                commentTemp += c.strip().replace('\r','').replace('\n', '')

            commentList= re.findall(reRule,commentTemp)
            comment = ''
            for i,c in enumerate(commentList):
                comment += c

            item['photoName'] = photoName
            item['mainPhoto'] = mainPhoto
            item['subhead'] = subhead
            item['originalPrice'] = originalPrice
            item['shopPrice'] = shopPrice
            item['photo'] = photo
            item['baseConfiguration'] = baseConfiguration
            item['phoneType'] = phoneType
            item['comment'] = comment

            yield item


        except:
            pass


