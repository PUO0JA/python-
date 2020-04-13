def Total_bonus(Total_basic):
    if(Total_basic<=7000):
        Bonus=7000*8.33
        print('The bonus that would be given will be' + str(Bonus))
        return(Bonus)
    elif(Total_basic>7000):
        Bonus=(Total_basic*8.33)/100
        print('The bonus that would be given will be' + str(Bonus))
        return(Bonus)
    elif(Total_basic>21000):
        Bonus=0
        print('The bonus is' + str(Bonus))
        return(Bonus)
        
def pf(Total_basic, Allowance):
    Total=Total_basic+Allowance
    if(Total<15000):
        p_f=(Total*12)/100
        print('The providend fund would be' + str(p_f))
        return(p_f)
    else:
        p_f=(Total*12)/100
        print('The providend fund would be' + str(p_f))
        return(p_f)
def Esic(Gross):
    if(Gross<=21000):
        esic=(Gross*0.75)/100
        print('The Employee state Insurance corp. would be' + str(esic))
        return(esic)
    else:
        print('You are not eligible for ESIC you can go for other group insurances')
        return(0)
        
def In_hand(Gross, Allowance, T, P, E, Tds):
    Take_home_salary=((Gross+Allowance+T)-(P+E+Tds))
    print('Your take home salary will be' + str(Take_home_salary))
    return(Take_home_salary)
        
        
print('This app will calculate your pf, Esic and bonus and finally THE TAKE HOME SALARY')
print('corresponding to the basic wages and thr other components you give into the system')

Name=input('Enter the name of the employee')
City=input('Enter the name of the city')
Wage=int(input('Enter the basic wage of the employee as per govt. rules'))
Hra=int(input('Enter the Hra of the employee'))
Allowance=int(input('Enter the basic allowance of the employee as per the govt. rules'))
lwf=int(input('Enter the lwf as decided by govt according to the city'))
Tds=int(input('Enter the tds your company cuts usually from the employees salaries usually'))
Total_basic=Wage+Hra
Gross=Total_basic+lwf+Allowance
print('Total_basic=Wage+Hra')
print('Gross=Total_basic+lwf+Allowance')
T=Total_bonus(Total_basic)
print(T)
P=pf(Total_basic, Allowance)
print(P)
E=Esic(Gross)
print(E)
S=In_hand(Gross, Allowance, T, P, E, Tds)
print(S)
print('Hence, ' + Name + ' Working in the city ' + City + ' will get the salary Rupees ' + str(S))


