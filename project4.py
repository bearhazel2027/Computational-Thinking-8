print("Welcome to the clothes shop!This game is called Clash or Cash!")
print("In this game there is a preset mystery pant color. You will have to pick the top and "
"shoe color based on the clue you got for the pant color. If the colors you picked for the top and shoes " \
"match with the pants then you get coins. But if make a clash, you lose :(. The game goes twice so you can try different combos or you might get a different pant clue! GOOD LUCK!")

import random
hidden_number = random.randint(1,2)


#loop starts here from line 

for i in range(2):
    if hidden_number > 1 : 
        pant_color = "green"
        print("Time to play!Your clue is: I have a double letter, the letter rhymes with bee. When birds look down below this is the color they see. ") 
        shoe_color = input("Please pick your shoe color")
        top_color = input("Please pick your top color")
        if top_color == "pink" or "Pink" or "yellow" or "Yellow" and shoe_color == "black" or "black" or "White" or "white" or "yellow" or "Yellow" or "pink" or "Pink":
            print ("YOU MADE A MATCH AND WON THE CASH!!!!!!!! +1000000 coins")
        else:
            print ("CLASH CLASH CLASH. YOU LOSE!")
    else:
        pant_color = "blue"
        print("Time to play!Your clue is: I am calm and cool like a peaceful tide. I am opposite of orange. ") 
        shoe_color = input("Please pick your shoe color")
        top_color = input("Please pick your top color")
        if top_color == "orange" or "Orange" or "White" or "White" or "blue" or "Blue" and shoe_color == "black" or "black" or "White" or "white" or "blue" or "Blue" or "Orange" or "orange":
            print ("YOU MADE A MATCH AND WON THE CASH!!!!!!!! +1000000 coins")
        else:
            print ("CLASH CLASH CLASH. YOU LOSE!")
