# Database 04 Many to one relationships 02

## Many to one relationships 2
### 개요
- User과 다른 모델 간의 모델 관계 설정
    - User & Article
    - User & Comment

- Article(N) - User(1) : 0개 이상의 게시글은 1명의 회원에 의해 작성될 수 있다
- Comment(N) - User(1) : 0개 이상의 댓글은 1명의 회원에 의해 작성될 수 있다.


## Article & User
### 모델 관계 설정

- Article - User 모델 관계 설정     

    User 외래 키 정의
    ```python
    # articles/ models.py
    
    from django.conf import settings

    class Article(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        ...
        ...
    ```

- User 모델을 참조하는 2가지 방법

    내부적인 구동 순서와 반환 값에 따른 이유.   
    기억해야 할 것은 **User 모델은 직접 참조하지 않는다**
    
    - get_user_model()

        - 반환 값 : User Object(객체)

        - 사용 위치 : **modles.py가 아닌 다른 모든 위치**

    - settings.AUTH_USER_MODEL
        - 반환 값 :'accounts.User' (문자열)

        - 사용 위치 : models.py


- Migration
    ```shell
    $python manage.py makemigrations
    ```
    - 오류 발생
    - 기존에 테이블이 있는 상태에서 필드 추가하려기 떄문에 생기는 과정
    - 기본적으로 모든 필드엔 NOT NULL이라 데이터 없이는 새로운 필드가 추가되지 못함
    
    - 1을 입력하고 진행
    
    - 추가하는 외래 키 필드에 어떤 데이터를 넣을 것인지 직접 입력해야한다
    
    - 마찬가지로 1을 입력하고 진행
        - 기존에 작성된 게시글 있으면 다 1이 한 것처럼 처리

    ```shell
    $python manage.py migrate
    ```
    - migrate 진행

### 게시글 CREATE
- 기존 ArticleForm 출력 변화 확인

- User 모델에 대한 외래 키 데이터 입력을 위해 불필요한 input이 출력됨

- form에서 제외 필요
    - exclude or fields 설정

- 게시글 작성 시 에러 발생 : user_id 필드 데이터가 누락되어있다

- save의 commit을 활용해 작성 시 작성자 정보도 함께 저장해해야한다.

    ```python
    # views.py

    @login_required
    def create(request0):
        if request.method == 'POST':
            from = ArticleForm(request.POST)
            if form is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('articles:detail', article.pk)      
    ```


### 게시글 READ
- html에서 article.user로 작성자 받아오기 가능


### 게시글 UPDATE

- 게시글 수정 요청 사용자와 게시글 작성 사용자를 비교하여   
    본인의 게시글만 수정할 수 있도록 해야한다

    ```python
    # views.py

    @login_required
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.user == article.user:
            ...
        
        else:
            return redirect('articles:index')
    ```

- 해당 게시글의 작성자가 아니면     
 수정/삭제 버튼을 출력하지 않는다

    ```django
    {% if request.user == article.user %}
    <!-- 수정/삭제 버튼 위치 -->
    {% endif %}
    ```

### 게시글 DELETE

- 마찬가지로 삭제 요청하려는 사람과 게시글을 작성한 사람을 비교하여     
    본인의 게시글만 삭제할 수 있도록 하기
    
    ```python
    # views.py

    @login_required
    def delete(request, pk):
        article = Article.objects.get(pk=pk)
        if request.user == article.user:
            article.delete()
        return redirect('articles:index')
    ```

## Comment & User
### 모델 관계 설정

- 모델 관계 설정 - USER 외래 키 정의

    ```python
    # articles/models.py

    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        ...
    ```

- Migration
    - 이전과 동일한 상황
    - 기존 테이블에 빈 값으로 추가될 수 없기 때문에 기본 값 설정 과정 필요

### 댓글 CREATE

- 마찬가지로 동일한 에러 발생
- user_id 필드 데이터 누락

- 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 작성
    ```python
    # views.py

    def comments_create(request, pk):
        article = Article.objects.get(pk= pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article.pk)
        ...
    ```

### 댓글 READ

- 댓글 출력 시 댓글 작성자와 함께 출력
    
    ```html
    <!-- detail.html -->

    {% for comment in commenmts %}
    {{comment.user}} - {{comment.content}}
    {% endfor %}
    ```    

### 댓글 DELETE

- 삭제 요청 시 사용자 비교를 통해 본인 댓글만 삭제 가능하게
    
    ```python
    # views.py

    def comments_delete(request, article_pk, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
    ```

- 작성자가 아니면 댓글 삭제 버튼을 출력하지 않도록 추가하기
    ```django
    {% if request.user == comment.user %}
    <!-- 수정/삭제 버튼 위치 -->
    {% endif %}
    ```

## View decorators
- view 함수의 동작을 수정하거나 추가 기능을 제공하는 데 사용되는 python 데코레이터
    - 코드의 재사용성을 높이고 뷰 로직을 간결하게 유지'

- 데코레이터 종류
    - Allowed HTTP methods
    - Conditional view processing
    - GZip compresstion
    - ...

    - 공식문서서 https://docs.djangoproject.com/en/4.2/topics/http/decorators/


### Allowed HTTP methods
- 특정 HTTP method로만 view 함수에 접근할 수 있도록 제한하는 데코레이터

- 주요 Allowed HTTP methods
    
    1. require_http_mehtods(["METHOD1", "METHOD2", ...])
        - 지정된 HTTP method만 허용
        ```python
        from django.views.decorators.http import require_hjttp_methods

        @require_http_methods(['GET', 'POST'])
        def func(request):
            pass
        ```
    
    2.  require_safe()
        - GET과 HEAD method만 허용
        ```python
        from django.views.decorators.http import require_safe

        @require_safe
        def func(request):
            pass
        ```

    3. requie_POST
        - POST method만 허용
        ```python
        from django.views.decorators.http import require_POST

        @require_POST
        def func(request):
            pass
        ```

- 주요 특징
    - 지정되지 않은 HTTP method로 요청이 들어오면 HttpResponseNotAllowed (405)를 반환
        - 405 mdn 검색해보면 알 수 있다
        - Method Not Allowed
        - 클라이언트에서 오는 오류류

    - 대문자로 HTTP method 를 지정

- require_GET 대신 require_safe를 권장하는 이유
    - 웹 표준 준수
        - GET과 HEAD는 안전한 메소드로 간주됨
    
    - 호환성
        - 일부 소프트웨어는 HEAD 요청에 의존

    - 웹 표준을 준수하고, 더 넓은 범위의 클라이언트와 호환되며, 안전한 HTTP 메소드만을 허용하는 view 함수를 구현할 수 있음




## ERD
### 개요
- "Entity-Relationship Diagram"
- DB의 구조를  시각적으로 표현하는 도구
- Entity(개체), 속성, 그리고 엔티티간의 관계를 그래픽으로 나타낸다
- 시스템 논리적 구조를 모델링하는 다이어그램

- https://www.lucidchart.com/pages/er-diagrams
- ![alt text](image-23.png)
- ![alt text](image-24.png)

### ERD 구성 요소
1. Entity 엔티티
    - DB에 저장되는 객체나 개념
    - ex) 고객, 주문, 제품

2. Attribute 속성
    - 엔티티의 특성이나 성질
    - ex) 고객(이름,주소,전화번호)

3. Relationship 관계
    - 엔티티 간의 연관성
    - ex) 고객이 '주문'한 제품

- 개체와 속성
    - 개체 : 회원(User)
    - 속성 : 회원번호(id), 이름(name), 주소(addess) 등
        - 개체가 지닌 속성 및 속성의 데이터 타입

- 관계 : 회원과 댓글 간의 관계. 회원이 작성한 댓글

- Cardinality
    - 한 엔티티와 다른 엔티티 간의 수직 관계를 나타내는 표현

    - 주요 유형
    1. 일대일 (one-to-one, 1:1)
    2. 다대일 (many-to-one, N:1)
    3. 다대다 (many-to-many, M:N)

- Cardinality 표현
    - 선의 끝부분에 표시되며 일반적으로 숫자나 기호(까마귀 발)로 표현됨

    ![alt text](image-26.png)

- Cardinality 적용
    
    - 회원은 여러 댓글을 작성한다.

    - 각 댓글은 하나의 회원만 존재한다.
    - 그럼 user쪽은 one, comment쪽은 제로 or 매니


- ERD의 중요성
    - DB 설계의 핵심 도구
    - 시각적 모델링으로 효과적인 의사소통
    - 실제 시스템 개발 전 데이터 구조 최적화에 중요

### ERD 제작 사이트

- 무료 사이트
    - Draw.io (diagram=s.net)
        
        - 별도의 회원가입 없이 바로 사용 가능
        - 다양한 다이어그램 템플릿 제공
        - https://app.diagrams.net/
    
    - ERDCloud
        - 실시간 협업 기능 지원
        - https://www.erdcloud.com/


## 참고
### 추가 기능 구현

- 인증된 사용자만 댓글 작성 및 삭제

    - @login_required를 comments_create, comments_delete에 붙이기