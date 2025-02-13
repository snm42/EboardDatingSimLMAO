default samDaysPicked = 0

label sam:
    $ samDaysPicked += 1
    if samDaysPicked == 1:
        jump samDay1
    elif samDaysPicked == 2:
        jump samDay2
    else:
        jump samDay3

label samDay1:
    # Go to campus and get food.

    # Ending 1 - Taco bell
    # you accidentally say taco bell is mid and sam ghosts you forever

    j "goon 1"
    $ renpy.movie_cutscene("images/important.webm")
    "gooon"

    jump checkDay

label samDay2:
    # Plan out a full frontal assault on GDS (library breakout room)
    "goon 2"

    # Ending 2 - Snitch on Sam
    # Locks out of visiting for the rest of the days
    # Sam is forcibly removed from the library.
    
    jump checkDay

label samDay3:
    # Fight against public safety (club penguin card-jitsu)
    "goon 3"

    # Ending 3 - Sam dies

    # Ending 4 - Sam lives
    jump checkDay

label samEnding:
    # If sam dead, visit gravestone
    # If sam alive, he gets assassinated
    jump checkDay