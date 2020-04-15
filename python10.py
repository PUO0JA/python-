def make_them_feel_bad(userlist):
    exp=''.join(userlist)
    print('you are such a ' + exp)
    return(exp)
 


input_expressions=str(input('Enter the list of expressions you want to use separated by spaces'))
userlist=input_expressions.split()
print('Your list of expressions is', userlist)

Boom_have_fun_now=map(make_them_feel_bad, userlist)
print(list(Boom_have_fun_now))
