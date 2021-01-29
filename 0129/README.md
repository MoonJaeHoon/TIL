# JSON 영화정보 크롤링
## A.
```py
import requests
from tmdb import URLMaker

# api 요청 예시
# https://api.themoviedb.org/3/movie/550?api_key=02d5fda86a011a7b2e4d1739e5a38041
# api_key=02d5fda86a011a7b2e4d1739e5a38041
def popular_count():
    url_maker = URLMaker(key = '02d5fda86a011a7b2e4d1739e5a38041')
    url = url_maker.get_url()
    res = requests.get(url).json()
    
    return len(res['results'])

if __name__ == '__main__':
    print(popular_count())
```
- 1페이지만 영화정보를 가져오고 `len()`함수를 적용하면 영화개수를 구할 수 있는 문제여서 매우 평이한 난이도였다.

## B.
```py
import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    url_maker = URLMaker(key = '02d5fda86a011a7b2e4d1739e5a38041')
    url = url_maker.get_url()
    res = requests.get(url).json()
    movie_result = res['results']
    average_8 = [d for d in movie_result if d['vote_average']>=8]
    return average_8

if __name__ == '__main__':
    pprint(vote_average_movies())    

```
- B번은 평점이 8 이상인 영화들만 추출하여 리스트를 반환하는 문제였기 때문에 if 조건문을 활용한 `list comprehension`으로 간단하게 구현이 가능하였다.

## C.
```python
import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    url_maker = URLMaker(key = '02d5fda86a011a7b2e4d1739e5a38041')
    url = url_maker.get_url()
    res = requests.get(url).json()
    movie_result = res['results']
    
    sorted_ratings = sorted(movie_result, key = lambda x: x['vote_average'],reverse=True)[:5]
    return sorted_ratings

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())
```
- C 역시도 리스트를 반환하는 문제였고, 문제의 목적은 순위를 매겨서 상위 5개의 영화만 반환하는 문제였습니다.
- 역시 리스트 반환값이 결과이기 때문에 `list comprehension`을 사용하였고, sorted 함수를 사용하였는데 `lambda` 함수를 활용하였습니다
- `lambda function`에 대해 추가적인 설명을 더하자면, 리스트의 원소가 dict 타입이고, 그 `dict`의 `key`인 `vote_average`가 정렬기준이 되므로, 리스트의 원소 `dict`타입 `x`의 해당 `value`값인 `x['vote_average']`를 사용하였습니디ㅏ.

## D.
```python
import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    url_maker = URLMaker(key = '02d5fda86a011a7b2e4d1739e5a38041')
    url = url_maker.get_url(category='search',feature='movie',query=title)
    res = requests.get(url)
    movie_dict = res.json()

    if len(movie_dict['results'])==0: # 올바르지 않은 영화제목으로 id가 없음
        return None
    else:   # id를 기준으로 찾아보기, 추천영화 없으면 알아서 빈 리스트이다.
        movie_id = movie_dict['results'][0]['id']
        language = 'ko'
        new_url = 'https://api.themoviedb.org/3/movie/' + f'{movie_id}' + f'/recommendations?api_key=02d5fda86a011a7b2e4d1739e5a38041&language={language}'
        new_res = requests.get(new_url)
        recommend_dict = new_res.json()
        title_list = [results['title'] for results in recommend_dict['results']]
        return title_list
        
if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None

```
- D는 url로부터 영화정보를 가져온 뒤, `id`를 찾은 다음 해당 id를 이용해 추천영화들의 제목을 찾아주는 문제였습니다
- 따라서 두번째로 구해야하는 url은 `TMDB`에서 제공하는 영화추천 URL이었고, 이것을 우선 파악하였습니다.
- `id`가 없을 때에 대하여 조건이 있었기 때문에 `if` 조건문을 활용하였습니다.
- 이후 `requests`를 이용하여 두번째 URL을 요청하고 추천 영화들의 정보로부터 영화제목인 `title`을 `key`값에 `mapping` 되는 `value`들을 찾았습니다.
- 역시 리스트가 반환 결과값이므로 `list comprehension`을 활용하였습니다

## E.
```py
import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    url_maker = URLMaker(key = '02d5fda86a011a7b2e4d1739e5a38041')
    url = url_maker.get_url(category='search',feature='movie',query=title)
    res = requests.get(url)
    movie_dict = res.json()
    if len(movie_dict['results'])==0: # 올바르지 않은 영화제목으로 id가 없음
        return None
    else:   # id를 기준으로 찾아보기, 
        movie_id = movie_dict['results'][0]['id']
        new_url = 'https://api.themoviedb.org/3/movie/' + f'{movie_id}' + f'/credits?api_key=02d5fda86a011a7b2e4d1739e5a38041&language=en-US'
        new_res = requests.get(new_url)
        credits_dict = new_res.json()
        cast_10 = [cast['original_name'] for cast in credits_dict['cast'] if cast['cast_id']<10]
        crew_directing = list(set(crew['original_name'] for crew in credits_dict['crew'] if crew['department']=='Directing'))
        return {'cast':cast_10,'crew':crew_directing}
    

if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None
```

- 사실 위의 문제들과 구조는 매우 비슷한 문제였다. 하지만 한 문제 안에서 `2가지 list`를 가져온 다음 해당 리스트들을 `dict`로 만든다는 것이 이 문제의 핵심이었다.
- **pjt01**과 마찬가지로 역시 이번에도 마지막 문제가 그나마 현업에서도 응용할 수 있을 것 같은 문제였다. (~~물론 데이터의 양도 방대하고 구조도 훨씬 더 복잡하겠지만~~)
- 우선 D처럼 ID를 통해 URL을 새로 받아왔고, 해당 URL을 요청함으로써 `cast`와 `crew`라는 `key`를 가진 `json` 형식의 데이터를 `response`받을 수 있었다.
- `cast_id`가 10보다 작은 `cast`들을 리스트로서 반환하는 것은 역시 `list comprehension`을 사용하면 편했다.
- 문제는 두번째 리스트인 감독들의 리스트였는데, `Directing`에 해당하는 이들을 필터링한 결과 감독들의 이름이 중복되는 것을 알 수 있었다.
  - 중복제거를 위한 가장 쉬운 방법이 무엇이라고 배웠는가? : 답) set()
  - `set`을 적용한 결과 `set type`의 자료구조가 형성되므로 `list`형태로 한번더 변환해주었다.
- 이제 우리가 원하는 2가지의 `list`를 모두 가져왔으니, 이들을 `value`로 가지는 `dict`를 구축하였다.