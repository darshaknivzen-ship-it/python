# from array import array
# from collections import deque

# from primitive_types import first
# letters = ["a", "b", "c", "d"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5
# # combined = zeros + letters
# # print(combined)

# numbers = list(range(20))
# # print(numbers)

# chars = list("hellow darshak")
# # print(len(chars))

# # number = list(range(20))
# # print(number[::2])
# # print(number[::-2])

# num = [1, 2, 3, 4, 4, 4, 5, 4, 4, 9]

# # first, second, *other, last = num
# # print(first)
# # print(other)
# # print(last)

# # letters = ["a", "b", "c", "d"]
# # items = (0, "a")
# # index, letter = items
# # for index, letter in enumerate(letters):
# #     print(index, letter)

# letter = ["a", "b", "c", "d"]
# # letter.append("e")
# # letter.insert(3, "-")
# # print(letter)

# # letter.pop(0)
# # letter.remove("c")
# # del letter[0:2]
# # letter.clear()
# # print(letter)

# let = ["a", "b", "c", "d"]

# # print(let.count("b"))
# # if "e" in let:
# # print(let.index("e"))


# number = [1, 57, 35, 44, 5]
# # number.sort(reverse=True)
# # print(sorted(number))
# # print(number)


# # items = [
# #     ("product1", 10),
# #     ("product2", 9),
# #     ("product3", 20)
# # ]


# # ite.sort(key=lambda item: item[1])

# # print(ite)


# # arr = []
# # for i in ite:
# #     arr.append(i[1])


# # arr = list(map(lambda items: items[1], ite))
# # print(arr)

# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 20)
# ]

# arr = list(map(lambda items: items[1], items))
# arr = [item[1] for item in items]
# # print(arr)

# filterd = list(filter(lambda items: items[1] >= 10, items))
# filterd = [item for item in items if item[1] >= 10]

# # print(filterd)


# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]

# # print(list(zip("abc", list1, list2)))


# bs = []

# bs.append(1)
# # bs.append(2)
# # bs.append(3)

# # print(bs)

# # last = bs.pop()
# # print(last)
# # print(bs)

# # bs.pop()
# # if not bs:
# #     bs[-1]


# queue = deque([])

# queue.append(1)
# queue.append(2)

# queue.popleft()
# # print(queue)

# # if not queue:
# # print("empty !!")

# point = (1, 2, 3, 4)

# # print(point[0:2])

# # x = 58
# # y = 98

# # x, y = y, x

# # print("X :", x)
# # print("Y :", y)


# # n = array("i", [1, 2, 3])


# num1 = [1, 1, 2, 3, 4, 4]
# f1 = set(num1)
# s1 = {1, 5}

# print(f1 | s1)
# print(f1 & s1)

# if 5 in s1:
#     print("yes")

# point = {"x": 1, "y": 2}

# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20

# if "a" in point:
#     print(point["a"])

# print(point.get("a", 0))

# del point["x"]
# print(point)

# for key, value in point.items():
#     print(key, value)

# value = []
# for x in range(5):
#     value.append(x * 3)

# from sys import getsizeof

# value = (x * 2 for x in range(1000000))

# print("gen :", getsizeof(value))

# value = [x * 2 for x in range(1000000)]

# print("gen :", getsizeof(value))

# value = {x * 2 for x in range(1000000)}

# print("gen :", getsizeof(value))

# num = [1, 2, 3]
# print(*num)


# values = list(range(5))

# values = [*range(5), *"hello"]
# print(values)


# f = {"x": 1}
# s = {"x": 10, "y": 2}

# c = {**f, **s, "z": 1}
# print(c)


# ============ exer ========

sentence = "This is a common   interview question"

count = {}

for char in sentence:
    if char == " ":      # ignore spaces
        continue
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)


sort = sorted(count.items(), key=lambda val: val[1], reverse=True)
print(f"max ch in used : {sort[0]}")
