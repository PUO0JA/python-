def find_length(l2):
    l2_len=[len(i) for i in l2]
    return(l2_len)    

def sort_list(l1,l2):
    pairs=zip(l1,l2)
    sort=[i for _, i in sorted(pairs)]
    return sort

N=int(input('Enter the number of elements you want in your list of strings:'))
l1=[]
for i in range(0,N):
    num=int(input('Enter the non-repeating numbers defining the positions of the strings'))
    l1.append(num)
print('The list l1 is: ')
print(l1)

l2=[]
for i in range(0,N):
    alp=str(input('Enter the non-repeating string elements'))
    l2.append(alp)
print('The final list is: ')
print(l2)
print('The final string is: ')
final=[]
for i in range(0,N):
    final=[l1, l2]
print(final)    

a=find_length(l2)
print('The length of strings in list l2 are: ')
print(a)

print('The sorted list is: ')   
b=sort_list(l1,l2)
print(b)

    
for i in range(0,N):
    if(a[i]==l1[i]):
        print(l2[i].upper())
    elif((a[i]<l1[i])or(a[i]>l1[i])):
         print(l2[i].lower())
    elif(b[i]==final[i]):
         print(l2[i])
    else:
        print('Wrong input')
       
        
