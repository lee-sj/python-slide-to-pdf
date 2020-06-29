# -*- coding: utf-8 -*- 
# 이미지관련, url 관련 import
from PIL import Image
from urllib.request import urlopen

# 온라인강의에 있는 slide 의 페이지 만큼 반복한다. 
# 총페이지가 20페이지 일경우 아래의 코드는 for i in range(1,21): 이다
for i in range(1,PAGE수를_+1_한_값을_여기_적는다):
    # 이미지 열기
    im = Image.open(urlopen(위_주석_6_의 결과물을 여기에 붙여넣는다.))
    # 이미지 저장
    im.save('{0}.png'.format(i))
