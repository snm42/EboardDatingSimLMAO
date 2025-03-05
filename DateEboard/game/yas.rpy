default yasDaysPicked = 0
label yas:
    $ yasDaysPicked += 1
    if yasDaysPicked == 1:
        jump yasDay1
    elif yasDaysPicked == 2:
        "You can't seem to get that car crash out of your head quite yet."
        "Maybe it's better to not try and see his grave."
        jump checkDay
label yasDay1:
    play music "Kevin MacLeod - Crossing the Divide.mp3"
    scene honorfront
    "..."
    "???" "Hello!"

    show yas neutral
    "You turn to see Yaseen heading towards you."

    y "How are you doing?"
    y "I was just playing some Monster Hunter with my friends."
    y "Honestly, I thi-"
    show yas shock
    y "Oh shit is that a car?!"
    play sound "car accident.mp3"
    hide yas
    "..."
    "..."
    "..."
    "You see Yaseen, lying dead on the floor."
    "Another casuality of the honors crosswalk."
    "..."
    m "Rest in peace."
    jump checkDay