
def add(no1,no2):
    ret=no1+no2
    return ret
    
def main():
    value1=int(input("enter first number "))
   

    value2=int(input("enter second number"))
    
    ans=add(value1,value2)
    print("addition of two number is",ans)

if __name__ == "__main__":
    main()