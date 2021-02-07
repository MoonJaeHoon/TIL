> dict객체로부터 가장 큰 value를 갖는 key를 어떻게 빼올수있을까?

```py
my_key = ['a','b','c','d']
my_val = [100,90,40,100]
input_dict = {k:v for k,v in zip(my_key,my_val)}

max_key = max(input_dict,key=lambda k: input_dict[k])
print(max_key)
```
```
a
```

- max 함수에 내장되어있는 key 옵션을 활용할 수 있다.

> 추가 (lambda 활용없이 다음과 같이 쓸 수도 있다.)
```py
my_key = ['a','b','c','d']
my_val = [100,90,40,100]
input_dict = {k:v for k,v in zip(my_key,my_val)}

max_key = max(input_dict,key=input_dict.get)
print(max_key)
```
```
a
```