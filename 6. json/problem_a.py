import requests

def popular_count():
    # 여기에 코드를 작성합니다.  
    # 1. URL 및 요청변수 설정
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=423115a7b5585375b2590b4770f1a0b9&region=KR&language=ko'
    response = requests.get(URL)
    
    # 결과값 URL로 보기: print(response.status_code, response.url)
    
    # 2. 요청 보낸 결과 저장
    data = response.json()
    movie = data.get('results')

    # 3.popular 영화목록 개수
    return len(movie)



if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
