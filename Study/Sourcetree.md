\* clone : 원격 저장소 복사  
\* 현재 branch / head branch  

\* commit내용 작성 요령  
  : 요약 한줄 작성 → 한줄 띄움 → 자세한 내용 작성  

\* 이전 commit으로 되돌리기  
  : "코드뭉치 버리기"  
  : "checkout"  
  
\* merge  
    : 최종 master branch로 합치는 과정  

\* reset후, 다른 내용 작성 후, push (3가지)  
  1. 강제 push 또는 터미널에서 `$ git push --force`  
  2. 병합(merge) 후 push  
  3. brach를 만들어서 되돌림  
  
\* revert로 되돌리기
  : "커밋 되돌리기"  
  : 또다시 되돌리려면 "초기화 -> hard"  
  : 내용은 바껴도 commit은 남길 수 있다 but 충돌 나기 쉽다  
   
   
  : 여러개 되돌릴때는 최신부터 순서대로 reverT반복 (하나 revert한 상태에서 다른 요소 revert)  
  : 터미널에 작성 `$ git revert HEAD HEAD~1` HEAD~1은 부모요소
  : 터미널 빠져나가기 `ESC` → `:WQ`

\* 커밋하지않은 변경사항 (2가지)  
  1. → 임시 저장(커밋) → 체크아웃 → 다시 브랜치로 돌아옴 → 작업 → 커밋 덮어쓰기("마지막 커밋 정정")  
     git에 branch올린 후, 정정했을 때 → "$ git push --force"  

  2. 스태시 (임시 저정공간)에 저장 → 다시 사용할때 "스태시 적용"  
     신규파일(스테이지에 없는 파일/untracted) 은 스태시가 안 됨 / 그러므로 스테이지에 올리고 사용  
  
\* "브랜치 삭제"
  
\★* Rebase (재배치)  
  : 두 브랜치 합침  
  : 협업시 주의해야함 / 이미 원격저장소에 올라간 경우  
  
  
