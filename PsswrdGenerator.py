# Password Generator
import random
import string
import re

# Welcome!
print('Hello, Welcome to Gabriels Password Generator!')
print('This Program can generate up to 2,000,000 different passwords')
print('**Password Strength Test Included**')

def Generator():
    #Value/Word Choices
    adjective = random.sample(adjective_list, 1)
    animal = random.sample(animal_list, 1)
    num = random.sample(num_list, 1)
    symbol = random.sample(symbol_list, 1)
    password = adjective + animal + num + symbol
    password = "".join(password)

    # Merging Words
    randomnumber = random
    password = adjective + animal + num + symbol

    password = "".join(password)
    # Password Strength
    v = password
    if(len(v)>=8):
        if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
            print('         ')
            print('This password is considered:')
            print('Strong')
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
        print('         ')
        print("The password generated was Weak... Generating New Password")
        Generator()
    else:
        print('         ')
        print('You have entered an invalid password.')

    #Password Created
    print('         ')
    print('Your New Password is....')
    print('         ')
    print(password)


# Variables
print('         ')
userready = input('Press Enter to Receive New Password: ')
adjective_list = ["Handsome", "Angry", "Confused", "Funny", "Wild", "Losing", "Adorable", "Adventurous", "Agressive", "Bewildered", "Bloody", "Breakable", "Brave", "Bright", "Beautiful", "Busy", "Calm", "Cool", "Careful", "Cautious", "Clever", "Cloudy", "Confused", "Cute", "Curious", "Crowded", "Determined", "Different", "Depressed", "Dizzy", "Doubtful", "Enchanting", "Evil", "Excited", "Famous", "Fancy", "Fair", "Faithful", "Frail", "Fragile", "Glorious", "Scary", "Selfish", "Rich", "Spotless", "Splendid", "Tender", "Terrible", "Ugly", "Tired"]
animal_list = ["Woodpecker", "Sheep", "Shark", "Salamander", "Rat", "Raccoon", "Rabbit", "Rhino", "Quail", "Duck", "Possum", "Platypus", "Porcupine", "Puma", "Bear", "Mouse", "Octopus", "Lobster", "Llama", "Lion", "Dog", "Dragon", "Cheetah", "Panther", "Monkey", "Pig", "Elephant", "Beaver", "Bat", "Beagle", "Hyena", "Snail", "Snake", "Stoat", "Swan", "Tamarin", "Tapir", "Tarantula", "Termite", "Tiger", "Toad", "Tortoise", "Toucan", "Turkey", "Turtle", "Vole", "Vulture", "Wallaby", "Walrus", "Warthog", "Wasp", "Weasel", "Whale", "Wildebeest", "Wolf", "Wolfhound", "Wolverine", "Wombat"]
num_list = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99"]
symbol_list = ["!","@","#","$","%","&","_"]
Generator()



# Finish
print('         ')
user_finished = input('Would you like to generate a different password? (Y/N): ')


while user_finished== 'Y':
    print('Running Generator...')
    Generator()
    print('         ')
    user_finished = input('Would you like to generate a different password? (Y/N): ')
else:
    print('Ciao!')
