# This is for dialogue shortcuts

define a = Character("Alex")
define s = Character("Sebastian")
define c = Character("Calvin", color="#33FFCC")
define y = Character("Yaseen")
define j = Character("Sam")
define m = Character("Me")

# This is for variables as needed

default day = 0

# This is where the game starts. Feel free to edit your lines as needed.

label start:
    "You find yourself walking to GITC 3700, to attend your first IGDA general body meeting!"
    "As a new transfer student, you worry that it'll be hard to find a fun and exciting club that will accept you."
    "Despite this, you muster the courage to step into the large room that lay right in front of you."

    # Edit this part to say what y'all want.
    "???" "Hello everybody, welcome to the first meeting of IGDA in the spring semester!"
    a "My name is Alex and remarkably I'm still  your president."
    a "Goons. Introduce yourselves."
    s "I am Sebastian."
    c "I am Calvin."
    y "I am Yaseen."
    s "I am Sam."

    "You are instantly enamored (platonically) with these absolute buffoons of an eboard council."

    m "I guess I should try to get to know them better so I can get a better understanding of the club culture."

    "You sit through a whole meeting listening about these 'game jams' and 'Renpy' things."

    "After the meeting ends, you decide to look at their Discord profiles and see who's available to hang out."
    
    jump checkDay

    return

# Each day will have different eboard members available to spend the day with.

label checkDay:
    $ day += 1
    if day == 1:
        jump pickSomeoneDay1
    elif day == 2:
        jump pickSomeoneDay2
    elif day == 3:
        jump pickSomeoneDay3
    elif day == 4:
        jump pickSomeoneDay4
    elif day == 5:
        jump pickSomeoneDay5
    else:
        jump finalDay


label pickSomeoneDay1:
    menu:
        "Who should I hit up today?"
        "Calvin":
            "I decide to DM Calvin."
            jump cal
        "Sam":
            "I decide to search for Sam."
            jump sam
        "Sebastian":
            "I decide to call up Sebastian."
            jump seb
        "Alex":
            "I decide to visit Alex."
            jump ale
        "Test":
            "I decide to test the code."
            jump test

    return

label pickSomeoneDay2:
    menu:
        "Who should I hit up today?"
        "Calvin":
            "I decide to DM Calvin."
            jump cal
        "Alex":
            "I decide to visit Alex."
            jump ale
        "Test":
            "I decide to test the code."
            jump test

    return

label pickSomeoneDay3:
    menu:
        "Who should I hit up today?"
        "Sam":
            "I decide to search for Sam."
            jump sam
        "Yaseen":
            "I decide to find Yaseen."
            jump yas
        "Alex":
            "I decide to visit Alex."
            jump ale
        "Test":
            "I decide to test the code."
            jump test

    return

label pickSomeoneDay4:
    menu:
        "Who should I hit up today?"
        "Sam":
            "I decide to search for Sam."
            jump sam
        "Sebastian":
            "I decide to call up Sebastian."
            jump seb
        "Alex":
            "I decide to visit Alex."
            jump ale
        "Test":
            "I decide to test the code."
            jump test

    return

label pickSomeoneDay5:
    menu:
        "Who should I hit up today?"
        "Calvin":
            "I decide to DM Calvin."
            jump cal
        "Sebastian":
            "I decide to call up Sebastian."
            jump seb
        "Yaseen":
            "I decide to find Yaseen."
            jump yas
        "Alex":
            "I decide to visit Alex."
            jump ale
        "Test":
            "I decide to test the code."
            jump test

    return

label finalDay:
    # This will go through each member and sequentially show your respective endings. I'll fix the ordering later.
    jump testEnding

    return