### 비동기 처리(중요💛)  
- 순차적으로 작업 실행 (X)  
- 오래걸리는 작업을 실행시키면서 뒤의 코드를 실행시킴  
- Promise 객체 사용 : 대기, 이행, 거부 상태  

### 비동기 호출 - keyword  
- 패턴1   
```python
async function asyncFunction(){
            await [Promise객체]
}
```  
- 패턴2  
```python
[Promise객체]
    .then(콜백함수)
    .then(콜백함수)
    .catch(콜백함수)
```  

- - -  

## Fatch API  
- 외부 API호출  
- 자바스크립트 내부 기능 이용  
- Postman과 유사 / 네트워크 통신을 위해 제공  
- Promise 객체를 반환함  
- Request, Response 객체 사용 / response가 promise  

- - - 

#### 실습 ★   어려움

resolve 함수  
> 반환
reject 함수  
> error 발생
Mat.floor()  
> 소수점이하 버림   
Math.random()  
> 0~1 사이의 랜덤한 숫자 반환
