# Django 02 Template & URLs

- Django Template system : 데이터 표현을 제어하면서 표현과 관련된 부분을 담당

## Template System

### Django Template System

- HTML의 콘텐츠를 변수 값에 따라 변경하기
- views의 context = {}에 {키 : 밸류} 값이 있고 render에 연결된다면 
- html에서 {{키}} 로 가져올 수 있다


### Django Template Language

- DTL : Template에서 조건, 변수, 반복 등의 프로그래밍적 기능을 제공하는 시스템

1. Variable
    - render 함수의 세번쨰 인자로 딕셔너리 데이터를 이용
    -  딕셔너리 key의 문자열이 template에 사용가능한 변수명이 됨
    - dot('.')을 사용해 변수 속성에 접근도 가능

2. Filters
    - 표시할 변수를 수정할 때 사용(변수+|+필터)
    - chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
    - 약 60개의 빌트인 필터를 제공
3. Tags
    - 반복 또는 논리를 수행해 제어 흐름을 만듦
    - 일부 태그는 시작과 종료 태그가 필요
    - 약 24개의 빌트인 태그를 제공
4. Comments
    - DTL에서 주석
    - {# name #}, {% commment %} ~ {% endcomment %}

DTL 실습중

- Django 공식문서 보는 법 - Django document filter 따위로 구글링
- 아래로 가지말고 오른쪽 목차에서 찾기

## 템플릿 상속

- Template inheritance
    
    페이지의 공통 요소를 포함하고

    하위 템플릿이 재정의 할 수 있는 공간을 정의하는

    기본 'skeleton' 템플릿을 작성해 상속 구조를 구축

- 상위 템플릿 base.html에서 block을 활용(그 안 쪽이 자식에 전달되는 공간을 정의함)

### 상속 관련 DTL 태그

- 'extends' tag
    - {% extends 'path' %}
    - 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림
    - **반드시 자식 템프릿 최상단에 작성되어야 함**
    - settings에 TEMPLATES의 DIR 위치가 기본 경로

- 'block' tag
    - {% block name %}{% endblock name %}
    - 하위 템플릿에서 재정의 할 수 있는 블록을 정의
    - 상위 템플릿에 작성해 하위 템플릿이 작성할 수 있는 공간을 지정하는 것


## 요청과 응답

### HTML form
- 데이터를 보내고 가져오기 : HTML form을 통해 상호작용

- http 요청을 서버에 보내는 가장 편리한 방법 -> form
- form element : 사용자로부터 할당된 데이터를 서버로 전송
- 웹에서 사용자 정보를 입력하는 여러방식을 제공 (text, password, checkbox 등)

### form 핵심 속성
- action : 데이터를 어디로 (목적지)
- method : 어떤 방식으로 보낼건지 (HTTP request methods = GET or POST)
    - GET은 검색(조회)-URL에 보임, POST는 삭제 수정 생산 조직 등

- input : 사용자의 데이터를 입력받을 수 있는 요소(type으로 다양한 유형 받음)
    - 핵심 name : 사용자가 입력한 데이터에 붙이는 이름(key)으로, 이 값을 통해 데이터에 접근

- Query String Parameters
    - 기본 URL과 ?로 구분되고, &(앰퍼샌드)로 연결된 key=value쌍
    - 사용자 입력데이터를 URL주소 파라미터를 통해 서버로 보낸다
    - https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=HI 따위


### form 활용

- HTTP request 객체 확인
![image-9](https://github.com/user-attachments/assets/388c12e1-1cb3-4479-ae14-561cc007057b)


## Django URLs
- URL dispatcher : 운항 관리자, 분배기로 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

### Variable Routing
- 현재 문제점은, 템플릿의 많은 부분이 중복되고 URL의 일부만 변경될 경우 계속 비슷한 URL과 템플릿을 작성해야하나??

- 그래서 나온 게 Variable Routing 변수 경로. URL에 변수를 포함하자!

- 작성법
    ```
    <path_converter:variable_name>
    <타입:변수명>
    <int:num>
    <str:name>
    ```
- Path converters : URL 변수의 타입을 지정


### App URL 정의

- 각 앱에 URL을 정의하는 것 : 프로젝트와 각 앱이 URL을 나누어 관리를 편하게

- 2번째 앱 p\만들었다가 views 변수명이 겹치거나 패턴이 동일한 RUL 주소를 사용 할 수 이씀
- **URL을 각자 APP에서 관리하자**
- include() 프로젝트 내부 앱들의 URL 을 참조할 수 있도록 매핑하는 함수
```python
# pjt/urls.py
from django.urls import path, include
```

## URL 이름 지정
- 문제점? 기존 주소에 /index 따위가 붙으면서 달라짐 -> 사용하는 곳 전부 변경해야해??
**이름을 주어주자**

### Naming URL patterns
- 이름 짓는 방법 path 함수의 name='name' 따위로 정의하고

- url 사용하는 모든 곳에 {% url 'name' arg %} 로 지정 (html에서)


## URL 이름 공간
- 이름 지정 후 남은 문제
- 두 앱의 url 이름이 같은 경우? 구분 가능해?
- 단순히 이름으론 분리될 수 없구나!
- key를 하나 붙이자!
### app_name 속성
- urls에 app_name이란 변수를 설정한다 app_name = 'index' 따위로
- URL tag를 {% url 'articles:index' %} 형태로 전부 변경하기 (최종형태. 이거로만 씀)

## 참고

### 추가 템플릿경로 지정
- 템플릿 기본 경로 외에도 커스텀 경로로 추가가 가능하다! 
- settings.py의 TEMPLATES 찾아간다
- 'DIRS' : [BASE_DIR/'templates'], 추가하면 된다
- BASE_DOR은 settings에서 경로지정을 편하게 하기 위해 최상단 지점을 지정해 둔 변수
    ```python
    # Build paths inside the project like this: BASE_DIR / 'subdir'.

    BASE_DIR = Path(__file__).resolve().parent.parent
    ```
- OS마다 경로 표현이 달라서 저렇게 저장하는 것

### DTL 주의사항
- Python 문법을 따라했지만 Python으로 돌아가는 게 아니다.
- 프로그래밍적 로직 x 표현을 위한 것
- 프로그래밍적 로직은 view 함수에서 처리하자
- 공식문서 무조건 참조
    - https://docs.djangoproject.com/ko/4.2/ref/templates/builtins/
