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
    key "K_TAB" action NullAction()  
    key "K_LCTRL" action NullAction()
    key "K_RCTRL" action NullAction()


define watched = ""

define reel = 0

define count = 0

define liked = 1

define score = 0

define skipamt = 0

define mood = 0

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

define nexttext = 0

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.1 xmaximum 300 at alpha_dissolve # This is the timer bar.

init:
    $ timer_range = 0
    $ timer_jump = 0

# time = the time the timer takes to count down to 0.
# timer_range = a number matching time (bar only)
# timer_jump = the label to jump to when time runs out

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
                $ quick_menu = False
                show screen my_keys
                window hide
                pause
                show cal forwards at truecenter:
                    ease 0.2 zoom 5 yalign 0.25
                window hide
                pause
                c "get out."
                $ mood = 1
                hide screen my_keys
                $ quick_menu = True
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

    show cal horrified

    c "NOO MY PHONE DIED!"

    show cal neutral at center

    c "oh well, thanks for hanging out with me."

    if score >= 36:
        c "you've got a good sense of humor."
        c "i'm glad you enjoyed them."
        c "let's add eachother on IGsDAgram next time!"

        show cal up at center

        c "alright, i'll see you around!"

    elif score < 36:
        c "you've got a weird taste in videos..."
        c "please get a better sense of humor."

        c "see ya."
        $ mood = 1


    jump checkDay


label fuckyou:

    c "um..."

    c "i don't really have any other ideas..."

    c "please leave."

    $ mood = 1

    jump checkDay

label calDay2:
    scene dorm

    if mood == 0:
        show calb neutral happy at left
        with dissolve
        c "good to see you again!"
        
        show calb think at center
        with move
        c "guess what we are gonna do today..." 
    else:
        show calb neutral mad at left
        with dissolve
        c "yo."
        c "i'm surprised you asked to hang again."
        c "i'm gonna give you another chance to redeem yourself."
        show calb neutral mad at center
        with move
        c "try to guess what we are doing today."
    

    

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
            $ quick_menu = True
            jump guess

label circus:
    $ quick_menu = False
    show screen my_keys
    show calb forwards
    c "you know what you did."
    c "suffer."
    play music "circus.mp3"
    window hide
    scene clown
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

    show screen my_keys
    $ quick_menu = False

    c "oh yeah, no save scumming or pausing for you!"

    c "i hope you got something to take notes on, because you only have 10 seconds to answer each question."

    c "lets get this party started."
    
    # list of all possible questions
    # it consist of dictionaries, that describe each question:
    # key "question" has value of a question, key "category" makes sense for bot, key "answer" is a list of answers, that are lists [answer itself, right/wrong]
    # the order of this keys is not matter
    $ q_list = [
    {"question": "who is in seben eleben?",
    "type": "multi",
    "answer": [ ["Miku", "right"], ["Teto", "wrong"], ["Cashier", "wrong"], ["Homeless Guy", "wrong"] ]}, 

    {"question": "what is the name of the Homeless Guy's technique?",
    "type": "multi",
    "answer": [ ["Pink Emptiness", "right"], ["Purple Hollow", "wrong"], ["Magenta Marrow", "wrong"], ["Pink Nothingness", "wrong"] ]}, 

    {"question": "about how many minutes do you need to stay to hear miku in seben eleben simulator?",
    "type": "enter",
    "answer": [ ["2", "right"]]},

    {"question": "what is the 7th game that i have made?",
    "type": "multi",
    "answer": [ ["igbl", "right"], ["igdl", "wrong"], ["Skybeam+", "wrong"], ["Petit Dej", "wrong"] ]},

    {"question": "how many endings does Petit Dej have?",
    "type": "enter",
    "answer": [ ["3", "right"]]},

    {"question": "who is the fifth character in GIVE THANKS?",
    "type": "multi",
    "answer": [ ["Engineer", "right"], ["Alex", "wrong"], ["Miku", "wrong"], ["Sebastian", "wrong"] ]},

    {"question": "what is the amount of french men in FRANCE DEFANCE?",
    "type": "type",
    "answer": [ ["4", "right"]]},

    {"question": "who is June's husband?",
    "type": "multi",
    "answer": [ ["Mark", "right"], ["Me", "wrong"], ["Mars", "wrong"], ["Jake", "wrong"] ]},

    {"question": "what is June looking for?",
    "type": "multi",
    "answer": [ ["Ummagumma", "right"], ["Pink Floyd", "wrong"], ["Love", "wrong"], ["A CD", "wrong"] ]},

    {"question": "what is the 3rd ending called in The Quest for Ummagumma?",
    "type": "multi",
    "answer": [ ["Touch Grass", "right"], ["Gave Up", "wrong"], ["Parry", "wrong"], ["Bad", "wrong"] ]},

    {"question": "which line is at the top of igbl's 1st minigame?",
    "type": "multi",
    "answer": [ ["FINISH THE ESSAY!!!!", "right"], ["FINISH THE ESSAY!!!", "wrong"], ["FEED YOURSELF!!!", "wrong"], ["FEED YOURSLEF!!!", "wrong"] ]},

    {"question": 'how is "coffee" spelled in Bad Barista?',
    "type": "multi",
    "answer": [ ["coughee", "right"], ["cofee", "wrong"], ["koughee", "wrong"], ["cuofee", "wrong"] ]},

    {"question": 'which game jam was "im really thirsty." made for?',
    "type": "multi",
    "answer": [ ["GMTK", "right"], ["Global Game Jam", "wrong"], ["October Game Jam", "wrong"], ["Godot Plug n Play", "wrong"] ]},

    {"question": 'why is the cashier present in "im really constructive."?',
    "type": "multi",
    "answer": [ ["he needs a side job.", "right"], ["it is a sequel to im really thirsty.", "wrong"], ["he likes construction.", "wrong"], ["he wanted to get another job.", "wrong"] ]},

    {"question": 'why does bobl need access to your mic?',
    "type": "multi",
    "answer": [ ["to blow it away.", "right"], ["to record you.", "wrong"], ["to blow the bobl.", "wrong"], ["to pop the bobl.", "wrong"] ]},

    {"question": "what's the difference between Skybeam and Skybeam+?",
    "type": "multi",
    "answer": [ ["A day/night cycle.", "right"], ["new poem mechanics.", "wrong"], ["10 new poems.", "wrong"], ["less grass.", "wrong"] ]},
    ]
   
    # game variables
    #####
    

    $ wrong_answers = 0     # amount of wrong answers
    $ quiz_length = 3       # number of questions in one game
    $ q_to_ask = []         # list of questions to ask in one game

    $ time = 10
    $ timer_range = 10
    $ timer_jump = 'loser'
    
   
    # let's choose some questions to play with
    while len(q_to_ask) < quiz_length:        # will work until we'll get enough questions for quiz
        $ a = random.choice(q_list)    # randomly pick a question from a list of all questions
        if a not in q_to_ask:                 # this question will be added only if we don't have it yet
            $ q_to_ask.append(a)

    label quize_game:                             # game loop

        $ a = random.choice(q_to_ask)      # randomly pick the question from a list
        $ q_to_ask.remove(a)                     # remove it from list to not to ask it twice
        
        # ugly part... next variables are necessary to fill menu
        $ question = a["question"]

        show calb mic 
        show screen countdown
        if a["type"] == "multi":
            $ huh = [0,1,2,3]
            $ random.shuffle(huh)
            $ answ_0 = a["answer"][huh[0]][0]
            $ answ_1 = a["answer"][huh[1]][0]
            $ answ_2 = a["answer"][huh[2]][0]
            $ answ_3 = a["answer"][huh[3]][0]
            jump multi

        else:
            jump type


        menu multi:
            c "[question]"
            "[answ_0]":
                if a["answer"][huh[0]][1] == "right":
                    $ time += 5
                    show calb up        
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    $ time += 2
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
            "[answ_1]":
                if a["answer"][huh[1]][1]  == "right":
                    $ time += 5
                    show calb up 
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    $ time += 2
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
            "[answ_2]":
                if a["answer"][huh[2]][1]  == "right":
                    $ time += 5
                    show calb up 
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    $ time += 2
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
            "[answ_3]":
                if a["answer"][huh[3]][1]  == "right":
                    $ time += 5
                    show calb up 
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    $ time += 2
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1

        $ quiz_length -= 1
        if -1 <= wrong_answers <= 1:
            show calb neutral
        elif wrong_answers < -1:
            show calb neutral happy
        elif wrong_answers > 3:
            show calb forwards
            hide screen countdown
            pause
            jump loser
        elif wrong_answers > 1:
            show calb neutral mad
        if quiz_length > 0:
            $ nexttext = random.choice(randonext)

            c "[nexttext]"
            jump quize_game
        else:
            jump quizEND

        

        label type:
            if quiz_length <= 0:
                jump quizEND
            c "[question]"
            $ typed = renpy.input("[question]",allow="0123456789")
            if typed == a["answer"][0][0]:
                $ time += 5
                show calb up 
                "CORRECT!"
                $ wrong_answers -=1
            else:
                $ time += 2
                show calb down
                "WRONG!"
                $ wrong_answers +=1
            $ quiz_length -= 1
            if -1 <= wrong_answers <= 1:
                show calb neutral
            elif wrong_answers < -1:
                show calb neutral happy
            elif wrong_answers > 3:
                show calb forwards
                hide screen countdown
                pause
                jump loser
            elif wrong_answers > 1:
                show calb neutral mad
            if quiz_length > 0:     
                $ nexttext = random.choice(randonext)
                c "[nexttext]"
                jump quize_game
            else:
                jump quizEND


    label quizEND:
        hide screen countdown
        show calb neutral happy
        c "wow, you made it!"
        c "you really are a true calvin fan."

        hide screen my_keys
        $ quick_menu = True
        jump checkDay


    label loser:
        show calb neutral mad
        c "..."
        c ""
        hide screen my_keys
        $ quick_menu = True
        jump checkDay
   
    $ quick_menu = True
    hide screen my_keys
    jump checkDay

