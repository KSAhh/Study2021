### EB  
- Elastic Beanstalk  
- 웹 앱과 서비스의 배포, 관리, 증감 돕는 서비스  

- 필수 구성 요소 : Python 3.6 이상, pip, virtualenv, awsebcli
  - `$ pip --version` : pip 버전확인  
  - `$ virtualenv --version` : virtualenv 버전확인  
  - `$ eb --version` : awsebcli 버전확인  
  - `$ pip install virtualenv` : virtualenv 설치  
  - `$ pip install awsebcli` : awsebcli 설치  

1. `$ mkdir aws-eb` : 작업폴더 생성  
2. 가상환경폴더 생성 및 활성화  
3. `$ pip install django==2.2.1` : 2.2.1버전 장고 설치  
4. `$ pip freeze` : Django 버전확인  
5. `$ git clone 레포 주소` : repository 가져오기
6. `$ ls` : 현재 파일 확인. 이때 가져온 repo 이름 확인  
7. `$ cd 레포 이름`  
8. `$ code .`  

<br>

9. `$ python manage.py runserver` : 오류를 통해 필요한 package 확인  
10. 
.. 노트에
