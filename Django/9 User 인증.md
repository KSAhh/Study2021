Django에서 지원
- user table : admin 페이지 내부
- auth
  - token발급 해줌
  - Authentication (인증)
  - 회원가입 요청 → 서버가 User table에 저장 → 로그인 요청 → 서버가 Usertable에서 회원 정보 확인 → 서버가 user에 token 제공
  - 함수 : `authenticate`, `login`, `logout`  


- models.py 파일  
```python
class User(AbstractUser) # AbstractUser를 상속받으며 AbstractUser내의 column들을 이용함
```  
> AbstractUser 위에서 `F10` 누르면 속성이 나옴
  >> admin페이지에 있는 모델의 column  
  >> AbstractBaseUser 위에서 `F11`을 누르면 또 다른 민감한 속성들이 나옴
  >> AbstractBaseUser가 부모클래스, AbstractUser가 자식 클래스

- - -  

### 실습  
1. manage.py 위치로 이동
2. account app 생성 `$ python manage.py startapp account`
3. setting.py  
    ```python
    INSTALLED_APPS = [
        'account'
    ]
    ```  
    
### 실습 - 로그인  
4. account app 내 views.py (로그인)
    ```python
    form django.shortcuts import render, redirect
    from django.contrib.auth.forms import AuthenticationForm, UserCreationForm AuthenticationForm은 로그인, UserCreationFrom은 회원가입 용도
    from django.contrib.auth import authenticate, login
    
    def login_view(request): # Django에서 제공하는 login기능과 충돌하기 때문에 "_view"를 붙여줌으로써 충돌 없앰
        # post방식으로 들어왔을 때
        if request.method == 'POST': 
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username") # cleaned_data는 유효성 검사를 통과한 data
                                                             # username이라는 cleaned data를 가져와서 username변수에 저장함
                password = form.cleaned_data.get("password")
                user = authenticate(request = request, username = username, password = password) # form에서 받은 username, password를 authenticate에 넣음
                if user is not None:  # user table에 정보가 존재할 때
                    login(request, user)
                    
                return redirect("home") # login성공해도 실패해도 홈으로 보내줌                                                                      

        # get방식으로 들어왔을 때
        form = AuthenticationForm() 
        return render(request, 'login.html', {'form':form})
    ```  
5. Blog app내 `form django.contrib import admin` 삭제
6. account app 내 urls.py 생성
    ```python
    from django.urls import path
    from .views import *
    
    urlpatterns = [
        path('login/', login_view, name="login"), # paht('페이지 이름', view.py의 클래스, name="사용할 이름")
    }
    ```
7. 프로젝트 폴더 내 urls.py
    ```python
    urlpatterns = [
        path('account/' , inclue('account.urls')
    ]
    ```
8. account app 내 templates폴더 생성
9. account app 내 templates폴더 내 login.hmtl 생성
    ```python
    {% extends 'base.html' %}
    {% block content %}
    <h1>Login</h1>
    
    <form action="{%url 'login%}" method="post"> # 이미지 없으므로 enctype 속성 사용 안 함
        {%csrf_token%}
        {{form.as_p}}
        <button type="submit"> submit </button>
    </form>
    {% endblock %}
    ```
> action은 Blog프로젝트 의 create함수와 묶어서 사용할 수 있음  
  >> 그 이유는 login.html을 렌더링 해주는 (views.py내) login_view함수는 get방식으로 들어옴  
  >> crete, update함수 같은 DB에 접근하는 함수는 POST Method로 요청이 들어옴  
  >> 
10. base.hmtl 일부
    ```python
    <a class = "nav_link" href="{% url 'login'%}"> Login </a> # 'login': urlpatterns에 사용한 name
    ```
    
- - -  

### 실습 - 로그아웃  
4. account app 내 views.py (로그아웃)
    ```python
    from django.contrib.auth import authenticate, login, logout
        
    def logout_view(request):  # Django에서 제공하는 logout기능과 충돌하기 때문에 "_view"를 붙여줌으로써 충돌 없앰
        logout(request)
        return redirect("home")
    ```
5. account app 내 urls.py
    ```python
    urlptterns = [
        path('logout/', logout_view, name="logout"),
    ]
    ```
6. base.html 일부
    ```python
    <a class = "nav_link" href="{% url 'logout'%}"> Logout </a> # 'logout': urlpatterns에 사용한 name
    ```  
    
- - -  

### 실습 - 회원가입  
4. (완성본은 10) account app 내 views.py 
    ```python  
    from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # AuthenticationForm은 로그인, UserCreationFrom은 회원가입 용도
    
    def register_view(request):
        form = UserCreattionForm()
        return render(request, 'signup.html',{'form':form})
    ```  
5. account app 내 urls.py  
    ```python  
    urlpatterns = [
        path('register/', register_view, name = 'signup"),
    ]
    ```  
6. (완성본은 9) account app 내 templates 폴더 내 signup.html 생성  
    ```python  
    {% extends 'base.html' %}
    {% block content %}
    
    <h1>Sign Up</h1>
    <form action="" method="post"> # 이미지 없으므로 enctype 속성 사용 안 함
        {%csrf_token%}
        {{form.as_p}}
        <button type="submit"> submit </button>
    </form>
    {% endblock %}
    ```  
7. base.hmtl 일부  
    ```python
    <a class = "nav_link" href="{% url 'signup'%}"> Signup </a> # 'signup': urlpatterns에 사용한 name
    ```
8. 이 상태로 서버를 돌려보면 지켜야 할 규칙이 많은 것을 확인할 수 있음  
9. account app 내 templates 폴더 내 signup.html  
    ```python
    {% extends 'base.html' %}
    {% block content %}
    <h1>Sign Up</h1>
    
    <form action="{%url 'signup' %}" method="post"> # 이미지 없으므로 enctype 속성 사용 안 함
        {%csrf_token%}
        {{form.as_p}}
        <button type="submit"> submit </button>
    </form>
    {% endblock %}
    ```  
> action = {%url 'signup' %} 추가  
10. account app 내 views.py  
    ```python
    from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # AuthenticationForm은 로그인, UserCreationFrom은 회원가입 용도
    
    def register_view(request):
        if request.method == "POST": #POST방식으로 들어왔을 때
          form = UserCreationForm(request.POST)
          if form.is_valid(): # 유효성 검사
            user = form.save() # 폼 내의 꼭 필요한 정보가 없기 때문에 forms.py 응용할 때 처럼 임시저장할 필요없음. 즉, commit하지 않음
            login(request, user)
          return redirect('home') # indentation을 줄임. 유효성 검사를 통과하지 못해도 홈으로 가야하기 때문
            
        else:
          form = UserCreattionForm()
          return render(request, 'signup.html',{'form':form})
    ```
- - -  

### 실습 - 로그인 이후 정보 띄우기  
- html 내부에서 자유롭게 활용
    ```python
    {% if user.is_authenticated %} # user가 authenticated인지, anonymous인지 상태 확인
    {% endif %}
    
    {% if not user.is_authenticated %} # user가 authenticated인지, anonymous인지 상태 확인
    {% endif %}
    ```  
- - -  
- - -  

# USER확장  

### 실습  
1. accout app내 models.py  
    ```python
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    
    class CustomUser(AbstractUser): # User model에 AbstractUser상속받음
        # 원하는 column추가
        nickname = models.CharField(max_length=100)
        university = models.CharField(max_length=50)
        location = models.CharField(max_length=200)
    ```
2. 프로젝트 내 settings.py에 사용할 모델을 설정해줌  
    ```python
    # 30줄 위치 
    AUTH_USER_MODEL = 'account.customUser' #AUTH_USER_MODEL='앱.클래스명' 형식
    ```  
3. `$ python manage.py makemigrations`
4. `$ python manage.py migrate`
  - 오류발생⚠️ : `django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency account.0001_initial on databse 'default'.`
  - 프로젝트 내 settings.py 35번째 줄 `'django.contrib.admin',` 주석처리
  - 프로젝트 내 urls.py `path('admin/', admin.site.urls),` 주석처리
  - 다시 `$ python manage.py migrate`  
  - 안내 확인 가능 : `Applying account.0001_initial...OK`
  - 주석 다시 풀어줌  
5. MODELS에 맞는 회원가입 창 만들기. account app 내 forms.py 생성 
  > account app 내 views.py에 있는 UserCreationForm을 상속받기  
  
    ```python 
    from django contrib.auth.forms import UserCreationForm
    from .models import CustomUser
    class RegisterForm(UserCreationForm): # UserCreationForm을 상속받음
        class Meta: # 메타클래스의 모델을 Custom model로 바꿀 것
          model = CustomUser
          fields = ['username', 'password1', 'password2, 'nickname', 'location', 'university'] # 추가된 3가지 column도 추가해줌
     ```
 6. account app 내 views.py  
    ```python
    from django.contrib.auth.forms import AuthenticationForm, ############# UserCreationForm 필요없음
    from .forms import RegisterForm ############# RegisterForm 불러옴
    
    def register_view(request):
        if request.method == "POST": #POST방식으로 들어왔을 때
          form = RegisterForm(request.POST) #############기본 로그인과 다른 점
          if form.is_valid(): # 유효성 검사
            user = form.save() # 폼 내의 꼭 필요한 정보가 없기 때문에 forms.py 응용할 때 처럼 임시저장할 필요없음. 즉, commit하지 않음
            login(request, user)
          return redirect('home') # indentation을 줄임. 유효성 검사를 통과하지 못해도 홈으로 가야하기 때문
            
        else:
          form = RegisterForm() #############기본 로그인과 다른 점
          return render(request, 'signup.html',{'form':form})
    ```
7. account app 내 admin.py  
    ```python
    from django.contrib import admin
    from .models import CustomUser
    
    admin.site.register(CustomUser)
    ```
        
