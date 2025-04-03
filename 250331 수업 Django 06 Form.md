# Django Form

## 개요
- HTML form은 비정상적인 악의적인 요청 필터링이 불가능
- 유효한 데이터인지 확인 필요
- 유효성 검사 : 수집한 데이터가 정확하고 유효한지 확인하는 과정
    - 구현하기 위해선 입력 값, 형식, 중복, 범위, 보안 등 많은 것을 고려해야함
    - 직접 하지 않고 장고의 Form을 사용

## Form class 
- 사용자 입력 데이터를 수집하고 처리 및 유효성 검사를 수행하기 위한 도구
- 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공

### Form class 정의
```python
# articles/forms.py   경로나 이름 고정은 아니지만 보통 여기에 forms.py로 둠
from django import forms

class AticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```
- forms.Form이 models.Model처럼 클래스 상속받는 대상
- TextField 없다

### Form class를 적용한 new 로직
- .models 불러왔던 것처럼 view에서 적용

```python
# articles/views.py
from .forms import AticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
```
- html form 안쪽에서 {{form}} 으로 적용 가능
  
- ![image](https://github.com/user-attachments/assets/60f32959-7536-4797-8e3c-668f6831bdeb)

- html 속에서 {{form}} 하면 실제로 적용되는 html 구조

### Form rendering options
- label input쌍을 특정 HTML 태그로 감싸는 옵션(div로 감쌌던 것처럼)
- {{form.as_p}} 따위로 사용가능
- 가능한 것들은 공식 문서의 form-rendering-options 참조

**Form class가 불러오는 것이 무엇인지 확실히 이해하기**

## Widgets

- HTML **input** element 표현을 담당
- 단순하게 input 요소의 속성 혹은 출력되는 부분을 변경하는 것
```python
# articles/forms.py

from django import forms

class AticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget = forms.Textarea)
```
- 위에 있는 것처럼 표현하면 변경가능
- 공식문서 forms/widgets 참조

# Django ModelForm
- Form : 사용자 입력 데이터를 DB에 저장하지 않을때 (ex. 검색, 로그인)
- ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때 (ex. 게시글 작성, 회원가입)
- Model과 연결된 From을 자동으로 생성해주는 기능을 제공 (Form+Model)
- 왜 나왔는가? 생긴 거 봐바 비슷하잖아 model이랑. 그러니까 2번 쓰기 싫은거지

```python
# articles/forms.py

from django import forms
from .models import Article

class AticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget = forms.Textarea)
```
- 같은 결과가 출력됨! 왜?? model을 불러와서 거기에 맞는 폼을 제작해줌

## Meta class
- Model Form의 정보를 작성하는 곳(메타데이터 생각)

### fields 및 exclude 속성
- 일단 모델은 존재해야함
- fields로는 출력할 것들을 쓰기
- exclude로는 제외할 것들을 쓰기
- 전체 표현은 '\_\_all__' 

### 주의 사항
- 장고에서 모델폼에 대한 추가 정보나 속성을 작성하는 클래스 구조를 meta 클래스로 작성했을 뿐이며 파이썬의 inner class와 같은 문법적인 관점으로 접근하지 말것것

## ModelForm 적용
### ModelForm을 적용한 create 로직

```python
# articles views.py

from .forms import ArticleForm

def create(request):
    form = ArticleForm(request.POST)
    # 이제는 통째로 받아온다
    if form.is_valid():
        # 유효성 검사를 통과 한다면
        article = form.save()
        return redirect('articles:detail', article.pk)
    # 통과하지 못했다면
    # 현재 사용자가 게시글을 작성하는 템플릿을 다시 한 번 응답
    context = {
        # form이 유효성 검사를 거치면
        # 유효성 검사를 통과 못했던 이유를 담고 있다 
        'form' : form,
    }
    return render(request, 'articles/new.html', context)

```

- 제목 input에 공백을 입력 후 제출 시 에러 메세지 출력되는 것을 확인
- 유효성 검사의 결과

- is_valid() : 여러 유효성 검사를 실행하고 데이터가 유효한지 여부를 불리언으로 반환
- 별도로 명시하지 않아도 모델 필드에는 빈값은 허용하지 않는다
- 따라서 빈 값을 입력하면 is_valid는 False가 되고 form에 이유를 남겨서 다음 코드로 진행

### ModelForm을 적용한 edit 로직

```python
# articles views.py

from .forms import ArticleForm

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)

```

### ModelForm을 적용한 update 로직

```python
# articles views.py

from .forms import ArticleForm

def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)

```
## save 메서드

- DB 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드
- save()가 생성과 수정을 구분하는 방법?
    - instance 여부로 생성과 수정을 결정! 수정일떈 instance=article 쓴 것처럼


## Django Form 정리
- 사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구
- HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움


# HTTP 요청 다루기
## View 함수 구조 변화
- new&create view 함수 간 공통점과 차이점
    - 공통점 : 데이터를 생성을 구현하기 위함
    - 차이점 : new는 GET method 요청만을 create는 POST method 요청만을 처리
- 즉 차이점을 활용하면 함수를 합칠 수 있겠구나!

## new & ceate 함수 결합
### 새로운 create view 함수
- GET이면 new 행동, POST이면 create 행동
```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # POST가 아니라면 (GET, PUT, DELETE 등..)
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)

```
- 흐름을 확실히 이해해라 강의자료 주석 확인!
### 기존 new 관련 코드 수정 
- new url은 제거
- new 키워드 create으로 변경
- render에 new 템플릿을 create 템플릿으로 변경
### request method에 따른 요청의 변화
- articles/create/ 로 요청이 들어오지만
    - GET : 게시글 생성 페이지를 줘
    - POST : 게시글 생성해줘


## edit & update 함수 결합
- 같은 방식으로 합치기 edit을 update로 흡수 (POST가 아니라면)

# 참고
## ModelForm의 키워드 인자 구성
- 원래는 modelfrom(data=request.POST, instance=article) 인데 첫번째 키워드 인자라 생략가능 data는. instance는 9번째라 불가능
- 공식문서 참조

- 아래는 화장실 갔다오느라 못들음 다시 듣고 정리하기

## Widgets 응용

## 필드를 수동으로 렌더링

