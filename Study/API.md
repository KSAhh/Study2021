### 기타  
- URL : Uniform Resource Locator  
  - 구성
    > 프로토콜 : http / https / file / ...  
    
    > 호스트주소 : www.naver.com / www.google.com / ...    
    
    > 파일경로 : /home / /index.html /... / 서버에 있는 파일, resource의 경로  
  
    > Query parameter : 형식 ?id=1&postId=1 / ... / 검색, 필터링, 데이터 교환시 사용  

- - -  

## HTTP (Hyper Text Transfer Protocol)  
- Hyper Text : 관련된 문서와 오가며 정보 얻게 해주는 text  
- Transfer Protocol : 인터넷에서 정보 주고받을 때 지켜야 할 규칙  
- 구성 : 요청(Request) ↔ 응답(Response)  

- 요청(request) 메소드  
  `Get`  
    >  읽기 URL에 표시된 resource 가져옴  
    
  `POST`  
    > 수정 body에 정보를 담아 서버에 입력  
  
  `PUT`  
    > 수정  
    > (전체) 수정 URL에 표시된 resource와 바꿔 치기  
  
  `PATCH`  
    > 수정  
    > (일부) 수정 URL에 표시된 일부만 수정  
    > PUT과 다름  
  
  `DELETE`  
    > 삭제 URL에 표시된 특정 resource 삭제  
    
- - -  

## JAVA (Java Script Object Notation)  
- 형식  
  > Key : Value  
  > ex) "이름":"홍길동"  
- 데이터 교환 : JSON형식 多 사용 / 이전에는 XML형식도 사용  

- **JSON**  
  > 특징 
    - XML보다 가벼움  
    - 많은 프로그래밍 언어 지원  
    - 네트워크상의 전송 : 직렬화 과정 거침(string(문자열)형식으로 보냄) / 수신 : 역직렬화 과정 거침 (object형식으로)  
  > 형식 예시  
    - [MDN JSON 문서](https://developer.mozilla.org/ko/docs/learn/javascript/objects/json)  
    - [같은 페이지의 Superhero data](https://mdn.github.io.learning-area/javascript/oojs/json/superheroes.json.)  
  > 실습1  
  ```python
  Chrome      →     F12     →     Console창      →     "mdn json" 검색     →     "Working with Json" 클릭      →     본문의 [https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json.] 클릭     →     Text 등장     →     Text 복사     →     Console에 "let super_hero" 입력      → Text 붙여넣기 → ★[1]
  
  직렬화  
  "JSON" 입력    →   "JSON.stringify(super_hero);" 입력  →   Console 내부 내용이 string형식으로 출력됨

  역직렬화
  "JSON.parse(serialized);" 입력
   ```  
   > JSONPlaceholder
   
      - [사이트](https://jsonplaceholder.typicode.com/)  
      - Fake online REST API 사이트  
      - 기능 : REST API 테스트, 프로토타이핑 / 바꾼다고 유지되지 않음. 나중에 원상복구 됨  
      - 프론트헤드 쪽에서 만들 때 유용  
      - ★[3] Resources 중 한 가지 클릭하면 틀 확인 가능  
      - Resources를 이용하려 할 때 locator(url)가 중요  
   > 실습2  
   ```python
   JSONPlaceholder 검색     →    "post/" 클릭     →     url 복사

    <Get>
    1. Postman 프로그램 실행
    2. 서버에 요청 보내기위해 "+" 클릭
    3. Untitled Request 이름의 요청 생성됨
    4. Get 선택
    5. url 붙여넣기   
    6. Send 클릭
    7. 웹사이트에 나온 내용과 같은 코드가 나옴

  <POST>      # POST에서 사용하지 않는 것을 넣은 경우 에러 발생할 수 있음
  1. 서버에 요청 보내기위해 "+" 클릭
  2. Untitled Request 이름의 요청 생성됨
  3. POST 선택
  4. url 붙여넣기     # url뒤에 "/(숫자)"를 넣어주면 "ID가 (숫자)인 post"가 출력
  5. Send 클릭
  6. id 자동생성됨
  ```  
  
- - -  

## API (Application Programming Interface)  
- Application : 서비스, 응용프로그램  
- Programming Interface : 서비스들이 데이터에 접근하도록 돕는 도구 / ex)리모컨  
- 종류 : SOAP(Simple Object Access Protocol), REST(REpresentational State Transfer), GraphQL(Graph Query Language) / SOAP 어렵다고 함  

- Rest
  > 소프트웨어 architecture / 설계의 지침, 원칙  
  > 모두 지켜야할 필요 x  
  > 구성요소 : 자원, 행위, 표현
  ```python
  GET/likelion/member/8th/list
  PATCH/likelion/member/8th/홍길동
  
  자원
  /likelion/member/8th/list
  /likelion/member/8th/홍길동
  
  행위
  GET
  PATCH
  ```
  ```python
  표현
  {
      "members":["김멋사",...,"하멋사"]
  }
  ```  
