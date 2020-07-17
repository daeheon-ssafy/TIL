https://github.com/mulcamp-ed/TIL

# Git

### 준비하기

윈도우에서 git을 활용하기 위해서 git bash를 설치한다 초기 설치를 완료한 이후에 컴퓨터에 author정보를 입력한다.

```python
$ git config --global user.name {user name}
$ git config --global user.email {user email}
```

### 1. 저장소 초기화

```python
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/TIL/.git/
```

* .git  폴더가 생성되며, 여기에 git과 관련된 모든 정보가 저장된다.
* git bash에 (master) 라고 표시가 된다.

### 2. add

working directory (작업공간)  변경된 사항을 이력으로 저장하기 위해 반드시 staging area에 올려야한다.

```python
$ git add git_정리.md # 특정파일
$ git add python/ # 특정폴더
$ git add . #현재 디렉토리의 모든 파일
```



### 3. commit

* 버전의 이력을 확정짓는 명령어, 해당 시점을 스냅샷으로 만들어서 기록을 한다.

* 커밋시에는 반드시 log 메세지를 작성해야하며, log메세지는 변경사항을 알 수 있도록 명확하게 작성해주면 된다.

  ```python
  $ git commit -m '깃 정리 문서 작성'
  ```

## 원격 저장소

### 0.repository 생성

### 1. 원격 저장소를 local에 등록

```python
$ git remote add origin '깃 레파지트리 주소'
$ git remote -v # 현재 등록된 remote 정보를 확인 가능.
```

### 2. push

* 원격 저장소로 업로드

  ```python
  $ git push origin master
  ```

## 우리의 루틴

* 집에서 한것이 최신버전이고 싸피에서 git 작업을 한 번도 하지 않은 경우

  ```python
  git clone '원격 저장소 주소(레파지토리 주소)'
  ```

  * 원격 저장소를 기준으로 최신 버전의 파일이 다운로드 받아짐
  * .git 폴더도 자동 생성되어 짐. (git DB가 들어 있기 때문.)

* 싸피에서 한 것이 최신 버전이고 집에서 작업을 하는경우

  ```python
  pull-> add-> commit-> push
  ```

  ```python
  git pull origin master
  ```

  

* 집에서 한것이 최신버전이고 집에서하는경우

  ```python
  add-> commit -> push
  ```

  



