import requests
from pprint import pprint


def vote_average_movies():
    # 여기에 코드를 작성합니다.  
    # 1. URL 및 요청변수 설정 및 요청 보낸 결과 저장
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=423115a7b5585375b2590b4770f1a0b9&region=KR&language=ko'
    response = requests.get(URL)
    data = response.json()
    movie = data.get('results')

    # 2. popular 영화목록 중 평점 8점 이상 영화목록 출력
    lst = []
    for i in range(len(movie)): 
        output = movie[i] # movie 리스트의 각 딕셔너리 추출
        vote_average = output.get('vote_average') # 각 딕셔너리별 평점 추출
        
        if vote_average >= 8: # 평점 8점 이상
            popular_movie = movie[i] 
            title = popular_movie.get('original_title') # 영화 제목 추출
            lst.append(title) # 리스트 만들기
            
    return lst

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
