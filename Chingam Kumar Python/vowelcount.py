a=input("Enter the string ")
a=a.lower()
b=list(a)
c=0
for i in b:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        c=c+1
print("Number of vowels in the sentence is ",c)