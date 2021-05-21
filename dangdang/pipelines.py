# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

''' dd表SQL创建语句 '''
'''
create table dd(
    id int not null PRIMARY KEY AUTO_INCREMENT ,
    title VARCHAR (100),
    price VARCHAR (15),
    comment_count VARCHAR (15),
    shop_name VARCHAR (50),
    goods_link VARCHAR (100),
    shop_link VARCHAR (100)
)AUTO_INCREMENT = 1;

'''

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class DangdangPipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='766766',
            db='dangdang',
            use_unicode='True'
            # charset='utf-8'
        )
        cursor = conn.cursor()
        for i in range(0, len(item['title'])):
            title = item['title'][i]
            price = item['price'][i]
            comment_count = item['comment_count'][i]
            shop_name = item['shop_name'][i]
            goods_link = item['goods_link'][i]
            shop_link = item['shop_link'][i]
            sql = f'insert into dd(title, price, comment_count, shop_name, goods_link, shop_link) values("{title}", "{price}", "{comment_count}", "{shop_name}", "{goods_link}", "{shop_link}")'
            # print(sql)
            try:
                cursor.execute(sql)
                conn.commit()
            except Exception as e:
                print('sql语句错误', e)
                conn.rollback()
        conn.close()
        return item
