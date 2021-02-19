def chkTF(num):
    if num%5==0:
        return True
    else:
        return False
   
def main():
    print("enter number")
    value=int(input())
    bret=chkTF(value)
    
    if bret==True:
        print("true")
    else:
        print("false")
        
if __name__ == "__main__":
    main()