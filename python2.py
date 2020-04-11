a=10
p=10
t=a*p
print('The total money you have corresponding to the no. of apples you have to buy'+ str(t))
apples_count=int(input('how many apples you want to buy:'))
#Enter the no. of apples you want
print('Apple you want to buy ='+str(apples_count))
apples_price=int(input('what is the price of apples'))
#This is the price of the apples in the market
print(apples_price)
total_price=apples_count*apples_price
print('The total price of apples will be'+ str(total_price))
if(((apples_count>a)and(apples_price<=p))or((apples_count==a)and(apples_price<p))):  #mummy condition
    cost=apples_count*apples_price
    print('The apples will cost you dollars'+ str(cost)+ 'Hence you are good to go')
elif((apples_count==a)and(apples_price==p)):  #chota bhai behen condition
      cost=apples_count*apples_price
      print('The apples will cost you dollars'+ str(cost)+ 'fine you will not get scolded')
else:  #papa condition
    cost=apples_count*apples_price
    print('Come back home son you don not have enough money you just have dollars'+ str(t)+ 'and you need dollars'+str(cost))
      
