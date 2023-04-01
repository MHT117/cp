x=input().lower() 
def name(str):
    n=set(str)
    if(len(n)%2==0):
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
name(x)