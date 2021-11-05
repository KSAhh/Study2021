### Github에 업로드  
  ```python
  1. echo "# 레포지토리명" >> README.md                       # README.md 파일을 만들고 "# 레포지토리명"을 적음 / 필요한 프로그램이나 패키지를 적어줌
  2. $ git init                                               # git 배포  
  3. $ git status                                             # 상태확인. 어떠한 파일을 수정했는지 확인 (빨간색 파일)  
  4. $ git add .                                              # git에 .을 추가한다. / "."은 모든 것을 의미 / staging area에 올라감  
  5. $ git status                                             # 빨간색 파일이 초록색 파일로 바뀜  
  6. $ git commit -m "설명"                                   # 설명 작성  

  7. $ git config --global user.email "ID@EAMIL"              # commit이 안되는 경우, github이메일 정보 입력  
  8. $ git config --global user.name "깃허브이름"             # github와 동일해야 함
  9. 다시 commit 
  10. $ git remote add origin 깃허브 레포지토리 링크          # github 저장소와 연동 / "origin"이라는 remote이름으로 연결됨  
  11. $ git push -u origin main (또는 $ git push remote이름 branch이름) # "origin"이라는 리모트이름 & master branch에 업로드  
  ```  
  
### .gitignore  
> Github에 올리지 않아도 되는 파일(Cash 등)을 올리지 않고 저장해주는 역할  
```python
    1. vscode에서 ".gitignore"파일 생성
    2. gitignore (gitignore.io 또는 https://www.toptal.com/developers/gitignore) 접속
    3. "VisualStudioCode", "Django", "Python" 입력 후 검색
    4. Ctrl + A
    5. 복사
    6. 프로젝트 폴더 밑(manage.py가 있는 위치)에 ".gitignore"파일 생성 후 붙여넣기
    7. 14번째 줄 media 밑에 "venv" 입력            # "venv"폴더를 안 올린다는 의미
```  

### 디렉토리 vscode로 열기  
- 디렉토리에서 마우스 우클릭 → Git Bash Here 클릭 → `code .` 입력 → vscode열림

### Git 명령어
```python
  $ git status                             # git 저장소의 상태를 확인
  $ git log                                # 커밋 내역 / q로 벗어남
  $ git branch                             # 현재 브랜치 확인
  $ git branch 브랜치 명                   # 새로운 브랜치 생성
  $ git checkout 브랜치 명                 # 해당 브랜치로 이동
  
  $ git push origin 브랜치                 # 원격 저장소의 특정 브랜치에 업로드 
  $ git pull origin 브랜치                 # 원격 저장소의 특정 브랜치에서 변경사항 pull 해오기
  $ git clone http://원격 저장소 주소.git  # 원격 저장소에 있는 파일 전체 복사
```
