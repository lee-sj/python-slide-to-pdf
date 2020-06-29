# -*- coding: utf-8 -*- 
# 이미지관련, url 관련 import
from PIL import Image
from urllib.request import urlopen

# 1. eclass 온라인 강의에 접속한다.  
# 2. 왼쪽하단부 Slide e-Book을 선택한다. 
# 3. 우클릭 검사로 개발자 도구를 열고, 다운로드하고자하는 이미지를 찾는다. 
# 4. 파일명 위에서 우클릭을하고 Open in new tab을 선택한다. 
# 5. 인터넷 주소창의 URL 이 오른쪽과 같다면 성공 http://contents.hufs.ac.kr/contents ... pages/1.png 
# 6. 해당 주소를 복사한후 작은따옴표(' ')안에 넣고 파일명의 숫자를 $d 로 바꾸고 닫힘 따옴표 뒤에 %i 를 붙인다. 
# 'http://contents.hufs.ac.kr/contents ... pages/%d.png'%i

# 온라인강의에 있는 slide 의 페이지 만큼 반복한다. 
# 
for i in range(1,PAGE수를_+1_한_값을_여기_적는다):
    # 이미지 열기
    im = Image.open(urlopen(위_주석_6_의 결과물을 여기에 붙여넣는다.))
    # 이미지 저장
    im.save('{0}.png'.format(i))
