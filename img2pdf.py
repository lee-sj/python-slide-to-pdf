from PIL import Image

# pdf 로 만들 이미지를 묶을 빈 리스트 생성
imagelist = []

# pdf 저장의 기준을 잡을 첫페이지 세팅
img1 = Image.open('1.png')
img1 = img1.convert("RGB") 

# 총페이지가 20페이지 일경우 아래의 코드는 for i in range(2,21): 이다
# 1페이지는 기준을 잡기위해서 따로 세팅을 해주어서 2로 시작한다.
for i in range(2,PAGE수를_+1_한_값을_여기_적는다):
    img = Image.open('%d.png'%i)
    img = img.convert("RGB") 
    imagelist.append(img)

# OUTPUT = pdf 파일명을 원하는 이름으로 변경한다.
img1.save('OUTPUT.pdf', save_all=True, append_images=imagelist)
