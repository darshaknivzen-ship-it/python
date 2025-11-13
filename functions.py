# def dreet():
#     print(" hi there")
#     print("wlcome back!")


# dreet()
# def dreet(first_name, last_name):
#     print(f" hi {first_name}  {last_name}")
#     print("wlcome back!")


# dreet("darshak", "vaddoriya")

# def name(first_name):
#     print(f"hi {first_name}")
#     return first_name


# print(name("darshak"))

# def increment(number,another, by=2):
#     return number + by


# print(increment(2,2))

# def multiply(x, y):
#     return x * y


# multiply(2, 4)
# print(multiply(2, 4, 5, 6))

# def multiply(*number):
#     print(number)


# multiply(1, 2, 3, 4, 5)


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(1, 2, 3, 4, 5))


# def save_user(**user):
#     print(user)


# save_user(id=1, name="darshak", age=22)

# message = "a"


# def greet(name):
#     global message
#     message = "b"


# greet("Mosh")
# print(message)


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("start")
# print(multiply(1, 2, 3, 4))


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("fizz_buzz")
    elif input % 3 == 0:
        print("fizz")
    elif input % 5 == 0:
        print('buzz')
    else:
        print(input)


fizz_buzz(15)
