
winter_points = 0
summer_points = 0
spring_points = 0
fall_points = 0

questions = 5
results = "active"

if questions > 3 and results == "active":
    print("This quis is open for taking")
else:
    print("This quiz is currently unavalible")
print("Welcome to your personality quiz: What seasons make up you?")
qone = input("First question: Do you prefer (A) clouds or (B)sun?")
if qone == "clouds" or qone == "A": 
    winter_points += 1
    fall_points += 1
    print("Nice! Question two ")
elif qone == "sun" or qone == "B":
    spring_points += 1
    summer_points += 1
    print("Nice! Question two ")
qtwo = input("Do you like sweats or jeans or shorts ")
if qtwo == "jeans":
    fall_points += 1
    print("ME TOO!")
elif qtwo == "sweats":
    winter_points += 1
    print("Cozy!")
elif qtwo == "shorts":
    summer_points += 1
    spring_points += 1
    print("Cool!")
qthree = input("Do you like lemonade or tea ")
if qthree == "tea":
    fall_points += 1
    winter_points += 1
    print("YAY!")
elif qthree == "lemonade":
    summer_points += 1
    spring_points += 1
    print("Refreshing!!")
qfour = input("Do you prefer boots or sneakers ")
if qfour == "boots":
    spring_points += 1
    print("SPLISH SPLASH")
elif qfour == "sneakers":
    summer_points += 1
    print("Good for nice walks :)")
#here I put spring vs summer when i previously had them together
qfive = input("Do you like warm colors or cool colors ")
if qfive == "cool" or "cool colors":
    winter_points += 1
    print("So pretty")
elif qfive == "warm" or "warm colors":
    fall_points += 1
    print("nice to see out the window!")
#here I put winter vs fall when i previously had them together

# end of quiz 

if winter_points > 3:
    print("you are WINTER")
elif spring_points > 3:
    print("you are SPRING")
elif summer_points > 3: 
    print("you are SUMMER")
elif fall_points > 3:
    print("you are FALL")
else:
    print("you are a mix of different seasons!")

