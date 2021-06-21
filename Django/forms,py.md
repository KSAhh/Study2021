### 메타 클래스  
- class 내의 class

# 실습  

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
      {{form}} #그대로 폼 받기
      <button type="submit"> submit </button>
</form>
```
