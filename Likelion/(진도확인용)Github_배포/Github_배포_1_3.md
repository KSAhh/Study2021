# Command

    git init
> initial   
> git 저장소 초기화

    git add .
> 변경된 내용 staging area에 올림

    git commit -m "설명" 
> commit에 대한 설명   
> Check point 생성

    git remote add origint http://원격 저장소 주소.git
> 원격 저장소와 로컬 저장소(remote repository)를 연결

    git branch 브랜치 명
> new 브렌치 생성

    git checkout 브랜치 명
> 해당 브렌치로 이동

    git push origin 브랜치
> 원격 저장소의 특정 브렌치에 프로젝트 "저장"

    git pull origin 브랜치
> 원격 저장소의 특정 브랜치에서 벼경사항 "pull" 

    git clone http://원격저장소 주소.git
> 원격 저장소의 파일 전체 "복사"

    git status
> git 저장소 "상태 확인"   
> 남아있는 파일 확인
- - -
공유 작업
1. 원격 저장소 생성 (repository)  
2. 팀원 추가 (Collaborator)  
3. 초기 프로젝트 push  
4. 팀원들의 로컬에 프로젝트 pull(또는 clone)  
5. 팀원 각자 브랜치 생성 -> 작업  
6. 브랜치에 작업한 내용 push  
7. pull request  
8. request 확인 후 Master와 merge  

3  
git bash  
-> "git init"  
-> "git remote add origin https://~(repository 주소)"  
-> "git add ." -> "git commit -m "~""  
-> "git status"  
-> "git push origin master" // 초기프로젝트 push

4  
팀원  
git bash  
-> "cd .."  
-> "mkdir other_user"(바탕화면에 other_user폴더생성)  
-> "cd other_user"  
-> git clone https://~(repository url)"(초기 프로젝트 다운)  
-> "ls"(확인)  

5,6  
git bash  
-> "git branch"(default brach인 master로 나옴)  
-> "git branch (이름)"(생성)  
-> "git branch"(이름으로 바뀜)  
-> "git checkout (이름)"(이름 brach로 이동)  
-> "code ."(vscode 열림)  
-> 작업  
-> "git add ."  
-> "git status"(변경 사항 나옴)  
-> "git commit -m "(설명)"  
-> "git push origin (이름)"(원격 저장소 branch에 올림. 새로운 branch 만들어짐)  
-> "git status"(commit할 내용 없는 지 확인)  
-> github에 들어가서 확인  

7  
github 사이트  
-> repository내의 Pull requests  
-> New pull request
-> base (어디에 적용할 것인지), compare (어디서 적용할 것인지) 선택  
-> 변경내용 확인가능  
-> create pull request  
-> 제목, 내용  
-> create pull request  
-> 팀장이 승인/거절  

- - -
★mater 내용 복습

- - -
# fork

1. 작업하고싶은 Repository fork  
2. 자신의 로컬에서 작업  
3. 변경사항을 자신의 브랜치에 push  
4. 원본 repository 소유자에게 Pull request 요청  
5. 소유자가 pull request를 수용하여 merge하면 collaborator 자동 추가  

1  
github  
-> repository 선택  
-> fork

2  
git bash  
-> "mkdir fork"(fork라는 폴더 만듦)  
-> "ls"  
-> "cd fork"
-> git clone (원본repository url)"  
-> "ls"  
-> "code ."  
-> 작업  
-> cd Spoon-Knife"  
-> "git status"  
-> "git add ."  
-> "git commit -m "(변경내용)"  
-> git checkout -b jungho"(jungho라는 brach를 만들면서 바로 체크아웃)  
-> git push origin jungho"(jungho 브랜치에 올라감)  
