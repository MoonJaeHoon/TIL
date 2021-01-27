# Scope개념은 크게 4종류로 나눠 볼 수 있다.

-   Local Scope
-   Enclosed Scope
-   Global Scope
-   Built-in Scope

[##_Image|kage@FuQJr/btqT8Htiwwl/VudvKAQFOKUNGUYRRvx3s1/img.png|alignCenter|data-origin-width="0" data-origin-height="0" data-ke-mobilestyle="widthContent"|출처 :&nbsp;https://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html||_##]

> 간단하게 다음 문제들을 풀어보면서 자신이 파이썬의 LEGB 룰에 대하여 잘 알고 있는지 확인해보자.

1) local scope

```
def local_scope():
    local_var = 1
    print(local_var)

local_scope()
print(local_var)

```

정답)

1

NameError





2) Enclosed Scope

```
def enclosing_scope():
    enclosing_var = 6
    def inner_func():
        inner_var = 3
        print(enclosing_var * inner_var)
    inner_func()
    print(inner_var)

enclosing_scope()
```

정답)

18

NameError





3-1) Global Scope

```
global_var = 5

def outer_func():
    outer_var = global_var + 2
    print(outer_var) 
    def inner_func():
        inner_var = global_var * 9
        print(inner_var)
    inner_func()

outer_func()
print(global_var)

```

정답)

7

45

5





3-2)

```
global_var = 5

def outer_func():
    outer_var = global_var + 2
    print(outer_var)
    def inner_func():
        global_var = global_var * 9
        print(global_var)
    inner_func()

outer_func()
print(global_var)

```

정답)

7

UnboundLocalError





4) Built-in Scope

파이썬 파일을 작성하는 가장 상위 공간이다.







### 연습문제

> 무슨 값이 출력될까요? 혹은 어떤 에러가 출력될까요?

1-1.

```
def change1():
    a=2

def change2():
    global a
    a=2

a=1
print(a)
change1()
print(a)
change2()
print(a)
```

정답)

1

1

2



1-2.

```
def change1():
    a=3
    
def change2():
    global a
    a=2

a=1
print(a)
change2()
print(a)
change1()
print(a)
```

정답)

1

2

2





2.

```
def change():
    g_variable=1
    lst[1]=4

g_variable = 0
lst = [1,2,3]

print(lst,g_variable)
change()
print(lst,g_variable)
```

정답)

\[1, 2, 3\] 0

\[1, 4, 3\] 0



###

list : mutable 객체 (수정가능)

int : immutable 객체 (수정불가)

이기 때문이다



3.

```
def change():
    a=2
    global a
a=1
change()
print(a)
```

정답)

SyntaxError



\# 기본적인 문법이 잘못되었다. global은 그 변수명이 저장되기 전에 사전에 선언되어야 한다.



4.

```
def change():
    val = 20
    lst[1]=0
    print(val, lst)

val = 10
lst = [1,2,3]
change()
print(val, lst)
```

정답)

20 \[1, 0, 3\]

10 \[1, 0, 3\]



###

이것 역시 immutable 과 mutable 객체이기 때문이다.



5.

```
def change():
    val = 20
    lst=[0,1]
    print(val, lst)

val = 10
lst = [1,2,3]
change() 
print(val, lst)
```

정답)

20 \[0,1\]

10 \[1, 2, 3\]



###

list가 mutable한 객체라는 것은

인덱스를 취하고 수정하였을 때 수정이 가능하다는 뜻이지,

함수내에서 전역변수 lst를 아예 새로 저장하는 것이 가능하단 뜻이 아니기 때문이다.

위의 코드는 전역변수 lst에 인덱스로 접근하는 것이 아니라

새로운 지역변수 lst 저장하는 코드이기 때문에 수정이 되지 않은 것이다.



6.

```
def change():
    val += 20
    lst[1]=0
    print(val, lst)

val = 10
lst = [1,2,3]
change()
print(val, lst)
```

정답)

UnboundLocalError



\# 2번째 줄에서 파이썬은 이렇게 인식한다. => "아하, 좌변의 "저장하려고 하는 변수명 val"을 보니 함수 내에서 val 이라는 지역변수를 새로 만들거구나~~

\# 그런데 val=val+20 이라는 식을 실행하려고 보니 우변의 val은 지역변수니까 아직 없는데? 하며 Error를 출력하는 것이다.



7.

```
global_var = 5

def outer_func():
    outer_var = global_var + 2
    global_var = outer_var + 2 
    print(outer_var) #7
    print(global_var) # 9
    def inner_func():
        inner_var = global_var * 9
        print(inner_var) # 81
    inner_func()

outer_func()
print(global_var) # 5

```

정답)

UnboundLocalError



\# 위 6번과 유사한 문제였다. 파이썬은 우선적으로 저장되는 변수명들을 싹 다 살펴본다.

\# 그렇기 때문에 3번째 라인 좌변으로부터 global\_var이 지역변수로서 새로 선언되겠네?

\# 이렇게 파이썬이 기억하고 있는 상태에서 2번째 라인 우변에 global\_var이 먼저 나타났으니, 아직 지정안한 변수인데? 하며 Error를 출력하는 것이다.