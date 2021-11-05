##### pygments 패키지  
- 코드 highliting  


오류  
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
``` 
  # project/settings.py
  INSTALLED_APPS = [
      ...
      'rest_framework',
      'snippets.apps.SnippetsConfig'
  ]  
```

3. 모델 생성
```
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

4. Serializer 생성
- instance를 JSON으로 직렬화
- json을 instance로 역질렬화
- Form과 유사 : `required`, `max_length` ...
```
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

5. serializer 사용
```
  python manage.py shell    # shell 실행
  
  # instance 생성
  from snippets.models import Snippet
  from snippets.serializers import SnippetSerializer
  from rest_framework.renderers import JSONRenderer
  from rest_framework.parsers import JSONParser
  
  snippet = Snippet(code='foo = "bar"\n')
  snippet.save()
  snippet = Snippet(code='print("hello, world")\n')
  snippet.save()
  
  # serialization1
  serializer = SnippetSerializer(snippet)
  serializer.data
  #### {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}

  # serialization1 - json으로 변환
  content = JSONRenderer().render(serializer.data)
  content
  #### b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}'

# serialization1
  serializer = SnippetSerializer(snippet)
  serializer.data

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
