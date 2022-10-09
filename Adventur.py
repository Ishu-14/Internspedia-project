# ADVENTURE GAME
name = input("Please Enter Your Name: ")
print("HELLO,HOLA!!", name, "! Welcome to adventure World Game!")
answer_yes = ["Yes", "Y", "yes", "y","YES"]
answer_no = ["No", "N", "no", "n","NO"]
start = input("Would You like to play the game or not [yes/no] ? : ")

if start in answer_yes :
    print("\nGreat! Let's play the game!")
    print("________________________________")
    print("\nIt is dark and you are walking blindly in a damp smelly place. Your foot makes a squising sound with each step \nThe creepy voices continues to call out you,'JJ!!! JJ!!! Save me!!")
    adv=input("What steps will you follow : \n[Follow the voice] \n[Turn and run] \nEnter your choice :")
    if adv=="Follow the voice" :
        print("Whosoever it is knows my name, you think. \nMaybe they need my help? \nThe voice grew lowder as you goes towards it")
        response=input("You found a person in creepy place founding the way out of that place, \nwill you help[yes]/[no] : ")
        
        if response in answer_no:
            print("\nYou are a good Human. He was a Ghost ")
        
        elif response in answer_yes:
            print("\nNow, ghost is trying to kill you. Will, you able to hunt the ghost? (Yes / No)")
            ans3 = input("Enter your choice: ")
            
            if ans3 in answer_yes:
                print("\nCongrats! He was a ghost & You hunt the Ghost with your bravery.")
                print("You got stars 6/6 , go to stage 2..")
        
            elif ans3 in answer_no:
                print("\nSorry! You are dead. He was a Ghost & He killed you. GAME OVER")
            
            else:
                print("\nYou typed the wrong input. SORRYY!")
        else:
            print("\nYou typed the wrong input. SORRYY!")
    elif adv=="Turn and run":
        print("You Saved yourself from the deadly ghost!! Congratulations")
        gg=input("Will you play stage 2 [yes]/[no] : ")
        if gg in answer_yes:
            print("Your stage two is loading ,PLZ wait.....")
        elif gg in answer_no:
            print("Thankyou!")
            quit()
        else:
            print("\nYou typed the wrong input. SORRYY!")
            
    else:
        print("\nYou typed the wrong input. SORRYY!")
            
else:
    print("Oh! sorry!! you are dead, good work...")
    quit()
