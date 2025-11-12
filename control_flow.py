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

from operator import truediv


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

for x in range(5):
    for y in range(3):
        print(f"({x} , {y})")
