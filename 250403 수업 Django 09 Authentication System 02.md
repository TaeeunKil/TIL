# Django 09 Authentication System 02

## 회원 가입
- User 데이터를 Create 하는 과정! 즉 GET이면 페이지 POST면 유저 생성
- UserCreationForm()
    - 회원 가입시 사용자 입력 데이터를 받는 built-in **ModelForm**
    - DB에 저장하기 위한 회원가입이기 때문에 모델폼이다. 그러면 형식 
    
### 페이지와 로직 작성

- url.py
    ```python
    urlpatterns = [
        path('signup/', views.signup, name='signup'),
        ]
    ```
- views.py
    ```python
    from django.contrib.auth.forms import UserCreationForm

    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            # 회원가입 템플릿과 회원정보 작성을 위한 form을 응답
            form= UserCreationForm()
        context = {
            'form' : form,
        }
        return render(request, 'accounts/signup.html', context)
    ```
- signup.html
    ```html
    <body>
        <h1>회원가입</h1>
        <form form action="{% url 'accounts:signup' %}" method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit">
        </form>
    </body>
    ```


- settings.py의 LANGUAGE_CODE = 'ko-kr'로 한글화 가능능
- ![image-4](https://github.com/user-attachments/assets/aab6288f-e993-4079-8ccf-353c9381df55)


### 그러면 로직 에러가 난다

- ![image-5](https://github.com/user-attachments/assets/5aeb4f03-d448-4ec8-94fb-b893a5404d02)![image-6](https://github.com/user-attachments/assets/10aa2af7-0b84-4fe3-9383-ad038854398a)

- 회원 가입에 사용하는 UserCreationForm이 과거 Django 기본 유저 모델로 인해 작성된 클래스

- 즉 우리가 만들었던 그 커스텀 유저폼으로 안 바뀐 빌트인 모델을 썼다는 에러

### 커스텀 모델로 덮어쓰기
- 커스텀 유저 모델을 사용하려면 다시 작성해야하는 Form
    - UserCreationForm : 회원 가입, UserChangeForm : 회원정보 수정
    - 둘 다 clase Meta: model=User이기 떄문에 재작성해야한다
- 상속 후 일부분만 재작성
    ```python
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm
    from django.contrib.auth import get_user_model

    class CustomUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
    
    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
    ```
- 상속을  from .models import User, model=User 로 안하는 이유?
    - get_user_model()
        - 현재 프로젝트에서 활성화된 사용자 모델을 반환하는 함수
        - 결과로 User object를 받아온다
    - get_user_model()을 사용해 User 모델을 참조하면 커스텀 User 모델을 자동으로 반환해주기 때문
    - Django는 필수적으로 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조하고 있음
    
    - 이후에도 이렇게 쓰는 경우가 생길 것

### 회원 가입 로직 수정
- CustionUserCreationForm으로 변경
- views.py
    ```python
    from .forms import CustomCreationForm

    def signup(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 회원가입 템플릿과 회원정보 작성을 위한 form을 응답
        form= CustomCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
    ```


## 회원 탈퇴

- User 객체를 Delete 하는 과정

### 페이지와 로직 작성
- url.py
    ```python
    urlpatterns = [
        path('delete/', views.delete, name='delete'),
        ]
    ```
- views.py
    ```python
    def delete(request):
        request.user.delete()
        return redirect('articles:index')
    ```
- index.html
    ```html
    <form form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원 탈퇴">
    </form>
    ```

## 회원 정보 수정
- User 객체를 Update 하는 과정
- UserChangeForm() : 회원 정보 수정 시 사용자 입력 데이터를 받는 buit-in **ModelForm**

### 회원 정보 수정 페이지 작성

- url.py
    ```python
    urlpatterns = [
        path('update/', views.update, name='update'),
        ]
    ```
- views.py
    ```python
    from .forms import CustomUserChangeForm

    def update(request):
        if request.method == 'POST':
            # 기존 유저 정보 instance = request.user
            form = CustomUserChangeForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            # 회원가입 템플릿과 회원정보 작성을 위한 form을 응답
            form= CustomUserChangeForm(instance=request.user)
        context = {
            'form' : form,
        }
        return render(request, 'accounts/update.html', context)
    ```
- signup.html
    ```html
    <body>
        <h1>회원 정보 수정</h1>
        <form form action="{% url 'accounts:update' %}" method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit">
        </form>
    </body>
    ```

### UserChangeForm 그냥 사용 시 문제점
- User모델의 모든 정보들(fields)까지 모두 출력됨
- admin 시점에서 사용가능하게 만들어져있기 때문
- 일반 사용자들이 접근해서는 안되는 정보는 출력하지 않도록 해야 함
- **즉 CustomUserChangeForm에서 출력 필드를 조정!!**

### CustomUserChangeForm 출력 필드 재정의
- User Model의 필드 목록을 먼저 확인
    - https://docs.djangoproject.com/en/4.2/ref/contrib/auth/
- form.py
    ```python
    class CustomUserChangeForm(UserChangeForm):
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
            fields = ('first_name','last_name', 'email',)
    ```

## 비밀 번호 변경
- 인증된 사용자의 Session 데이터를 Update 하는 과정
- PasswordChangeForm() : 비밀번호 변경 시 사용자 입력 데이터를 받는 built-in **Form**
### 비밀번호 변경 페이지 작성
- ![image-8](https://github.com/user-attachments/assets/275e2a36-26f1-4fff-bd72-a7a8f183cf13)

- djnango는 비밀번호 변경 페이지를 회원정보 수정 form 하단에서 별도 주소로 안내 : /user_pk/password/
- 굳이 안 따라도 되지만 추천하는 느낌?

-  project/url.py
    ```python
    urlpatterns = [
        path('<int:user_pk>/password/', views.change_password, name='change_password'),
        ]
    ```
- views.py
    ```python
    from django.contrib.auth.forms import PasswordChangeForm

    def change_password(request, user_pk):
        if request.method == 'POST':
            # data = request.POST
            # user = request.user 의 느낌
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            # 회원가입 템플릿과 회원정보 작성을 위한 form을 응답
            form= PasswordChangeForm(request.user)
        context = {
            'form' : form,
        }
        return render(request, 'accounts/change_password.html', context)
    ```
- change_password.html
    ```html
    <h1>비밀번호 변경</h1>
    <form form action="{% url 'change_password' user.pk %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
    ```

### 세션 무효화 방지
- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못하고 로그아웃 처리됨
- 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
- update_session_auth_hash(request, user)
    - 암호 변경 시 세션 무효화를 막아주는 함수
    - 암호가 변경되면 새로운 password의 Session Data로 기존 session을 자동으로 갱신
- views.py
    ```python
    from django.contrib.auth.forms import PasswordChangeForm
    from django.contrib.auth import update_session_auth_hash
    # update_session_auth_hash 불러오기

    def change_password(request, user_pk):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                # 이 부분이 달라진다
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('articles:index')
        else:
            form= PasswordChangeForm(request.user)
        context = {
            'form' : form,
        }
        return render(request, 'accounts/change_password.html', context)
    ```

## 로그인 사용자에 대한 접근 제한
- 2가지 방법이 있다 
- is_authenticated 속성, login_required 데코레이터

### is_authenticated 속성
- 사용자가 인증되었는지 여부를 알 수 있는 User model의 속성 boolean
    - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
    - 비인증 사용자에 대해서는 항상 False

- index.html
    ```html
    {% if request.user.is_authenticated %}

    {% else %}
    ```
    user.is_authenticated로도 사용 가능     
    로그인과 비로그인 상태에서 화면 출력을 다르게 설정 가능

- views.py
    ```python
    def login(request):
        if request.user.is_authenticated:
            return redirect('articles:index')
    
    def signup(requset):
        if requset.user.is_authenticated:
            return redirect('articles:index') 
    ```
    인증된 사용자라면 로그인/회원가입 로직을 수행할 수 없도록 하기 가능


### login_required 데코레이터
- 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터
- 비인증 사용자의 경우 /accounts/login/ 주소로 redirect 
- 적용하기
    - views의 함수 위에 @login_required를 붙인다
    ```python
    from django.contrib.auth.decorators import login_required

    @login_required
    def create(request):
        pass
    ```
    - 위 형태로 적용가능
    - 게시글 작성/수정/삭제 또는 로그아웃/탈퇴/수정/비밀번호 변경

## 참고
### is_authenticated 코드
- 메서드 아니다! 속성이다 () 없어도 된다
- ![image-9](https://github.com/user-attachments/assets/fbbfccf3-bee3-4dc0-8343-5127785f5745)

- https://github.com/django/django/blob/main/django/contrib/auth/base_user.py#L85

### 회원가입 후 자동 로그인?
- 회원가입 성공한 user 객체로 login 진행하는 코드를 추가
- 유효성 검사를 통과 했을 때 작동되게
- views.py
    ```python
    def signup(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            # 이부분이 추가됨
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form= CustomCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
    ```

### 회원 탈퇴 개선
- 탈퇴와 함께 기존 사용자의 Session Data를 삭제하고싶다

- 사용자 객체 삭제 이후 logout을 불러오자
- **단, 탈퇴(1) 후 로그아웃(2)의 순서가 바뀌면 안된다**
- 먼저 로그아웃이 진행되면 해당 요청 객체 정보가 없어지기 떄문에 탈퇴에 필요한 유저 정보 또한 없어지기 때문
- views.py
    ```python
    def delete(request):
        request.user.delete()
        auth_logout(request)
    ```
### PassworChangeForm 인자 순서
- PasswordChangeForm이 다른 Form이랑 다르게 인자를 받는 이유?

- 부모 클래스인 SetPasswordForm의 생성자 함수 구성을 따르기 떄문에
- user 객체를 첫번째로 받는다.
- ![image-10](https://github.com/user-attachments/assets/cde1d1d6-c66d-4c56-940d-f1d5c0f97d9e)

https://github.com/django/django/blob/4.2/django/contrib/auth/forms.py#L378

### Auth buit-in form 코드

- UserCreationForm()
    - https://github.com/django/django/blob/4.2/django/contrib/auth/forms.py#L149
- UserChangeForm()
    - https://github.com/django/django/blob/4.2/django/contrib/auth/forms.py#L170
- PasswordChangeForm()
    - https://github.com/django/django/blob/4.2/django/contrib/auth/forms.py#L422
