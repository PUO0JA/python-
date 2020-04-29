st=[]
n=int(input('Enter the no. of characters in the string'))
print('Enter the string:')
for i in range(0,n):
    d=str(input('Enter the Element:'))
    st.append(d)

print("The list of the inputted string' character elements are: ", st)
lst=[]
def ind(st):
    for i in st:
        a=(st.index(i))
        if(a%2==0):
            val=ord(i)
            k=chr(val+1)
            lst.append(k)
        else:
            val=ord(i)
            k=chr(val-1)
            lst.append(k)
    print('The string entered by the user is :', st)    
    print('The updated list is :',lst)
        
    return 0
ind(st)


