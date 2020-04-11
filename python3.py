money=20
items={'apple':2,'banana':4,'orange':6}

for item_name in items:
    print('....................................................')
    print('Each' + item_name + 'costs' + str( items[item_name] ) + 'dollars')
    input_count=int(input('Enter the no. of' + item_name + 'you want to buy'))
    Total_amount=input_count*items[item_name]
    Balance=money-Total_amount

    while balance!=0:
        updated_balance=balance-Total_amount
        updated_balance+=1

        if(Total_amount<Balance):
              print('Your item is costing you' + str( Total_amount ) + 'since it is in your budget hence you are good to go')
              print('Dollars' + str( Total_amount ) + 'Have been deducted from your account and now you have' + str( Balance ) + 'amount left in your wallet')
              print('You have' + str(input_count) + 'no. of fruits with you as of now')
        else:
              print('Your wallet is now empty you may stop now or buy less no. of' + item_name)
              input_count=int(input('Enter the no. of' + item_name + 'you want to buy'))
              Total_amount=input_count*items[item_name]
             if((Total_amount<Balance)or(Total_amount==Balance)):
                  print('Your item is costing you' + str( Total_amount ) + 'since it is in your budget hence you are good to go')
                  print('Dollars' + str( Total_amount ) + 'Have been deducted from your account')

        print('now you have' + str( updated_balance ) + 'amount left in your wallet')    
                        
