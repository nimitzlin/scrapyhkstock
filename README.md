# simple scrapyhkstock
##项目

抓取http://quote.eastmoney.com/hk/HStock_list.html 上的全港股列表
然后根据列表再去抓取 每个股票的详细财务信息

##依赖库

pip install scrapy
pip install scrapy-splash
apt-get install docker-ce

##运行

sudo docker pull scrapinghub/splash
sudo docker run -p 8050:8050 scrapinghub/splash

配置 settings.py 里面的splash地址为上面docker的地址
python main.py
