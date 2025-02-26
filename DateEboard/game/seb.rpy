default sebDaysPicked = 0

screen samplescreen:
    frame:
        xpadding 40
        ypadding 40
        xalign 0.5
        yalign 0.5
        text "this text is in the middle" yalign 0.5 xalign 0.5

label seb:
    $ sebDaysPicked += 1
    if sebDaysPicked == 1:
        jump sebDay1
    elif sebDaysPicked == 2:
        jump sebDay2
    else:
        jump sebDay3

label sebDay1:
    s "Let's play tribal hunters!"
    call screen samplescreen
    jump checkDay

label sebDay2:
    s "Let's play uhh"
    jump checkDay

label sebDay3:
    s "What it's like to be drank"
    jump checkDay