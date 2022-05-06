# 관통 pjt 06

***

## DB를 활용한 웹 페이지 구현

### 아마  조금 다듬어진 코드 ? 🤔

- 결과물은 pjt05와 유사하지만, 조금은 다른 코드

  new와 create / edit와 update 합치기

  Django ModelForm 활용하기 (데이터 유효성 검증, 에러메시지 출력 등)

## 1. 학습한 내용

- CRUD

- ModelForm

  데이터 유효성 검증 is_valid()

- Widget

- Django View decorators

  method 제한두기

## 2. 어려웠던 부분
- Django ModelForm

  AttributeError: module 'django.forms' has no attribute 'Modelform' 에러
  과제할 때도 떴었는데, 주의하자!!

  ```
  class 앱form(forms.ModelForm)
  ```

  ```django
  from django import forms
  from django.forms.widgets import NumberInput
  from .models import Movie
  
  class MovieForm(forms.ModelForm):
  	pass

- d-flex

  여전히 어려운 정렬하기

  정렬은 따로 div 만들어서 해주자
  ex. card는 class 안에 d-flex 넣지말고 따로 하기!

## 3. 소감

돌아온 Django😎

오랜만에 하는 거라 낯설어서 이게 뭐더라 처음에 당황했었지만, 차근차근 처음부터 다시하니 재밌었다.
역시 하고 나면 뿌듯한 장고🙌

p.s. 알고리즘 하다가 웹 하니까 살 거 같네요....하하하하하 
알고리즘 다시 공부하러 가야죠...ㅠㅠ
