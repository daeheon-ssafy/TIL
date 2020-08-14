## django

* dynamic web : 동적 웹페이지 사용자 요청에따라 응답이 다르게옴. (<-> static web : github page, html, css)

* python web framework : 웹페이지를 개발하는 과정에서 겪는 어려움을 줄이는것이 주목적이다.

  ​											기본적인 구조나 필요한 코드를 제공해줌

  ​											파이썬 기반

  ​											spotify, instagram, dropbox, delivery Hero

* 개발자 커뮤니티가 활성화 되어있다.

* 웹 서버를 구축한다는 느낌

* ```모델-뷰-컨트롤러 모델 패턴```을 따르고 있다.(not MVC but MTV)

  * Model : 데이터 관리
  * template : 인터페이스
  * view : 중간관리(상호 동작)







## 시작하기

Django 3.1

```pip list```

* 장고 설치하기

  ```
  pip install django
  # 특정 버전
  pip install django==3.0.8
  ```

  





### 프로젝트

* 하이픈 사용 x

* python, django에서 기본적으로 사용되는 이름 x

* ex: 

  ```
  django-admin startproject first_project
  ```

  * ```first_project```라는 이름으로 폴더가 생성

    * 여기 안에는 ```first_project```

      * first_projet: 프로젝트 설정 파일이 들어있음

      * manage.py :창고 명령어를 실행하기 위한거

        ```python manage.py 장고명령어```

* 가장 바깥의 프로젝트 폴더명은 수정가능하나 setting 파일이 들어있는 폴더명은 건드리지 말자.







* 장고 실행하기

  ```
  python manage.py runserver
  ```

  











## 앱

* 장고 프로젝트는 application의 집합체로 동작
  * 실제로 어떠한 역할을 해주는 것이 app.
  * 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있음.
    * 어플리케이션: 하나의 역할 및 기능 단위로 쪼개진 행태.
      * 회원관리/ 글 작성, 수정, 글 삭제 / 데이터를 수집 분석 / .......
      * 어플리케이션을 이렇게 나눠야한다라는 기준은 없다.
      * 작은 프로젝트라면 어플리케이션을 따로 나누지 않아도 된다.



이름: 복수형으로 만든다 

* ```python manage.py startapp articles```
  * 해당 앱 이름으로 폴더가 생성됨 (앱폴더)
  * 바로해야하는일 무조건 바로해야 안까먹음!!!
  * ```settings.py```에 내가 생성한 app을 등록해 줘야함.
  * ```installed_app```에 가장 윗줄에 등록해준다.
  * laguage_code = 'ko-kr' 왠만하면 소문자로
  * time_zone = 'Asia/Seoul' 대소문자 주의.





## MTV(MVC 패턴)

Model : 장고에서는 Model

View : 장고에서는 Template

Controller : 장고에서는 View



* 3대장 : 우리가 가장 밀접하게 수정해야 하는 파일명
  * urls.py
  * views.py
  * templates (html 들)

* urls.py 에서 해야할 일

  path('url 패턴/', 실행이 되어야 하는 views에 있는 함수, 해당 path의 별명)

  * 많이 놓치는 부분 : url 뒤에 슬러쉬!

* views.py에서 해야할 일

  * 함수를 정의(첫번째 인자로 request 필수	
  * return은 꼭 필요
    * render:주로 template 과 함께 respense 할 때 사용되는 함수.

* template에서 해야할 일

  * 폴더 명은 반드시 ```templates```인 것을 확인







## 장고 동작 정의 방법

* Template Variable

  * html 과 같은 tempate에서 views.py에서 준비한 변수를 가져다가 쓰는 방법.

  * render() 세번째 인자로 ```{'key': value}```와 같이 딕셔너리 형태로 넘겨주면 Template에서 key를 이용하여 value를 가져 올 수 있다.

    ```
    context = {'key':value}
    return render(request, 'index.html', context)
    ```

    ```
    {{ key }} 이렇게 value를 보여줄 수 있다.
    ```

* variable Routing(동적 라우팅)

  * url 주소 일부를 변수처럼 사용해서 동적인 주소를 만드는 것.

    ```https://127.0.0.1:8000/hello/문자열```

    urls.py

    ```
    path('hello/<str(타입):name(저장되는 변수명)>/', views.hello
    ```

    views.py

    ```
    def hello(request, name(저장되는 변수명)):
    	print(name)
    	context = {
    		'name' : name,
    	}
    	return render(request, 'hello.html', cotext)
    ```

    template(hello.html)

    ```
    <body>
    이름은 : {{ name }} # context의 key값을 사용하면 value를 출력한다.
    </body>
    ```





* DTL (tag와 filter)

  * 로직을 표현 할때는 : ```{% for %}```

  * 값을 표현 할 때는 : ```{{ }}```

  * 주석으로 나타내고 싶을때는 : `{{# #}}` or `{% comment %}` 주석할 내용 `{% endcomment %}`

  * for 태그

    * 반복을 위한 태그

      ```
      {% for 임시변수 in iterable 한 객체 %}
      {% endfor %}
      ```

    * for empty

      ```
      {% for 임시변수 in iterable 한 객체 %}
      	값이 하나라도 있으며 여기가 실행
      {% empty %}
      	출력할 값이 없으면 출력.
      {% endfor %}
      ```

  * if 태그

    * 조건을 구분하기 위한 태그

      ```
      {% if 조건문 %}
      {% elif 조건문 %}
      {% else %}
      {% endif %}
      ```

  *  나머지는 dtl문서를 참고. (구글 검색시 django built in template 검색)

* Form

  * HTML form tag 의미

  * 입력받은 데이터를 어딘가로 보낼때 사용

    ```
    # action : 보내려는 목표 # method : http method (get / post)
    <form action="" method="GET">
    
    	input 데이터를 입력 받게 적절히 코딩 하면 됨.
    	
    	# 오락실 버튼
    	<input type="button">
    	
    	# 미사일 버튼
    	<input type="submit">
    	
    	<button></button>
    </form>
    ```

    * action 에 들어가는 목표 url 설정 주의 사항

      ```
      action="/catch/"
      => 127.0.0.1:8000/catch?name=asdf
      
      현재 주소 : 127.0.0.1:8000/index
      action="catch/"
      => 127.0.0.1:8000/index/catch?name=asdf
      ```

      











































### Django Template Language (DTL)

* django template system 에서 사용하는 built-in template system 이다.
* 조건, 반복, 치환, 필터, 변수 등의 기능을 제공.
* 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한것
* 파이썬 처럼 if, for을 사용할 수 있지만 이것은 단순히 python code로 실행되는 것은 아님.





syntax

* variable : {{ }}
* filter : {{ variable|filter }}
* tags : {% tag %}





## 템플릿 시스템 설계 철학

* 장고는 탬플릿 시스템이 표현을 제어하는 도구이자 표현에 관련된 로직일뿐이라고 생각한다.
* 템플릿 시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안된다.
* 