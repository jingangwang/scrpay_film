# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import pymysql

from scrapy_film import mysql_config


class SaveToDBPipeline(object):

    def process_item(self, item, spider):
        _sql = "insert into film_info (film_name,film_score,film_download_urls) values(%s,%s,%s)"
        _args = (item['film_name'][0], item['film_score'][0], ",".join(item['film_download_urls']))
        conn = pymysql.connect(host=mysql_config.db_config['test'].get('host'),
                               port=mysql_config.db_config['test'].get('port'),
                               user=mysql_config.db_config['test'].get('user'),
                               passwd=mysql_config.db_config['test'].get('passwd'),
                               db=mysql_config.db_config['test'].get('db'),
                               charset=mysql_config.db_config['test'].get('charset'))
        cursor = conn.cursor()
        affect = cursor.execute(_sql, _args)
        conn.commit()
        cursor.close()
        conn.close()
        logging.info("保存影片数据，result：%s, input_data: %s", affect, _args)
        return item
