#code begin here
import csv as c 


expenses=[]    
try:
    with open('expenses.csv', 'r') as file:
        reader = c.reader(file)
        try:
            next(reader)  # Skip the header
        except:
            print('There are no previous expenses')
        for row in reader:
            if row:
                expense = {
                    'date':row[0],
                    'category':row[1],
                    'description': row[2],
                    'amount': float(row[3])
                }
                expenses.append(expense)
except FileNotFoundError:
    pass



print('Welcome to PERSONAL  EXPENSE TRACKER')

while (True):                                  #here the original project begins
    print('===== MENU =====')
    print('1:Add an expense')
    print('2:View all expenses')
    print('3:View total spending')
    print('4.View all expenses on specific date')
    print('5.Export  expenses to CSV file ')
    print('6.Delete an expense')
    print('7:Exit')
     
    try:
        choice=int(input('Enter your choice : ' )) #asking user to give a choice
    except:
        print('Enter valid choice')
        continue
    
    if choice==1:
        def ExpenseTracker():
            
            while (True):
                global date 
                date = input('Enter date when when you did expense : ' )
                if date=='':
                    print('Enter valid date')
                else:
                    break
            
            while (True):
                              global category
                              category = input('Enter type of expense : ' )
                              if category=='':
                                  print('Enter valid category')
                              else:
                                  break
        ExpenseTracker()
        description=input('Enter some detail about your expense : ')
        
        while (True):
                try:
                    amount=float(input('Enter total amount you spent : '))
                    if amount<=0:
                        print('Amount should be valid')
                    else:
                        break
                except:
                     print('Please enter  valid amount')                
                
                                                        
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
                     print(f'Expense {i}')
                     print(f'''Date : {s['date']} 
                     Category : {s['category']} 
                     Description : {s['description']}
                     Amount : {s['amount']}''')
                     i+=1

    elif choice==3:      # total spending    
          total=0
          for j in expenses:
                    total=total +float( j['amount'])
          print('Total amount = ',total,sep='')
          print('Thank you! Keep tracking your expenses.')
    
    elif choice==4:
        specific_date=input('Enter date too see all expenses on that date: ')
        y=1
        expenses_found=False
        for x in expenses:            
            if specific_date==x['date']:
                print(f'Expense {y}')
                expenses_found=True
                print(f'''Category : {x['category']} 
                     Description : {x['description']}
                     Amount : {x['amount']}''')
                y+=1 
        if not expenses_found:
                         print('No expense available on that date try after adding an expense')                                                  
    
    elif choice==5:
        with open('expenses.csv','w',newline='') as file: 
            writer = c.writer(file)
            writer.writerow(["Date","Category","Description","Amount"])            
        with open('expenses.csv','a',newline='') as file:         
            writer = c.writer(file)            
            for expense in expenses:
                 writer.writerow([expense['date'],expense['category'],expense['description'],expense['amount']])
             
        print("Expenses exported successfully!")
                              
    elif choice==6:
        while (True):
            try:
                index=int(input('Enter the number of expense to delete: '))
                d=index-1
                expenses.pop(d)
                print('Expense deleted successfully')
                break
            except :
                print('Enter valid expense number')
                
    
    elif choice==7:
         print('THANK YOU FOR USING PERSONAL EXPENSE TRACKER')
         break
    
    else:
         print('invalid input try again')
     