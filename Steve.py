# - Import random
# - Engine 
#     - Play function
# - Map
#     - next_scene function
#     - opening_scene function
# - Scenes
#     - Intro/entry scene(broom closet)
#         - Enter
#             - Room and game description
#             - Action input from user
#         - Exit leads to hallway
#     - Hallway
#         - Enter function
#             - Description (include door labels)
#             - Action input from user
#         - Steve function random chance
#     - Mess Hall/Dining room
#         - Enter function
#             - Room description
#             - Action input from user
#         - Food choices
#             - Live(all but one food option)
#             - Die(one clear bad choice food, special unique death condition/message)
#             - Set to return a True value once the user has executed the action of picking a non-death food
#         - Exit function
#         - Steve function random chance
#     - Bathroom
#         - Enter function
#             - Room description
#             - Action input from user
#         - Use bathroom function
#             - Set to return True once user uses restroom
#         - Wall safe
#             - Nice-to-have
#             - Contains repellent (one-use item to get rid of Steve one time)
#     - Infirmary
#         - Room is a nice-to-have
#         - Enter function
#             - Room description
#             - Action input from user
#         - Largely full of jokes and world-building items for the user to find, no gameplay advancement in this room
#     - Escape Condition
#         - Check for values returned by the use bathroom, food choice, and liquor functions
#     - Death scenes
#         - Create funny death lines
#         - Function for handling death conditions
#     - Bar
#         - Enter Function
#             - Room description
#             - Action input from user
#         - Cabinet function
#             - Describe available liquor
#             - List of liquor types
#             - Input for user to select type of alcohol
# Create classes for all hierarchy objects
import random
import sys
# list of possible messages for the Death function
death_messages = ["Steve chuckles as you feel something seem to slowly seep out of you. At this point, you learn goats are capable of smiling maliciously. You wish you hadn't learned that. Thankfully, you won't know it much longer, as you collapse on the ground...","Well that didn't work at all. Good look reincarnating!","Y'know, it was a good thing you took out that life insurance policy!"]


inv = {
    "food":0,
    "booze":0,
    "toilet":0
}


# If a player loses, select a random death message and display it
def Death():

        message = death_messages[random.randint(0,len(death_messages) - 1)]
        print(message)
        sys.exit(0)

# define a "hallway" in which the user can access the functions for the other rooms
def Hallway():
        print('''
        You find yourself in the ship's main hallway. Nearby, you see 3 doors. These lead to:
        Dining Room
        Bar
        Bathroom
        ''')
        user_action = input("What would you like to do? ").lower()

        if user_action == "broom closet":
            print("The aardvark told you to get out of here!")
        elif user_action == "dining room":
            DiningRoom()
        elif user_action == "bar":
            Bar()
        elif user_action == "bathroom":
            Bathroom()
        else:
            print("That must be a room in some bizarro dimension where nothing makes sense.")

# run a randomizer to determine if Steve spawns, intended to be used when the player enters any room but the hallway
def Steve():
    spawn_roll=random.randint(1,100)
    
    if spawn_roll in range(0, 33):
        print("Suddenly, the air chills and the lights flicker. As they stabilize again, you see a small, goat-like creature floating in the middle of the room.")
        i = 1
        while True:
            user_action = input("What would you like to do? ").lower()

            if (user_action == "run") or (user_action == "exit"):
                player_exit = True
                return player_exit
            
            else:
                print("That doesn't do anything!")
                if i == 3:
                    Death()
                    
                i += 1
                

def BroomCloset():

    print('''
    You awaken in your trusty broom closet, the room that has served you so well while hiding from security aboard this cruise ship. Suddenly, what appears to be a miniature aardvark appears through the air vent.

    "Steve the Devourer has arrived! You must run, quickly! He will encourage you to do fun and relaxing things aboard this ship to fatten up your soul for his feast!" it exclaims.

    "..." you reply.

    "...Steve the Devourer is a soul-gobbling goat from the Abyss. I don't have time to convince you, just trust me and get out of here!" the aardvark implores.

    "..." you reply.

    "Oooook, this is such a stimulating conversation, but you have to go. Remember to eat, go to the bathroom, and get yourself something to drink for the trip!" it says with a motherly intonation.

    You shrug and consider whether to exit the broom closet.
    ''')
    while True:
        user_action = input("What would you like to do? ").lower()

    
        if user_action == "exit":
            print("You exit the broom closet, bidding farewell to the miniature aardvark.")
            break
        else:
            print("That's not quite right...")

def DiningRoom():
    foods = [
        "Steak",
        "Chicken Cordon Bleu",
        "Seared Salmon",
    ]
    print("You enter the ship's Dining Room. There are a few choices for dinner tonight. You can order: ")
    for food in foods:
        print(food)
            
    Steve()
    
    while True:
        user_action = input("What would you like to do? ").lower()

        if user_action == "steak":
            print("Good choice! A medium rare steak appears in front of you. You tear off a bite with your teeth, fold it up in a napkin, and place it in your bag.")
            inv["food"] = 1
            break
        elif user_action == "chicken cordon bleu":
            print("A juicy piece of Chicken Cordon Bleu appears. You cut into it, a lovely stream of molten cheese flowing out. Bringing your fork to your mouth, you savor the delicious combination of ingredients. Then you wrap up the rest of it in a napkin and shove it into your bag, you Cretin.")
            inv["food"] = 1
            break
        elif user_action == "seared salmon":
            print("A salmon appears in front of you, swimming in midair. It appears confused and perhaps annoyed. The chef rushes over, grabs the salmon, and sprints off. Moments later a plate of seared salmon appears in front of you. You warily take a bite, look around, then store the remainder of your dish in a napkin and secure it in your bag.")
            inv["food"] = 1
            break
        elif user_action == "exit":
            break
        else:
            print("That is not an option here.")
        
liquors = [
        "Whiskey",
        "Vodka",
        "Gin",
        "Tequila",
        "Rum",
    ]
liquor_choice = "None"

def Bar():
    
    print('''
    You enter the bar, or at least what is marked as a bar. It appears to be haphazard chair and table storage in which a few passengers are having panic attacks. You notice a liquor cabinet with the door ajar. You can:

    Open Liquor Cabinet
    Exit
    
    '''
    )
    Steve()
    
    while True:
        user_action = input("What would you like to do? ").lower()

        if user_action == "open liquor cabinet":
            print("There are several bottles of liquor available. You can choose:")

            for liquor in liquors:
                print(liquor)
            
            liquor_choice = input("Which bottle do you take? ").lower()

            if (liquor_choice == "whiskey") or (liquor_choice == "vodka") or (liquor_choice == "gin") or (liquor_choice == "tequila") or (liquor_choice == "rum"):
                print("You take a swig and tuck the bottle into your bag.")
                inv["booze"] = 1
                break
            else:
                print("That isn't an option.")
        elif user_action == "exit":
            break
        else:
            print("You can't do that here.")


def Bathroom():
    
    print('''
    You enter the bathroom. As you look around you realize this is, in fact, a bathroom. You can:

    Use The Toilet

    '''
    )
    Steve()
    
    while True:
        user_action = input("What would you like to do? ").lower()

        if user_action == "use the toilet":
            print("It's best we not dwell on exactly what's happening right now.")
            inv["toilet"] = 1
            break
        elif user_action == "exit":
            break
        else:
            print("That is not an option here.")

def EscapePod():
    print("You finally make your way to the escape pod! You see a chair with flight straps and a big button labeled Launch. You can:")
    print("Launch")
    
    i = 0
    while True:
        user_choice = input("What would you like to do? ").lower()

        if user_choice == "launch":
            return True
        elif i > 2:
            Death()
           
        else:
            print("You can't do that here.")
            i += 1
def check_stock():
    
    if inv["food"] == inv["booze"] == inv["toilet"] == 1:
        return False
    else:
        return True
    
    

def play():
    BroomCloset()
    while True:
        Hallway()
        check_stock()
        if check_stock() == False:
        
            if EscapePod() == True:
                print('As you move away from the docking collar, you see a ghastly goat-like face appear in the mirror and say "Remember, a free soul is a tasty soul" and laughs maniacally. You have no idea how you were able to hear the goat. You take a long pull from your bottle and settle in until you are rescued.')
                break
        
        
play()