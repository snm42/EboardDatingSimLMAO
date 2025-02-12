# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    menu:
        "Calvin":
            jump cal
        "Sam":
            jump sam
        "Sebastian":
            jump seb
        "Yaseen":
            jump yas
        "Alex":
            jump ale

    return
