a=int(input())
b=int(input())
try:
    print("file open")
    print(a/b)
    k=int(input())
    print(k)
except ZeroDivisionError as e:
    print("you can not divide a number by 0",e)
except ValueError as e:
    print("Invalid input",e)
except Exception as e:
    print("something went wrong",e)
finally:
    print("close file")