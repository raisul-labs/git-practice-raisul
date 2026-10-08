from datetime import date
from utils import add, subtract, multiply, divide


def main():
    print("Name: Md Raisul Islam")
    print("Today's Date:", date.today())

    print("\nCalculator")
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))

    try:
        print("Division:", divide(10, 2))
        print("Division:", divide(10, 0))
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()