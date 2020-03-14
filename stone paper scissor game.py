import random 
  
print("\n              S T O N E     P A P E R     S C I S S O R     G A M E\n") 
  
while True: 
    
    print("""Enter your choice : 
    a. Press '1' to select 'Stone'. 
    b. Press '2' to select 'Paper'.
    c. Press '3' to select 'Scissor'.\n""") 
      
    user_choice = int(input("Enter YOUR choice: ")) 
  
    while user_choice > 3 or user_choice < 1: 
        user_choice = int(input("Enter valid input: ")) 

    if user_choice == 1: 
        c_nm = 'Stone'
    elif user_choice == 2: 
        c_nm = 'Paper'
    else: 
        c_nm = 'Scissor'
 
    print("YOUR choice is: ",c_nm) 
    print("\nNow, its COMPUTER'S turn.......") 

    comp_c = random.randint(1, 3) 

    while comp_c == user_choice: 
        comp_c = random.randint(1, 3) 

    if comp_c == 1: 
        comp_c_nm = 'Stone'
    elif comp_c == 2: 
        comp_c_nm = 'Paper'
    else: 
        comp_c_nm = 'Scissor'
          
    print("COMPUTER'S choice is: ",comp_c_nm,"\n") 
  
    print(c_nm," V/s ",comp_c_nm) 

    if((user_choice == 1 and comp_c == 2) or
      (user_choice == 2 and comp_c ==1 )): 
        print("Paper wins !!! \n", end = "") 
        result = "Paper"
          
    elif((user_choice == 1 and comp_c == 3) or
        (user_choice == 3 and comp_c == 1)): 
        print("Stone wins !!! \n", end = "") 
        result = "Stone"
    else: 
        print("Scissor wins !!!\n", end = "") 
        result = "Scissor"

    if result == c_nm: 
        print("\nYOU WIN !!!\n") 
    else: 
        print("\nCOMPUTER WINS !!!\n") 
          
    print("Do you want to play again? (y/n)") 
    ans = input() 
  
    if ans == 'n' or ans == 'N': 
        break

print("\n           T H A N K S     F O R     P L A Y I N G     ! ! ! ! !\n") 
