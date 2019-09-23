import random
import readline
import smtplib
import ssl

"""Weekly shopping list and meal generator v0.01 with random choice generation for lazy mem-breads."""

nights = ['Sunday night','Monday night','Tuesday night','Wednsday night','Thursday night','Friday night']
meals = {1:'Lasagna',2:'Chilli con carne', 3:'Burgers', 4:'Butter chicken', 5:'Pizza', 6:'Thai curry', 7:'Drumsticks', 8:'Shepards pie', 9:'Dal', 10:'Carnitas', 11:'Cabonara', 12:'Risotto', 13:'Wraps'}
ingredients = {'Mince':0,'Olive oil':0,'Onion':0,'Garlic':0,'Cumin':0,'Chilli powder':0,'Oregano':0,'Salt':0,'Pepper':0,'Worcestershire sauce':0,'Tomato cans':0,'Black beans':0,'Red beans':0,'Fish sauce'
:0,'Cocoa powder':0,'Chicken':0, 'Dal':0,'Chilli':0,'Ginger':0,'Black mustard seeds':0,'Cumin seeds':0,'Tumeric':0,'Coriander powder':0,'Butter':0,'Coriander leaves':0,'Lasagna sheets':0,'Tomato Paste':0
,'Bread rolls':0,'Rice':0,'Butter chicken paste':0,'Cashew/peanut':0,'Greek yoghurt':0, 'White flour':0, 'Salami':0, 'Mozzerella':0, 'Yeast':0,'Basil':0,'Thai curry paste':0,'Coconut cream can':0,'Frozen veg':0,'Chicken Drumsticks':0,'Honey':0,'Soy sauce':0,'Corn chips':0,'Wraps/Pita':0,'Salad':0,'Tuna cans':0,'Cheese':0,'Beef stock':0, 'Potatoes': 0,'Milk':0,'Pork roast':0,'Lemon juice':0,'Tortillas':0
,'Pasta':0,'Cream':0,'Eggs':0,'Bacon':0,'Parmesan cheese':0,'Mushrooms':0,'White wine':0,'Risotto Rice':0,'Chicken stock':0}

recipes = {'Chilli con carne':{'Mince':680,'Olive oil':45,'Garlic':30,'Cumin':10,'Chilli powder':15,'Oregano':0,'Salt':7,'Pepper':2,'Worcestershire sauce':15,'Tomato cans':2,'Black beans':1,'Red beans':1
,'Fish sauce':15,'Cocoa powder':10,'Corn chips': 1},'Dal':{'Onion':2,'Tomato cans':2,'Chilli':2,'Ginger':10,'Black mustard seeds':5,'Cumin seeds':5,'Tumeric':5,'Coriander powder':5,'Butter':90,'Coriander leaves':10},'Lasagna':{'Mince':500,'Olive oil':30,'Onion':1,'Garlic':2,'Chilli powder':5,'Oregano':5,'Salt':2,'Pepper':2,'Tomato cans':2,'Lasagna sheets':9,'Tomato Paste':30},'Burgers':{'Mince':500,'Salt':7,'Pepper':2,'Bread rolls':6},'Butter chicken':{'Chicken':500, 'Rice':300,'Butter chicken paste':50,'Cashew/peanut':50, 'Greek yoghurt':50,'Butter':50},'Pizza':{'White flour':500, 'Salami':10, 'Mozzerella':200,'Yeast':5,'Salt':7,'Basil':5,'Tomato cans':1,'Tomato Paste':50},'Thai curry':{'Chicken':500, 'Rice':300,'Thai curry paste':50,'Coconut cream can':1,'Frozen veg':200,'Chilli':2},'Drumsticks':{'Chicken Drumsticks':8,'Honey':30,'Soy sauce':30,'Rice': 300,'Chilli':2},'Wraps':{'Wraps/Pita':6,'Salad':100,'Tuna cans':2,'Cheese':50},'Shepards pie':{'Mince':500,'Olive oil':15,'Onion':1,'Tomato Paste':15,'Salt':2,'Pepper':2,'White flour':30,'Beef stock':500,'Worcestershire sauce':15,'Potatoes':4,'Butter':40,'Milk':125},'Carnitas':{'Pork roast':1000,'Garlic':30,'Lemon juice':200,'Oregano':10,'Salt':5,'Pepper':5,'Cumin':5,'Tortillas':4},'Cabonara':{'Pasta':400,'Cream':100,'Eggs':4,'Bacon':200,'Parmesan cheese':50,'Garlic':2,'Olive oil':30},'Risotto':{'Butter':60, 'Parmesan cheese':60, 'Mushrooms':300,'White wine':100,'Risotto Rice':300,'Bacon':100,'Garlic':1,'Onion':1,'Chicken':400,'Olive oil':60, 'Chicken stock':800}}


def email():
    """This module will email Membrillo the shopping list"""
    global message
    sender_email = "holafrescabot@gmail.com"
    receiver_email = "silmembredes@gmail.com"
    password = "zvdqdkmjmmpoxyie"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email,password)
    try:
        server.sendmail(sender_email, receiver_email, message)
        print('Email sent!')
    except:
        print('Error :( ')
    server.quit()
	
	
choice = ''
message = ''

while choice.lower() != 'yes':
        selection = []
        rand_no = input('Do you want to choose the meal plan?  ')
        print('\n')
        if rand_no.lower() == 'yes' or  rand_no.lower() == 'y':
                for k,v in meals.items():
                        print('Press {} for {} '.format(k,v))
                print('\n')
                for x in range(len(nights)):
                        print('Enter your selection for {}: \n'.format(nights[x]))
                        temp = int(input())
                        if type(temp) != int:
                                print('Enter the number of the meal you want!')
                                temp = int(input())
                        selection.append(meals[temp])
        else:
                while len(selection) != len(nights):
                        robot_choice = meals[random.randint(1,len(meals))]
                        if robot_choice not in selection:
                                selection.append(robot_choice)

        print('The meals for the week are: \n')
        for x in range(len(nights)):
                print("{} we're having {}".format(nights[x],selection[x]))
        choice = input("Is this correct? (Type 'yes' or 'no') \n")


print("For the following week, you'll need:\n")
for x in selection:
        for k,v in recipes[x].items():
                ingredients[k] += v
for k,v in ingredients.items():
	if v != 0:
            message += "{} grams/ml/units of {}\n".format(v,k)
            print("{} grams/ml/units of {}".format(v,k))

print('Sending email maybe')
email()		
