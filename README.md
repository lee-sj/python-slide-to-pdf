# python-slide-to-pdf
한국외국어대학교 온라인강의 강의자료 pdf 만들기  

## 순서 
강의자료 > 이미지로 저장 (img-saver)  
이미지 > pdf 변환 (img2pdf)

## img-saver
한국외국어대학교 온라인강의 강의자료 이미지로 저장하기

``` shell
$ pip install pillow
```
### 이미지 URL 확인
1. eclass 온라인 강의에 접속한다.  
2. 왼쪽하단부 Slide e-Book을 선택한다. 
3. 우클릭 검사로 개발자 도구를 열고, 다운로드하고자하는 이미지를 찾는다. 
4. 파일명 위에서 우클릭을하고 Open in new tab을 선택한다. 
5. 인터넷 주소창의 URL의 첫 부분과 끝 부분이 오른쪽과 같다면 성공 http://contents.hufs.ac.kr/contents ... pages/1.png 

### python 파일 수정
6. 해당 주소를 복사한후 작은따옴표(' ')안에 넣고 파일명의 숫자를 $d 로 바꾸고 닫힘 따옴표 뒤에 %i 를 붙인다. 
7. 파이썬 파일의 주석을 확인하고 페이지 수 설정과 6번의 결과물을 알맞는 곳에 붙여넣기한다. 

### 파일 실행 - 이미지 생성
8. img-saver.py 파일을 실행한다. 
``` shell
$ python img-saver.py
```

## img2pdf
강의자료 이미지를 묶어서 pdf로 변환하기

### python 파일 수정
1. img-saver와 같이 페이지 수를 설정한다. 
2. 만들고자 하는 pdf 파일의 파일명얼 수정한다. 

### 파일실행 - pdf 생성
3. img2pdf.py 파일을 실행한다. 
``` shell
$ python img2pdf.py
```
