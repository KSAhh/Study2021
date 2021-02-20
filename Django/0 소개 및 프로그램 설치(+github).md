### 작업환경 설치(윈도우)  
1. python 설치  
    ```
    "python.org" 접속 → "Python 3.8.3" 클릭 → 'Add Python 3.8 to PATH' 체크 → install → Next...
    ```  
2. Visual Studio Code  
    ```
    "vscode" 검색 → "Visual Studio Code - Code Editing. Redeifined" 클릭 → "Downloads for Windows" 클릭 
    ```  
3. Git Bash  
    ```
    "git bash" 검색 → "Git for Windows" 접속 → "Download" 클릭 → Next... → 'Use Visual Studio Code as Git's default editor' 설정 → Next...
    ```  
4. Postman  
  - API테스트 도구  
    ```
    [사이트 이동](https://www.postman.com/downloads/)  
    ```   
- - -  

# FramWork
- fram: 틀 / work: 일하다  
- 짜여진 환경에서 개발하도록 돕는것  
- 반복 작업을 표준화해서 묶어 놓은 개발환경 
- 정해진 방식으로 코드 짜도록 강요(O) / 필요할 때 가져다 씀(X) 
- ex) Django(웹 만들기 위함)  

# 라이브러리  
- 반복 작업을 줄여주는 역할  
- 정해진 방식으로 코드 짜도록 강요(X) / 필요할 때 가져다 씀(O)  

## Django  
- 웹 어플리케이션 프레임워크    
- MVT패턴 (티키타카)  
    - Model Template View  
    - Model : "data저장 형태 결정" / DB에 저장되는 data / 표 형태 / ORM제공  
        - ORM : Object-Relational Mapping / SQL언어 없이 DB 쉽게 연결해줌  
    - Template : "화면 수정" / 사용자가 보는 화면  
    - View : "data 처리, 가공" / 웹 요청받아 얻은 data를 가공 후, template에 보냄  
    - URLconf : "가공한 data를 화면으로 보냄" / url설계 / view와 template 이어줌  
- 기능
    - python 기반  
    - admin기능 제공  
    - 쉬운 URL파싱 기능  

<br>

- Project  
> settings.py : 전체 프로젝트 관리하는 설정 file  
> urls.py : 프로젝트의 URL 관리 파일  
> wsgi.py 또는 asgi.py : 프로젝트를 서비스하기 위한 파일. 배포할 때 사용  
> \_\_init__.py : 해당 directory가 Python Package의 일부임을 Python에게 알려주는 file  
- App  
> Django프로젝트를 이루는 작은 단위


> views.py : 웹 요청 받음. 받은 데이터를 처리, 가공  
> models.py : Dagtabase와 관련  
> admin.py : 관리자 관련  
> apps.py : Project에게 App의 존재를 알려줄때

- - -  

# 실습

### gitignore  
    ```
    1. vscode에서 ".gitignore"파일 생성
    2. gitignore (gitignore.io 또는 https://www.toptal.com/developers/gitignore) 접속
    3. "VisualStudioCode", "Django", "Python" 입력 후 검색
    4. Ctrl + A
    5. 복사
    6. 프로젝트 폴더 밑(manage.py가 있는 위치)에 ".gitignore"파일 생성 후 붙여넣기
    7. 14번째 줄 media 밑에 "venv" 입력            # "venv"폴더를 안 올린다는 의미
    ```
> Github에 올리지 않아도 되는 파일(Cash 등)을 올리지 않고 저장해주는 역할  

<br>

### github에 업로드  
```python
1. echo "# 레포지토리명" >> README.md                         # README.md 파일을 만들고 "# 레포지토리명"을 적음 / 필요한 프로그램이나 패키지를 적어줌
2. $ git init                                               # git 배포  
3. $ git status                                             # 상태확인. 어떠한 파일을 수정했는지 확인 (빨간색 파일)  
4. $ git add .                                              # git에 .을 추가한다. / "."은 모든 것을 의미 / staging area에 올라감  
5. $ git status                                             # 빨간색 파일이 초록색 파일로 바뀜  
6. $ git commit -m "설명"                                    # 설명 작성  
6-1. $ git log                                              # 커밋한 내용 볼 수 있음 / q로 벗어남
7. $ git config --global user.email "ID@EAMIL"              # commit이 안되는 경우, github이메일 정보 입력  
8. $ git config --global user.name "깃허브이름"              # github와 동일해야 함
9. 다시 commit하기  
10. $ git remote add origin 깃허브 레포지토리 링크             # github 저장소와 연동 / "origin"이라는 remote이름으로 연결됨  
11. $ git push -u origin master (또는 $ git push remote이름 branch이름)                             # "origin"이라는 리모트이름 & master branch에 업로드  
```  
```python
git branch (또는 git status)          # 현재 브랜치 확인
git branch 브랜치 명                   # 새로운 브랜치 생성
git checkout 브랜치 명                 # 해당 브랜치로 이동
git push origin 브랜치                 # 원격 저장소의 특정 브랜치에 프로젝트 저장
git pull origin 브랜치                 # 원격 저장소의 특정 브랜치에서 변경사항 pull 해오기
git clone http://원격 저장소 주소.git   # 원격 저장소에 있는 파일 전체 복사
git status                             # git 저장소의 상태를 확인
```

### 함수  
- text_split  
    ```python
    views.py파일
        def count(request):
            text_split = text.split()
    ```  
    > 띄어쓰기 단위로 문자가 끊겨서 저장됨  
    ```python
    views.py파일
        text_split = text.split(' ')  # 배열로 저장 (LIST)
        print(text_split[5])  # LIST중 5번째 데이터 출력
    ```  

- - -  

[Word Counter](wordcount1234.herokuapp.com)  
- views.py 파일  
    ```python
    def count(request):
    text = request.GET['fulltext']
    text_split = text.split(' ')

    word_dic = {}                   # 비어있는 word dictionary 생성
    for word in text_split:
        if word in word_dic.keys(): # word가 word_dic.keys()값에 있으면
            word_dic[word] += 1     # 단어 개수에 하나 추가
        else:
            word_dic[word] =1       # keys값에 없으면 word_dic[]에 1을 넣음. 즉 생성
    ```  
