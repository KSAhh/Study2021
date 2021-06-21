### 메타 클래스  
- class 내의 class

# 실습1 - forms.py 생성 후 기존의 form 태그 내부 대체하기

- forms.py파일
```python
from django import forms # forms는 Django에서 제공
from .models import Blog # models 내의 Blog 클래스

class BlogForm(foms.ModelForm): # Django에서 지원해주는 forms를 상속받음
                                # Blog폼을 만듦  
  class Meta: #meta class
    model = Blog
    fields = ['title', 'writer', 'body', 'image'] # model내의 필드
                                                  # 폼을 제공하는 기능
                                                  # 작성된 시간처럼 자동으로 넣어주는 기능을 넣지 않기. 일종의 이름표
``` 
> forms : 폼들을 모으기 때문에 s를 붙임


- views.py파일
```python
form .forms import BlogForm

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})
```

- new.html파일
```python
<form action="{%url 'create'%}" method="post" enctype="multipart/form-data">
      {%csrf_token%}
      {{form}} # 그대로 폼 받기
               # 또는 {{forms.as_p}} p태그에 감싸기
               # 또는 <talbe>{{forms.as_table}}</table> table태그에 감싸기
      <button type="submit"> submit </button>
</form>
```

# 실습2 - forms.py에 유효성 검사 추가하기

- 기존 views.py일부
```python
def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.image = request.FILES['image']
    new_blog.save()
    return redirect('detail', new_blog.id)
```

- 수정한 views.py 일부
```python
def create(request):
    form = BlogForm(request.POST, request.FILES) # forms.py에서 만든 이름
    if form.is_valid(): # 유효성 검사
        new_blog = form.save(commit=False) # 임시저장
                                           # forms.py의 BlogForm에 pub_date라는 정보가 빠져있기 때문
        new_blog.pub_date = timezone.new()
        new_blog.save()
        return redirect('detail', new_blog.id)  # 유효성 검사에 성공했을 때
    return redirect('home') # 유효성 검사에 실패했을 때
```
