# 간단정리

1. 함수 사용하는 이유

   - 코드의 짜임새가 좋아짐, 가독성이 높아짐
   - 코드를 묶어주기 때문에 재사용을 할 수 있다.

   

2. 함수의 기본 특징

   - **return** **vs** **print**

     - return : **최종 결과값을 반환**하는 것
     - print : **단순 값을 화면에 출력**하는 것

     

3.  함수를 호출하는 방법

   `함수명(입력되어지는 값, ...)`

   - 인자 vs 매개변수

     - 인자 : 실제로 입력되는 값

     - 매개변수 : 입력되는 값을 받을 변수

     - 매개변수의 갯수로 입력되는 값의 갯수를 정한다.

       - 가변인 경우 예외.

       

4. 일급 객체(first class object)

```python
1. 함수를 변수에 담을 수 있어야 한다.
2. 함수를 인자에 전달할 수 있어야 한다.
3. 함수를 반환값으로 전달할 수 있어야 한다.

위 3개의 조건을 모두 만족한다면 일급객체라고 할 수 있다.

def first():
	return 3
	
def second():
	return first
	
def third(func):
	return func()

sample = second()
print(third(sample))
```



5. 위치 인자

```python
def func1(input1, input2):
    ....
    
func1('hi','ed')
```



6. 키워드 인자

```python
def func1(input1, input2, input3):
    ....
    
func2(input2='hi', input1 = 'hello', input3 = 'ed')
func2('hi', input2='ed', input3='bye') # 가능
func2(input1 = 'hi', 'ed', 'bye') # 불가능

## 키워드인자와 위치 인자를 같이 사용할 때에는 무조건 위치 인자를 앞에서 사용하고 뒤에서 키워드 인자를 사용해야 한다.


```



7. 기본값 인자

```python
def func3(input1, input2='ed'):
    ....
```



8. 가변 인자

```python
몇 개의 인자가 입력되는 지 모를 때 사용
매개변수 명 앞에 * 를 찍어서 나타낸다.

# 함수 정의할 때 매개변수 위치에서 사용

def func4(*args):
    print(type(args)) # <class 'tuple'>
    튜플 특징 : 수정은 불가, 리스트처럼 사용가능하다.
        
    print(*args) : 매개변수가 아닌 자리에서 * 를 같이 찍으면 이 동작은 unpacking 동작이 된다.
    

* unpacking이 사용되는 시점
args = ['hello', 'world', 'welcome', 'programming', 'world']

def func5(input1, input2, input3, input4, input5):
    print(f'{input1} {input2} {input3} {input4} {input5}')
          
        
## 다음과 같은 return에 unpacking을 사용해선 안됨.
## 원칙적으로 함수는 return 값으로 packing값을 반환하기 때문에 Error가 발생하는 것!!

def func5(*args):
	return *args 

# 만약 args = a,b 였다면 return a,b로 반환해야 할텐데
# return *args 의 의미는 : unpacking 하여 return a b 가 되므로 에러발생

```



9. 가변 키워드

   `**kwargs` dict(name='ed', location='구미')



10. 이름 공간

    - Local => Enclosed => Global => Builtin (LEGB)

    

11. 재귀함수

    - 내가 나를 호출하는 함수
    - 코드 가독성이 좋음.
    - 설계는 어렵다. 메모리를 많이 차지한다. 그래서 느리다. 사용할 땐 신중하게

    

12. 에러 종류

    - SyntaxError : 문법적 오류
    - ZeroDivisionError : 숫자를 0으로 나누려고 할 때
    - NameError : 'abc' is not defined
    - TypeError :
      - 자료형의 타입이 잘못되었을 때 `1 + '3'`
      - 매개변수의 갯수와 입력받는 인자의 갯수가 다를 때
    - ValueError : 자료형에 대한 타입은 올바른데 잘못된 값이 입력되는 경우
      - int('3.5')
    - IndexError : list에서 인덱스를 잘못 입력한 경우
    - KeyError : dictionary에서 없는 key 로 값 조회를 한 경우
    - ModuleNotFoundError : import를 잘못한 경우
    - importError : 모듈은 가져왔는데 그 속에서 클래스나 함수를 찾을 수 없을 때
    - KeyboardInterrupt : `ctrl + c` 등으로 종료한 경우

    

13. try / except / else / finally

```python
try: # try문 안에 있는 코드에서 에러가 발생했을 때 -> except
    코드1
    코드2
    코드3
except: # try문 안에서 에러가 발생한 경우, 코드 실행
    코드4 (에러 발생시 실행할 코드)
else: # try문 안에서 에러발생 없이 무사히 코드가 실행이 완료된 경우, 코드 실행
    코드5
finally: # 에러가 발생하던 말던, try 코드가 실행완료 되면 무조건 실행.
    코드6
```







