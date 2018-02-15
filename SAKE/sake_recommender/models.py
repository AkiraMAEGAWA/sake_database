from django.db import models

# Create your models here.

class Sake(models.Model):
    
    # 酒の銘柄
    brand = models.CharField(max_length=128)
    
    # 生産地
    producing_area = models.CharField(max_length=128)

    # 種類 e.g) ビール, 日本酒, 焼酎 
    sake_type = models.CharField(max_length=128)

    # URL 紹介ページなど
    urls = models.URLField(null=True, blank=True)
