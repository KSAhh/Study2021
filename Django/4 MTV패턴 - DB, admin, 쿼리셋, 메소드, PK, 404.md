# CRUD  
- Create  
> 2개의 함수 작성
>> ex) `new`: 함수 / new.html 보여줌  // `create` : 함수 / DB에 저장  
- Read  
- Uadate  
> 2개의 함수 작성  
> 수정할 데이터의 id값 받아야 함  
>> ex) `edit`: 함수 / edit.html 보여줌 // `update` : DB에 적용  
- Delete  

# Model  
- DB뒤적뒤적 / Data에 접속, 관리하도록 돕는 객체  
- Django와 별개  
- 여러개 (O)  
- Class(붕어빵틀) VS Object(붕어빵)  
      - object : 독립적인 data  

### 쿼리셋 (ueryset)  
- 전달받은 객체목록 / list  

### 메소드 (method)  
- 쿼리셋들을 처리하는 방법  
- `.all()` : 모든것  
- `.count()`: data개수  
- `.first()` : 첫 번째 객체  
- `.last()` : 마지막 객체  

### migration  
- makemigrations  
> 파이썬 코드를 DB가 알아들을수 있게 번역  
> 앱 내의 migration 폴더를 만들어 models.py의 변경사항 저장  
- migrate  
> DB에 그 내용을 적용. 알려줌  
> Migration폴더를 실행시켜 DB에 적용  

### PK  
- Primary Key  
- 데이터 구분자 / 모델에서 찍어낸 수많은 객체들을 구분 / 이름표  
- 관계형 DB  

### path-converter  
- 여러 객체 다루는 계층적 url이 필요할 경우 / url계층적 디자인  
- 형식: `<type:name>`  
- ex) 페이지 url에 뜸  
      "www.dreamary.com/profile/1"  
      "www.dreamary.com/profile/2"  
      "www.dreamary.com/profile/3"  

### URL Path  
- `path('URL', views 내부의 함수, name="url의 이름"),`  
> 'URL' : 페이지 주소 / 로컬호스트 / ex) introduce/,  
> 함수 : url이 불렸을 때 실행할 함수 / ex) views.home  
> name : 해당 path를 대표하는 이름 / ex) name = "home"  

\* `render` : 요청이 들어오면 이 html 파일을 보여줘  
\* `redirect` : 요청을 들어오면 저쪽 url로 보내  

- - -  

##### 기타설정확인 - 수정X  
- 프로젝트 폴더 내 settings.py  
```python
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',       # default는 sqlite
        'NAME': BASE_DIR / 'db.sqlite3',
     }
  }
```

<br>
- - -  
# 실습  

### Model 사용하기  
- django 공식 documentation 참고   
```python
  1. app폴더 내 models.py
      class Blog(models.Model):                                # "Class" : 이런 데이터를 처리할 것임을 알림 / 무조건 대문자로 시작
          title = models.CharField(max_length=200)             # 최대 length가 200인 문자열
          pub_date = models.DateTimeField('date published')    # 날짜와 시간
          body = models.TextField()                            # 긴 문자열
             
          def __str__(self):                                   # 사용자가 적은 title이 admin에 뜨길 원하는 경우, 추가
              return self.title
  2. $ python manage.py makemigrations                         # migration 만듬. DB에게 번역 / "migrations"폴더 생성됨  
  3. $ python manage.py migrate                                # 데이터베이스에 적용 / "db.sqlite3"파일 생성됨  
```  
> `title`, `pub_date`, `body` : 모델의 속성   

필드타입 | HTML위젯 | 필수옵션 | 설명  
---- | ---- | ---- | ----  
BooleanField | CheckboxInput | - | True/False값 가지는 필드  
CharField | TextInput | max_length | 문자열 데이터 저장하는 필드
|||| 최대 글자수 반드시 지정  
DateField | TextInput | - | datetime.date 인스턴스인 날짜 데이터 저장 필드
|||| 달력 위젯과 오늘 날짜 입력 기능을 기본 제공  
DateTimeField | TextInput | - | date.datetime 인스턴스인 시간 데이터 저장 필드
|||| 두 개의 TextInput, 달력 위젯, 오늘 날짜 입력 기능 제공  
FloatField | NumberInput | - | Python의 float과 같은 실수 데이터 저장 필드  
IntegerField | NumberInput | - | Python의 integer과 같은 정수 데이터 저장 필드
|||| -2147483648 ~ 2147483647 사이 값 저장 가능
|||| 글자 수 제한 없는 문자열 데이터 저장 필드  
TextField | Textarea | - | max_length값 지정하면 폼에서는 제한되지만, DB에는 영향 주지 않음  
> 필드옵션  
>> `blank` : validation시에 empty 허용여부  
>> `null` : null값 허용 여부  
>> `db_index` : 인덱스 필드인지  
>> `default` : 디폴트 값이나 함수 지정  
>> `unique` : 현재 테이블 내 유일한 값인지  
>> ...


<br>

### Admin 사용하기  
```python
  1. admin 계정 생성  
    $ python manage.py createsuperuser -> ....
  2. admin에 추가한 model 알리기  
  3. 생성한 model을 django에 알리기. app내 admin.py 파일 
      from .models import 클래스                                # . : 같은 폴더위치에 있는 models파일 / 앱이름에 해당하는 클래스를 가져오기   
      admin.site.register(클래스)                               # admin 사이트에 앱이름에 해당하는 클래스를 등록
```  
> 클래스 : models.py에 사용한 것  

<br> 

### READ - Model 내의 data 출력  
- 순서 : model → view → template  
```python
  1. app 내 views.py  
    from .models import Blog
    
    def home(request):
        blogs = 클래스.objects (또는 클래스.objects.all())       # 앱 내의 객체를 blogs에 담음 / blogs는 template에 사용할 이름 
        return render(request, 'home.html', {'blogs': blogs})
  2. 프로젝트 폴더 내 urls.py
      from blog.views import *
      urlpatterns = [
            path('', home, name="home"),
      ]
   
  3. app내 html
    {{ blogs }}                     # 출력: Blog.Blog.objects
    {{ blogs.all }}                 # 출력: <QuerySet [<Blog: 타이틀>]>
    
    {% for blog in blogs.all %}     # 모든 객체가 담김
      <div class="container">
          <h1>{{ blog.title }}</h1>
          <p>{{ blog.pub_date }}</p>
          <p>{{ blog.body }}</p>
      </div>
    {% endfor %}
```  
> `앱명.objects` : admin의 data  
> `blogs` : 쿼리셋 (queryset) / template에 동일한 이름 사용해야 함  

<br>


### READ - error 띄우기 / html끼리 연결하면서 data공유하기, error  
- 과정  
1. PK : n번째 블로그 객체 / 게시글 id  
2. path Converter : 사이트/blog/객체번호(n)  
3. get_object_or_404 : object 가져오고, 없으면 404 에러 띄우는 함수  
```python
    1. 프로젝트 폴더 내 urls.py
        urlpatterns = [
            path('blog/<int:blog_id>', Blog.views.detail, name="detail"),               # <int:blog_id> : 각 게시물의 id값이 들어갈 공간 / path-converter
        ]

    2. app내 views.py
       from django.shortcuts import render, get_object_or_404
       from .models import Blog
       def detail(request, blog_id):
           blog_detail = get_object_or_404(Blog, pk=blog_id)                        # get_object_or_404(Class, PK="")
           return render(request, 'detail.html', {'blog': blog_detail})             # blog 이름 동일
   
    3. home.html
        {% for blog in blogs.all %}
        <div class="container">
            <h1>{{ blog.title }}</h1>
            <p>{{ blog.pub_date }}</p>
            <p>{{ blog.summary }}<a href="{% url 'detail' blog.id%}">...more</a></p>    # href내용 중요. detail과 연결하면서 blog.id객체 넘겨줌 
        </div>
        {% endfor %}
   
    4. detail.html
         <h1>{{ blog.title }}</h1>                                                  # blog 이름 동일  
         <p>{{ blog.pub_date }}</p>                                                 # blog 이름 동일
         <p>{{ blog.body }}</p>                                                     # blog 이름 동일
         <a href="{% url 'home' %}">돌아가기</a>
```  
> ❗️ (views.py의 pk변수명) == (urls.py의 변수명) 같아야함  

### READ - data를 html에 연결  
```python
  1. app폴더 내 models.py
    class Blog(models.Model):
        def summary(self):              # 자기자신의 객체 중,
            return self.body[:100]      # body를 100자로 제한하여 return
  
  2. app폴더 내 html
     {% for blog in blogs.all %}
      <div class="container">
      <p>{{ blog.summary }}</p>
      </div>
      {% endfor %}
```  
- - -  

### CREATE - Admin에 접속하지 않고 Data 작성  
```python
  1. app내 view.py
    
    from django.shortcuts import render, get_object_or_404, redirect    # redirect 추가
    from django.utils import timezone                                   # 라이브러리? 추가
    from .models import Blog                                            # Blog data 불러옴
    def new(request):
        return render(request, 'new.html')
    def create(request):                                                # create 함수
        blog = Blog()                                                   # Blog data를 blog에 저장
        blog.title = request.GET['title']                               # submit 버튼으로 들어온 title데이터를 GET 메소드로 blog.title에 저장
        blog.body = request.GET['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog.id))                        # str: url은 문자형이기 때문에 사용
        
  2. new.html

      <h1>Write Your blog</h1>
      <form action="{%url 'create'%}" method="post">
            {%csrf_token%}
            <p>제목 : <input type="text" name="title"></p>
            <p>작성자 : <input type="text" name="writer"></p>
            본문 : <textarea name="body" id="" cols="30" rows="10"></textarea>
            <button type="submit">submit</button>
      </form>
      
  3. 프로젝트폴더 내 url.py
  
      from blog.views import *
      urlpatterns = [
            path('new/', new, name="new"),
            path('create/', create, name="create"),
      ]
      
```
> `request.GET['title']` : new.html 파일에 form태그 요소의 name  

- - -  

### Update - Admin에 접속하지 않고 Data 수정  
```python
  1. app내 edit.html
      
      <h1>Update Your blog</h1>
      <form action="{% url 'update' blog.id %}" method="post">
            {%csrf_token%}
            <p>제목 : <input type="text" name="title" value ="{{ blog.title}}"></p>
            <p>작성자 : <input type="text" name="writer" vlaue="{{ blog.writer }}"></p>
            본문 : <textarea name="body" id="" cols="30" rows="10">{{blog.body}}</textarea>
            <button type="submit">submit</button>
      </form>

  2. app내 views.py
  
      from django.shortcuts import render, get_object_or_404, redirect
      from django.utils import timezone
      from .models import Blog
      def edit(request, id):
            edit_blog = Blog.objects.get(id = id)
            return render(request, 'edit.html', {'blog':edit_blog})
      def update(request,id):
            update_blog = Blog.objects.get(id=id)
            update_blog.title = request.POST['title']
            update_blog.writer = request.POST['writer']
            update_blog.body = request.POST['body'] 
            update_blog.pub_date = timezone.now()
            update_blog.save()
            return redirect('detail', update_blog.id)

  3. 프로젝트폴더 내 urls.py

      from blog.views import *
      urlpatterns = [
            path('edit/<str:id>', edit, name="edit"),
            path('update/<str:id>', update, name="update"),
      ]

  4. app내 detail.html
  
      <a href="{%url 'edit' blog.id%}">Update</a>
```  

- - -  

### Delete - Admin에 접속하지 않고 data 삭제  
```python
  1. app내 views.py
  
      def delete(request,id):
            delete_blog = Blog.objects.get(id=id)
            delete_blog.delete()
            return redirect('home')
            
  2. 프로젝트폴더 내 urls.py

      from blog.views import *
      urlpatterns = [
            path('delete/<str:id>',delete,name="delete")
      ]

  3. app내 detail.html
  
      <a href="{%url 'delete' blog.id%}">Delete</a>
```
