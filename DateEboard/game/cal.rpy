screen my_keys():
    #Dismiss keys
    key "K_ESCAPE" action NullAction()
    key "mouseup_3" action NullAction()
    key "mousedown_4" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()   
    key "any_K_PAGEUP" action NullAction()  

define c = Character("Calvin", color="00ffc1")

define watched = ""

define reel = 0

define count = 0

define liked = 1

define score = 0

define skipamt = 0

define quizscore = 0

define likes = {
    "images/reel1.webm": 0,
    "images/reel2.webm": 1,
    "images/reel3.webm": 1,
    "images/reel4.webm": 1,
    "images/reel5.webm": 1,
    "images/reel6.webm": 1,
    "images/reel7.webm": 1,
    "images/reel8.webm": 1,
    "images/reel9.webm": 1,
    "images/reel10.webm": 0,
    "images/reel11.webm": 0,
    "images/reel12.webm": 0,
    "images/reel13.webm": 1,
    "images/reel14.webm": 1,
    "images/reel15.webm": 1,
    "images/reel16.webm": 1,
    "images/reel17.webm": 1,
    "images/reel18.webm": 1,
    "images/reel19.webm": 1,
    "images/reel20.webm": 0,
    "images/reel21.webm": 1,
    "images/reel22.webm": 1,
    "images/reel23.webm": 0,
    "images/reel24.webm": 1,
    "images/reel25.webm": 1,
    "images/reel26.webm": 1,
    "images/reel27.webm": 1,
    "images/reel28.webm": 1,
    "images/reel29.webm": 1,
    "images/reel30.webm": 0,
    "images/reel31.webm": 0,
    "images/reel32.webm": 1,
    "images/reel33.webm": 1,
    "images/reel34.webm": 1,
    "images/reel35.webm": 0,
    "images/reel36.webm": 0,
    "images/reel37.webm": 0,
    "images/reel38.webm": 1,
    "images/reel39.webm": 0,
    "images/reel40.webm": 0,
    "images/reel41.webm": 0,
    "images/reel42.webm": 0,
    "images/reel43.webm": 1,
    "images/reel44.webm": 0,
    "images/reel45.webm": 1,
}

define stopguess = 0

define stopout = 0

define stopmore = False

define silence = 0

label cal1:
    scene dorm 
    show cal neutral at left 
    with dissolve

    c "yo. how's it going?"

    c "i was just scrolling on social media, wanna watch some with me?"

    menu:
        "Yeah sure!":
            jump reelstart

        "Uhhh no thanks.":
            jump fuckyou

label reelstart:

    show cal phone hold at left

    c "alright! here's the first one."

    show cal phone show at center
    with move

    c "i hope you like it!"

    jump reels

label reels:
    while count < 45:
        $ reel = "images/reel" + str(renpy.random.randint(1, 45)) + ".webm"
        while reel in watched:
            $ reel = "images/reel" + str(renpy.random.randint(1, 45)) + ".webm"

        if renpy.movie_cutscene(reel):
            $ skipamt = skipamt + 1
            show cal forwards
            if skipamt < 3:
                c "why'd you do that."
                c "don't skip the videos."

                show cal phone show

                c "pay attention."
            else:
                window hide
                pause
                show cal forwards at truecenter:
                    ease 0.2 zoom 5 yalign 0.25
                window hide
                $ quick_menu = False
                pause

                c "get out."
                return



            jump reels
        
        $ watched = watched + reel

        show cal phone hold at center

        c "did you like that one?"

        menu:
            "yeah!":
                $ liked = 1
                c "interesting."

            "no...":
                $ liked = 0
                c "interesting."
            
        if liked == likes[reel]:
            $ score = score + 1
        
        show cal phone show at center

        c "alright, here is the next one."
        
        $ count = count + 1

    c "aw my phone died..."

    show cal neutral at center

    c "oh well, thanks for hanging out with me."

    if score >= 36:
        c "you've got a good sense of humor."
        c "i'm glad you enjoyed them."
        c "let's add eachother on IGsDAgram later!"

        show cal up at center

        c "alright, i'll see you around!"

    elif score < 36:
        c "you've got a weird taste in videos..."
        c "please get a better sense of humor."

        c "see ya."


    return


label fuckyou:

    c "um..."

    c "i don't really have any other ideas..."

    c "please leave."

return

label cal:
    scene dorm
    show cal neutral at left
    with dissolve

    c "good to see you again!"

    show cal think at center
    with move

    c "guess what we are gonna do today..."
    

    menu guess:
        "I don't know, what?":

            if stopguess > 3:
                c "thats it."

                c "GET OUUUUUUUUT!"
                show cal forwards at truecenter:
                    ease 0.2 zoom 5 yalign 0.25
                window hide
                $ quick_menu = False
                $ renpy.pause(delay=0.01)
                return

            show cal forwards 
            c "i said guess."
            show cal neutral 
            $ stopguess += 1
            jump guess
        
        "Are we gonna go somewhere?":
            if stopout == 1:
                jump circus
                
            show cal down 
            c "nope!"
            c "try again!"
            show cal neutral 

            $ stopout = 1
            jump guess

        "More videos?":
            show cal neutral
            if stopmore:
                jump circus
            c "no."
            c "i mean unless you want to i guess."
            $ stopmore = True
            menu:
                "i want to rewind time":
                    c "its your playthrough i guess..."
                    show cal phone hold at left 
                    with ease
                    jump reelstart
                "nah i'm good.":
                    c "alright, then guess again!"
                    jump guess
                


        "Is it quiz time?":
            show cal up 
            c "that's right!"
            show cal neutral at left
            with ease
            jump cal22

        "*remain silent*":
            show cal neutral
            $ silence += 1
            $ quick_menu = False
            show screen my_keys
            $ renpy.pause(delay=2*silence,hard=True)
            show cal forwards
            $ renpy.pause(delay=2*silence,hard=True)
            show cal neutral
            hide screen my_keys
            jump guess

label circus:
    show cal forwards
    c "you know what you did."
    c "suffer."
    play music "circus.mp3"
    window hide
    scene clown
    $ quick_menu = False
    show screen my_keys
    show cal forwards at truecenter:
        ease 154 zoom 5 yalign 0.3
    $ renpy.pause(delay=154,hard=True)
    hide screen my_keys



label cal22:
    
    c "let's season this place up a bit shall we?"

    show stage behind cal
    with slidedown
    show mic at left with moveinleft
    
    c "alright! first question:"

    show cal think
    show screen my_keys
    $ quick_menu = False

    c "what was the name of the homeless man's special technique?"
    menu:
        "Purple Hollow":
            show cal down
            c "WRONG!"
        "Magenta Marrow":
            show cal down
            c "WRONG!"
        "Pink Emptiness":
            show cal up
            c "CORRECT!"
            $ quizscore += 1 
        "Pink Nothingness":
            show cal down
            c "WRONG!"

    show cal think
    
    c "how long do you need to stay in seben eleben simulator to hear miku?"
    $ answer = renpy.input("how many minutes do you need to stay in seben eleben simulator to hear miku?",allow="0123456789")

    if answer == "120":
        c "CORRECT!"
        show cal up
    else:
        c "WRONG!"
        show cal down

    c ""


    return