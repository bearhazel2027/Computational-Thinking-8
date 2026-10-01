
passengerclass=input("Welcome to the Titanic, the unsinkable ship. Try to survive. Please choose your character, Captain, First passenger, Second class passenge, Third class passenger.")
if passengerclass == "First":
    pronouns=input("Please write your pronouns")
    age=int(input("Please write your age"))
    if age < 18:
        print("You walk down to your room with your parents.(2 days to collision")
    else:
        print(f"You walk down to the  {passengerclass}deck(2 days to collision)")
        print("You set your stuff down on your bed and survey the room. It's nice and furnished. And as a bonus the hallway outside your room directly connects to the deck.")
        print("All of a sudden someone burst through the door. It's a man and he is out of breath. What do you do?")
        moral=input("Help,Security,Shoo him")
    if moral == "Security": 
        print("Security bursts in after the man and he's dragged away.")
    elif moral == "Help":
        print("You run to the doors and quickly shut and lock them.")
    elif moral == "Shoo him":
        print("You push the man out of your room and lock the doors. THE AUDACTITY of some people. Just WALKING into peoples rooms like that!!")
elif passengerclass == "Second":
    pronouns=input("Please write your pronouns")
    age=int(input("Please write your age"))
    if age < 18:
        print("You walk down to your room with your parents.(2 days to collision")
        print("The room is warm even if it is a little bland.")
    else: 
        print(f"You walk down to the  {passengerclass}deck(2 days to collision")
        exploring=input("Your parents are going up to the deck. Do you go too or explore?")
        if exploring == "explore":
            print("You wave goodbye to your parents are start off into the halls.")
        else:
            print("Your parents decide that they want you to explore. They wave goodbye and you start walking through the halls.")
elif passengerclass == "Third":
    pronouns=input("Please write your pronouns")
    age=int(input("Please write your age"))
    if age < 18:
        print("You walk down to your room with your parents.(2 days to collision")
    else:
         print(f"You walk down to the  {passengerclass}deck(2 days to collision")
elif passengerclass == "Captain":
    pronouns=input("Please write your pronouns")
    age=int(input("Please write your age"))
    print(f"You wake up in your cabin to the feel of rocking waves in the night. You get up, get dressed, and step out onto the deck into the moonllight. You slept about 2 hours and its 1020(Two days till collision")
else:
    print("Don't forget to capatilize your answer!!!!! Try again") 




