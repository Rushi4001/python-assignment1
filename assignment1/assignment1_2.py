def chknum(num):
    if num%2==0:
        return True
    else:
        return False
        
def main():
    print("enter one number")
    value=int(input())
    
    bret=chknum(value)    
    if bret== True:
        print("{} is even number ".format(value))
    else:
        print("{} is odd".format(value))

if __name__ == "__main__":
    main()