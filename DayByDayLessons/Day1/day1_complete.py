""""""
"""
    Today's Lesson
    ---------------
    1. We will cover Print statements
        -> Is a computer dumb?
        -> Airplanes and dogs on the screen?
    2. We will begin learning about Strings
        -> What is text?
        -> What are variables?
    3. Project: Letter to the future
        -> Set career, goals, accomplishments
    4. Project: Shopping Cart
        -> Write down some vegetables, snacks, items
    5. Project: Mad Libs
        -> Nouns, Adjectives
"""

# Part 1.1 - Getting used to print statements
print("Hello World!")
print("The weather today is 70 degrees and sunny")
print("My favorite colors are green and blue")
print("2 + 2 = 4")
print("This computer follows my commands!")
# Practice - Print your favorite book, tv show, and favorite song
print("I love Harry Potter!")
print("The Big Bang is a funny show")
print("Halsey has some awesome songs!")
# Part 1.2 - Draw a plane and a dog
print("    __!__")
print("_____(_)_____")
print("   !  !  !")
print("")
print("^..^      /")
print("/_/\\_____/")
print("  /\\   /\\")
# Practice - Draw
print("")
print("   |")
print(" .'|'.")
print("/.'|\\ \\")
print("| /|'.|")
print(" \\ |\\/")
print("  \\|/")
print("   `")

# Part 2 - Learn about Strings
name = "John"
age = "36"
favorite_color = "green"
print(name)
print(age)
print(favorite_color)
print(name + " is " + age + " years old")
print(name + "'s favorite color is " + favorite_color)
print(name.upper())
print(name.lower())
first_name = "Bob"
last_name = "Roger"
full_name = first_name + " " + last_name
print(full_name)

# Part 3 - Project: Letter to the Future
career = "Software Engineer"
goal1 = "climb mount everest"
goal2 = "become a great chef"
goal3 = "learn scuba diving"
accomplishment1 = "won first place in a marathon"
accomplishment2 = "traveled to 30 different countries"
print("Dear future me,")
print("")
print("I hope that when you look back on this letter you will be having a successful life as a " + career + ".")
print("As of the me right now I want to " + goal1 + ", " + goal2 + ", and " + goal3 + ".")
print("I hope the you of the future have reached those goals.")
print("My dream accomplishments would be to have " + accomplishment1 + " and " + accomplishment2 + ".")
print("If you did all that, then you made my dreams come true")

# Part 4 - Project: Shopping Cart
meats = "Turkey Slices, Pepperoni, Chicken Wings"
vegetables = "Carrots, Broccoli, Lettuce, Cabbage"
snacks = "Chocolate Chip cookies, Fruit Snacks, Ice Cream"
items = "Colored Pencils, Notebooks, Rulers"
print("Don't forget to buy everything from the grocery store!")
print("We need 3 meats, " + meats + ".")
print("We need 4 vegetables, " + vegetables + ".")
print("Also get 3 snacks, " + snacks + ".")
print("And finally don't forget about " + items)

# Part 5 - Project: Mad Libs
noun1 = "Dog"
noun2 = "Donut"
noun3 = "Football"
adjective1 = "Crazy"
adjective2 = "Sparkly"
adjective3 = "Funny"

print("The " + adjective1 + " " + noun1 + " thought the " +
      adjective2 + " " + noun3 + " was a " + noun2 +
      " and accidentally tried to eat it! We laughed out loud because it was so " +
      adjective3 + "!")
