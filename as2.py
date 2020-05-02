import re
def camel(s):
    list=[i for i in re.split('([A-Z][^A-Z]*)',s) if i]
    print('The list of words in the string is: ', str(list))
    





s=input('Enter the string')
print('String is', s)
camel(s)
