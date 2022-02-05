## 배운점.
1. [repeat 함수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/repeat)
   repeat함수를 통해 for 구문을 대체할 수가 있다.

2. 중첩 for 구문 사용 시, 변수 = 0를 꼭 지정하여야 한다.
   
```javascript

    var i = 0
    var j = 0
    var result="";
    for (i; i<column; i++){
        for (j; j<row; j++){
            result += "*"
        }
        result +="\n"
    }
```
위와 같이 for 구문 안에 j=0를 지정 하지 않으면, j의 for 루프는 한번만 동작한다. 그 이유는 j가 한번 돌고나서 row보다 큰 값을 유지하기 때문이다.