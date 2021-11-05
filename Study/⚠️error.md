TypeError: argument of type 'WindowsPath' is not iterable  
- 원인  
  - 띄어쓰기 오류  
  - `$ python manage.py makemigrations` -> `$ python manage.py migration`  

IndentationError: expected an indented block  
- 원인 : if, while, for, def 등에서 들여쓰기 잘못된 부분 있음  
- 해결 : 에러 메시지에서 line number 확인하고 소스코드 수정  

inconsistent use of tabs and spaces in indentation  
또는 IndentationError: unindent does not match any outer indentation level  
- 원인 : 들여쓰기와 탭을 혼용할 경우  
- 해결 : 들여쓰기를 지웠다가 탭을 해줌

IndentationError: unindent does not match any outer indentation level  
- 원인 : 외부코드를 복사한 경우 많이 나타남. vscode에서 tab을 space-bar를 누른걸로 인식함  
- 해결 : 들여쓰기를 지웠다가 탭을 해줌  

Permission denied  
- 원인 : 로컬에 설치된 python version이 여러개 일때
- 해결 : `Ctrl + Shift + P` → `python: Select Interpreter` → `자신이 쓰는 python버전 선택`   
        : [사이트](https://gentlesark.tistory.com/32)  
  
error: failed to push some refs to "https://github.com/~~.git"  
hint: Updates were rejected because the remote contains work that you do  
hint: not have locally. This is usually caused by another repository pushing  
hint: to the same ref. You may want to first integrate the remote changes  
hint: (e.g., 'git pull ...') before pushing again.  
hint: See the 'Note about fast-forwards' in 'git push --help' for details.  
- 원인 : Repository를 만들 때, README.md를 미리 생성하고 main branch에 push 하는 경우  
- 해결 : `$ git push -u origin +master` +를 붙여줌  
    - : [사이트](https://doozi316.github.io/errorlog/2019/09/30/error1/)  

warning: LF will be replaced by CRLF in Study/기타.md.  
- 원인
  - MAC or Linux를 쓰는 개발자와, Window를 쓰는 개발자가 협업할 때 발생
  - Whitespace 에러  
  - 유닉스 시스템에서는 한 줄의 끝이 LF(Line Feed)로 이루어지지만, 윈도우에서는 줄 하나가 CR(Carriage Return)와 LF(Line Feed) 즉, CRLF로 이루어지기 때문  
  - 어느 한 쪽을 선택할지 Git은 혼란스러움  
- 해결  
  - 자동 변환해주는 Git의 기능(core.autocrlf) on
  - git에 코드를 추가(커밋) 할 때 : CRLF → LF 변환  
  - git의 코드를 조회(clone) 할 때 : LF → CRLF 변환
  - Window사용자 : `git config --global core.autocrlf ture` 현재 프로젝트에만 적용하려면 --global 제외  
  - Linux, MAC : `git config --global core.autocorlf true input`  
  - 이외에 에러 메세지 끄고 싶을 때 : git config --global core.safecrlf false  
  - [사이트](https://blog.jaeyoon.io/2018/01/git-crlf.html)  

UnboundLocalError: local variable 'gun' referenced before assignment  
- 원인 : 지역변수가 전역변수처럼 쓰였을 때  
- 해결
  - 전역변수로 변경  
  - 함수 내에서 `global 변수명` 사용하거나, `함수형태 변경`  
  
SyntaxError: invalid syntax  
- 원인 : 앞 문장의 `)` 생략된 경우  ex) `print("happy"` 
- 해결 : `)` 추가  

python에서 한글이 깨지는 경우  
- 해결  
  - [사이트](steady-coding.tistory.com/262)  
  - vscode 기본 인코딩 옵션을 `euc-kr`로 변경 후 소스코드에 추가  
    ```python
      # -*- coding: euc-kr -*-
      import sys
      import io
      sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
      sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
    ```  
push에 실패한 경우  
  ``` remote: error: GH007: Your push would publish a private email address.
  remote: You can make your email public or disable this protection by visiting:
  ```  
- 해결  
  - [사이트]()  
  - 방법1. Settings > Emails > Keep my email addresses private 체크해제
  - 방법2. Settings > Emails > Keep my email addresses private 체크 > 고유 {ID}+{username}@users.noreply.github.com 확인  
          ```
          $ git config --global user.email "{ID}+{username}@users.noreply.github.com" 
          $ git commit --amend --reset-author
          ```  
          
Secrete key 비공개  
[사이트](https://integer-ji.tistory.com/180)  

# vscode  
migration 초기화  
- https://velog.io/@kho5420/Django-Django-%EB%A7%88%EC%9D%B4%EA%B7%B8%EB%A0%88%EC%9D%B4%EC%85%98-%EC%B4%88%EA%B8%B0%ED%99%94  
- https://velog.io/@inyong_pang/Django-Migrate-%EC%B4%88%EA%B8%B0%ED%99%94

뭔지 잘 모르겠을때  
- 주석 

return database_name == ':memory:' or 'mode=memory' in database_name  
- setting.py 'NAME': str(BASE_DIR / 'db.sqlite3'),'  
