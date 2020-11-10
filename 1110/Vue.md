## Vue Directive

```html
<div id="app">
    
</div>

<!-- vue CDN 추가 -->
<script>
	const app = new Vue({
        el: '#app', // 어떤 엘리먼트와 연결할 지 정함.
        data: {
            // vue 에서 사용되는 변수들
            // 다양한 정보의 타입이 저장될 수 있다.
        },
        methods: {
            // vue 에서 사용할 함수들을 정의하는 곳
            // 메소드를 정의 할 때는 화살표 함수를 사용하지 않는다. (this)
        }
    })
</script>
```

* v-html

  * innerHTML 로 할당
  * HTML 을 그대로 읽기 때문에 XSS 공격에 취약

* v-text

  * innerText로 할당
  * {{ 머스타치 }} : 보간법 (interpolation)

* v-if, v-if-else, v-else

  * 조건문에 따라서 해당 Tag의 렌더링(노출)여부를 결정
  * 조건문에 부합되지 않으면 아예 코드 자체가 렌더링 되지 않는다.
  * v-if, v-else 를 사용할 때 사이에 어떠한 Tag가 있으면 제대로 동작하지 않는다.

* v-show

  * v-show의 값에 따라 css display 속성을 조절해서 화면 노출을 결정.

* v-for

  * 반복문

* v-bind

  * HTML 표준속성에 Vue의 데이터를 연결

  * `:` (shortcut)

  * Object 형태(키-벨류)로 사용하면 value가 true 인 경우만 바인딩 된 값으로 할당 가능.

    `:class = "{ 클래스 이름:false }"`

* v-model

  * 양방향 바인딩
  * 입력되어지는 태그 (input, TextArea, Select) 사용

* v-on

  * 이벤트
  * `@` (shortcut)



* this 정리

  * obj.functionCall() => this === obj : 메소드 호출되었을때

  * 그 외 => this === window

    ```html
    const myObj = {
    	myFunc : function () {
    		console.log(this) //myObj
    		// 1. 콜백 함수에서 this를 obj로 만드는 방법 (.bind)
    		axios.get(URL)
    			.then(function () {
    				console.log(this) // myObj
    		}.bind(myObj))
    		
    		// 2. 콜백 함수에서 this를 obj로 만드는 방법
    		axios.get(URL)
    			.then(() => {
    				console.log(this)
    			})
    		}
    	}
    ```







## computed & watch

### computed

* 값을 캐싱하기 때문에 값이 변하지 않으면 기존에 계산된 값(캐싱된 값)을 사용

* x + 2 = 3      /  3을 사용하다가 x의 값이 변하면 변한 값으로 사용

* 특정한 데이터를 직접적으로 가공하여 다른 값으로 만들어 사용할 때 주로 활용

  `반갑습니다. 00 시 입니다.`

* 최종 데이터형식이 정해져 있고 변경된 값은 항상 최종 데이터 형식을 가지기 때문에 `선언형 프로그래밍`



### Watch

* 데이터가 변경이 되는지 지켜보고 변경이 된다면 특정 함수를 실행.

* 특정한 데이터의 변화에 따라서 다른 데이터 혹은 환경등을 변화 시켜야 하는 경우에 주로 활용.

  `00시의 날씨는 00 입니다.`

* `명령형 프로그래밍`