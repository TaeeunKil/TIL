# Django 08 Authentication System

## Cookie & Session
### HTTP
- HTML 문서와 같은 리소스를 가져올 수 있도록 해주는 규약. 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초
- 특징
    - 비 연결 지향(connectionless) : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
    - 무상태 (stateless) : 연결을 끊는 순간 클라이언트 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
- 예를들면 장바구니에 담은 상품 유지, 로그인 상태 유지 불가능

### 쿠키
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 서버가 제공하여 클라이언트에 저장되는 작은 데이터 파일
- 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

- 예시
    1. 브라우저가 웹 서버에 웹 페이지를 요청
    2. 웹 서버는 요청된 페이지와 함께 쿠키를 포함한 응답을 브라우저에게 전송
    3. 브라우저는 받은 쿠키를 저장소에 저장. 속성(만료 시간, 도메인, 주소 등)도 함께 저장됨
    4. 이후 브라우저가 같은 웹 서버에 웹 페이지를 요청할 때, 저장된 쿠키 중 해당 요청에 적용 가능한 쿠키를 포함하여 함께 전송
    5. 웹 서버는 받은 쿠키 정보를 확인하고, 필요에 따라 사용자 식별, 세션 관리 등을 수행
    6. 웹 서버는 요청에 대한 응답을 보내며, 필요한 경우 새로운 쿠키를 설정하거나 기존 쿠키를 수정

- 장바구니 예시
    - 개발자 도구 - Network - cartView.pang 확인
    - 서버는 응답과 함께 Set-Cookie 응답 헤더를 브라우저에 전송 (클라이언트에게 쿠키를 저장하라고 전달하는 것)
    - 저장된 상태를 무식하게 쿠키 요청을 계속 보내서 헤ㅐ당 상태를 보여주는 것
    - 쿠키를 비우면 장바구니도 사라진다

- 쿠키의 작동 원리와 활용
    1. 쿠키 저장 방식
        - 브라우저(클라이언트)는 쿠키를 KEY-VALUE의 형태로 저장
        - 쿠키에는 이름, 값 외에도 만료 시간, 도메인, 경로 등의 추가 속성이 포함됨
    2. 쿠키 전송 과정
        - 서버는 HTTP 응답 헤더의 Set-Cookie 필드를 통해 클라이언트에게 쿠키를 전송
        - 브라우저는 받은 쿠키를 저장해두었다가, 동일한 서버에 재요청 시 HTTP 요청 Header의 Cookie 필드에 저장된 쿠키를 함께 전송
    3. 쿠키의 주요 용도
        - 두 요청이 동일한 브라우저에서 들어왔는가?
        - 이를 이용해 사용자의 로그인 상태 유지 가능
        - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억시켜 주는 역할
    - 서버에게 나 로그인된 사용자야 라는 인증 정보가 담긴 쿠키를 매 요청마다 계속 보내는 것

- 쿠키 사용 목적
    1. 세션 관리(Session management)
        - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
    2. 개인화(Personalization)
        - 사용자 선호 설정(언어 설정, 테마 등) 저장
    3. 트래킹(Tracking)
        - 사용자 행동을 기록 및 분석
        
### 세션
- 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지. 상태 정보를 저장하는 데이터 저장 방식
- 쿠키에 담겨오는 데이터가 세션 데이터로 매 요청시마다 세션 데이터가 들어오는 것

- 작동 원리
    1. 클라리언트가 로그인 요청 후에 인증에 성공하면 서버가 session 데이터를 생성 후 저장
    2. 생성된 session 데이터에 인증할 수 있는 session id를 발급
    3. 발급한 session id를 클라이언트에게 응답 (데이터는 서버에 저장, 열쇠만 주는 것)
    4. 클라이언트는 응답 받은 session id를 쿠키에 저장
    5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함꼐 쿠키(session id가 저장된)를 서버에 전달
    6. 쿠키는 요청 때마다 서버에 전송되므로 서버에서 session id를 확인해 로그인 되어있다는 것을 계속해서 확인하도록 함

- 두 줄 요약
    1. 서버에서는 세션 데이터를 생성 후 저장하고 이 데이터에 접근할 수 있는 세션 ID를 생성하고 이 ID를 클라이언트 측으로 전달하면 클라이언트는 쿠키에 이 ID를 저장
    2. 이후 클라이언트가 같은 서버에 재요청 시마다 저장해 두었던 쿠키도 요청과 함께 전송


## Django Authentication System
- 사용자 인증과 관련된 기능을 모아 놓은 시스템
- Authentication(인증) : 사용자가 자신이 누구인지 확인하는 것(신원 확인)
- 사전 준비
    - 두 번째 app accounts 생성 및 등록
    - auth와 관련된 키워드나 경로가 내부적으로 accounts라는 이름으로 사용하고 있으므로 되도록 accounts로 지정하는 것을 권장


## Custom User model
- 이미 admin 하면서 해본 것. 내장되어있다
- 
### User model 대체하기
- 기존 User Model의 한계
    - 지금까지 별도의 정의 없이 내장된 auth 앱에 작성된 User 클래스를 사용했음
    - Django의 기본 User 모델은 username, password 등 제공되는 필드가 매우 제한적
    - 추가적인 사용자 정보(예: 생년월일, 주소, 나이 등)이 필요하다면 이를 위해 기본 User Model을 변경하기 어려움
        - 별도의 설정 없이 사용할 수 있어 간편하지만 개발자가 직접 수정하기 어려움
    - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L406
- 내장되어있다
    - settings.py에 apps 보면 django.contrib.auth
    - 찾아가보면 AbstractUser를 상속받는 껍데기 형태로 존재하는데 AbstractUser가면 모델 확인 가능
    - 우리는 그 상속 형태를 따라가면 된다!
- User Model 대체의 필요성
    - 프로젝트 특정 요구사항에 맞춰 사용자 모델을 확장할 수 있음
    - 예를 들어 이메일을 username으로 사용하거나, 다른 추가 필드를 포함시킬 수 있음

- Custom User Model
    - AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성
    - 기존 User 클래스도 AbstractUser를 상속받기 떄문에 커스텀 해도 같은 모습을 가진다
    ```python
    # accounts/models.py

    from django.contrib.auth.models import AbstractUser

    class User(AbstratUser):
        pass
    ```
    - django 프로젝트에서 사용 중인 기본 User 모델을 우리가 작성한 User 모델로 사용할 수 있도록 AUTH_USER_MODEL 값을 변경 (수정 전 기본 값은 auth.User)
    - AUTH_USER_MODEL은 settings.py에 없던 값이라 추가해줘야한다.
    ```python
    # settings.py

    AUTH_USER_MODEL = 'accounts.User'
    ```
    - admin site에 대체한 User 모델 등록
        - 기본 모델이 아니라 등록하지 않으면 admin 페이지에 출력되지 않는다
    ```python
    # accounts/admin.py

    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User

    admin.site.register(User, UserAdmin)
    ```

- **주의** 프로젝트 중간에 AUTH_USER_MODEL를 변경할 수 없음!1!!
- auth_user 테이블 자체가 accounts_user 테이블로 바뀌는 것으로 db를 아예 초기화 하고 해야한다.
- 프로젝트를 시작할 때 무조건 User 모델을 대체해야 한다.
    - 장고 측에서 강력하게 권장한다 커스텀 User 모델을 설정하라고
    - 커스텀 User 모델은 기본 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있음
    - 단, 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 한다.


## Login
- Login은 Session을 Create하는 과정(회원가입은 User을 Creat해서 DB에 저장하는 과정)
- AuthenticationForm()
    - 로그인 인증에 사용할 데이터를 입력 받는 built-in form
- 로그인 페이지 작성
  - accounts/urls.py
    ```python
    app_name = 'accounts'
    urlpatterns = [
        path('login/', views.login, name='login'),
    ]

    ```
  - accounts/views.py
    ```python
    # 초기 버전
    from django.contrib.auth.forms import AuthenticationForm
    
    def login(request):
        if request.method == 'POST':
            pass
        else:
            form = AuthenticationForm()
            context = {
                'form': form,
            }
        return render(request, 'accounts/login.html', context)

    ```
  - accounts/login.html
    ```
    <h1>로그인</h1>
    <form action="{% url 'accounts:login' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>

    ```
  - 말로해보기
    ```
    from django.contrib.auth.forms import AuthenticationForm

    urls에 login 추가
    html에 login form POST, form.as_p로 작성
    views에 request.method == 'POST'라면 데이터를 받아들일거고 (당장은 pass)
    아니라면 form = AuthenticationForm() 받는다
    login.html 화면 전달
    ```
    그러면 AuthenticationForm으로 나오는 걸 확인 가능        
    ![image-2](https://github.com/user-attachments/assets/05d3ba74-d7a2-4d0d-a34f-3e471a20c634)


- 로그인 로직 작성
  - 코드
    ```python
    # accounts/views.py (완성된 버전)
    from django.shortcuts import render, redirect
    from django.contrib.auth import login as auth_login
    from django.contrib.auth.forms import AuthenticationForm
    
    def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            # form = AuthenticationForm(request, data=request.POST) 도 가능
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('articles:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)

    ```
  - 말로 표현해보기
    ```
    from django.contrib.auth import login as auth_login
    
    request.method == 'POST'라면
    form = AuthenticationForm(request, request.POST)
    첫번째 인자 request, 두번째 인자는 data
    
    유효성 검사 통과하면
    auth_login 하는데 첫번쨰 인자는 request, 두번째는 로그인 인증된 유저 객체(form.get_user())
    
    return은 redirect
    ```

- login(request, user) : AuthenticationForm을 통해 **인증된** 사용자를 로그인 하는 함수

- get_user() : AuthenticationForm의 인스턴스 메서드로 유효성 검사를 통과하면 로그인 한 인증된 사용자 객체를 반환

- 세션 데이터 확인하기
    - 로그인하고 발급받았다면 django_session 테이블에서 확인 가능
    - 브라우저에서 개발자 도구 - Application - Cookies에서 확인가능

## Logout
- Logout은 Session을 Delete하는 과정
- logout(request)
    - DB에서 현재 요청에 대한 Session Data를 삭제
    - 클라이언트의 쿠키에서도 Session Id를 삭제

- 로직 작성
- accounts/urls.py
    ```python
    
    urlpatterns = [
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
    ]
    ```
- articles/index.html
  ```html
    <!-- articles/index.html -->
    <h1>Articles</h1>
    <a href="{% url 'accounts:login' %}">Login</a>
    <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
    </form>
  ```
- accounts/views.py
  ```python
  # accounts/views.py
    from django.contrib.auth import logout as auth_logout

    def logout(request):
        auth_logout(request)
        return redirect('articles:index')
  ```

- 말로 요약해보기
    ```
    urls에 추가
    
    html은 submit 버튼만 있으면 된다 요청은 logout 링크로
    
    views에서는 from django.contrib.auth import logout as auth_logout을 받아오고 auth_logout(request)하면 끝
    
    redirect로 화면 돌아가기기
    ```


## Template with Authentication data
- 템플릿에서 인증 관련 데이터를 출력하는 방법
- 예를 들어 현재 로그인 되어있는 유저 정보를 출력하고 싶다면?
    ```html
    <h3> Hello {{user.username}} </h3>
    ```
- user라는 context 데이터 사용 가능한 이유는 장고가 미리 준비한 context가 존재한다.

- context processors
    - 템플릿이 렌더링 될 때 호출 가능한 context 데이터 목록
    - 작성된 context 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨 
    - 자주 사용하는 데이터 목록을 미리 템플릿에 로드한 것으로 settings에 있다
    ![image-3](https://github.com/user-attachments/assets/00b33ec2-50b7-4110-8bfb-3759705c871e)

## 참고
### 쿠키의 수명
1. Session cookie
    - 현재 세션 종료 시 삭제
    - 브라우저 종료 시 삭제
2. Persistent cookies
    - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

### 쿠키와 보안
- 제한된 정보 : 쿠키에는 중요하지 않은 정보만 저장(사용자 ID, 세션 번호)
- 암호화 : 중요한 정보는 서버에서 암호화해서 쿠키에 저장
- 만료 시간 : 쿠키에는 만료 시간을 설정해서 시간 지나면 자동 삭제
- 도메인 제한 : 쿠키는 특정 웹사이트에서만 사용할 수 있도록 설정할 수 있음
- 많은 국가에서 쿠키 사용에 대한 사용자 동의를 요구하는 법규를 시행
- 웹사이트는 쿠키 정책을 명시하고 필요하면 동의 얻어야함

### Django에서의 세션 관리
- database-backed sessions 저장 방식을 기본 값으로 사용
- session 정보는 DB의 django_session 테이블에 저장
- 요청 속 특정 session를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 데이터를 알아냄

### AuthenticationForm 내부 코드
- AuthenticationForm() - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L316
- 위의 get_user() 인스턴스 메서드 - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L387

### AbstractUser class
- 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본 클래스
- 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
- DB 테이블을 만드는 데에 사용되지 않는다
- 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨
- models.Model -> class AbstractBaseUser -> class AbstractUser -> class User 순으로 상속된

### User 모델 대체하기 Tip
- 공식문서 보면서 순서대로 진행하는 것을 권장
- https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model
