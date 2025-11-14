try:
    file = open("main.py")
    age = int(input("Age :"))
    xfactor = 10 / age

except (ValueError, ZeroDivisionError):
    print("not valid age")
else:
    print("no any exceptions")
finally:
    file.close()
