def calculator(first_number, second_number, operation):
    if(operation=='add'):
        add_result=first_number+second_number
        return(add_result)
    elif(operation=='subtract'):
        sub_result=first_number-second_number
        return(sub_result)
    else:
        print('Invalid move')
num_1=int(input('first number ='))
num_2=int(input('second number ='))
oper=input('operation')
a=calculator(num_1, num_2, oper)
print(a)


        
