running = True
again = 'That was fun! would you like to do it again? (type y or n)'


while running == True:
    print("Type 'start' to get started calculating the ROI")
    print("Type 'quit' to exit")
    re1 = input().lower()

    #easy
    if re1 == 'start':
        running_easy = True
        while running_easy == True:
            try:
                income = float(input("what is the investment's total monthly income?(please enter as a positive number)"))
                expenses = float(input("what is the investment's total monthly expenses?(please enter as a positive number)"))
                investment = float(input("What was the total initial investment?(please enter as a positive number)"))
                if income < 0 or expenses < 0 or investment < 0:
                    print('please use positive numbers this time.')
                else:
                    print(f'The anual ROI for your investment is about {str((((income - expenses) *12)/investment) * 100   )}%')
                    qagain = input(again)
                    if qagain == 'n':
                        running_easy = False
                    if qagain != 'y' and qagain != 'n':
                        continue

            except:
                print('I dont think you expressed yourself numerically there...\n please try that.')
                
    if re1 == 'quit':
        running = False
        
    

print('You have ended our fun. Goodbye.')
