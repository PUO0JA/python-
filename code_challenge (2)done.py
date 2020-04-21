# Ask a user to enter a number
# Ask a user to enter a second number
# Calculate the total of the two numbers added together
# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
def addition(a,b):
    res=a+b
    return res

a=int(input('Enter the first number'))
b=int(input('Enter the second number'))

r=addition(a,b)
print('The result is',r)
