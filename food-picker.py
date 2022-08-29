# Food/Recipe Picker

choice = input("You tryna make food or get food? m/g")
if choice == 'g':
    type = input("So, then, are you looking for something healthy or not? h/n")
    if type == 'h':
        print("Your choices are Chipotle or Bibibop. Take it or leave it.")

    if type == 'n':
        type = input("You want a burger, chicken, or tacos? b/c/t")
        if type == 'b':
            print("Okay, Swenson's, Wendy's, or McDonalds?")
        elif type == 'c':
            print("Popeye's or Chic Fil A?")
        elif type == 't':
            print("So, you're going to Taco Bell.")

elif choice == 'm':
    genre = input("Do you want something fast or slow?")
    if genre == 'f':
        print("Sounds to me like you want Kimchi Toast or Gyudon.")
    elif genre == 's':
        food = input("Do you want to eat Korean, Japanese, or Chinese food?")
        if food == 'k':
            print("You want tteokbokki or korean fried chicken?")
        elif food == 'j':
            print("So, we thining of like sushi or something like gyudon?")
        elif food == 'c':
            print("Let's try making some dumplings then!")