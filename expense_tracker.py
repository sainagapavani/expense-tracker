#Question / Problem Statement: Create a console-based Expense Tracker program in Python that allows the user to record daily expenses and view summaries like total spending. Use only the concepts learned till Chapter 6qw(loops, conditionals, lists, dictionaries, and basic input/output).
#Sample Output:
#Welcome to Expense Tracker 💸
#======= MENU =======
#1️⃣Add Expense
#2️⃣View All Expenses
#3️⃣View Total Spending
#4️⃣Exit
#=====================
#Enter your choice (1-4): 1
#Enter date (DD-MM-YYYY): 05
#category (Food, Travel, Shopping, etc): Food  

#code begin here

expenses=[]    # it is a list which contains all expenses 

print('Welcome to GOLMAAL  EXPENSE TRACKER')

while (True):                                  #here the original project begins
    print('===== MENU =====')
    print('1 : Add an expense')
    print('2:View all expenses')
    print('3:View total spending')
    print('4:Exit')
    
    choice=int(input('Enter your choice : ' )) #asking user to give a choice 
    
    # if 1 was selected
    
    if choice==1:
        date = input('Enter date when when you did expense : ' )
        category=input('Enter type of expense : ' )
        description=input('Enter some detail about your expense : ')
        amount=float(input('Enter total amount you spent : '))
        
        expense={
            'date':date,
            'category':category,
            'description':description,
            'amount':amount
        }
        expenses.append(expense)
        
        print("Your expense added successfully")
    elif choice==2:
            if len(expenses)==0:
                print('No expense available try after adding an expense')
            else:
                 print('==== THESE ARE YOUR EXPENSES ==== ')
                 
                 i=1
                 for s in expenses:
                     print(f'''Date : {s['date']} 
                     Category : {s['category']} 
                     Description : {s['description']}
                     Amount : {s['amount']}''')
                     i+=1
# total spending    
    elif choice==3:
          
          
          
          totall=0
          for j in expenses:
                    total=0
                    total=total +float( j['amount'])
                    print('Total amount = ',total,sep='')
    elif choice==4:
         print('THANK YOU FOR USING GOLMAAL EXPENSE TRACKER')
         break
    else:
         print('invalid input try again')
     
