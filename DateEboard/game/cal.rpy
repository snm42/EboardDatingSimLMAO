init python:
    import random


screen my_keys():
    #Dismiss keys
    key "K_ESCAPE" action NullAction()
    key "mouseup_3" action NullAction()
    key "mousedown_4" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()   
    key "any_K_PAGEUP" action NullAction()  


define watched = ""

define reel = 0

define count = 0

define liked = 1

define score = 0

define skipamt = 0

define right = False

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

define randonext = [
    "alright, next question.",
    "next question...",
    "okay, next one.",
    "let's see if you can get this one...",
    "this next one should be free.",
    "ooooh this one is hard...",
    "surely you'll know this next one.",
    "next.",
    "hmmm...what to ask next...",
    "uhhhhhhhhhhhhhhhhh",
    "the next equestion is obvious.",
    "next question.",
    "let us proceed to the following question.",
    "let us proceed.",
    "lets get to the next one.",
]

define calDaysPicked = 0

define wrongs = 0


label cal:
    $ calDaysPicked +=1
    if calDaysPicked == 1:
        jump calDay1
    if calDaysPicked == 2:
        jump calDay2
    if calDaysPicked == 3:
        jump calDay3


label calDay1:
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
        $ reel = "images/reel" + str(random.randint(1, 45)) + ".webm"
        while reel in watched:
            $ reel = "images/reel" + str(random.randint(1, 45)) + ".webm"

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
                jump checkDay




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


    jump checkDay


label fuckyou:

    c "um..."

    c "i don't really have any other ideas..."

    c "please leave."

    jump checkDay

label calDay2:
    scene dorm
    show calb neutral happy at left
    with dissolve

    c "good to see you again!"

    show calb think at center
    with move

    c "guess what we are gonna do today..."
    

    menu guess:
        "I don't know, what?":

            if stopguess > 3:
                show calb neutral mad
                c "thats it."

                c "GET OUUUUUUUUT!"
                show calb forwards at truecenter:
                    ease 0.2 zoom 5 yalign 0.25
                window hide
                $ quick_menu = False
                $ renpy.pause(delay=0.01)
                jump checkDay

            show calb forwards 
            c "i said guess."
            show calb neutral 
            $ stopguess += 1
            jump guess
        
        "Are we gonna go somewhere?":
            if stopout == 1:
                jump circus
                
            show calb down 
            c "nope!"
            c "try again!"
            show calb neutral 

            $ stopout = 1
            jump guess

        "More videos?":
            show calb neutral
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
            show calb up 
            c "that's right!"
            show calb neutral happy
            with ease
            jump cal22

        "*remain silent*":
            show calb neutral
            $ silence += 1
            $ quick_menu = False
            show screen my_keys
            $ renpy.pause(delay=2*silence,hard=True)
            show calb forwards
            $ renpy.pause(delay=2*silence,hard=True)
            show calb neutral
            hide screen my_keys
            jump guess

label circus:
    show calb forwards
    c "you know what you did."
    c "suffer."
    play music "circus.mp3"
    window hide
    scene clown
    $ quick_menu = False
    show screen my_keys
    show calb forwards at truecenter:
        ease 154 zoom 5 yalign 0.3
    $ renpy.pause(delay=154,hard=True)
    hide screen my_keys
    jump checkDay



label cal22:
    
    c "let's season this place up a bit shall we?"

    show stage behind calb
    with slidedown
    show mic at left with moveinleft

    c "oh yeah, no save scumming for you!"

    show screen my_keys
    $ quick_menu = False
    
    # list of all possible questions
    # it consist of dictionaries, that describe each question:
    # key "question" has value of a question, key "category" makes sense for bot, key "answer" is a list of answers, that are lists [answer itself, right/wrong]
    # the order of this keys is not matter
    $ q_list = [
    {"question": "who is in seben eleben?",
    "type": "multi",
    "answer": [ ["Miku", "right"], ["teto", "wrong"], ["Cashier", "wrong"], ["Homeless Guy", "wrong"] ]}, 

    {"question": "what is the name of the Homeless Guy's technique?",
    "type": "multi",
    "answer": [ ["Pink Emptiness", "right"], ["Purple Hollow", "wrong"], ["Magenta Marrow", "wrong"], ["Pink Nothingness", "wrong"] ]}, 

    {"question": "about how many minutes do you need to stay to hear miku in seben eleben simulator?",
    "type": "enter",
    "answer": [ ["2", "right"]]},


    ]
   
    # game variables
    #####
    

    $ wrong_answers = 0     # amount of wrong answers
    $ quiz_length = 3       # number of questions in one game
    $ q_to_ask = []         # list of questions to ask in one game
   
    # let's choose some questions to play with
    while len(q_to_ask) < quiz_length:        # will work until we'll get enough questions for quiz
        $ a = random.choice(q_list)    # randomly pick a question from a list of all questions
        if a not in q_to_ask:                 # this question will be added only if we don't have it yet
            $ q_to_ask.append(a)

    label quize_game:                             # game loop
        if -1 <= wrong_answers <= 1:
            show calb neutral
        elif wrong_answers < -1:
            show calb neutral happy
        elif wrong_answers > 3:
            show calb forwards
        elif wrong_answers > 1:
            show calb neutral mad


        $ a = random.choice(q_to_ask)      # randomly pick the question from a list
        $ q_to_ask.remove(a)                     # remove it from list to not to ask it twice
        
        # ugly part... next variables are necessary to fill menu
        $ question = a["question"]

        c "[question]"
        if a["type"] == "multi":
            $ huh = [0,1,2,3]
            $ random.shuffle(huh)
            $ answ_0 = a["answer"][huh[0]][0]
            $ answ_1 = a["answer"][huh[1]][0]
            $ answ_2 = a["answer"][huh[2]][0]
            $ answ_3 = a["answer"][huh[3]][0]

            $ cor_1 = a["answer"][huh[0]][1]
            $ cor_2 = a["answer"][huh[1]][1]
            $ cor_3 = a["answer"][huh[2]][1]
            $ cor_4 = a["answer"][huh[3]][1]
            jump multi

        else:
            jump type
    
        menu multi:
            c "[question]"
            "[answ_0][cor_1]":
                if a["answer"][huh[0]][1] == "right":
                    show calb up        # checks the description of question if it's the right one
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
            "[answ_1][cor_2]":
                if a["answer"][huh[1]][1]  == "right":
                    show calb up 
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
            "[answ_2][cor_3]":
                if a["answer"][huh[2]][1]  == "right":
                    show calb up 
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
            "[answ_3][cor_4]":
                if a["answer"][huh[3]][1]  == "right":
                    show calb up 
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1


        $ quiz_length -= 1
        if quiz_length > 0:
            jump quize_game
        else:
            jump quizEND

        label type:
            if quiz_length <= 0:
                jump quizEND
            c "[question]"
            $ typed = renpy.input("[question]",allow="0123456789")
            if typed == a["answer"][0][0]:
                show calb up 
                "CORRECT!"
                $ wrong_answers -=1
            else:
                show calb down
                "WRONG!"
                $ wrong_answers +=1
            $ quiz_length -= 1
            if quiz_length > 0:     
                jump quize_game


    label quizEND:
        c "wow, you made it!"
        c "you really are a true calvin fan."
   
    $ quick_menu = True
    hide screen my_keys
    jump checkDay