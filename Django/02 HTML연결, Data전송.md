### html끼리 연결  
```python
  # 프로젝트/urls.py  
    import 앱명.views # as사용하면 앱 이름 축약 가능
    urlpattens= [
        path('about/', wordcount.views.about, name='about'),      # about
    ]  
  
  # 첫 번째 .html파일  
    <a href="{% url 'about' %}">ABOUT</a>                         # about

  # 두 번째 .html파일 명
    about.html 
```
> `name='about'`과 `url 'about'`은 같아야함  
> `<form action="{%%}">`도 `href="{%%}"`처럼 연결할 수 있음  

<br>

### data 전송  
   ```python
    # home.html
      <form action="{% url 'count' %}">
        <textarea cols="40" rows="10" name="fulltext"></textarea>     # 'fulltext'라는 이름으로 textarea 데이터 저장
      </form>
        
    # views.py
      def count(request):
          text = request.GET['fulltext']                              # text에 GET방식으로 fulltext내용을 넣음
          print(text)                                                 # fulltext에 들어간 내용을 터미널에서 볼 수 있음 (생략가능)
          return render(request, 'count.html')
```

### data 출력    
  ```python
   # views.py                                                                                
     def count(request):                                                                          
        text = request.GET['fulltext']
        text_split = text.split(' ')                                     # 띄어쓰기마다 구분
        return render(request, 'count.html', {'length'=len(text_split), 'full' : text_split})       # 중요 / count.html에 full, length라는 이름 사용
          
   # count.html
     {{full}}                                                             # template 변수 출력
```  
> `{'full' : text_split}` : text_spllit의 내용을 full이라는 이름으로 전달  
> `len()` : 길이 세는 함수(?)
> length, full이 dictionary

