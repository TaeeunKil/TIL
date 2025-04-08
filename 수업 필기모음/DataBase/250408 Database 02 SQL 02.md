# Database 01 SQL 01

## Managing Tables

![image-13](https://github.com/user-attachments/assets/ebc1f377-f349-4520-a7c5-9a9a96a38886)


- 지금은 DDL

### Create a table
- 테이블 생성

- CREATE TABLE syntax
    ```SQL
    CREATE TABLE table_name(
        column_1 data_type constraints,
        column_2 data_type constraints,
        ...,
    );
    ```
    - 각 필드에 적용할 데이터 타입 작성
    - 테이블 및 필드에 대한 제약조건 작성

- 예시
    ```SQL
    CREATE TABLE examples(
        ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
        LastName VARCHAR(50) NOT NULL,
        FirstName VARCHAR(50) NOT NULL
    );
    ```

- PRAGMA
    - 테이블 schema(구조) 확인
        ```sql
        PRAGMA table_info("examples");
        ```
    - cid
        - Column ID 의미하며 각 컬럼의 고유한 식별자를 나타내는 정수 값
        - 직접 사용하지 않으며 PRAGMA 명령과 같은 메타데이터 조회에서 출력 값으로 활용됨

- SQLite 데이터 타입
    1. NULL : 없음
    2. INTEGER : 정수
    3. REAL : 부동 소수점
    4. TEXT : 문자열
    
    5. BLOB : 이미지 동영상 문서 등의 바이너리 데이터


- Constraints 
    - 제약 조건으로 테이블의 필드에 적용되는 규칙 또는 제한 사항
    - 데이터의 무결성을 유지하고 DB의 일관성을 보장

- 대표 제약 조건 3가지
    
    - PRIMARY KEY

        - 해당 키를 기본 키로 지정

        - INTEGER에만 적용된다! INT, BIGINT 등과 같은 유형도 적용되지 않음
    - NOT NULL : 해당 필드에 NULL 값을 허용하지 않는다
    - FOREIGN KEY : 다른 테이블과의 외래 키 관계를 정의

- AUTOINCREMENT 
    - 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성
    - 필드의 자동 증가를 나타내는 특수한 키워드

    - 주로 PRIMARY KEY 필드에 적용
    - INTEGER PRIMARY KEY가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
    - 삭제된 값은 무시되면서 재사용 불가능


- 장고는 NOT NULL, INTEGER PRIMARY KEY AUTOINCREMENT 자동으로 설정



## Modifying table fields
### ALTER TABLE

- 테이블 및 필드 조작

- 역할
    | 명령어                         | 역할              |
    |-------------------------------|----------------- -|
    | `ALTER TABLE ADD COLUMN`      | 필드 추가          |
    | `ALTER TABLE RENAME COLUMN`   | 필드 이름 변경      |
    | `ALTER TABLE DROP COLUMN`     | 필드 삭제          |
    | `ALTER TABLE RENAME TO`       | 테이블 이름 변경    |

#### ALTER TABLE ADD COLUMN syntax
 - ADD COLUMN 키워드 이후 추가하고자 하는 필드 이름과 데이터 타입과 제약 조건 작성
    ```sql
    ALTER TABLE
        table_name
    ADD COLUMN
        column_definition;
    ```

    - 단, 추가하고자 하는 필드에 NOT NULL 제약조건이 있을 경우 NULL이 아닌 기본 값 설정 필요

- ALTER TABLE ADD COLUMN
    - 테이블 생성 시 정의한 필드는 기본 값이 없어도 NOT NULL 제약조건으로 생성되며 내부적으로 Default value = NULL 로 설정됨
    ```SQL
    ALTER TABLE
        examples
    ADD COLUMN
        Country VARCHAR(100) NOT NULL DEFAULT 'default value';

    ALTER TABLE examples
    ADD COLUMN Age INTEGER NOT NULL DEFAULT 0;

    ALTER TABLE
        examples
    ADD COLUMN
        Address VARCHAR(100) NOT NULL DEFAULT 'default value';
    ```

#### ALTER TABLE RENAME COLUMN syntax

- RENAME COLUMN 뒤에 이름을 바꾸려는 필드의 이름을 지정 후 TO 키워드 뒤에 새 이름을 지정
    ```sql
    ALTER TABLE
        table_name
    RENAME COLUMN
        current_name TO new_name;
    ```

#### ALTER TABLE DROP COLUMN syntax
- DROP COLUMN 키워드 뒤에 삭제 필드 이름 지정
    ```SQL
    ALTER TABLE 
        table_name
    DROP COLUMN
        column_name;
    ```

#### ALTERE TABLE RENAME TO syntax
- RENAME TO 키워드 뒤에 새로운 테이블 이름 지정
    ```SQL
    ALTER TABLE
        table_name
    RENAME TO
        new_table_name;
    ```


## Delete a table
### DROP TABLE
- 테이블 삭제
- DROP TABLE syntax
    ```SQL
    DROP TABLE table_name;
    ```


**sqlite는 컬럼 수정(타입, 제약조건 등) 불가**  

**대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용**

## Modifying Data
![image-13](https://github.com/user-attachments/assets/ebc1f377-f349-4520-a7c5-9a9a96a38886)
- 지금은 DML!

### Insert data

- 테이블 레코드 삽입

    ```SQL
    INSERT INTO table_name (c1, c2, ...)
    VALUES (v1, v2, ...);
    ```
    - INSERT INTO 다음에 테이블 이름, 괄호 안에 필드 목록
    - VALUES 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성

- 예시

    ```SQL
    INSERT INTO
        articles (title, content, createdAt)
    VALUES
        ('hello', 'world', '2000-01-01'),
        ('mytitle', 'mycontent', DATE());
    ```
    - 여러 개면 쉼표로 괄호를 연속적으로 쓰기
    - DATE() 함수를 통해 입력도 가능. 공식문서 참조
    - https://www.sqlite.org/lang_datefunc.html

### Updata data

- 테이블 레코드 수정
- UPDATE syntax    
    ```SQL
    UPDATE table_name
    SET column_name = expression,
    [WHERE
        condition];
    ```
    - SET 다음에 수정할 필드와 새 값을 지정
    - WHERE 에서 수정할 레코드를 지정하는 조건 작성
    - WHERE 없으면 모든 레코드 지정

- 활용
    ```SQL
    UPDATE
        articles
    SET
        title = 'update Title',
        content = 'update Content'
    WHERE
        id = 1;
    ```
    - SET에서 한 번에 여러 필드의 수정 가능

### Delete data

- 테이블 레코드 삭제

- DELETE syntax

    ```sql
    DELETE FROM table_name
    [WHERE
        condition];
    ```
    - DELETE FROM 다음에 테이블 작성
    - WHERE 에서 삭제할 레코드 지정
    - 지정 안하면 모든 레코드를 삭제

- 작성일이 오래된 순 2개 삭제

    ```SQL
    DELETE FROM
        articles
    WHERE id IN (
        SELECT id FROM articles
        ORDER BY createdAt
        LIMIT 2
    )
    ```
    - 이런 식으로 조건을 합칠 수도 있음

## Multi table queries
### Join

- 필요한 이유

    - 테이블을 분리하면 관리는 용이하나 출력시 문제

    - 테이블 한 개 만을 출력할 수 밖에 없어 결합해서 출력하는 것이 필요함
    - 이 때 JOIN 사용

- id 부여는?
    - user에 articlesId를 부여하면 안 된다. 그럼 2번 아티클을 쓴 유저를 다시 추가해야함
    - 반대로 article에 usersId를 ㅇ년결하면 생각한대로 적용 가능
    - N:1 관계에서 N쪽이 외래키를 들고있어야한다!!!!

- 사전 준비
    ```sql
    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
    );

    CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userId INTEGER NOT NULL,
    FOREIGN KEY (userId) 
        REFERENCES users(id)
    );
    ```
    - FOREIGN KEY 방식을 기억해라

### Joining tables

- JOIN clause
    - 둘 이상의 테이블에서 데이터를 검색하는 방법

### INNER JOIN

- INNER JOIN clause
    - ![image-16](https://github.com/user-attachments/assets/644ddf78-f506-41d3-b636-97fe31c57fa8)

    - 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환

- INNER JOIN syntax
    ```sql
    SELECT
        select_list
    FROM    
        table_a
    INNER JOIN table_b
        ON table_b.fk = table_a.pk
    ```
    
    - FROM 이후 메인 테이블 지정 table_a
    - INNER JOIN 이후 메인 테이블과 조인할 테이블을 지정 table_b
    - ON 키워드 이후 조인 조건을 작성
    - 조인 조건은 a 와 b의 레코드를 일치시키는 규칙을 지정

- 예시

    ![image-18](https://github.com/user-attachments/assets/c85711b5-80f6-4257-b71f-b5177406c6da)

    ![image-21](https://github.com/user-attachments/assets/6d156156-1e95-4bb7-b1f9-275ec6446afb)

    ```sql
    SELECT * FROM A
    INNER JOIN B
        ON B.no = A.no
    ```

    - 실습예시
    ```SQL
    SELECT articles.title, users.name
    FROM articles
    INNER JOIN users
        ON user.id = articles.userId
    WHERE
        users.id = 1;
    ```

### LEFT JOIN clause
- LEFT JOIN clause
   - ![image-17](https://github.com/user-attachments/assets/d12a1559-23de-4707-a81a-77844ca8fa9c)


   - 오른쪽 테이블과 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환

- LEFT JOIN syntax
    ```SQL
    SELECT
        select_list
    FROM
        table_a
    LEFT JOIN table_b
        ON table_b.fk = table_a.pk
    ```
    - FROM 이후 왼쪽 테이블 지정 table_a
    - LEFT JOIN 이후 오른쪽 테이블을 지정 table_b
    - ON 키워드 이후 조인 조건을 작성

- 예시
    ![image-18](https://github.com/user-attachments/assets/fbf819ee-b15d-4398-9255-6a94c5d86cf7)

    ![image-19](https://github.com/user-attachments/assets/6be7d48a-45ee-4b4f-8e0b-febf6af4f3fc)


## 참고
### 타입 선호도
- Type Affinity
    
    - 컬럼에 데이터 타입이 명시적으로 지정되지 않았거나 지원하지 않을 때, SQLite가 자동으로 추론하는 것
    
    - https://www.sqlite.org/datatype3.html

- 목적
    1. 유연한 데이터 타입 지원
        - 데이터 타입 지정 없이도 저장 조회 가능
        - 컬럼에 저장되는 값의 특성을 기반으로 유추

    2. 간편한 데이터 처리
        - INTEGER Type Affinity 가진 열에 문자열 데이터를 저장해도, 자동으로 숫자 변환 처리

    3. SQL 호환성
        - 다른 DB와 호환 가능
        
### NOT NULL

- 반드시 써야하나?
    - no
    - 하지만 대부분 정의 (null 저장 필요 없어서)
    - 값이 없다는 걸 기록하는 것은 0이나 빈 문자열로 대체하는 것을 권장

### 날짜와 시간

- SQLite에는 날짜 시간을 저장하기 위한 별도 데이터 타입이 없음
- 대신 함수를 사용해 표기 형식에 따라 TET, REAL, INTEGER로 저장
-  https://www.sqlite.org/datatype3.html
