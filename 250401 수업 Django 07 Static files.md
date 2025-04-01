# Django 07 Static files


## Static files
### Static files 제공하기
- 정적 파일 : 서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (이미지, JS, CSS 등)

#### 웹 서버와 정적 파일일
- 웹 서버의 기본 동작은 **특정 위치(URL)에 있는 자원**을 요청(HTTP request)받아서 응답(HTTP response)을 처리하고 제공하는 것
- 이는 자원에 접근 가능한 주소가 있다는 의미
- 웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원을 제공함
- 즉 **정적 파일을 제공하기 위한 경로(URL)**가 있어야함

### Static files 기본 경로
- app폴더/static/
- \+ app_name/ 경로에 이미지 파일 배치
- static files 경로는 DTL의 static tag를 사용해야함
- 빌트인tag가 아니기 때문에 load tag를 사용해 import 후 사용 가능
```html
index.html

{% load static %}

<img src="{% static 'articles/sample-1.png' %}" alt ="img">
```
- STATIC_URL을 개발자 도구로 확인 가능

- STATIC_URL
    - 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
    - 실제 파일이나 디렉토리 경로가 아니며, URL로만 존재
    - settings.py에 존재
    -  URL + STATIC_URL + 정적파일 경로


### Static files 추가 경로
- STATICFILES_DIRS에 문자열 값으로 추가 경로 설정 (리스트)
- DIRS 기억해라
```python
#settings.py

STATICFILES_DIRS =[
    BASE_DIR / 'static',
]

```
- 이러면 기본 경로에 static 폴더 생성해도 가능
- DTL로 쓸 때 파일명만 써도 가능
0

**정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요**

## Media files
- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
### 이미지 업로드
- ImageField()
    - 이미지 업로드에 사용하는 모델 필드
    - 이미지 파일의 경로 문자열이 어장됨
- 제공 전 준비사항
    - settings.py에 **MEDIA_ROOT**, **MEDIA_URL** 설정
    - 작성한 MEIA_ROOT와 MEDIA_URL에 대한 URL 지정  
- **MEDIA_ROOT** : 미디어 파일들이 위치하는 디렉토리의 절대 경로
- **MEDIA_URL** : 미디어_루트에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)

```python
#settings.py
MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = 'media/'
```
- URL 지정
```python
# project/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    # 기존 경로들
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

- 사실 settings.py에 주석으로 적힌힌 공식문서 참조해서 복사해오면 된다
```
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

```
- 모델에 ImageField 추가
    - blank =True로 속성을 작성해 빈 문자열이 저장될 수 있도록 제약 조건 설정
    - 왜? 게시글 작성 시 이미지 업로드 없이도 작성 가능하도록
    - 기존 필드 사이에 작성해도 실제 테이블에서는 가장 뒤에 추가됨
- migration 진행
    - ImageField는 Pillow 라이브러리 필요
- form 요소에 enctype 속성 추가
```html
<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
```
- ModelForm의 2번째 인자 files에 요청 받은 파일 데이터 작성
    - ModelForm이 상속받은 BaseModelForm의 생성자 함수의 2번째 위치 인자로 파일을 받도록 설정되어 있음
    - ArticleForm(request.POST, request.FILES)

### 업로드 이미지 제공
- url 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
- article.image : 업로드 파일의 파일 이름
- article.image.url : 업로드 파일의 경로
- 이미지를 업로드 하지 않았을 경우에 대해서도 예외 처리 해야한다

```html
<!-- articles/detail.html -->

{% if article.image %}
    <img src = "{{article.image.url}}" alt ="img">
{% endif %}
```

### 업로드 이미지 수정
- 수정 페이지 form에도 enctype 추가
- update view 함수에서 업로드 파일에 대한 추가 콛 작성

## 참고
### 미디어 파일 추가 경로
- 'upload to' argumnet
- ImageField()의 upload_to 속성을 사용해 다양한 추가 경로 설정가능

### BaseModelForm
- request.FILES가 두 번째 위치 인자인 이유
    - 생성자 함수 키워드 인자 참고