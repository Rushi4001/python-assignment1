
def chknum(num):
    if num==0:
        return True
    elif num<0:
        return False
    else:
        return num
        
def main():
    print("enter the number")
    value=int(input())
    bret=chknum(value)
    
    if bret==True:
        print("zero".format(value))
    elif bret==False:
        print("negative".format(value))
    else:
        print("positive".format(value))

if __name__=="__main__":
    main()