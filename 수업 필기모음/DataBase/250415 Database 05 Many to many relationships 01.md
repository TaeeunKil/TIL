# Database 05 Many to many relationships 01

## Many to many relationships

- N:M or M:N

- 한 테이블의 0개 이상의 레코드가 다른 테이블 0개 이상의 레코드와 관련된 경우
- **양쪽 모두에서 N:1 관계를 가짐!!**

- M:N 관계의 역할과 필요성 이해하기
    - 병원 진료 시스템 모델 관계를 만들며 M:N 관계의 역할과 필요성 이해하기
    - 환자와 의사 2개의 모델을 사용하여 모델 구조 구상하기

    - 제공된 99-mtm-pratice 프로젝트를 기반으로 진행

### N:1의 한계

- 예시
    - 의사와 환자 간 모델 관계 설정을 한다고 가정해보자
    - 한 명의 의사에게 여러 환자가 예약할 수 있다면
    - 1번 환자가 두 의사 모두에게 진료 받고자 하는 경우 

    - 환자 테이블에 1번 환자가 중복으로 입력되는 경우가 생긴다
    - 외래 키 컬럼에 1,2 형태로 저장하려면 DB타입 이슈도 생긴다
    - 예약 테이블을 따로 만들자!!

### 중개 모델

#### 1. 예약 모델 생성

- 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 생성

- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

    ```python
    from django.db import models


    class Doctor(models.Model):
        name = models.TextField()

        def __str__(self):
            return f'{self.pk}번 의사 {self.name}'


    # 외래키 삭제
    class Patient(models.Model):
        name = models.TextField()

        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'


    # 중개모델 작성
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

        def __str__(self):
            return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    ```

- 왜래키를 다 받아온다


#### 2. 예약 데이터 생성

- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행

- 의사와 환자 생성 후 에약 만들기

    ```python
    doctor1 = Doctor.objects.create(name='allie')
    patient1 = Patient.objects.create(name='carol')

    Reservation.objects.create(doctor=doctor1, patient=patient1)
    ```

#### 3. 예약 정보 조회

- 의사와 환자가 예약 모델을 통해 각각 본인의 진료 내역 확인
    ```python
    doctor1.reservation_set.all()
    
    patient1.reservation_set.all()
    ```

#### 4. 추가 예약 생성

- 1번 의사에게 새로운 환자 예약 생성
    ```python
    patient2 = Patient.objects.create(name='duke')

    Reservation.objects.create(doctor=doctor1, patient=patient2)
    ```

- 예약 모델에 새롭게 생성되는 것을 확인

#### 5. 예약 정보 조회

- 1번 의사의 예약 정보 조회하면 2개 나오는 것을 확인가능능




**Djnago에서는 'ManyToManyField'로 중개모델을 자동으로 생성**

### ManyToManyField

- M:N 관계 설정 모델 필드

- Django ManyToManyField
    
    - 환자 모델에 ManyToManyField 작성
        - 의사 모델에 작성해도 상관 없다(1:N과의 차이점!!) 
        
        - 대신 참조/역참조 관계를 기억해야 한다
            - 필드를 쓴 곳에서 안 쓴 곳으로 탐색하는 게 참조
            - 필드를 안 쓴 곳에서 쓴 곳으로 탐색하는 게 역참조

        ```python
        from django.db import models


        class Doctor(models.Model):
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 의사 {self.name}'


        class Patient(models.Model):
            # ManyToManyField 작성
            doctors = models.ManyToManyField(Doctor)
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 환자 {self.name}'        
        ```

    - DB 초기화 후  migration하면 생성된 중개 테이블 hospitals_patient_doctors 확인 가능

    
    - 예약 생성 (환자가 예약)

        ```python
        # patient1이 doctor1에게 예약
        patient1.doctors.add(doctor1)
        
        # patient1 - 자신이 예약한 의사목록 확인
        patient1.doctors.all()

        # doctor1 - 자신이 예약된 환자목록 확인
        doctor1.patient_set.all()
        ```

    - 예약 생성 (의사가 예약)

        ```python
        # doctor1이 patient2을을 예약
        doctor1.patient_set.add(patient2)

        # doctor1 - 자신의의 예약 환자목록 확인
        doctor1.patient_set.all()

        # patient1, 2 - 자신이 예약한 의사목록 확인
        patient2.doctors.all()
        patient1.doctors.all()
        ```
    - 중개 테이블에서 예약 현황 확인 가능능
    - 예약 취소하기
        - 이전에는 Reservation 찾아서 지워야 했다면 이제는 .remove()로 삭제 가능
    
        ```python
        # doctor1이 patient1 진료 예약 취소
        doctor1.patient_set.remove(patient1)
        doctor1.patient_set.all()
        patient1.doctors.all()
        
        # patient2가 doctor1 진료 예약 취소
        patient2.patient_set.remove(doctor1)
        patient2.doctors.all()
        doctor1.patient_set.all()

        ```

**만약 예약 정보에 병의 증상, 예약일 등 추가 정보가 포함되어야 한다면??**

### through argument

- 중개 테이블에 **'추가 데이터'**를 사용해 M:N 관계를 형성하려는 경우에 사용

- 'through' argument
    - Reservation Class 작성 및 through 설정
        - ManyToManyField는 2개만 만들어줘서 추가하려면 새로운 클래스가 필요

        - 대신 through 인자를 통해 연결한다다

        - 예약 정보에 '증상' 과 '예약일' 추가

        ```python
        from django.db import models


        class Doctor(models.Model):
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 의사 {self.name}'


        class Patient(models.Model):
            doctors = models.ManyToManyField(Doctor, through='Reservation')
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 환자 {self.name}'


        class Reservation(models.Model):
            doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
            patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
            symptom = models.TextField()
            reserved_at = models.DateTimeField(auto_now_add=True)

            def __str__(self):
                return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
        ```
    
    - 데이터베이스 초기화 후 migration 진행
    - 의사 1명과 환자 2명 생성

    - 예약 생성 방법 - 1
        -  Reservation class를 통한 예약 생성

            ```python
            # 1. Reservation class를 통한 예약 생성
            reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')

            reservation1.save()

            doctor1.patient_set.all()

            patient1.doctors.all()
            ```

    
    - 예약 생성 방법 - 2
        
        - Patient 또는 Doctor의 인스턴스를 통한 예약 생성 **(through_defaults)**

            ```python
            # 2. Patient 객체를 통한 예약 생성
            patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})

            doctor1.patient_set.all()

            patient2.doctors.all()
            ```
        
    - 생성과 마찬가지로 의사 환자 모두 각각 예약 삭제 가능

        ```python
        doctor1.patient_set.remove(patient1)

        patient2.doctors.remove(doctor1)
        ```

- M:N 주요 사항
    - M:N 관계로 맺어진 두 테이블에는 물리적 변화 없음
    - ManyToManyField는 중개 테이블을 자동으로 생성
    - ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
        - 다만 작성 위치에 따른 참조/역참조 방향 주의
    
    - N:1은 완전한 종속이었지만 M:N은 종속적인 관계가 아님
    - '의사에게 진찰받는 환자 & 환자를 진찰하는 의사' 이렇게 2가지의 형태 모두 표현 가능

## ManyToManyField

- ManyToManyField(to, **options)
    - M:N 관계 설정 시 사용하는 모델 필드

- 특징
    - 양방향 관계 : 어느 모델에서든 관련 객체에 접근할 수 있음
    - 중복 방지 : 동일한 관계는 한 번만 저장됨

- 대표 인자 3가지
    - related_name
        - 역참조시 사용하는 manager name을 변경
            ```python
            class Patient(models.Model):
                # ManyToManyField - related_name 작성
                doctors = models.ManyToManyField(Doctor, related_name='patients')
            ```
        - 환자.doctors.메서드()처럼 의사.patient_set.메서드()를 의사.patients.메서드()로 만들 수 있다
        - 1:N 외래키에서도 가능하나 권장하지 않는다

    - symmetrical
        - 관계 설정 시 대칭 유무 설정

        - ManyToManyField가 동일한 모델(재귀적인, 대댓글따위)을 가리키는 정의에서만 사용
        - 기본은 True
            - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)

            - 즉, 내가 당신의 친구라면 자동으로 당신도 내 친구가 됨

            - source - 관계를 시작하는 모델
            - target - 관계의 대상이 되는 모델

        - False일 경우 : True와 반대로 대칭되지 않음  

    - through
        - 사용하고자 하는 중개모델을 지정
        - 일반적으로 추가 데이터를 M:N관계와 연결하려는 경우에 활용

- M:N에서의 대표 조작 methods
    - add() : 관계 추가, 지정된 객체를 관련 객체 집합에다 추가
    - remove() : 관계 제거, 관련 객체 집합에서 지정된 모델 객체를 제거

- 1:N은 단수, M:N은 복수로 하는 것이 관례
    - 많은 기능 추가시 헷가리지 않도록



### 좋아요 기능 구현

- 양쪽 모두에서 N:1 관계를 가지는 걸 활용해서 만들어보자

- Article(M) - User(N)
    - 0개 이상의 게시글은 0명 이상의 회원과 관련
    - 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있음


## 모델 관계 설정
- Article에 ManyToManyField 작성 - 좋아요는 유저보다 게시글에 종속되는 게 맞는 듯?(상관없음)

    ```py
    #articles/models.py
    class Article(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    ```
- migration 시 에러 발생!!
    
    - 역참조 매니저 충돌
        - N:1
            - '유저가 작성한 게시글'
            - **user.article_set.all()**
        - M:N
            - '유저가 좋아요 한 게시글'
            - **user.article_set.all()**
        
        - like_users 필드 생성 시 자동으로 역참조 매니저 .article_set이 생성됨

        - 그러나 이전 N:1 관계에서 같은 이름의 매니저를 사용 중임
            - user.article_set.all() 해당 유저가 작성한 모든 게시글 조회

        - user가 작성한 글과 user가 좋아요 누른 글을 구분할 수 없게 됨!
        - 즉 ForeignKey 혹은 ManyToManyField 둘 중 하나에 related_name 작성 필요

- related_name 작성 후 재진행
- 생성 확인

- 이 예시에서의 realted manger
    ```
    article.user  
    - 게시글을 작성한 유저 (N:1)

    user.article_set  
    - 유저가 작성한 게시글 (역참조) (N:1)

    article.like_users  
    - 게시글을 좋아요 한 유저 (M:N)

    user.like_articles  
    - 유저가 좋아요 한 게시글 (역참조) (M:N)
    ``` 

## 기능 구현

- URL
    - path('<int:article_pk>/likes/', views.likes, name='likes'), 추가

- view

    ```python
    # articles/views.py
    '''
    좋아요 추가 / 좋아요 취소
    언제 추가하고 언제 취소할지 어떻게 구분할 것인가?
    좋아요를 요청하는 주체는 request.user
    request.user가 지금 특정 게시글에 좋아요를 누른 유저 목록에 있다면 or 없다면으로 나누기기
    '''
    @login_required
    def likes(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    ```
- index

    ```django
    <!-- articles/index.html -->

    {% for article in articles %}
    <form action="{% url 'articles:likes' article.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소" />
        {% else %}
        <input type="submit" value="좋아요" />
        {% endif %}
    </form>
    <hr>
    {% endfor %}

    ```
- 출력 확인