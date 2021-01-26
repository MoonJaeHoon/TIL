# 파이썬 JSON 파일 읽고 다루기



`json.dump()` : `dictionary` 형태의 자료를 `json` 자료구조로 변환 (인코딩)

`json.load()` : `json` 형태의 자료를 `dictionary` 타입으로 변환시켜준다. (디코딩)



ex) 

```python
import json

movie_json = open('data/movie.json', encoding='UTF8')
movie_dict = json.load(movie_json)		# 불러온 json을 파이썬의 dict 구조로 바꾸는 함수
print(type(movie_json))
print(type(movie_dict))
```

```
<class '_io.TextIOWrapper'>
<class 'dict'>
```



```python
with open("new_movie.json", "w") as json_file:
    json.dump(movie_dict, json_file)

```

- `json.dump()` 함수는 python의 `dict` 타입에 적용하면 `Json object`로 변환해줄 수 있다.



![image-20210126193322830](0122_json_Python.assets/image-20210126193322830.png)







