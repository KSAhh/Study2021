
#### 직렬화  
- instance to JSON  

#### 역직렬화  
- JSON to instance  

#### 오류  
- `ImportError: cannot import name 'Required' from 'typing_extensions'`  
- 해결 : 버전 문제 `pip install typing_extensions==3.10.0.0`  


- - -  

# 실습  
1. 패키지 설체  
```
  $ pip install djangorestframework
  $ pip install pygments
```  
- pygments : 코드 highlighting

2. "snippets" app 생성 및 추가
```python 
  # project/settings.py
  INSTALLED_APPS = [
      ...
      'rest_framework',
      'snippets.apps.SnippetsConfig'
  ]  
```

3. 모델 생성
```python 
  # app/models.py
  ...
  from pygments.lexers import get_all_lexers
  from pygments.styles import get_all_styles

  LEXERS = [item for item in get_all_lexers() if item[1]]
  LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
  STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

  class Snippet(models.Model):
      created = models.DateTimeField(auto_now_add = True)
      title = models.CharField(max_length=100, blank=True, default='')
      code = models.TextField()
      linenos = models.BooleanField(default=False)
      language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
      style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
```   
```
  $ python manage.py makemigrations snippets
  $ python manage.py migrate
```

4-1. Serializer 생성
- instance를 JSON으로 직렬화
- json을 instance로 역질렬화
- Form과 유사 : `required`, `max_length` ...
```python 
  # app/serializers.py
  from rest_framework import serializers
  from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

  class SnippetSerializer(serializers.Serializer):
      """직렬화/역직렬화 field 정의"""
  # 값 검증을 위한 옵션 추가 가능
      id = serializers.IntegerField(read_only=True)
      title = serializers.CharField(required=False, allow_blank=True, max_length=100)
      code = serializers.CharField(style={'base_template':'textarea.html'})
      linenos = serializers.BooleanField(required=False)
      language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
      style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

  # serialize가 호출됐을 때
      def create(self, validated_data):
          """검증한 데이터로 새 'Snippet' 인스턴스를 생성하여 반환"""
          return Snippet.objects.create(**validated_data)

      def update(self, instance, validated_data):
          """검증한 데이터로 기존 'Snippet' 인스턴스를 업데이트한 후 반환"""
          instance.title = validated_data.get('title', instance.title)
          instance.code = validated_data.get('code', instance.code)
          instance.linenos = validated_data.get('linenos', instance.linenos)
          instance.language = validated_data.get('language', instance.language)
          instance.style = validated_data.get('style', instance.style)
          instance.save()
          return instance
```
4-2. ModelSerializer 생성
```python
  class  SnippetSerializer(serializers.ModelSerializer):
      class Meta:
          model = Snippet
          fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
```


5. serializer 사용  
- 일반적인 model : serializer = SnippetSerializer(snippet)  
- queryset : serializer = SnippetSerializer(Snippet.objects.all(), many=True)  
```python 
  python manage.py shell    # shell 실행
  
  # instance 생성
  from snippets.models import Snippet   # from [app명].models import [클래스]
  from snippets.serializers import SnippetSerializer
  from rest_framework.renderers import JSONRenderer
  from rest_framework.parsers import JSONParser
  
  snippet = Snippet(code='print("hello, world")\n')
  snippet.save()
  
  # serialization1 - 일반적인 model
  serializer = SnippetSerializer(snippet)
  serializer.data
  #### {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}

  # serialization1 - json으로 변환
  content = JSONRenderer().render(serializer.data)
  content
  #### b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}'

  # serialization2 - queryset
  serializer = SnippetSerializer(Snippet.objects.all(), many=True)
  serializer.data
  # [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]

  # deserialization
  import io

  stream = io.BytesIO(content)
  data = JSONParser().parse(stream)

  # deserialization - native datatype to object instance
  serializer = SnippetSerializer(data=data)
  serializer.is_valid()
  #### True
  serializer.validated_data
  #### OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
  serializer.save()
  #### <Snippet: Snippet object>
```  

6. ModelSerializer 사용
```python
  # app/serializers.py
  class SnippetSerializer(serializers.ModelSerializer):
    ...
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
```  

7-1. READ, CREATE 기능  
- GET : 기존 데이터 보여줌  
- POST : 새 데이터 생성  
```python
  # app/views.py
  from django.http import HttpResponse, JsonResponse
  from django.views.decorators.csrf import csrf_exempt
  from rest_framework.parsers import JSONParser
  from snippets.models import Snippet
  from snippets.serializers import SnippetSerializer
  
  @csrf_exempt
  def snippet_list(request):
      """
      List all code snippets, or create a new snippet.
      """
      if request.method == 'GET':
          snippets = Snippet.objects.all()
          serializer = SnippetSerializer(snippets, many=True)
          return JsonResponse(serializer.data, safe=False)

      elif request.method == 'POST':
          data = JSONParser().parse(request)
          serializer = SnippetSerializer(data=data)
          if serializer.is_valid():
              serializer.save()
              return JsonResponse(serializer.data, status=201)
          return JsonResponse(serializer.errors, status=400)
```

7-2. SEARCH, UPDATE, DELETE  
- GET : 검색   
- PUT : 생성/업데이트
- DELETE : 삭제  
```python
  @csrf_exempt
  def snippet_detail(request, pk):
      """
      Retrieve, update or delete a code snippet.
      """
      try:
          snippet = Snippet.objects.get(pk=pk)
      except Snippet.DoesNotExist:
          return HttpResponse(status=404)

      if request.method == 'GET':
          serializer = SnippetSerializer(snippet)
          return JsonResponse(serializer.data)

      elif request.method == 'PUT':
          data = JSONParser().parse(request)
          serializer = SnippetSerializer(snippet, data=data)
          if serializer.is_valid():
              serializer.save()
              return JsonResponse(serializer.data)
          return JsonResponse(serializer.errors, status=400)

      elif request.method == 'DELETE':
          snippet.delete()
          return HttpResponse(status=204)
```  

8-1. 전체 데이터 목록 읽기  
```python
  $ python manage.py runserver  
  $ http http://127.0.0.1:8000/snippets/
```  

8-2. 특정 데이터 목록 읽기  
```python
  $ http http://127.0.0.1:8000/snippets/2/
```  


![image](https://user-images.githubusercontent.com/66674138/140513218-f2545691-e6b6-47a6-b746-55058fc6cc7e.png)


![image](https://user-images.githubusercontent.com/66674138/140513303-358e2391-7dfa-4434-8564-86a4abe0800f.png)


![image](https://user-images.githubusercontent.com/66674138/140513264-ab6f6340-acc5-42f6-9371-37f845c770f9.png)

![image](https://user-images.githubusercontent.com/66674138/140513271-238da2dc-1906-49e5-9a96-fed91b658da1.png)







