import os
from urllib.parse import urlparse
import requests

# pip install Pillow

from PIL import Image
from io import BytesIO
# 이미지 URL 주소 요청
url = "https://img1.newsis.com/2023/01/20/NISI20230120_0001180781_web.jpg"
r = requests.get(url)
# 이미지 파일 가져오기
i = Image.open(BytesIO(r.content))
print( type(i) )
# URL 에서 파일명 추출
parsed_url = urlparse(url)
origin_file = os.path.basename(parsed_url.path)
# 이미지 확장자 확인
img_format = i.format           # 이미지 포맷 확인 : jpg, png, gif, webp
ext = img_format.lower() if img_format else 'img'
# 이미지 파일 저장하기
# filename = "./" + origin_file + "." + ext
filename = "./" + origin_file
i.save(filename)
print("파일명 : " + filename)
print("이미지 파일을 저장하였습니다.")
# 저장한 이미지 열어보기
i.show()