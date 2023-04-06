#check user inputted string is symmetrical or not.
def strsymmetric(s):
    a=len(s)//2
    b1=s[0:a]
    b2=s[a:]
    if b1==b2:
        print(f"\"{s}\"  Is Symmetircal  String")
    else:
        print(f"\"{s}\"  Is Not Symmetircal String")
def inputstr():
       s=input("Enter String:")        
       strsymmetric(s)
inputstr()
