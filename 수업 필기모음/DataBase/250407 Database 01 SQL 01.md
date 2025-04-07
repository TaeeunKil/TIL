# Database 01 SQL 01

## Database

- 데이터베이스 : 체계적인 데이터 모음

- 데이터 : 저장이나 처리에 효율적인 형태로 변환된 정보

- 증가하는 데이터 사용량
    - 배달의 민족 국내 주문 건수 6억 8천만 건 (2000)

    - 구독자 2억 3840만명이 1000억 시간 넷플릭스 시청(2023 1~6월)
    - 전세계 모든 데이터의 약 90%는 2015년 이후 생산된 것(IBM)

- 데이터 센터의 성장
    - 네이버 - 제2데이터센터에 6500억 투자(2020)

    - 카카오 - 제1데이터센터와 제2데이터센터에 1.5조 투자(2022)
    - 전 세계 데이터 센터 시장 2022년부터 2026년까지 연평균 20% 이상 성장 예상

- 데이터를 저장하고 잘 관리하여 활용할 수 있는 기술이 중요해짐 
- 우리가 알고 있는 데이터 저장 방식은 어떤 것이 있을까?

- 기존의 데이터 저장 방식
    1. 파일(File) 이용
        - 어디에서나 쉽게 사용 가능

        - 데이터를 구조적으로 관리하기 힘들다

    2. 스프레드 시트(Spreadsheet) 이용
        - 테이블과 열과 행을 사용해 데이터를 구조적으로 관리 가능

- 스프레드 시트의 한계
    - 크기 : 약 100만행까지만 저장 가능

    - 보안 : 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공
    - 정확성
        - 공식적으로 이름이 바뀐다면? 

        - 모든 테이블 위치에서 해당 값 업데이트가 필요함
        - 찾기 및 바꾸기로 가능하긴 해도 만약 여러 시트에 분산되어 있을 경우 변경에 누락 or 추가 문제 가능성

- 즉 데이터베이스 역할은 데이터를 저장하고 조작 CRUD

## Relational Database
### 개요
- 데이터 베이스를 저장한다는 것 = 구조적으로 저장한다

- 관계형 데이터베이스 
    - 데이터 간에 관계가 있는 데이터 항목들의 모음
    - 테이블, 행, 열의 정보를 구조화하는 방식

    - 서로 관련된 데이터 포인터를 저장하고 이에 대한 엑세스를 제공
    - 고객 id를 저장한 고객 테이블을 주문테이블에서 배정해 연결하는 것 따위

- 관계 : 여러 테이블 간의 논리적인 연결

- 특정 날짜에 구매한 모든 고객, 지난 달에 배송일이 지연된 고객 조회 등 가능능

- 관계형 DB 예시
    - ![image-3](https://github.com/user-attachments/assets/919dd93b-d06d-4017-be0f-fff2fc10dbd0)

    - 각 데이터에 고유한 식별 값을 부여하기 **(기본 키. Primary Key)**
    - 다른 테이블에 고유한 식별 값을 저장하기 **(외래 키. Foreign Key)**
    

- 관계형 DB 키워드
    1. Table (aka Relation) : 데이터를 기록하는 곳
    2. Field (aka Column, Arttribute) : 각 필드에는 고유한 데이터 형식이 지정됨
    3. Record (aka Row, Tuple) : 각 레코드에는 구체적인 데이터 값이 저장됨
    
    4. Database (aka Schema) : 테이블의 집합

    5. Primary Key (aka 기본 키, PK) : 각 레코드의 고유한 값이며 레코드의 식별자
    6. Foreign Key (aka 외래 키, FK)
        - 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
        - 각 레코드에서 관계를 만드는데 사용
        - 다른 테이블의 기본 키를 참조


### RDBMS
- DBMS(DataBase Management System)
    - 데이터베이스를 관리하는 소프트웨어 프로그램

    - 데이터 저장 및 관리를 용이하게 하는 시스템
    - 데이터베이스와 사용자 간의 인터페이스
    - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

- RDBMS (Relational DataBase Management System) : 관계형 DB를 관리하는 SW

- 종류로는 SQLite, MySQL, PostgreSQL, Oracle Databse 등

- SQLite : 경량의 오픈 소스 DB관리 프로그램. 내장되어있어 간단하고 효율적인 저장 및 관리 가능


## SQL
### 개요

- SQL(Stucture Query Language) : 구조화된 DB에서 CRUD 요청을 하기위한 언어. 
- 즉 DB와 대화를 위한 언어

- SQL Syntax
    - 대소문자를 구분하지 않음. 하지만 대문자로 작성할 것을 권장(명시적)
    - SQL Statements의 끝에는 세미콜론이 필요. 명령어의 마침표 역할

### SQL Statements
- SQL을 구성하는 가장 기본적인 코드 블록
- SQL Statements 예시
    ```sql
    SELECT column_name FROM table_name;
    ```

- SELECT Statement라 부르고 2개의 keyword로 구성됨

- 목적에 따른 4가지 SQL Statements 유형
    ![image-11](https://github.com/user-attachments/assets/338cb7d0-5de0-4d8f-a06f-b4744b5d4bcf)

    1. DDL - 데이터 정의 : 데이터의 기본 구조 및 형식 변경

    2. DQL - 데이터 검색 : 데이터 검색
    3. DML - 데이터 조작 : 데이터 조작(추가, 수정, 삭제)
    4. DCL - 데이터 제어 : 데이터 및 작업에 대한 사용자 권한 제어(장고를 통해 하고있음)

- 단순히 암기하고 실행하는 게 아니라 SQL 을 통해 관계형 DB를 잘 이해하고 다루는 방법을 학습

## Querying data
### SELECT
- SELECT statement : 테이블에서 데이터를 조회
    ```sql
    SELECT 
        column_name 
    FROM 
        table_name;
    ```
- SELECT 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
- FROM 이후 데이터를 선택하려는 테이블의 이름을 지정

- 테이블 employees에서 LastName, FirstName 필드의 모든 데이터를 조회
    ```sql
    SELECT 
        LastName, FirstName
    FROM 
        employees;
    ```

- 테이블 employees에서 모든 필드 데이터를 조회
    ```sql
    SELECT 
        * 
    FROM 
        employees;
    ```

- 조회 시 출력을 바꾼다
    ```sql
    SELECT 
        FirstName AS '이름'
    FROM 
        employees;
    ```

- 연산 후 출력
    ```sql
    SELECT 
        Name,
        Milliseconds / 60000 AS '재생 시간(분)'
    FROM 
        tracks;
    ```

## Sorting data
### ORDER BY
- ORDER BT statement : 조회 결과의 레코드를 정렬
- ORDER BY syntax
    
    ```sql
    SELECT 
        column_name 
    FROM 
        table_name;
    ORDER BY
        column1 [ASC|DESC],
        column2 [ASC|DESC],
        ...;
    ```
    - FROM clause 뒤에 위치
    - 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC, 기본 값), 내림차순(DESC)으로 정렬

- 오름 차순으로 조회
    
    ```sql
    SELECT 
        FirstName
    FROM 
        employees
    ORDER BY
        FirstName;
    ```

- 내림차순으로 조회
    
    ```sql
    SELECT 
        FirstName
    FROM 
        employees
    ORDER BY
        FirstName DESC;
    ``` 
    - Descending(내림차순)의 약어

- 하나를 기준으로 내림차순으로 정렬하고 다른 거 기준으로는 오름차순
    
    ```sql
    SELECT 
        Country, City
    FROM 
        customers
    ORDER BY
        Country DESC, City;
    ```
    - 앞에 정렬된 기준 영역 안에서 다음 정렬을 한다다

- NULL이 있을 경우 정렬 시 먼저 출력

- statement 실행 순서
    - FROM - SELECT - ORDER BY
    1. 테이블에서 FROM
    
    2. 조회하여  SELECT
    3. 정렬 ORDER BY


## Filtering data
- Keywords
    - Clause
        - DISTINCT
        - WHERE
        
        - LIMIT

    - Operator
        - BETWEEN
        - IN
        - LIKE
        - Comparison
        
        - Logical

### DISTINCT
- DISTINCT : 조회 결과에서 중복 레코드 제거

    ```sql
    SELECT DISTINCT
        column_name 
    FROM 
        table_name;
    ```
- SELECT 키워드 바로 뒤에 작성해야 한다
- 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정해야한다

- 중복없이 오름차순 조회

    ```sql
    SELECT 
        FirstName
    FROM 
        employees
    ORDER BY
        FirstName;
    ```
### WHERE
- WHERE : 조회 시 특정 검색 조건을 지정

- WHERE syntax
    ```sql
    SELECT DISTINCT
        column_name 
    FROM 
        table_name
    WHERE
        search_condition;
    ```
    - FROM clause 뒤에 위치
    - search_condition은 비교연산자 및 논리연산자를 사용하는 구문이 사용됨

- 특정 필드 값의 데이터를 조회
    ```sql
    SELECT 
        LastName, FirstName, City
    FROM 
        employees
    WHERE
        City = 'Prague';
    ```

- 특정 필드 값이 아닌 데이터를 조회
    ```sql
    SELECT 
        LastName, FirstName, City
    FROM 
        employees
    WHERE
        City != 'Prague';
    ```

- NULL일 경우와 2개의 조건일 경우
    - NULL은 없다는 의미라 = NULL 불가능!!!!!!

    ```sql
    SELECT 
        LastName, FirstName, Company, Country
    FROM 
        employees
    WHERE
        Company IS NULL
        AND Country = 'USA';
    ```



- 2개의 조건이 OR일 경우
    ```sql
    SELECT 
        LastName, FirstName, Company, Country
    FROM 
        employees
    WHERE
        Company IS NULL
        OR Country = 'USA';
    ```

- 특정 값 이상, 이하 즉 특정 구간을 조회
    ```sql
    SELECT 
        Name, Bytes
    FROM 
        tracks
    WHERE
        Bytes BETWEEN 10000 AND 500000;
    -- WHERE
    --  Bytes >= 10000
    --  AND Bytes <= 50000; 
    ```

- 오름차순 추가

    ```sql
    SELECT 
        Name, Bytes
    FROM 
        tracks
    WHERE
        Bytes BETWEEN 10000 AND 500000
    ORDER BY Bytes;
    ```

- OR이 여러 개일 경우

    ```sql
    SELECT 
        LastName, FirstName, Country
    FROM 
        employees
    WHERE 
        Country IN ('Canada', 'Germany', 'France');
    -- WHERE
    --    Country = 'Canda'
    --    OR Country = 'Germany'
    --    OR Country = 'France';
    ```

- 위 조건의 역일 경우
    ```sql
    SELECT 
        LastName, FirstName, Country
    FROM 
        employees
    WHERE
        Country NOT IN ('Canada', 'Germany', 'France');
    ```

- 특정 값으로 끝나는 데이터 조회
    ```sql
    SELECT 
        LastName, FirstName
    FROM 
        employees
    WHERE
        LastName LIKE '%son';
    ```

- 크기가 일정하면서 특정 값을 포함하는 경우를 조회
    ```sql
    SELECT 
        LastName, FirstName
    FROM 
        employees
    WHERE
        FirstName LIKE '___a';
    ```

# Operators
- Comparison Operators 비교 연산자
    - =
    - \>=
    - \<=
    - !=
    - IS
    - LIKE
    - IN
    - BETWEEN ... AND

- Logical Operators 논리 연산자
    - AND &&
    - OR ||
    - NOT !

- IN Operator 값이 특정 목록 안에 있는지 확인

- LIKE Operator 값이 특정 패턴에 일치하는지 확인 (Wildcards와 함께 사용)

- Wildcard Characters
    - %
        - **0개 이상의 문자열**과 일치하는지 확인
    - _
        - **단일 문자**와 일치하는지 확인
    
    - 전화번호 형식 구분에 유용

### LIMIT
- 조회하는 레코드 수를 제한!
- LIMIT syntax

    ```sql
    SELECT DISTINCT
        column_name 
    FROM 
        table_name
    LIMIT [offset,] row_count;
    ```
    - 하나 또는 2개의 인자를 사용 (0 또는 양의 정수)
    - row_count는 조회하는 최대 레코드 수를 지정
    - 예를 들어, LIMIT 2, 5; 라면 3~7이 나온다. 2초과 5개

- 내림차순으로 7개만 조회
    ```sql
    SELECT 
        TracId, Name, Bytes
    FROM 
        tracks
    ORDER BY Bytes DESC
    LIMIT 7;
    ```

- 내림차순으로 4번째부터 7번째까지 조회
    ```sql
    SELECT 
        TracId, Name, Bytes
    FROM 
        tracks
    ORDER BY Bytes DESC
    LIMIT 3, 4;
    -- LIMIT 4 OFFSET 3;
    ```

## Grouping data
### GROUP BY

- 레코드를 그룹화하여 요약본 생성(집계함수와 함께 사용용)

- Aggregation Functions 집계 함수
    - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
    - SUM, AVG, MAX, MIN, COUNT

- GROUP BY syntax

    ```sql
    SELECT
        c1, c2, ... , cn, aggregate_function(ci)
    FROM 
        table_name
    GROUP BY
        c1, c2, ..., cn;
    ```
    - FROM 및 WHERE 절 뒤에 배치
    
    - GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성

- 예시

    1. Country 필드 그룹화
    ```sql
    SELECT 
        Country
    FROM 
        customers
    GROUP BY
        Country;
    ```
    
    2. COUNT 함수가 각 그룹에 대한 집계 값을 계산
    
    ```sql
    SELECT 
        Country, COUNT(*)
    FROM 
        customers
    GROUP BY
        Country;
    ```

- 활용
    - 필드를 그룹화 해서 각 그룹에 대한 평균을 내림차순 조회
    ```sql
    SELECT 
        Composer,
        AVG(Bytes) AS avgOFBytes
    FROM 
        tracks
    GROUP BY
        Composer
    ORDER BY
        avgOFBytes DESC;
    ```

    - 평균 값이 10 미만인 데이터 조회
    ```sql
    SELECT 
        Composer,
        AVG(Milliseconds/60000) AS avgOFMinute
    FROM 
        tracks
    WHERE
        avgOFMinute < 10
    GROUP BY
        Composer;
    ```  
     **에러발생!!! 에러발생!!! 에러발생!!! 에러발생!!!**

    - **HAVING** clause
        - **집계 항목**에 대한 세부 조건을 지정
        - 주로 GROUP BY와 함께 사용되며 GROUP BY가 없다면 WHERE 처럼 동작
        - 나눈 이유? 실행순서가 그룹화화보다 WHERE이 먼저 + 명시적으로 조건을 구분하기

    ```sql
    SELECT 
        Composer,
        AVG(Milliseconds/60000) AS avgOFMinute
    FROM 
        tracks
    GROUP BY
        Composer
    HAVING
        avgOFMinute < 10;
    ```

- statement 실행 순서
- FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY - LIMIT
    1. 테이블에서
    2. 특정 조건에 맞춰
    3. 그룹화하고
    4. 그룹 중에 조건 있으면 맞추고
    5. 조회하여
    6. 정렬하고
    7. 특정 위치의 값을 가져옴

## 참고
### Query
- DB에 정보를 요청하는 것

- SQL로 작성하는 코드를 일반적으로 쿼리문(SQL문) 이라고 함
### SQL 표준

- SQL은 미국 국립 표준 협회(ANSI)와 국제 표준화 기구(ISO)에 의해 표준이 채택됨
- 모든 RDBMS에서 SQL 표준을 지원

- 다만 각 RDBMS마다 독자적인 기능에 따라 표준을 벗어나는 문법이 존재함. 주의
