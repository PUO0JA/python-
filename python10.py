def make_them_feel_bad(userlist):
    exp=''.join(userlist)
    print(Name + ' is such a ' + exp)
    return(exp)
 

Name=str(input(print('Enter the name of the person you want to make feel good(sarcastically)')))
input_expressions=str(input('Enter the list of expressions you want to use separated by spaces'))
userlist=input_expressions.split()
print('Your list of expressions is', userlist)

Boom_have_fun_now=map(make_them_feel_bad, userlist)
print(list(Boom_have_fun_now))
