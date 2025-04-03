# Django 04 ORM

## ORM

- Object-Relational-Mapping 

- 객체 지향 프로그래밍 언어를 사용항여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

![image](https://github.com/user-attachments/assets/05a746d6-66ba-4d80-b29a-a9d707b7d999)


## QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬, 그룹화 하는데 사용하는 도구
- API를 사용하여 SQL이 아닌 Python으로 데이터를 처리

![image-1](https://github.com/user-attachments/assets/1906e6c5-c31c-4ebb-a07a-e3a0060021f6)


- QuerySet은 다중 요청의 결과, Instance는 단일 요청의 결과

- QuerySet API 구문
    - Article.objects.all()
    - ModelClass.Manager.QuerySetAPI()
    - 전체 게시글 조회를 요청하는 것
    - 메서드로 동작을 요청?

- Query
    - DB에 데이터를 보여 달라는 요청
    - 쿼리문을 작성한다 : 원하는 데이터를 얻기 위해 DB에 요청을 보낼 코드를 작성한다.
    - 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 DB에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet 자료 형태로 반환

- QuerySet
    - DB에서 전달받은 객체 목록(데이터 모음)
    - 순회가능한 데이터로 1개 이상의 데이터를 불러와 사용 가능
    - Django ORM을 통해 만들어진 자료형
    - 단. DB가 단일 객체를 반환할 시 모델(class)의 Instance로 반환됨
    - [] 형태로 리스트처럼 다루기 가능(인덱스, 반복, 슬라이싱)

- python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장,조회,수정 삭제하는 것

- CRUD : Create, Read, Update, Delete. 소프트웨어의 기본적인 데이터 처리 기능

- 실습
    - 라이브러리 중에는 settings.py에 앱등록 해야하는 경우가 있으니 **공식문서** 꼭 참조. 이름이 다를 수 있음.

    - 실제로 쳐야할 코드들들
    ```python
        # settings.py

    INSTALLED_APPS = [
        'articles',
        'django_extensions',
        ...
    ]
    ```
    ```bash
    $ pip install ipython
    $ pip install django-extensions
    $ pip freeze > requirements.txt
    ```

    - 앱 등록 순서
        1. 직접 생성한 app
        2. 설치한 앱(3rd party)
        3. 내장 앱
    - $ python manage.py shell
        - 장고 안에서의 터미널을 실행시키는 행위
        - QuerySet API 구문을 입력해 실제 데이터에 영향을 줌
        - 종료는 exit
    - django-extentions 설치한 이유 = 기본 shell은 기능이 적어서 shell_plus를 사용하기 위함
    - $ python manage.py shell_plus
        - 내장 앱의 모델도 불러올 수 있음

- Create
    - Data 객체를 만드는 3가지 방법     
    - ------------------ 1 -------------------    
        - 내부 shell에 명령
        - **article = Article()**  
        - shell에 클래스 선언 
        - Article()은 모델에 있는 클래스로 상속받은 것까지 한 2000줄 됨
        - **article**
        - shell에 그냥 치면 print 해줌
        - **article.title = 'first'**
        - **article.content = 'django1'**
        - 해당 테이블 열에 추가하는 행위로 아직은 출력해도 안나옴
        - **article.save()**
        - 실제 데이터 추가 완료
        - article.id, article.title, article.content, article.created_at 등 사용가능
        - **article.pk**
        - 장고에서 지원하는 것으로 Primary Key다. 고유하게 가지는 키로 id를 안 쓰고 pk를 씀         
    - ------------------ 2 -------------------    
        - **article = Article(title='second', content='django!')**
        - 초기 값으로 바로 넣어서 할 수도 있다.
        - 하지만 아직 저장 안 됨
        - 인스턴스 관점에서 만든거지 그걸 DB에 저장이 안 되어있어 PK 값이 배정되지 않음
        - **article.save()**
        - Article.objects.all() 해보면 쿼리셋 확인 가능
    - ------------------ 3 -------------------    
        - 위 2가지 방법은 저장을 따로 해주었지만 이번엔 바로 생성시키기
        - **Article.objects.create(title='third', content='django!')**
        - 바로 생성된 데이터가 반환이 된다.

    - save()
        - 객체를 DB에 저장하는 인스턴스 메서드로 models.Model 클래스에서 상속받은 메서드다. DB에 생성.
        - https://docs.djangoproject.com/en/4.2/ref/models/instances/#saving-objects

- Read
    - Return new QuerySets 대괄호 쿼리셋으로 주냐?
        - all() : 전체 데이터 조회
        - filter() : 주어진 매개변수와 일치하는 객체를 포함하는 QuerySet 반환
        - 리스트처럼 준다 즉 하나만 있어도 이터레이터처럼 사용가능
        - 
    - Do not return QuerySets 단일로 주냐?
        - get() : 주어진 매개변수와 일치하는 객체를 반환
        - 객체를 찾을 수 없으면 DoesNotExist 예외 발생
        - 둘 이상의 객체면 MultipleObjdectsReturned 예외 발생
        - 따라서 primary key처럼 uniqueness(고유성)을 보장하는 조회에서 사용하라

- Update
    - 가장 어렵게 만드는 놈
    - 먼저 조회를 하고 받아와야한다
    - 그 후 인스턴스 변수를 변경하고 save 호출

- Delete
    - 삭제하려는 데이터를 조회해서 받고 delete 메서드를 호출해라
    - **article = Article.objects.get(pk=1)**
    - **article.delete()**
    - 반환값은 삭제된 객체가 반환됨

## ORM with view

- Django shell에서 연습했던 QuerySet API를 직접 view 함수에서 사용하기

### 전체 게시글 조회
```python
# articles/views.py

from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

```
```html
<!-- articles/index.html -->

<h1>Articles</h1>
<hr>
{% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <hr>
{% endfor %}

```

## 참고
### Field lookups
- Query에서 조건을 구성하는 방법
- filter(), exclude(), get() 등 키워드 인자로 지정됨 
```python
# Field lookups 예시

# "내용에 'dja'가 포함된 모든 게시글 조회"
Article.objects.filter(content__contains='dja')

# "제목이 he로 시작하는 모든 게시글 조회"
Article.objects.filter(title__startswith='he')

```
- https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups

### ORM QuerySet API를 사용하는 이유

1. DB 추상화 : 특정 DB 시스템에 종속 X 일관적으로 가능
2. 생산성 향상: python 코드로 DB 작업 가능
3. 객체 지향적 접근 : DB 테이블을 Python 객체로 다를 수 있다

- https://docs.djangoproject.com/en/4.2/ref/models/querysets/
- https://docs.djangoproject.com/en/4.2/topics/db/queries/
