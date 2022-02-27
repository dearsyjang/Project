import requests
from pprint import pprint


def ranking(): 
    # 여기에 코드를 작성합니다.
    # 1. URL 및 요청변수 설정 및 요청 보낸 결과 저장
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=423115a7b5585375b2590b4770f1a0b9&region=KR&language=ko'
    response = requests.get(URL)
    data = response.json()
    movie = data.get('results')

    # 2. 평점 데이터 추출 및 평점순 정렬
    output = sorted(movie, key=lambda x: x['vote_average']) # 오름차순 정렬
    output.reverse() # 내림차순 정렬

    # 3. 리스트로 묶기
    lst = []
    for i in range(0, 5):
        lst.append(output[i])

    return lst


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
