# 상품관리사이트 (Django 샘플)

로컬에서 실행하는 간단한 상품 관리 사이트입니다. 상품 등록/수정/삭제/조회/목록 기능이 포함되어 있습니다.

요구 사항

- Python 3.11+ (문의: 사용자 요구에는 3.13이라고 되어 있으나, 현시점에서는 3.11/3.12 권장)
- Django 4.2+
- Pillow (이미지 업로드)

설치 및 실행 (Windows PowerShell 예)

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

개발 노트

- 미디어 파일은 `media/`에 저장됩니다. 개발 중 Django의 static/media 서빙이 설정되어 있습니다.
