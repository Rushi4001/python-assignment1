
def fun(num):
    icnt=0
    while icnt<num:
        print("*")
        icnt=icnt+1
def main():
    print("enter the number")
    value=int(input())
    fun(value)
    


if __name__ == "__main__":
    main()