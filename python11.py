def calculator(number_1, number_2, operation):
    if(operation=='addition'):
        result=number_1+number_2
        return result
    elif(operation=='subtract'):
        result=number_1-number_2
        return result
    elif(operation=='multiply'):
        result=number_1*number_2
        return result
    elif(operation=='divide'):
        result=number_1/number_2
        return result
    else:
        print('wrong input')
        




number_1=int(input('Enter the first number'))
number_2=int(input('Enter the second number'))
operation=str(input('Enter the operation'))
a=calculator(number_1, number_2, operation)
print(a)
s