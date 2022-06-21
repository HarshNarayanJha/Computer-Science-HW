# 8. Write a python program to check the person is eligible or not?
from datetime import date
import random
import time

# Eligibility Criteria:
#  - Age > 0
#  - Should know the correct value of `pi` upto 2 decimal places
#  - Should be able to solve a very simple mathematical expression
#  - Should be watching Spy x Family
#  - Should know the names of upcoming Pokemon games
#  - Should know that who will win PWC championships

# Name and Age part
print("Welcome to the person eligibility tester!\n")
name = input("What's your name: ")

st_time = time.time()

age = int(input(f"Nice name {name}. So tell me, what's your age? >>> "))
print("Well, leave that, I will calculate myself, tell me your birth year instead")

b_year = int(input(">>> "))
b_month = int(input("month please (month number, I don't understand month names) >>> "))
b_date = int(input("Why not tell me the birth date then >>> "))

bday = date(b_year, b_month, b_date)
calc_age_days = (date.today() - bday).days
bday_str = bday.strftime("%dth %B %Y")
bday_weekday = bday.strftime("%A")

print(f"So, you came on this Earth on {bday_str}. Hmm, wasn't that day {bday_weekday}?")
my_bday = date(2006, 3, 11)
if bday < my_bday:
    print(f"Awwww.. you are older than me, and by {(my_bday - bday).days} days. How Rude!")
elif bday > my_bday:
    print(f"Yepeee... atleast someone is less in age than me, and by {(bday - my_bday).days}")

print(f"\nAnyways, you are {calc_age_days} days old,")

years_100 = date(bday.year + 100, bday.month, bday.day)
total_lifespan = (years_100 - bday).days

if age <= 0 or calc_age_days <= 0:
    print(f"And if you live for at least 100 years... you have around {total_lifespan - calc_age_days} days left. You want achi.... wait a sec...")
    print(f"are you really {age} years old! OMG.. b-bb-b..yy-eeeeeee...")
    exit()
print(f"And if you live for at least 100 years... you have around {total_lifespan - calc_age_days} days left. You want achieve your goals real quick!")

# Maths part
print("\nGreat! Now let's get to some Maths")
if input("Ok! Now tell me the value of pi (upto 2 places after decimal) >>> ") != "3.14":
    print(f"Oh! You don't even know that and claim to be {age} years old? Get out of here")
    exit()

p_1 = random.randint(0, 100)
p_2 = random.randint(p_1, 100)
p_pow = random.randint(0, 2)
p_sol = (p_1 + p_2) ** p_pow
print(f"\nNow some real test. Tell me the value of ({p_1} + {p_2}) ** {p_pow}")
u_sol = int(input(">>> "))
if p_sol != u_sol:
    print(f"Learn some maths and then come here {name}. Are you really {age} years old?")
    exit()

# Pokemon
print("\nExcellent! Now for some real test")
u_poke = input("What's the name of your favourite Pokemon??? ")
if u_poke.lower() == "pikachu": print("I knew that. It's the favourite of all, Pikachu!")
elif u_poke.lower() == "greninja": print("I like Greninja Too")
elif u_poke.lower() == "lucario": print("Wow lucario? Isn't Ash's Lucario just the coolest?")
else: print(f"Hmmm... yes {u_poke}. Nice choice")

# Anime
print("\nNow tell me, what is the anime you are currently watching? (hint: it's a new one)")
anime = input(">>> ")
if anime.replace(" ", "").lower() != "spyxfamily":
    print("Go and watch Spy x Family before being eligible! It's A+")
    exit()

print("Spy x Family, it's awesome, right?")

# Scarlet Violet
print("\nNow the last question, Answer this correctly and you will be qualified")
print("What's is the name of upcoming pokemon games (any one)?")
poke_game = input(">>> ")
if poke_game.lower().replace("pokemon", "").strip() not in ['scarlet', 'violet']:
    print(f"It's Pokemon Scarlet and Pokemon Violet. You don't even know that and you call yourself a {u_poke} trainer? Byeeee")
    exit()

print("Ah, Scarlet Violet. Can't wait to play the upcoming Gen 9 game and watch new Gen 9 anime")
print()

# PWC
print("\nNow the last question, this is, for real. Answer this correctly and you will be qualified for sure")
print("Who will win the Pokemon World Coronations Series Championships?")
pwc_win = input(">>> ")
if pwc_win.lower() not in ['ash', 'leon']:
    print(f"{pwc_win}? Are you sure? Well I guess there is no point in letting anyone else win other than Ash or Leon. See ya!")
    exit()

print(f"{pwc_win}, yeah maybe. Let's see who will win this thing and become the world monarch!")
print()

time_taken = round(time.time() - st_time, 2)

print(f"So {name}, you are succesfully qualified and you are eligible. You passed this hard test in only {time_taken} seconds despite only having a mere experience of {calc_age_days} days!")
print(f"You are awesome, you even like {u_poke}, and praying for {pwc_win}'s win!")
print("Thanks for trying this out. Good bye and have a nice day learning Python!")
input()