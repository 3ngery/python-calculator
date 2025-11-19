#
from calculator import add , subtarct , multiply , divide

def main():
    print("==== angery's simple calculator ====")
    print(" choose missod :")
    print("1- ADD")
    print("2- SUBTARCT")
    print("3- MULTIPLY")
    print("4- DIVIDE")

    choice = input("enter choice ( 1 | 2 | 3 | 4 )")

    if choice not in ["1","2","3","4"]:
        print("Bad choice")
        return
    num1 = float(input("first input: ")).strip()
    num2 = float(input("second input: ")).strip()

    if choice == "1" :
        result = add(num1,num2)
    elif choice == "2":
        result = subtarct(num1,num2)
    elif choice == "3":
        result = multiply(num1,num2)
    elif choice == "4":
        result = divide(num1,num2)

    print(f"Results : {result}")

if __name__ == "__main__" :
    main()

