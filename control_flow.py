# ========== Comparison opraters============
# print(10 >= 3)
# print(10 < 20)
# print(10 <= 20)
# print(10 == 10)
# print(10 == "10")
# print(10 != "10")

# print("bag" == "BAG")

# ========== Conditional Statements============

# temperature = 25

# if temperature > 28:
#     print("Drink water")
# elif temperature > 25:
#     print("Not Drink Water")
# else:
#     print("not valid")

# ========== ternary oprater============


age = 19

if age >= 18:
    # print("Eligible")
    message = "Eligible"
else:
    # print("Uneligible")
    message = "Uneligible"

# print(message)

# ============ logical oprater=======

# and
# or
# not

high_income = True
good_credit = True
student = True


# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")

# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")


# if not student:
#     print("Eligible")
# else:
#     print("Not eligible")


# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")


# ========= Chaining comparison opraters =========

age = 18

# if age >= 18 and age < 65:

# if 18 <= age < 65:
#     print("Eligible")
# else:
#     print("Uneligible")


# =========== for loop ============

# for number in range(1, 4, 2):
#     print("Attemp", number, (number) * ".")


# =========== for else...  ============

# successfull = False
# for number in range(3):
#     print("Attempt")
#     if successfull:
#         print("Successfull")
#         break
# else:
#     print("attempt 3 times and filed")


# ==================== nested loop ===============

# for x in range(3):
#     for y in range(5):
#         print(f"({x} , {y})")


# print(type(5))
# print(type(range(5)))


# ==========iterables==========

for x in "darshak":
    print(x)

shoping_cart = [1, 2, 3, 4, 5, 6]

for item in shoping_cart:
    print(item)

# ========== while loop ==========


# number = 100
# while number > 0:
#     print(number)fef
#     number //= 2

command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# print(ord("B"))
# print(ord("b"))

# while True:
#     command = input(">")
#     print("Echo", command)
#     if command.lower() == "quit":
#         break


for x in range(2, 10, 2):
    print(f" even numbers: {x}")

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have     {count}")
