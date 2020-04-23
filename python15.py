class Sweetmenu:
    menu={}
    def test(self,name,price):
        self.name=name
        self.price=price
        self.menu[self.name]=self.price
    def display(self):
        print(self.menu)
    pass

sweet_menu=Sweetmenu()

n=int(input('Enter the no. of items you want to add in your menu'))
for i in range(0,n):
    sweet_menu.name=str(input('Enter the name of the sweet'))
    sweet_menu.price=int(input('Enter the price you want to desginate to the sweet'))
    print(str(sweet_menu.name)+' will cost you around '+str(sweet_menu.price)+' Dollars')
sweet_menu.display()
selected_items=[]    
def select_item(menu):
    for i in range(len(menu)):
        select=input('Select the sweet of your choice from the menu')
        selected_items.append(select)
    return selected_items
count=0
def Bill(selected_items, menu):
    for i in range(len(selected_items)):
       coun+=count+menu[i]
    print(coun)

    
            
            
a=select_item(menu)
print('The selected item are: ',a)
b=Bill(selected_items, menu)
print('The Bill of dollars',b)
        

