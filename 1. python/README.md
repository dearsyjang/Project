# 7기 관통 프로젝트

## 주의사항

* 프로젝트 진행시 해당 폴더를 바탕화면에 복사-붙여넣기를 하여 시작합니다.

* README.md에 프로젝트를 하면서 배운 점, 트러블 슈팅 등을 기록합니다.

## 목록

| 날짜      | 프로젝트                      | 링크            |
| --------- | ----------------------------- | --------------- |
| 1/21 (금) | Python을 활용한 데이터 수집 I | [폴더](./pjt01) |

## 가이드

### 저장소 복제 혹은 업데이트

* 최초 바탕화면에서 Git bash 열어서 `clone`

```bash
$ git clone https://lab.ssafy.com/s07/python/pjt
```

* 이후 바탕화면 폴더에서 Git bash 열어서 `pull` 

```bash
$ git pull origin master
```

### 프로젝트 진행

* `pjtxx` 폴더를 바탕화면에 복사-붙여넣기를 해주세요.

* 바탕화면에 있는 `pjtxx` 폴더에서 git 저장소로 초기화 해주세요.

```bash
$ git init
```

* `commit`을 해주세요. 

```bash
$ git add .
$ git commit -m 'Init'
```

* GitLab에서 `pjtxx` 라는 프로젝트를 생성하고 원격저장소 설정을 해주세요. 

    * 프로젝트 생성시 담당 교수님 Maintainer로 추가

```bash
$ git remote add origin <주소>
```

* 원격저장소에 `push`를 해보세요. (확인)

```bash
$ git push origin master
```

* 프로젝트를 하고 `commit`, `push`를 합니다.
