# 파이썬 리스트

파이썬 리스트(list)는 여러 값을 순서대로 저장하는 자료형입니다. 값의 순서가 있고, 수정이 가능하다는 점이 특징입니다.

## 1. 리스트 만들기

리스트는 대괄호 `[]`로 만듭니다.

```python
numbers = 
names = ["철수", "영희", "민수"]
empty = []
```

## 2. 리스트의 특징

- 순서가 있습니다.
- 같은 값이 여러 번 들어갈 수 있습니다.
- 수정할 수 있습니다.
- 서로 다른 자료형을 함께 넣을 수 있습니다.

```python
mixed = [1, "hello", 3.14, True]
```

## 3. 인덱스와 슬라이싱

리스트의 각 값은 인덱스로 접근합니다. 파이썬은 0부터 시작합니다.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)   # apple
print(fruits)   # cherry
print(fruits[-1])  # cherry
```

슬라이싱으로 일부 구간을 가져올 수 있습니다.

```python
print(fruits[0:2])  # ['apple', 'banana']
```

## 4. 수정하기

리스트의 값을 바꿀 수 있습니다.

```python
fruits = ["apple", "banana", "cherry"]
fruits = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']
```

## 5. 자주 쓰는 메서드

- `append()`: 마지막에 추가합니다.
- `insert()`: 원하는 위치에 추가합니다.
- `remove()`: 값을 삭제합니다.
- `pop()`: 인덱스로 삭제하고 값을 반환합니다.
- `sort()`: 정렬합니다.
- `reverse()`: 순서를 뒤집습니다.

```python
nums = 
nums.append(4)
nums.insert(1, 10)
nums.remove(3)
value = nums.pop()
nums.sort()
nums.reverse()
```

## 6. 자주 쓰는 함수

- `len()`: 길이를 구합니다.
- `sum()`: 숫자 리스트의 합을 구합니다.
- `max()`: 가장 큰 값을 구합니다.
- `min()`: 가장 작은 값을 구합니다.
- `sorted()`: 정렬된 새 리스트를 만듭니다.

```python
scores = 
print(len(scores))
print(sum(scores))
print(max(scores))
print(min(scores))
print(sorted(scores))
```

## 7. 반복문과 함께 사용하기

리스트는 반복문과 함께 자주 사용합니다.

```python
for item in ["A", "B", "C"]:
    print(item)
```

인덱스가 필요하면 `enumerate()`를 사용할 수 있습니다.

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

## 8. 예제

```python
shopping = ["milk", "bread", "eggs"]
shopping.append("coffee")
shopping.remove("bread")
print(shopping)
```

## 9. 정리

파이썬 리스트는 여러 값을 순서 있게 저장하고, 필요에 따라 수정할 수 있는 매우 유용한 자료형입니다. 데이터 묶음을 다룰 때 가장 많이 사용되는 기본 구조 중 하나입니다.