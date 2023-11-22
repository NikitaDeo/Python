n=int(input())
if(n%2!=0):
    print("weird")
else:
    if(n>2 and n<6):
        print("Not weird")
    elif(n>6 and n<21):
        print("weird")
    else:
        print("Not weird")