# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:01:58 2018

@author: Administrator
"""

import urllib.request
import re

all = []
#浏览器伪装
def pretends():
    headers = ("Uesr-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

#爬取函数，参数为:搜索关键词， 页数
def crawl(url,all):
    data = urllib.request.urlopen(url).read().decode('utf-8')
    names = re.findall("title=(.*?)>", data, re.S)
    names = names[:-1]
    all+=names
    print(names)


def main():
    origin_url = 'https://movie.douban.com/tag/%E6%81%90%E6%80%96%E7%94%B5%E5%BD%B1'
    pretends()
    for i in range(10):
        url = origin_url + '?start='+str(i*2)+'0&type=T'
        crawl(url, all)
    print(all)

if __name__ == '__main__':
    main()

# movies=['"恐怖游轮"', '"死寂"', '"伊甸湖"', '"死神的十字路口"', '"恐怖故事"', '"鬼乱5"', '"黑暗侵袭"', '"咒怨：白老妇"', '"德州电锯杀人狂3D"', '"生化危机4：战神再生"', '"极度深寒"', '"恐怖废墟"', '"厉鬼将映"', '"丧尸乐园"', '"人兽杂交"', '"太平间闹鬼事件"', '"新猛鬼街"', '"假发"', '"惊声尖叫3"', '"生人勿进"', '"黑暗侵袭2"', '"考死：血之期中考试"', '"食人鱼3D"', '"困惑的浪漫2"', '"惊声尖叫"', '"寂静岭"', '"针孔旅馆"', '"黑色星期五"', '"轮回"', '"寂静岭2"', '"恶魔的艺术2：邪降"', '"黑暗楼层"', '"鬼水怪谈"', '"生人勿进(美版)"', '"深空失忆"', '"九人禁闭室"', '"五月魔女"', '"豺狼计划"', '"兽餐"', '"不请自来"', '"老师的恩惠"', '"不明影像：绝对点击禁止"', '"极限空间"', '"趣味游戏美国版"', '"粉红色高跟鞋"', '"刺"', '"惊声尖叫4"', '"鬼哭神嚎"', '"死亡录像2"', '"怪形"', '"婴灵恶泣"', '"殉难者"', '"咒怨：黑少女"', '"嗜血破晓"', '"407航班"', '"午夜凶铃(美版)"', '"雪山惊魂2"', '"残虐你，娱乐我"', '"吓死鬼"', '"惊声尖叫2"', '"撕裂人"', '"鬼来电3"', '"第39号案件"', '"东瀛鬼咒"', '"罗斯玛丽的婴儿"', '"詹妮弗的肉体"', '"感染"', '"生化危机5：惩罚"', '"鬼来电"', '"诚聘保姆"', '"变蝇人"', '"三十极夜"', '"陌生人"', '"隔离区"', '"咒怨(美版)"', '"普罗旺斯惊魂记"', '"变态冻尸"', '"灵动：鬼影实录3"', '"魔窟"', '"格蕾丝"', '"咒怨3(美版)"', '"死魂盒"', '"狼人"', '"山村老尸 3 恶灵缠身"', '"藏尸楼"', '"蛇女"', '"逃亡鳄鱼岛"', '"昏迷"', '"搭车人"', '"下一个就是你2"', '"救我"', '"女同志吸血鬼杀手"', '"人形师"', '"变鬼3.1"', '"恐怖休息站2：别回头"', '"灭顶之灾"', '"末日侵袭"', '"来电惊魂"', '"残酷饭店"', '"驱魔"', '"丧尸出笼2：病毒"', '"恐怖列车"', '"第六感"', '"七月"', '"驴子潘趣"', '"灵魂密码"', '"咒怨2(美版)"', '"万能钥匙"', '"吸血家族汉密尔顿"', '"下一个就是你"', '"新万圣节2"', '"荒村客栈"', '"幽灵鬼屋"', '"咒乐园"', '"丧尸乐园2"', '"鬼雾"', '"两个月亮"', '"杀出狂人镇"', '"鬼债"', '"死色"', '"变种DNA"', '"猫：看见死亡的双眼"', '"新丧尸出笼"', '"抽象画中的越南少女"', '"夜魔"', '"卡莉的眼泪"', '"身后事"', '"9号谋杀案"', '"富江 冤有头"', '"堕入地狱"', '"移魂都市"', '"惊心食人族"', '"怪谈新耳袋：幽灵公寓"', '"午夜凶铃2(美版)"', '"地铁四重奏"', '"仪式"', '"幽灵船"', '"笔仙"', '"驱魔人前传"', '"神殿"', '"迷网杀机"', '"惊声尖笑5"', '"咒怨"', '"生化危机"', '"幻觉"', '"少年派的奇幻漂流"', '"恐怖故事"', '"解冻"', '"7500航班"', '"1303大厦"', '"鬼宿舍"', '"四条大路通阴司"', '"群尸屠城"', '"鬼来电"', '"捉迷藏"', '"房客"', '"魔掌"', '"买鬼回家"', '"生存游戏"', '"深海狂鲨"', '"老师不是人"', '"第一诫"', '"圣歌"', '"活死人黎明"', '"寂静的房子"', '"棺木"', '"恶灵空间2"']
