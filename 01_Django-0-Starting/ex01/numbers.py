def numbers():
    f = open("../d01/ex01/numbers.txt", "r")
    numbers = f.read()
    for num in numbers.strip().split(","):
        print(num)
    f.close()

if __name__ == '__main__':
    numbers()
