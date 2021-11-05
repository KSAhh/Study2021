### 태그  
- `<fieldset>` `</filedset/>`  
  > label과 control을 묶을 때  
- `<legend>` `</legend>`  
  > filedset의 자식요소  
  > 콘텐츠의 설명
  > 
  > ![예시코드](https://user-images.githubusercontent.com/66674138/140509959-4f00f0a7-4d7f-4e4f-a129-2f464dc4822f.png)
   
- `<label for="">`  
  > input 태그의 id와 연동
  > label을 클릭하면 텍스트 입력창으로 이동  
  > ![예시코드](https://user-images.githubusercontent.com/66674138/140510768-26b7d3b4-776c-4be9-8598-ff5fb509a051.png)

### 속성/필터/인수  
- `Forloop.counter`  
  > [참고](https://docs.djangoproject.com/ko/3.2/ref/templates/builtins/#ref-templates-builtins-tags)  
  > For 태그가 반복한 횟수  
  > 
  > ![image](https://user-images.githubusercontent.com/66674138/140510971-9f106d5f-d61a-4896-b5f1-1fdbe43f5bf4.png)  
  > ![image](https://user-images.githubusercontent.com/66674138/140511161-0282ac5e-9a39-4bd3-a52a-38ef97305f36.png)  
- `pluralize`  
  > 템플릿 내장 함수  
  > 접미사 's' 붙여줌  
  > 
  > ![image](https://user-images.githubusercontent.com/66674138/140511294-c1b1c2a9-29f9-4009-b978-3462c6d73746.png)  
- 인수  
  > 정의 : 함수를 호출할 때 매개변수 자리에 넘기는 변수  
  > Args (positional argument) : Arguments / 인자들  
  > Kwargs (Keyword argument) : named arguments / 키워드 된 인자들  

### python 예외  
- try exept 구문으로 예외 처리
- `KeyError`  
  > 매핑(사전) 키가 기존 키 집합에서 발견되지 않은 경우 발생  
- `NoReverseMatch`

### 내장함수  
- `HttpResponseRedirect(url)`  
  > 다른 response를 반환하지 않음
  > 그저 현재 app에서 다른 app으로 이동할 때 즉, URL 페이지로 redirect 할 때  
- `reverse( viewname, urlconf=None, args=None, Kwargs=None, current app=None)`  
  > Args와 kwargs는 동시에 전달하면 NoReverseMatch 예외 발생
  > urls.py  
  > 
  > ![image](https://user-images.githubusercontent.com/66674138/140511664-a5a13b23-4d00-4fd4-91a1-c83410083d06.png)  
  > views.py  
  > ![image](https://user-images.githubusercontent.com/66674138/140511693-575d03dc-4dbd-4c9e-8a6b-f1ba61a30c90.png)  
  > views.py (args)  
  > ![image](https://user-images.githubusercontent.com/66674138/140511739-bfd7e2dd-1b2d-4207-a6a7-875320ba94fd.png)  
  > views.py (kwargs)  
  > ![image](https://user-images.githubusercontent.com/66674138/140511786-e0a81967-5cca-45af-9bc3-a916f21d942f.png)  

### View  
- 경쟁상태
  > Generic view를 사용해야 하는 이유  
  > DB에서 값을 조회한 후 다시 DB에 입력하는 경우, 사용자가 여러 명일 때 신호가 겹쳐 정확한 값 반영 안될 수 있음  
- Generic view  
  > Django 제공
  > 일반적인 패턴을 추상화하여 python 코드를 작성하지 않아도 됨  
  > 경우  
    1. URL의 매개 변수에 따라 DB에서 data 가져올 때 
    2. 템플릿을 load하고 rendering 된 템플릿을 return 할 때
  > `ListView`  
    - model : 적용할 모델
    - template : app명/모델명_list.html  
  > `DetailView`  
    - model : 적용할 모델  
    - template : app명/모델명_detail.html



