
## 템플릿 언어
- python 사용하고자 할때 이용  
- HTML안에 쓰는 Django제공 언어 
- 로컬서버와 연결  

- `{{}}` : 템플릿 변수. 출력. 명사, `{%%}` : 템플릿 태그. 입력. 동사  
  > ex)  
    ```python
           {% for word, count in dic %}
           {{word}} : {{count}}
           <br>
           {% endfor %}           # 닫는 태그 필요
    ```  
- `{{python_value | filter }}` : 템플릿 필터.
  > ex)
  ```python
    {{value | length}}` : value 길이 반환  
    {{value | lower }} : value 소문자로 출력  
  ```  
  
  
## 템플릿 상속 - html  
- app별로 url관리  

```python
  1. 프로젝트 폴더 내 templates폴더 생성
  2. templates폴더 내 base.html파일 생성
  3. base.html에 home.html내용 복붙
  4. base.html
      {% block content %}                            # 이 사이에 페이지마다 변경될 내용 들어감
      {% endblock%}
  5. home.html에서 base.html과 중복되는 내용 삭제
  6. home.html 나머지 부분
      {% extends 'base.html' %}                      # base.html을 기본으로 가져옴
      {% block content %}
      인 겹치는 내용
      {% endblock %}
  7. 프로젝트 폴더 내                                  # django에게 기본으로 쓸 html파일 위치 알려줌
      TEMPLATES = [
        {
              'DIRS': ['프로젝트 폴더명/templates'],
         },
      ]
```  
##### 로그인/로그아웃 기능 시 템플릿 상속 `authenticated` 함수 사용할 때  
```python
  1. base.html
  
    # 로그인 되어있을 때
    {% if user.is_authenticated %} # 로그인이 되어있는지 (로그인시 authenticated 함수 사용함
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-toggle="dropdown"
            aria-haspopup="true" aria-expanded="false">환영합니다. {{ user.username }} 님!</a> # 템플릿 변수 username 출력

        # 로그아웃 기능
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item"
                href="javascript:{document.getElementById('logout').submit()}">Logout</a>
            <form id="logout" method="POST" action="{% url 'logout' %}">  
                {% csrf_token %} <input type="hidden" />    # 보안
            </form>
        </div>
    </li>
    
    # 로그인 안되어있을 때
    {% else %}    
    <li class="nav-item">
        <a class="nav-item nav-link" href="{% url 'signup' %}">Signup</a>
    </li>
    <li class="nav-item">
        <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
    </li>

 ```

## URL Include  
```python
  1. 첫번째 app내에 urls.py 파일 생성
  2. 프로젝트폴더 urls.py를 복붙
  3. 첫번째 app에 해당되는 것 제외하고 삭제
    - 수정 전 프로젝트폴더 urls.py
      from django.contrib import admin
      from django.urls import path         # 변경
      import 첫번째 앱.views                # 1
      import 두번째 앱.views                # 2
      urlpatterns = [
          path('admin/', admin.site.urls),                            
          path('', Blog.views.home, name='home'), 
          path('blog/<int:blog_id>', Blog.views.detail, name='detail'),   # 변경
          path('new/', Blog.views.new, name='new'),                       # 삭제
          path('blog/create/', Blog.views.create, name='create'),         # 삭제
          path('portfolio/', port.views.portfolio, name='portfolio'),
      ]
    
    - 수정 후 프로젝트폴더 urls.py
      from django.contrib import admin
      from django.urls import path, include            # include 추가
      import 첫번째 앱.views             
      import 두번째 앱.views             
      urlpatterns = [
          path('admin/', admin.site.urls),                            
          path('', Blog.views.home, name='home'), 
          path('blog/', include('blog.urls')),         # 변경
          path('portfolio/', port.views.portfolio, name='portfolio'),
      ]
      
    - 첫번째앱 내 urls.py
      from django.urls import path
      from . import views       # 1,2 합침
      urlpatterns = [
          path('<int:blog_id>/', views.detail, name='detail'),      # 변경
           path('new/', views.new, name='new'),                     # 변경
          path('create/', views.create, name='create'),             # 변경
      ]
```  
> 원리 : url 요청 → 프로젝트폴더 내 urls.py 검토 → `blog/`로 시작되는 내용은 첫번째앱 내 urls.py로 넘어감  

