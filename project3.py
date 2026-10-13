
winter_points = 0
summer_points = 0
spring_points = 0
fall_points = 0
#when the results are not set for active you cant take the quiz
questions = 5
results = "active"

if questions > 3 and results == "active":
    print("This quiz is open for taking")

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
    if qfive == "cool" or qfive == "cool colors":
        winter_points += 1
        print("So pretty")
    elif qfive == "warm" or qfive == "warm colors":
        fall_points += 1
        print("nice to see out the window!")


#here I put winter vs fall when i previously had them together

# end of quiz 

#If you have more winter than other points you are winter, if you have more fall points than other you are 
# fall, same for winter and spring. If you dont have one point total that is greater than other you get the
#response "you are a mix of different seasons"
    if winter_points > summer_points and winter_points > spring_points and winter_points > fall_points :
        print("you are WINTER")
    elif spring_points > summer_points and spring_points > winter_points and spring_points > fall_points :
        print("you are SPRING")
    elif summer_points > winter_points and summer_points > spring_points and summer_points > fall_points :
        print("you are SUMMER")
    elif fall_points > summer_points and fall_points > spring_points and fall_points > winter_points :
        print("you are FALL")
    else:
        print("you are a mix of different seasons!")
else:
    print("This quiz is currently unavalible")