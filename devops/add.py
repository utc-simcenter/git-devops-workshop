def add(x, y):
    return x+y

def test_answer():
    assert add(2,3) == 5

if __name__ == "__main__":
    x = input("Enter the first number you'd like to add: ")
    y = input("Enter the second number you'd like to add: ")
    print("The result is " + str(add(int(x), int(y))) )
