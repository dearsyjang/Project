import requests
from pprint import pprint


def recommendation(title):
    # 여기에 코드를 작성합니다.
    # 1. URL 및 요청변수 설정 및 요청 보낸 결과 저장
    Search_URL = 'https://api.themoviedb.org/3/search/movie?api_key=423115a7b5585375b2590b4770f1a0b9&language=ko&region=KR&query='
    query = title
    response = requests.get(Search_URL+query)
    data = response.json()
    movie = data.get('results')

    # 2. movie_id만 추출
    for i in range(len(movie)): 
        output = movie[i]
        movie_id = output.get('id')

    # 3. movie_id가 존재할 경우, id로 Recommendation_URL로 다시 요청변수 설정 및 요청 보낸 결과 저장
        if type(movie_id) == int:
            Recommendation_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=423115a7b5585375b2590b4770f1a0b9&language=ko'
            response2 = requests.get(Recommendation_URL)
            data2 = response2.json()
            movie2 = data2.get('results')
    
    # 4. 요청 결과 제목 추출 및 리스트로 묶기
        lst = []
        for i in range(len(movie2)):
            output2 = movie2[i]
            lst.append(output2.get('title'))

        return lst
    
    # 5. 검색 결과 없을 때, None으로 출력
    else:
        return None

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
