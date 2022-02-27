import requests
from pprint import pprint


def credits(title):
    # 여기에 코드를 작성합니다. 
    # 1. URL 및 요청변수 설정 및 요청 보낸 결과 저장
    Search_URL = 'https://api.themoviedb.org/3/search/movie?api_key=423115a7b5585375b2590b4770f1a0b9&language=ko&region=KR&query='
    query = title
    response = requests.get(Search_URL+query)
    data = response.json()
    movie = data.get('results')

    # 2. movie_id만 가져오기
    for i in range(len(movie)): 
        output = movie[i]
        movie_id = output.get('id')

    # 3. 가져온 movie_id로 Credits_URL 요청변수 설정 및 요청 보낸 결과 저장
        Credits_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=423115a7b5585375b2590b4770f1a0b9&language=ko'
        response2 = requests.get(Credits_URL)
        data2 = response2.json()

    # 4. 결과 중 cast와 crew 데이터만 추출
        cast_data = data2.get('cast')
        crew_data = data2.get('crew')
    
    # 5. 각각 세부 데이터 조건 

    # 리스트 묶기 위해 빈 리스트 우선 만들어주기
        cast_lst = []
        director_lst = []
        crew_lst = []

    # cast 데이터
        for i in range(len(cast_data)): 
            cast_data_dic = cast_data[i]
            cast_data_id = cast_data_dic.get('cast_id')
            cast_data_department = cast_data_dic.get('known_for_department')
        
            # cast_id가 10미만인 배우들의 이름 추출 및 리스트 묶기
            if cast_data_id < 10:
                cast_name = cast_data_dic.get('name')
                cast_lst.append(cast_name)
            
            # 감독 이름 추출 및 리스트 묶기
            elif cast_data_department == 'Directing':
                director = cast_data_dic.get('name')
                director_lst.append(director)

    # crew 데이터
        # 디렉팅 부서 crew 이름 추출 및 리스트 묶기
        for i in range(len(crew_data)):
            crew_data_dic = crew_data[i]
            crew_data_department = crew_data_dic.get('known_for_department')
            
            if crew_data_department == 'Directing':
                crew_name = crew_data_dic.get('name')
                crew_lst.append(crew_name)
        
        #crew 리스트에 감독 리스트 합치기
        crew = crew_lst + director_lst
        
        # 최종 출력 양식 설정하기
        final_dict = {'cast': cast_lst, 'crew': crew}

        return final_dict

    else:
        return None

    

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
