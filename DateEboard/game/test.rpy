# Variable that keeps track of how many times this route has been selected.

default testDaysPicked = 0

# Label that sends you to each person's script file.

label test:
    # Increment the tracking variable and send to corresponding day label
    $ testDaysPicked += 1
    if testDaysPicked == 1:
        jump testDay1
    elif testDaysPicked == 2:
        jump testDay2
    elif testDaysPicked == 3:
        jump testDay3
    elif testDaysPicked == 4:
        jump testDay4
    else:
        jump testDay5

# Each of the labels for each of the days, ends with 'jump checkDay' to return back to main script.

label testDay1:
    $ renpy.movie_cutscene("images/important.webm")
    jump checkDay

label testDay2:
    $ renpy.movie_cutscene("images/important.webm")
    jump checkDay

label testDay3:
    $ renpy.movie_cutscene("images/important.webm")
    jump checkDay

label testDay4:
    $ renpy.movie_cutscene("images/important.webm")
    jump checkDay

label testDay5:
    $ renpy.movie_cutscene("images/important.webm")
    jump checkDay


# Ending, should jump directly to next person's ending as we implement those.

label testEnding:
    "End"
    return
