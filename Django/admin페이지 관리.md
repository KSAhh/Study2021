### admin 변경목록  
- 기본값
  - 페이지 당 100개 항목
  - 자동 페이지네이션

- - -  

1. 
### 필드 정렬  
  ```python
    # polls/admin.py
    class QuestionAdmin(admin.ModelAdmin):
        fields = ['pub_date', 'question_text']
        
    admin.site.register(Question, QuestionAdmin)
  ```  

### 필드셋 정렬  
  ```python
    # polls/admin.py
    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,                  {'fields': ['question_text']}),
            ('Date information',    {'fields': ['pub_date']}),
        ]
        
    admin.site.register(Question, QuestionAdmin)
    admin.site.register(Choice)
  ```  
  
- - -  

2. 데이터 추가  
### 필드 리스트로 표시  
  ```python
    # polls/admin.py
    class ChoiceInline(admin.StackedInline):
        model = Choice
        extra = 3
        
    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None,                  {'fields': ['question_text']}),
            ('Date information',    {'fields': ['pub_date'], 'classes':['collapse']}),
        ]
        inlines = [ChoiceInline]
        
    admin.site.register(Question, QuestionAdmin)
    admin.site.register(Choice)
  ```  
  
### 필드 테이블로 표시  
  ```python
    # polls/admin.py
    class ChoiceInline(admin.TabularInline):
        ...
  ```  
  
- - -  

3. 기능  
### 열 추가 (정렬 포함 / 날짜 정렬 안됨)
  ```python 
    # polls/admin.py
    class QuestionAdmin(admin.ModelAdmin):
        ...
        list_display = ('question_text', 'pub_date', 'was_published_recently')
  ```  

#### 날짜열 정렬  
  ```python
    # polls/models.py
    import datetime # python의 표준 모듈
    from django.contrib import admin
    
    class Question(models.Model):
        ...
        @admin.display(
            boolean = True,
            ordering = 'pub_date',
            description = 'Published recently?',
        )
        def was_published_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.pub_date <= now       
  ```  

### 날짜 필터
  ```python 
    # polls/admin.py
    class QuestionAdmin(admin.ModelAdmin):
        ...
        list_filter = ['pub_date']
  ```  
  
### 검색  
  ```python 
    # polls/admin.py
    class QuestionAdmin(admin.ModelAdmin):
        ...
        search_fields = ['question_text']   # question_text 필드 검색
  ```  
- 내부적으로 LIKE query 사용  
- 검색 필드 수를 제한하면 효율적으로 DB 검색  
- 
