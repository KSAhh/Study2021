TypeError: argument of type 'WindowsPath' is not iterable  
- 원인  
  - 띄어쓰기 오류  
  - `$ python manage.py makemigrations` -> `$ python manage.py migration`  

inconsistent use of tabs and spaces in indentation  
- 원인 : 들여쓰기와 탭을 혼용할 경우  
- 해결 : 들여쓰기를 지웠다가 탭을 해줌

IndentationError: unindent does not match any outer indentation level  
- 원인 : 외부코드를 복사한 경우 많이 나타남. vscode에서 tab을 space-bar를 누른걸로 인식함  
- 해결 : 들여쓰기를 지웠다가 탭을 해줌  

Permission denied  
- 원인 : 로컬에 설치된 python version이 여러개 일때
- 해결 : `Ctrl + Shift + P` → `python: Select Interpreter` → `자신이 쓰는 python버전 선택`   
        : [사이트](https://gentlesark.tistory.com/32)  
  
# vscode  
- 주석 안될때 / 마이크로소프트 입력기로 변환  
```Ctrl + Shift```  

migration 초기화  
- https://velog.io/@kho5420/Django-Django-%EB%A7%88%EC%9D%B4%EA%B7%B8%EB%A0%88%EC%9D%B4%EC%85%98-%EC%B4%88%EA%B8%B0%ED%99%94  
- https://velog.io/@inyong_pang/Django-Migrate-%EC%B4%88%EA%B8%B0%ED%99%94

뭔지 잘 모르겠을때  
- 주석 

return database_name == ':memory:' or 'mode=memory' in database_name  
- setting.py 'NAME': str(BASE_DIR / 'db.sqlite3'),'  
