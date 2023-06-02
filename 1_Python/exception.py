x, y = input("Please input your Number: ").split()

try:
    re = int(x) / int(y)
except Exception as e:
    print(f"Exception Occured: {e}")
    re = None

print("Division is: ", re)