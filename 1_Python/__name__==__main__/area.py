def calculate_area(base, height):
    print("__name__: ", __name__)
    re = base * height
    return 1/2 * re

# area = calculate_area(10, 20)
# print(f"Area: {area}")

if __name__ == "__main__":
    print("I'm in area.py")
    area = calculate_area(10, 20)
    print(f"Area: {area}")
