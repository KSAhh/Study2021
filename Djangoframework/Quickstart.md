[튜토리얼 코드](https://github.com/encode/rest-framework-tutorial)

### Serializer / 직렬변환기  

- 데이터를 표현할 때 사용

##### views.py
- 클래스에 model속성이 아닌 queryset, serializer_class 속성 사용
- model속성을 사용하면 serializer와 queryset은 자동으로 설정됨  
- queryset, serializer_class 속성을 사용하면 API를 명시적으로 표현가능

##### urls.py  
- view 대신 viewset을 사용했기 때문에 router 클래스로 API에 대한 URL이 자동 생성됨

##### Serialize / 직렬화  
- 쿼리셋, 모델 인스턴스의 복잡한 데이터를 JSON, XML 등의 타입으로 쉽게 변환 가능한 python 데이터타입으로 변환  
- 파이썬 객체, queryset 객체를 REST API에서 사용할 json같은 타입으로 변환시켜줌

##### Deserialize  

##### API 접근 권한 오류  
- "detail": "Authentication credentials were not provided.  
- 해결 : ./admin에서 관리자 로그인 이후 정상 작동  

#### 실습  
- API 실행  
> 데이터 입력하면 적용됨  
> `curl -H ...`
  ![image](https://user-images.githubusercontent.com/66674138/140512901-5f2a46c9-4b18-4d15-b982-24c6a9928f47.png)  
  ![image](https://user-images.githubusercontent.com/66674138/140512993-d27eb63c-d459-4942-998d-ee1d5df54f86.png)  
 
- ![image](https://user-images.githubusercontent.com/66674138/140513144-5e2de79e-4958-4f54-954c-f05e14d2c5d1.png)  
- 
