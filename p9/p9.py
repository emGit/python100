from util import macro

def start():
    # p0()
    # p1()
    # p2()
    # p3()
    p4()

def p0():
    macro.moduleStart("")
    empty = {}
    programming_dictionary = {}

    ##Python Dictionaries
    programming_dictionary = {"Bug":"An error in a program that prevents the program from running as expected.", "Function":"A piece of code that you can easily call over and over again.", "Loop":"The action of doing something over and over again."}

    # Retrieving items from dictionary.
    # print(programming_dictionary["Function"])

    # Adding new items to dictionary.
    # Create an empty dictionary.
    empty_dictionary = {}

    # Wipe an existing dictionary
    # programming_dictionary = {}
    # print(programming_dictionary)

    # Edit an item in a dictionary
    programming_dictionary["Bug"] = "A moth in your computer."
    print(programming_dictionary)

    # Loop through a dictionary
    # for key in programming_dictionary:
    #   print(key)
    #   print(programming_dictionary[key])

def p1():
    macro.moduleStart("")
    student_scores = {
        "Harry":81,
        "Ron":78,
        "Hermione":99,
        "Draco":74,
        "Neville":62,
    }
    # 🚨 Don't change the code above 👆
    # TODO-1: Create an empty dictionary called student_grades.
    student_grades = {}

    # TODO-2: Write your code below to add the grades to student_grades.👇
    for i in student_scores:
        score = student_scores[i]
        if score > 90: student_grades[i] = "Outstanding"
        elif score > 80: student_grades[i] = "Exceeds Expectations"
        elif score > 70: student_grades[i] = "Acceptable"
        else: student_grades[i] = "Fail"
        # 🚨 Don't change the code below 👇
    print(student_grades)

def p2():
    macro.moduleStart("Nesting")
    # Nesting
    capitals = {
        "France":"Paris",
        "Germany":"Berlin",
    }

    # Nesting a List in a Dictionary
    travel_log = {
        "France":["Paris", "Lille", "Dijon"],
        "Germany":["Berlin", "Hamburg", "Stuttgart"],
    }

    # Nesting Dictionary in a Dictionary
    travel_log = {
        "France":{"cities_visited":["Paris", "Lille", "Dijon"], "total_visits":12},
        "Germany":{"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits":5},
    }

    # Nesting Dictionaries in Lists
    travel_log = [
        {
            "country":"France",
            "cities_visited":["Paris", "Lille", "Dijon"],
            "total_visits":12,
        },
        {
            "country":"Germany",
            "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
            "total_visits":5,
        },
    ]

def p3():
    macro.moduleStart("")
    travel_log = [
        {
            "country":"France",
            "visits":12,
            "cities":["Paris", "Lille", "Dijon"]
        },
        {
            "country":"Germany",
            "visits":5,
            "cities":["Berlin", "Hamburg", "Stuttgart"]
        },
    ]

    # 🚨 Do NOT change the code above

    # TODO: Write the function that will allow new countries
    # to be added to the travel_log. 👇
    def add_new_country(country, visits, cities):
        travel_log.append({"country":country, "visits":visits, "cities":cities})

    # 🚨 Do not change the code below
    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
    print(travel_log)

def p4():
    macro.moduleStart("Auction")
    import art
    print(art.logo)
    bids = {}
    while input("Any more bids? Type 'yes' or 'no'. ") == "yes":
        bids[input("What is your name?: ")] = input("What will you pay?: $")
    else:
        winner = "Null"
        high_bid = 0
        for i in bids:
            new_bid = int(bids[i])
            if new_bid > high_bid:
                winner = i
                high_bid = new_bid
        print(f"The winner is {winner}, with a bid of {high_bid}!")

start()