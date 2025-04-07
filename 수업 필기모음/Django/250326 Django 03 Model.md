# Django 03 Model

## model class

- models.py는 Database와 소통을 하는 부분

- Django Model
    - DB의 테이블을 정의하고 데이터를 조작(CRUD)할 수 있는 기능들을 제공
    - 즉 테이블 구조 설계하는 청사진 blueprint

- DB는 SQL 언어로 소통해야하지만, 쟝고를 통해 파이썬 명령에서 SQL 명령으로 번역
- 따라서 models.py를 통해 DB에 접근


- model class 작성
    ```
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
    ```

- 모델 클래스 살펴보기
    - 다음과 같은 테이블 구조를 만들 예정    
    ![image-10](https://github.com/user-attachments/assets/d225f173-79d1-454b-81c3-86bc89f0cc27)

    - id는 쟝고에서 자체적으로 배정한다(고유한 값). 그래서 title, content만 생성
    - from django.db import models 로 쟝고의 models.py를 가져온다.
    - 거기에 있는 클래스를 상속받는다. 그 파일의 클래스 내용을 다 가져와서 새 클래스에 넣기
    - models.대문자 나오는 애들 다 클래스를 불러온 거
    - 모델 클래스 변수명 - 각 테이블의 필드(컬럼을 여기서 필드로 말한다) 이름
    - 모델 필드 클래스 
        - 각 변수명에 할당한 models. 뒤에 나오는 애들을 말함
        - DB 테이블의 열을 나타내는 중요한 구성요소
        - 데이터의 유형과 제약 조건을 정의

## Model Field
- DB 테이블의 Field(열)을 정의
- 해당 필드에 저장되는 Field types(데이터 타입)과 Field options(제약 조건)을 정의

### Field types
- DB에 저장될 데이터 종류를 정의(models 모듈의 클래스로 정의되어 있음)

- CharField : 제한된 길이의 문자열을 저장. 따라서 최대길이 max_length는 필수다. 공식문서 가봐라. 유효성 검사(validation?)

- TextField : 길이 제한이 없는 대용량 텍스트 (무한대x 시스템따라 다름)

- 주요 필드 유형
    - 문자열
    - 숫자
    - 날짜/시간
    - 파일

### Field options
- 필드의 동작과 제약조건을 정의
- 공통 제약 조건이 존재함 모든 경우에 사용가능?

- 제약 조건(Constraint)
    - 특정 규칙을 강제하기 위해 테이블의 행렬에 적용되는 규칙 or 제한사항
    - ex 숫자만 저장되도록, 문자가 100자만 저장되도록 등

- 주요 필드 옵션
    - null : DB에서 NULL 허용할지? (DB에서 파이썬 None과 같음, 기본값 False)
    - blank : form에서 빈 값을 허용할지?(기본값 False)
    - default : 필드의 기본값을 설정


## Migrations

- model 클래스의 변경사항(생성 수정 삭제 등)을 DB에 최종 반영하는 방법

- models.py의 modle class에서 설계도 초안을 제작
- **makemigrations**를 통해 migrations 폴더에 migration 파일을 생성? 수정?
- **migrate**를 통해 db.sqlite3(DB) 와 통신

- 핵심 명령어 2가지
```
$ python manage.py makemigrations
$ python manage.py migrate
```
- db 파일 안에서 확인가능.
- 테이블 이름은 앱이름_클래스이름
- 기본앱들이 있기 떄문에 여러개 있는 게 정상

### 추가 Migrations

- 이미 생성된 테이블에 필드를 추가해야 한다면??

- DateTimeField 필드 옵션(optional)
    - auto_now : 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장
    - auto_now_add : 데이터가 처음 생성 될 때만 자동으로 현재 날짜 시간을 저장


- 추가 모델 필드 작성   
    1.  modles.py에 새 필드 설정    
    ![image-11](https://github.com/user-attachments/assets/df9b7e8f-3885-450e-8372-9f2859486f6a)

    2. 이미 기존 테이블이 존재하므로 필드를 추가 할 때 필드의 기본 값 설정이 필요.
        - 현재 대화 유지하면서 직접 기본 값 입력하기 (이번엔 이걸로)
        - 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법
    3. 추가하는 필드의 기본 값을 입력해야한다
        - 왜? 기존에 있던 값들에 넣어줘야하는 값
        - 날짜 데이터이기 때문에 직접 입력보단 Django의 제안 기본값을 사용하자
        - 아무것도 입력하지 않고 enter하면 Django가 제안하는 기본 값으로 설정됨
    4. migrations 이후 2번째 migration 파일이 생성됨 (커밋마냥 문제 생기면 이전으로 돌아가기 가능, 대신 의존 후 추가만 작성되므로 앞쪽이 삭제되면 불가능)
    5. migrate 후 테이블 필드 변화 확인

**model class에 변경사항(1)이 생기면**

**반드시 새로운 설계도를 생성(2)하고**

**이를 DB에 반영(3)해야 한다**

1. model class 변경 -> 2. makemigrations -> 3. migrate 

## Admin site
### 관리자 인터페이스
- Automatic admin interface
    - Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스
    - 데이터 확인 및 테스트 등을 진행하는데 매우 유용
1. admin 계정 생성
    - email은 선택사항
    - 비밀번호 입력 시 보안상 터미널에 출력되지 않는다! 입력 이어가라
    - $ python manage.py createsuperuser
2. DB에 생성된 admin 계정 확인
    - auth_user에 있다. 이 테이블에 유저가 저장됨
    - 관리자/스태프/일반 기본 구분은 is_00 로 확인 가능
    - is_active는 휴면
    - DB 저장 시간은 UTC 기준
3. admin에 모델 클래스 등록
    -  admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능
    - from .models import Article
    - admin.site.register(Article)
4. admin site 로그인 후 등록된 모델 클래스 확인
5. 데이터 생성 수정 삭제 테스트
6. 테이블 확인


## 참고

### DB 초기화
1. migration 파일 삭제
2. db.sqlite3 파일 삭제
**_init__.py나 migrations 폴더는 삭제하지마라**

### Migrations 관련
python manage.py 기타명령어
- showmigrations
    - migrations 파일들이 migrate 됐는지 안 됐는지 여부를 확인 가능
    - [X] 표시가 있으면 migrate가 완료되었음을 의미
- sqlmigrate articles 0001
    - 해당 migrations 파일들이 SQL언어로 어떻게 번역되어 DB로 전달되는지 확인 가능

### SQLite
- DB 관리 시스템 중 하나로 Django의 기본 db로 사용됨(파일로 존재, 가벼움, 호환성 좋음)
