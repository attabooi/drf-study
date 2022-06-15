# DRF-Study

# Day 1


1. args, kwargs 예제 코드 만들기

```python
def test(num1, num2, *args, **kwargs):
    print(f'{num1}')
    print(f'{num2}')
    print(args)
    print(kwargs)
    return 

test(1,2,3,4,5,6,7, num3 = 1000, num4 = 2000)
```


 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기


mutable은 변경이 가능하고, immutable은 변경이 불가능합니다.
상태를 변경할 수 있고 없고의 차이가 있습니다.

mutable 자료형 : list, dict

immutable 자료형 : int, str, tuple



3. DB Field에서 사용되는 Key 종류와 특징 서술하기

- FK : Foreign Key의 약자, 다른 테이블을 참조할떄 사용한다.
- UK : Unique Key의 약자, 중복 값을 허용하지 않는다.
- PK : Primary Key의 약자, 테이블에서 반드시 존재해야 한다.
    - PK는 두개 이상 존재 할 수 없고(한 테이블에 두개의 PK 불가), UK와 마찬가지로 중복 값을 허용하지 않는다.
    - Foreign Key를 사용하면 참조 할 테이블의 PK를 바라본다.
    - 따로 지정하지 않으면 id라는 PK가 설정되는데, 따로 PK를 지정하면 id가 사라지고 내가 지정한 값이 테이블의 Primary Key로 남는다.

4. django에서 queryset과 object는 어떻게 다른지 서술하기

Queryset은 전달받은 모델의 객체 목록(list)

object는 모델의 객체

