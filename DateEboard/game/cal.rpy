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
    "images/reel1.webm": 1,
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
    "images/reel46.webm": 1,
    "images/reel47.webm": 1,
    "images/reel48.webm": 1,
    "images/reel49.webm": 0,
    "images/reel50.webm": 1,
    "images/reel51.webm": 0,
    "images/reel52.webm": 0,
    "images/reel53.webm": 1,
    "images/reel54.webm": 1,
    "images/reel55.webm": 0,
    "images/reel56.webm": 1,
    "images/reel57.webm": 1,
    "images/reel58.webm": 1,
    "images/reel59.webm": 0,
    "images/reel60.webm": 1,
    "images/reel61.webm": 0,
    "images/reel62.webm": 0,
    "images/reel63.webm": 1,
    "images/reel64.webm": 1,
}

define stopguess = 0

define stopout = 0

define stopmore = False

define silence = 0.0

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
    "the next question is obvious.",
    "next question.",
    "let us proceed to the following question.",
    "let us proceed.",
    "let's get to the next one.",
    "hrmmmmm...",
    "this one is quite simple.",
    "if you don't know this one, then you're just stupid.",
    "i don't know if you can get this one...",
    "NEXT QUESTION!",
    "please get this one right.",
    "if you get this next one wrong, it's not gonna look good."
]

define calDaysPicked = 0

define nexttext = 0

define reelNum = len(likes)

define rewind = False

define perfect = True

define kicked = False



transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.1 xmaximum 300 at alpha_dissolve # This is the timer bar.

label cal:
    $ calDaysPicked +=1
    if calDaysPicked == 1:
        jump calDay3
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

    $ _skipping = False

    $ quick_menu = False

    show screen my_keys

    show cal phone hold at left

    c "alright! here's the first one."

    show cal phone show at center
    with move

    c "i hope you like it!"

    jump reels

label reels:
    while count < reelNum:
        $ reel = "images/reel" + str(random.randint(1, reelNum)) + ".webm"
        while reel in watched:
            $ reel = "images/reel" + str(random.randint(1, reelNum)) + ".webm"

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
                window hide
                pause
                show cal forwards at truecenter:
                    ease 0.2 zoom 5 yalign 0.25
                window hide
                pause
                c "get out."
                $ kicked = True
                $ mood += 1
                hide screen my_keys
                $ quick_menu = True
                $ _skipping = True

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

    $ quick_menu = True

    c "NOO MY PHONE DIED!"

    show cal neutral at center

    c "oh well, thanks for hanging out with me."

    if score == reelNum:
        show cal surprised
        c "woah...you liked and hated those reels the exact same as me!"
        show cal phone hold
        c "your sense of humor is truly top notch."
        show cal up
        c "let's play some games together sometime!"
        c "oh, and add me on IGsDAgram!"
        c "seeya!"

    elif 0.8*reelNum <= score < reelNum:
        $ perfect = False
        c "you've got a good sense of humor."
        c "i'm glad you enjoyed them."
        c "let's add eachother on IGsDAgram next time!"

        show cal up at center

        c "alright, i'll see you around!"

    elif score < 0.8*reelNum:
        $ perfect = False
        c "you've got a weird taste in videos..."
        c "please get a better sense of humor."

        c "see ya."
        $ mood += 1
    $ _skipping = True
    hide screen my_keys
    jump checkDay

define kicked2 = False

label fuckyou:

    c "um..."

    c "i don't really have any other ideas..."

    c "please leave."

    $ mood += 1

    $ kicked = True

    jump checkDay

label calDay2:
    if kicked:
        "Calvin doesn't seem to be responding to your messages..."
        "guess i should have paid attention."
        jump checkDay

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
                $ quick_menu = False
                show calb neutral mad
                c "thats it."
                c "GET OUUUUUUUUT!"
                show calb forwards at truecenter:
                    ease 0.2 zoom 5 yalign 0.25
                window hide
                $ renpy.pause(delay=0.01)
                $ kicked2 = True
                $ quick_menu = True
                jump checkDay

            show calb forwards 
            c "i said guess."
            show calb neutral 
            $ stopguess += 1
            jump guess
        
        "Are we gonna go somewhere?":
            if stopout == 1:
                $ mood += 1
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

            if rewind:
                $ quick_menu = False
                show screen my_keys
                show calb neutral mad
                c "you really are addicted to short form media huh?"
                c "what are you, an ipad kid?"
                c "or maybe you are just trying to avoid my quiz."
                c "well you know what."
                show calb down
                c "too bad!"
                jump cal22

            c "no."
            c "i mean unless you want to i guess."
            $ stopmore = True
            menu:
                "i want to rewind time":
                    $ calDaysPicked = 1
                    $ rewind = True
                    c "its your playthrough i guess..."
                    $ kicked2 = True
                    hide calb
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
            c "let's see just how much you know about my games."
            jump cal22

        "*remain silent*":
            show calb neutral
            $ silence += 1
            $ quick_menu = False
            show screen my_keys
            $ renpy.pause(delay=1.5**silence,hard=True)
            show calb forwards
            $ renpy.pause(delay=1.5**silence,hard=True)
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
        ease 150 zoom 5 yalign 0.3
    $ renpy.pause(delay=150,hard=True)
    $ quick_menu = True
    hide screen my_keys
    stop music fadeout 1.0
    $ kicked2 = True
    jump checkDay

define wrongdeath = 0
define perfectquiz = True
define perfectHW = True


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

    play music "gameshow.ogg"
    
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

    {"question": "about how many seconds do you need to stay to hear miku in seben eleben simulator?",
    "type": "enter",
    "answer": [ ["120", "right"]]},

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
    "type": "enter",
    "answer": [ ["4", "right"]]},

    {"question": "who is June's husband?",
    "type": "multi",
    "answer": [ ["Mark", "right"], ["Me", "wrong"], ["Mars", "wrong"], ["Jake", "wrong"] ]},

    {"question": "what is June looking for?",
    "type": "multi",
    "answer": [ ["Ummagumma", "right"], ["Pink Floyd", "wrong"], ["Love", "wrong"], ["A Vinyl", "wrong"] ]},

    {"question": "what is the 3rd ending called in The Quest for Ummagumma?",
    "type": "multi",
    "answer": [ ["Touch Grass", "right"], ["Gave Up", "wrong"], ["Parry", "wrong"], ["Bad", "wrong"] ]},

    {"question": "which line is at the top of igbl's 1st minigame?",
    "type": "multi",
    "answer": [ ["FINISH THE ESSAY!!!!", "right"], ["FINISH THE ESSAY!!!", "wrong"], ["FEED YOURSELF!!!", "wrong"], ["FEED YOURSLEF!!!", "wrong"] ]},

    {"question": 'how is "coffee" spelled in Bad Barista?',
    "type": "multi",
    "answer": [ ["coughee", "right"], ["cofi", "wrong"], ["koughee", "wrong"], ["cuofi", "wrong"] ]},

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
    
    {"question": 'how many bags of garbage are there in "im really constructive."?',
    "type": "enter",
    "answer": [ ["7", "right"]]},

    {"question": 'what shape is the green in "im really constructive."?',
    "type": "multi",
    "answer": [ ["cylinder", "right"],["sphere", "wrong"],["circle", "wrong"], ["rectangle", "wrong"]]},

    {"question": 'how many times can you use the hydration lamp in "im really thirsty."?',
    "type": "enter",
    "answer": [ ["2", "right"]]},

    {"question": 'which option in Petit Dej reveals a good memory?',
    "type": "multi",
    "answer": [ ["Parfait", "right"],["Orange Juice", "wrong"],["Fruit", "wrong"], ["Omelette", "wrong"]]},

    {"question": 'on what page does June smack you in The Quest for Ummagumma?',
    "type": "enter",
    "answer": [ ["82", "right"]]},

    {"question": 'how many unique colors does the level in bobl use?',
    "type": "enter",
    "answer": [ ["13", "right"]]},

    {"question": 'where is the homeless man in "im really constructive."?',
    "type": "multi",
    "answer": [ ["At the top", "right"],["Behind the trash", "wrong"],["Inside the cage", "wrong"], ["Next to the pillar", "wrong"]]},

    {"question": 'how many seconds do you have to stay in seben eleben to quit the game?',
    "type": "enter",
    "answer": [ ["180", "right"]]},

    {"question": 'how many combinations of people are there in Bad Barista?',
    "type": "enter",
    "answer": [ ["9", "right"]]},

    {"question": 'if you get a poem score of -18 in Skybeam+, what is the title of the poem?',
    "type": "multi",
    "answer": [ ["Killed Skills", "right"], ["just not right", "wrong"], ["Insomnia", "wrong"], ["All over", "wrong"]]},

    {"question": 'if you get a poem score of -18 in Skybeam, what is the title of the poem?',
    "type": "multi",
    "answer": [ ["just not right", "right"], ["Killed Skills", "wrong"], ["Insomnia", "wrong"], ["All over", "wrong"]]},

    {"question": 'what is the image in the pause menu of FRANCE DEFANCE?',
    "type": "multi",
    "answer": [ ["Nissan S-Cargo", "right"], ["Le Fishe", "wrong"], ["Spy TF2", "wrong"], ["Nissan Escargo", "wrong"]]},

    {"question": 'where are the models in igbl from?',
    "type": "multi",
    "answer": [ ["Roblox", "right"], ["Thingiverse", "wrong"], ["Sketchfab", "wrong"], ["TurboSquid", "wrong"]]},

    {"question": 'what sound does Alex make when GIVE in GIVE THANKS?',
    "type": "multi",
    "answer": [ ["Lego Yoda Death Sound", "right"], ["Half-Life Scientist Scream", "wrong"], ["Hey all, Scott here!", "wrong"], ["Tom Scott Scream", "wrong"]]},

    {"question": 'in Skybeam, what score gives you the poem "Restless"?',
    "type": "enter",
    "answer": [ ["5", "right"]]},

    {"question": 'in Skybeam+, what score gives you the poem "pi"?',
    "type": "enter",
    "answer": [ ["12", "right"]]},

    {"question": 'what color is the cashier?',
    "type": "multi",
    "answer": [ ["Green", "right"], ["Yellow", "wrong"], ["Blue", "wrong"], ["Brown", "wrong"]]},

    {"question": 'what color is the sirup in Bad Barista?',
    "type": "multi",
    "answer": [ ["Orange", "right"], ["Green", "wrong"], ["Tan", "wrong"], ["Brown", "wrong"]]},

    {"question": 'what do the ratios in Bad Barista add up to?',
    "type": "enter",
    "answer": [ ["1000", "right"]]},

    {"question": 'what was The Quest for Ummagumma made in?',
    "type": "multi",
    "answer": [ ["Google Slides", "right"], ["Power Point", "wrong"], ["Godot", "wrong"], ["MS Paint", "wrong"]]},

    ]
   
    # game variables
    #####
    

    $ wrong_answers = 0     # amount of wrong answers
    $ quiz_length = len(q_list)      # number of questions in one game
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
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
                    $ wrongdeath +=1
            "[answ_1]":
                if a["answer"][huh[1]][1]  == "right":
                    $ time += 5
                    show calb up 
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
                    $ wrongdeath +=1
            "[answ_2]":
                if a["answer"][huh[2]][1]  == "right":
                    $ time += 5
                    show calb up 
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
                    $ wrongdeath +=1
            "[answ_3]":
                if a["answer"][huh[3]][1]  == "right":
                    $ time += 5
                    show calb up 
                    "CORRECT!"
                    $ wrong_answers -=1
                else:
                    show calb down
                    "WRONG!"
                    $ wrong_answers +=1
                    $ wrongdeath +=1
        if time > 10:
            $ time = 10

        $ quiz_length -= 1
        if wrong_answers == 1:
            $ perfect = False
            $ perfectquiz = False
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
            $ typed = renpy.input("[question]",allow="-0123456789")
            if typed == a["answer"][0][0]:
                $ time += 5
                show calb up 
                "CORRECT!"
                $ wrong_answers -=1
            else:
                show calb down
                "WRONG!"
                $ wrong_answers +=1
                $ wrongdeath +=1
            if time > 10:
                $ time = 10
            $ quiz_length -= 1
            if wrong_answers == 1:
                $ perfect = False
                $ perfectHW = False
            if -1 <= wrong_answers <= 1:
                show calb neutral
            elif wrong_answers < -1:
                show calb neutral happy
            elif wrong_answers > 1:
                show calb neutral mad
            if wrongdeath > 3:
                show calb forwards
                hide screen countdown
                pause
                jump loser
            if quiz_length > 0:     
                $ nexttext = random.choice(randonext)
                c "[nexttext]"
                jump quize_game
            else:
                jump quizEND


    label quizEND:
        hide screen countdown
        show calb neutral
        stop music fadeout 1.0
        c "congrats on making it through the quiz."
        c "now it's time for the real challenge."
        c "i got some homework thats due tomorrow."
        c "mind helping me out?"
        show fakehw at left:
            yalign 0.5
        show fakeeqnsheet at right:
            yalign 0.45
        c "good luck."
        window hide
        pause
        
        $ hwscore = 0

        $ typed = renpy.input("Question 1:",allow="-0123456789.")
        if typed == "0.553":
            $ hwscore +=1
        $ typed = renpy.input("Question 2A:",allow="-0123456789.")
        if typed == "0.5":
            $ hwscore +=1
        $ typed = renpy.input("Question 2B:",allow="-0123456789.")
        if typed == "0.429":
            $ hwscore +=1
        $ typed = renpy.input("Question 2C:",allow="-0123456789.")
        if typed == "0.9":
            $ hwscore +=1
        $ typed = renpy.input("Question 2D:",allow="-0123456789.")
        if typed == "1.667":
            $ hwscore +=1
        $ typed = renpy.input("Question 3A.1:",allow="qwertyuiopasdfghjklzxcvbnm")
        if typed == "flammable":
            $ hwscore +=1
        $ typed = renpy.input("Question 3A.2:",allow="qwertyuiopasdfghjklzxcvbnm")
        if typed == "toxic":
            $ hwscore +=1
        $ typed = renpy.input("Question 3A.3:",allow="qwertyuiopasdfghjklzxcvbnm ")
        if typed == "health hazard":
            $ hwscore +=1
        $ typed = renpy.input("Question 3B:",allow="-0123456789.")
        if typed == "2":
            $ hwscore +=1
        $ typed = renpy.input("Question 3B:",allow="qwertyuiopasdfghjklzxcvbnm ")
        if typed == "use no water":
            $ hwscore +=1
        
        hide fakehw
        hide fakeeqnsheet
        c "alright, let me check your work."
        if hwscore == 10:
            show calb yiik
            c "wow, you did this HW perfectly!"
            show calb forwards
            c "that's suspicious."
            pause
            show calb neutral happy
            c "eh it don't matta you got it done and that's all i care about."
        elif hwscore >= 8:
            $ perfect = False
            $ perfectquiz = False
            c "good enough. that's enough to get a B."
            c "always remember: B's get degrees, C's get disease."
            c "and A's get ice cream or something idk"
            c "thanks for the help!"
        else:
            show calb neutral mad
            $ perfect = False
            $ perfectquiz = False
            c "...did you even try?"
            c "all that effort just to fall flat here."
            c "pick a better major next time..."
            jump loser

    
        show calb yiik
        c "holy crap, you actually made it!"
        if perfectquiz:
            show calb neutral happy
            c "you didn't even make a single mistake!"
            c "you really did do your research huh..."
            show calb think
            c "or maybe this is your hundreth attempt and you finally did everything perfectly."
            show calb up
            c "regardless, thanks for putting so much dedication to learning and playing my games."
        "if you actually made it here, please tell me how long this took and what kind of notes you took to pass, i'm curious."
        show calb neutral happy
        c "you really are a true calvin fan."
        c "you're the best, i can't wait to hang out with you again."
        c "see ya!"

        hide screen my_keys
        $ quick_menu = True
        jump checkDay


    label loser:
        stop music fadeout 1.0
        if mood >= 1:
            show calb neutral mad
            c "..."
            c "you come crawling back to me and all you do is disappoint."
            c "are you really that desperate?"
            c "just go."
            $ kicked2 = True
        else:
            show calb neutral
            c "welp...you tried."
            c "study harder next time, okay?"
            c "i'll see you around."
            c "bye."
        hide screen my_keys
        $ quick_menu = True
        jump checkDay
   
    $ quick_menu = True
    hide screen my_keys
    jump checkDay


define pulls = 0
define gacha = 200

define winner = False

default stage = False
default laundry = False
default stairs = False
default oak = False
default police = False
default pcmall = False
default of1 = False
default of2 = False
default of3 = False
default of4 = False
default of5 = False
default of6 = False
default of7 = False
default of8 = False

default numEnd = 74


label calDay3:
    if kicked2:
        "Calvin just sends you a gif that says 'DONT SAY THAT' with a dummy getting it's neck ripped out."
        "...i should probably stay away from him for my own safety."
        jump checkDay
    show screen my_keys
    $ quick_menu = False
    scene dorm
    show calb neutral
    c "hello."
    c "hide and seek."
    c "i hide, you seek."
    c "cya later loser"
    hide calb

    m "man what the fuck."
    m "guess i gotta get started."

    scene laurelin

    m "where to check first..."

    menu dorm:
        "Laundromat" if not laundry:
            m "maybe he went to do his laundry"
            m "let's take the elevator down."
            $ laundry = True
            jump laundry
        "The Stairs" if not stairs:
            $ stairs = True
            jump stairs
        "The Stage" if not stage:
            $ stage = True
            m "i wonder if he went back to the stage..."
            jump stage
        "Leave":
            jump laurelout


label stairs:
    scene laurelstair
    m "let's check if he just hid in the stairs."
    if gacha == random.randint(1,100):
        show calb neutral mad at center
        m "you thought this was a good hiding spot?"
        c "man fuck you, what kinda person takes the stairs."
        m "me."
        c "you got me there."
        c "whatever, congrats on finding me."
        if pulls == 0:
            $ winner = True
        jump finale
    elif pulls == numEnd:
        show calb neutral happy at center
        c "well well well look who it is."
        m "go fuck yourself."
        c "hey, not my fault you got a skill issue."
        jump finale
    else:
        m "damn he isn't here."
        m "what a stupid choice i made."
        $ pulls += 1
        jump dorm

label laundry:
    scene laundry
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral at center
        m "oh so you just went to do your laundry"
        show calb neutral happy
        c "yep, it's free laundry week yknow."
        "so real."
        show calb up
        c "thanks for playin and congrats on finding me."
        jump finale
    elif pulls == numEnd:
        show calb neutral at center
        c "man what took you so long?"
        m "who the hell hides in the laundry?"
        show calb up
        c "me. I was doing it."
        show calb neutral
        c "but i finished like 2 hours ago bro."
        c "i was just watching more videos here waiting for you."
        m "man i'm outta here."
        c "see ya."
        jump finale
    else:
        m "he isn't here."
        m "not doing laundry on free laundry week?"
        m "guess he has better things to do."
        $ pulls += 1
        jump dorm

label stage:
    scene stage
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy
        c "this place look familiar?"
        m "yep, it sure does."
        if wrongdeath <= 3:
            c "i still can't believe you made it through that."
            show calb up
            c "i gotta congratulate you again."
        elif perfectquiz:
            c "brings me back to when you perfected my quiz."
            c "36 whole questions and you got them all right."
            c "truly GOATed you are."
        else:
            show calb neutral mad
            c "i sure hope you've studied more since then."
            c "i expect better from you."

        show calb neutral happy
        
        if perfectHW:
            c "there's no way you completed that HW perfectly without cheating."
            c "or maybe it wasn't your first time seeing it, hehe."
            show calb up
            c "either way, great job."
            c "wouldn't have made it without ya."
        elif hwscore >= 8:
            c "i'm also impressed you managed to get that ChemE HW right."
            c "pretty insane, especially if you ain't a ChemE major."
            show calb up
            c "congratulations on that as well."
        else:
            show calb neutral mad
            c "you also need to study ChemE more."
            c "i don't care if it's not your major, learn it."
            c "it comes into handy more than you'd expect."
        c "welp. i'll see ya around."
        jump finale
    elif pulls == numEnd:
        show calb neutral happy
        c "I knew this would be the last place you looked."
        c "this place must be traumatizing for you, hehe."
        show calb up
        c "congratulations on finally finding me."
        c "i'll see ya round."
        jump finale
    else:
        m "ugh i hate this place."
        m "i never want to come back here ever again."
        m "i'm really glad he isn't here."
        scene laurelin
        $ pulls += 1
        jump dorm

define co =False
define ls = False
label laurelout:
    scene laurel
    m "alright where could he have gone..."
    menu laurel:
        "Go Back inside Laurel":
            m "maybe i missed something in laurel."
            scene laurelin
            jump dorm
        "Oak Hall" if not oak:
            $ oak = True
            m "he probably went to visit Oak Hall for something."
            jump oak
        "NJIT Police" if not police:
            $ police = True
            m "is he fucking reporting me to the police?"
            jump police
        "Old Parking Deck":
            m "did he go take pictures in the old parking deck?"
            jump oldpdeck
        "PC Mall" if not pcmall:
            $ pcmall = True
            m "he probbaly had to print something."
            jump pcmall
        "Department of Electrical and Computer Engineering" if not co:
            $ co = True
            m "i think he likes to use the bathroom in this place."
            jump co
        "Life Science and Engineering Center" if not ls:
            $ ls = True
            m "it is a pretty cool lookin building, surely he went into here."
            jump ls
        "Keep Going":
            m "he probbaly went to hide further than this."
            jump between

label co:
    scene computercenter
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "hey! just finished using the bathroom here."
        show calb up
        c "anyways, congrats!"
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "at last you have arrived."
        c "this building is tiny, i was sooo bored!"
        c "whatever, congrats."
        jump finale
    else:
        m "damn he isn't here."
        m "what a stupid choice i made."
        $ pulls += 1
        jump laurel

label ls:
    scene lifescience
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "yo! just came out of the building."
        c "it's really a nice place to study."
        show calb up
        c "anyways, congrats!"
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "there you are, finally!"
        c "this building is so close to Laurel, how did you not check it?"
        c "congrats, i guess."
        jump finale
    else:
        m "damn he isn't here."
        m "what a stupid choice i made."
        $ pulls += 1
        jump laurel
    
label oak:
    scene oak
    m "alright your hiding days are over."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "hey hey! I was just hanging around Oak before it gets demolished."
        c "still can't believe it's gonna happen for real."
        c "congrats on finding me!"
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "what took you so long bruh."
        c "Oak is literally next to Laurel, how did you not assume i'd hide here?"
        c "whatever. congrats or something."
        jump finale
    else:
        "(you check the entirety of Oak Hall)"
        m "fuck he isn't here."
        m "oh right...he doesn't have friends that live in Oak."
        m "i'm so stupid for trying to look here."
        $ pulls += 1
        jump laurel

label police:
    scene police
    m "he better not be reporting me as a stalker or something."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "yo, just reported some weird activity at GDS."
        c "something about food poisoning and RPS..."
        c "anyways, good job finding me!"
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "yep that's them officer, i told you they'd come for me."
        m "WHAT HOLD ON"
        show calb neutral happy
        c "hehe, gotcha"
        c "took you long enough, you deserved that."
        jump finale
    else:
        "(you briefly check inside the police station)"
        m "he isn't here."
        m "why would he even go here..."
        m "why did i check this spot?"
        m "i'm so dumb."
        $ pulls += 1
        jump laurel

label oldpdeck:
    scene parkold2
    m "oh god this place has 8 fucking floors."
    m "where to look first..."
    menu opdeck:
        "Floor 1" if not of1:
            $ of1 = True
            m "okay maybe he went to the bottom of the old parking deck."
            jump of1
        "Floor 2" if not of2:
            m "perhaps he is just somewhere on this floor."
            $ of2 = True
            jump of2
        "Floor 3" if not of3:
            m "let's try this floor."
            $ of3 = True
            jump of3
        "Floor 4" if not of4:
            m "the number 4 is unlucky, but let's try this anyways."
            $ of4 = True
            jump of4
        "Floor 5" if not of5:
            m "5 is his favourite number, surely he is here."
            $ of5 = True
            jump of5
        "Floor 6" if not of6:
            m "floor 6."
            $ of6 = True
            jump of6
        "Floor 7" if not of7:
            m "yknow what they say, lucky number 7."
            $ of7 = True
            jump of7
        "Floor 8" if not of8:
            m "he probably likes the top floor the best."
            $ of8 = True
            jump of8
        "Leave":
            m "nah theres no way he went in this old thing."
            scene laurel
            jump laurel

label of1:
    scene parkold1
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "hey, ya found me!"
        c "I was just looking at the random shit down here."
        c "it's weird that they don't let you enter from this floor anymore."
        show calb think
        c "wonder why that is..."
        show calb up
        c "anyways, congrats!"
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "finally made it huh."
        c "yknow i can only stare at these cars and walls for so long."
        c "and it kinda stinks down here."
        c "congrats, but better luck next time."
        jump finale
    else:
        m "damn he isn't here."
        m "what a stupid choice i made."
        $ pulls += 1
        jump opdeck

label of2:
    scene parkold2
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "what's up."
        c "i was too lazy to take the elevator so i just hid here."
        c "the view aint too bad on the side opposite of laurel."
        c "good job on finding me!"
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "what took you so long?"
        c "the old parking deck is pretty boring, i thought i was gonna die of boredom."
        c "oh well, congrats."
        jump finale
    else:
        m "no way he isn't here."
        m "god damn it i really don't want to search this whole thing."
        $ pulls += 1
        jump opdeck

label of3:
    scene parkold3
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "floor 3 oh yeah baybee"
        c "didn't expect me to be here didya?"
        c "good job mate, see ya round."
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "ugh finally."
        c "the rattles and noise of the parking deck was making my head hurt."
        c "congrats, now get outta here."
        jump finale
    else:
        m "aw man he ain't here."
        m "guess he must've went higher or lower than this floor."
        $ pulls += 1
        jump opdeck

label of4:
    scene parkold4
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "4 is an unlucky number in asian cultures."
        c "but i thought fuck it, let's hide here."
        c "good job on choosing the right floor!"
        jump finale
    elif pulls == numEnd:
        show calb neutral at center
        c "didn't think i would be here huh?"
        c "4 is an unlucky number so i don't blame you for taking so long"
        c "at least you got here in the end."
        c "see ya."
        jump finale
    else:
        m "i knew floor 4 would be a bust."
        m "should've trusted my gut."
        $ pulls += 1
        jump opdeck

label of5:
    scene parkold5
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "floor 5 yippee!!!!!"
        c "5 is my favourite number if you didn't know."
        show calb think
        c "i never really had a reason for it."
        c "it just stuck with me one day in elementary and now it just feels right."
        show calb neutral happy
        c "i mean, who doesn't love the number 5?"
        c "it's so easy to add and multiply."
        c "oh yeah, congratulations on finding me!"
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "there you are."
        c "you should've known that 5 is my favourite number man."
        show calb down
        c "i'm disappointed in you."
        show calb nuetral
        c "well, you found me anyways so good job or whatever."
        jump finale
    else:
        m "what?? not even on his favourite numbered floor?"
        m "guess he knew i'd check here."
        $ pulls += 1
        jump opdeck

label of6:
    scene parkold6
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "6!!!! FLOOR 6!!!!"
        c "can you tell that i'm running out of things to say about these floors?"
        c "i hope you don't mind that."
        c "at least you suffering ends here, good job!"
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "cmon man, floor 6 ws an obvious choice, how did you not choose it??"
        c "rookie mistake fam."
        c "good job, and get out."
        jump finale
    else:
        m "floor 6 is so generic, no wonder he ain't here"
        m "maybe i should stop looking at the parking deck."
        $ pulls += 1
        jump opdeck

label of7:
    scene parkold7
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "7 is the lucky number for you!"
        c "maybe we should go gambling!"
        c "i don't care if we ain't old enough, that's a quitter mindset."
        c "if you can find me, you can win a morbillion dollars, surely!"
        jump finale
    elif pulls == numEnd:
        show calb neutral mad at center
        c "7 is literally a lucky number and you CHOSE not to look here?"
        c "that's lowkey crazy bro."
        c "whatever, your loss not mine hehe."
        c "good job."
        jump finale
    else:
        m "man even with the luck of 7 he's not here."
        m "maybe there is a better number somewhere else."
        $ pulls += 1
        jump opdeck

label of8:
    scene parkold8
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb neutral happy at center
        c "*sigh*"
        c "i love being up here."
        c "the view is just so nice and the breeze is really refreshing."
        c "i'm glad you're here to enjoy it wth me."
        c "congratulations for finding me."
        jump finale
    elif pulls == numEnd:
        show calb neutral at center
        c "cmon man, i take pictures up here all the time, and it's the most interesting floor out of all!"
        c "why didn't you check here earlier?"
        c "at least it gave me a lot of time to savour the view."
        c "good job. seeya."
        jump finale
    else:
        m "not even floor 8???"   
        m "he takes pictures here all the time!!!"
        m "ugh, time to check somewhere else."
        $ pulls += 1
        jump opdeck

label pcmall:
    scene pcmall1
    m "why the hell is this hallway so long??"
    m "i guess he isn't here."
    scene pcmall2
    m "wait no this isn;t even the PC Mall yet, this is just the hallway."
    m "i gotta keep going."
    scene pcmall3
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        m "THERE YOU ARE!"
        c "hey. no yelling in the PC Mall."
        m "sorry."
        c "don't say sorry to me man."
        c "anyways, i had to print slides for my next class so i thought i might as well do that while hiding."
        c "ongrats on finding me!"
        jump finale
    elif pulls == numEnd:
        m "what kinda place is this?"
        c "it's a PC Mall."
        c "you're gonna find PC's inside."
        c "honstly what did you expect?"
        m "not...this?"
        c "reasonable."
        c "congrats and stuff. seeya."
        jump finale
    else:
        m "no printing for him today i guess."
        m "let's try elsewhere."
        $ pulls += 1
        jump laurelout

default ckb = False
default fmh = False
default books = False
default camp = False
default al = False


label between:
    scene ckb
    m "where to check next..."
    menu beeteen:
        "Central King Building" if not ckb:
            $ ckb = True
            "kino"
            jump ckb
        "Faculty Memorial Hall" if not fmh:
            $ fmh = True
            "kino"
            jump fmh
        "NJIT Bookstore" if not books:
            $ books = True
            jump books
        "Campbell Hall" if not camp:
            $ camp = True
            jump camp
        "Alley" if not al:
            $ al = True
            jump al
        "Go back to Laurel":
            jump laurelout
        "Go towards the Wellness and Events Center":
            jump wecout

default bot = False
default bot1 = False

label ckb:
    m "checking ckb..."
    menu ckbin:
        "Bottom Floor" if not bot:
            $ bot = True
            jump bot
        "Not Bottom Floor" if not bot1:
            $ bot1 = True
            jump bot1
        "Leave":
            jump between

label bot:
    scene ckb1
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump ckb

label bot1:
    scene ckb2
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump ckb
        
label fmh:
    scene fmh
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump between

label books:
    scene bookstore
    m "must be getting an IGDAzon package."
    scene folant
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump between

label camp:
    scene campbell
    m "what even is in here..."
    m "maybe he is just on the outside somewhere."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump between

label al:
    scene alley
    m "what a weird alley."
    m "calvin definitely would love to be here."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump between

label wecout:
    scene wec
    m "maybe somewhere around here..."
    menu wecs:
        "Go into the Wellness and Events Center":
            jump wec
        "Head to Tiernan Hall":
            jump tier 
        "Head to Kupfrian Hall":
            jump kup
        "Go towards Albert Dorman Honor's College":
            jump honor
        "Go towards the Campus Center":
            jump CC
        "Go back":
            jump between

define fence = False
define pool = False
define sto = False
define tra  = False
define bas  = False
define res  = False
define gym = False


label wec:
    scene chase
    m "where to check.[pulls]"
    menu wecin:
        "Fencing" if not fence:
            $ fence = True
            jump fence
        "Pool" if not pool:
            $ pool = True
            jump pool
        "Storage" if not sto:
            $ sto = True
            jump sto
        "Track" if not tra:
            $ tra = True
            jump tra
        "Basketball Court" if not bas:
            $ bas = True
            jump bas
        "Restricted Area" if not res:
            $ res = True
            jump res 
        "Gym" if not gym:
            $ gym = True
            jump gym
        "Leave":
            m "nah, wec is for losers."
            jump wecout

label fence:
    scene fencing
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump wecin

label pool:
    scene pool
    m "aw pool closed."
    m "maybe he sad too."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump wecin

label sto:
    scene storage
    m "where the hell"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump wecin
        
label tra:
    scene track
    m "ain't no way he exercising"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump wecin

label bas:
    scene basketball
    m "ain't no way he like basketball"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "I LOVE BALLS!"
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump wecin

label res:
    scene gdshosp
    m "i ain't allowed in here prolly..."
    m "and he ain't either wtf."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        c "look at view!"
        scene basketballtop
        hide calb
        m "vewy nice"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump wecin

label gym:
    scene gym
    m "ain't no way he workin out"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "yeah i ain't im a fatass."
        c" found me! good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here, lmao"
        show lilynose
        "Lily" "hi im Lily!"
        m "what in ze phoq"
        "Lily" "wreah!"
        $ pulls += 1
        jump wecin

define tf1 = False
define tf2 = False
define tf3 = False
define tf4 = False

label tier:
    scene tierins
    m "where to?"
    menu tierins:
        "Floor 1" if not tf1:
            m "yes... AIChE is here..."
            $ tf1 = True
            jump tf1
        "Floor 2" if not tf2:
            $ tf2 = True
            jump tf2
        "Floor 3" if not tf3:
            $ tf3 = True
            jump tf3
        "Floor 4" if not tf4:
            $ tf4 = True
            jump tf4
        "Leave":
            m "tiernan hall, YUCKY!"
            jump wecout

label tf1:
    scene aiche
    m "surely."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump tierins

label tf2:
    scene tier2
    m "surely."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump tierins

label tf3:
    scene tier3
    m "surely."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump tierins

label tf4:
    scene tier4
    m "surely."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump tierins

define tkup = False
define bkup = False

label kup:
    scene kupfrian
    m "maybe class in here."
    menu kupf:
        "Top Floor" if not tkup:
            $ tkup = True
            jump tkup
        "Bottom Floor" if not bkup:
            $ bkup = True
            jump bkup
        "Leave":
            jump wecout

label tkup:
    scene kupftopins
    m "class time?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "came out of class. hate this class."
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump kupf

label bkup:
    scene kupfbotins
    m "class time?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "came out of class. hate this class."
        c "found me. good job."
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here."
        $ pulls += 1
        jump kupf

define hin = False
define gigi=False
define vm=False
define sb =False
define gym2=False
define mapl=False
define ven=False


label honor:
    scene honorfront
    m "no way."
    menu honorf:
        "Go into Honor's" if not hin:
            $ hin = True
            jump hin
        "Gigi's Halal Food" if not gigi:
            $ gigi = True 
            jump gigi
        "Village Market" if not vm:
            $ vm = True
            jump vm
        "Smashburger" if not sb:
            $ sb = True
            jump sb
        "Other Gym" if not gym2:
            $ gym2 = True
            jump gym2
        "Maple Hall" if not mapl:
            $ mapl =True
            jump mapl
        "Venture Link" if not ven:
            $ ven =True
            jump ven
        "Go back":
            jump wecout

label mapl:
    scene mapleout
    m "fancy ass dorm bro gaddam."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "wish i could live here."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "nuh-uh."
        $ pulls += 1
        jump honorf

label hin:
    scene honorins
    m "where tf is he"
    m "gotte keep goin"
    scene honorgreen
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "i like green"
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here, obviously."
        $ pulls += 1
        jump honorf

label gigi:
    scene gigi
    m "mmm hungry."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "i like food. i very hungry."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "surpisngly not here."
        $ pulls += 1
        jump honorf
            
label vm:
    scene vm
    m "fuckin hate this overpriced place."
    scene vminside
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "i like overpaying!"
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "thank god he ain't in here. i'd be disappointed."
        $ pulls += 1
        jump honorf

label sb: 
    scene smashburger
    m "actually still owned by GDs."
    m "shittier than real Smashburger."
    scene smashburgerinside
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "i like borgir"
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here, he ain't smashin borgirs."
        $ pulls += 1
        jump honorf
label gym2: 
    scene gym2
    m "he doesn;t even have access here."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "i HATE JIM!!!!!!"
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here, lol."
        $ pulls += 1
        jump honorf

label ven: 
    scene venture
    m "he ain't a fockin entree pren ew er"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "i make a da product!"
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "yeah no shit he aint here."
        $ pulls += 1
        jump honorf

define red = False
define cyp = False
define ten = False

label CC:
    scene campusout
    m "where to check?"
    menu ccc:
        "Redwood" if not red:
            $ red = True
            jump red
        "Cypress" if not cyp:
            $ cyp = True
            jump cyp
        "Namoli Family Atheltic and Recreational Facility" if not ten:
            $ ten = True
            jump ten
        "Head to the Library":
            jump lib
        "Go to the New Parking Deck":
            jump npd
        "Go into the Campus Center":
            jump ccin
        "Go towards GITC":
            jump GITC
        "Go back":
            jump wecout



label red:
    scene redwood
    m "he fuckin hates this hall."
    m "and he ain't a freshamn no more."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "communal showers ew!!"
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here, unsurprisingly."
        $ pulls += 1
        jump ccc

label cyp:
    scene cypress
    m "his first hall."
    m "he has good memories here."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "i miss cypress actually..."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "he ain't here."
        $ pulls += 1
        jump ccc

label ten:
    scene tennis
    m "he don;t event play tennis."
    m "i don't think he can go in here."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "i was outside chilling actually."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "he ain't here, duh."
        $ pulls += 1
        jump ccc


define mie = False
define gf1 = False
define gf2 = False
define gf3 = False
define gf4 = False
define gf5 = False
define mf1 = False
define mf2 = False
define mf3 = False


label GITC:
    scene gitcout
    m "oh man options..."
    menu gitcc:
        "Go into the Guttenberg Information Technology Center":
            jump gitin
        "Makerspace":
            jump mak
        "Mechanical & Industrial Engineering Building" if not mie:
            $ mie = True
            jump mie
        "Go Back":
            jump CC

label gitin:
    scene gitc1
    m "WHY 5 FLOORS BRO?"
    m "at least the basement isn't an option."
    menu gitfuck:
        "Floor 1" if not gf1:
            $ gf1=True
            jump gf1
        "Floor 2" if not gf2:
            $ gf2=True
            jump gf2
        "Floor 3" if not gf3:
            $ gf3=True
            jump gf3
        "Floor 4" if not gf4:
            $ gf4=True
            jump gf4
        "Floor 5" if not gf5:
            $ gf5=True
            jump gf5
        "Leave":
            jump GITC

label gf1:
    scene gitc1
    m "where."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "ew CS."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no here."
        $ pulls += 1
        jump gitfuck

label gf2:
    scene gitc2
    m "where?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "robotics is here."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no here."
        $ pulls += 1
        jump gitfuck

label gf3:
    scene gitc3
    m "where!"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "hey you met us here lol"
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no here!"
        $ pulls += 1
        jump gitfuck

label gf4:
    scene gitc4
    m "where$"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "professionals here..."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no here!"
        $ pulls += 1
        jump gitfuck

label gf5:
    scene gitc4
    m "where"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "what even happens here."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no here!"
        $ pulls += 1
        jump gitfuck

label mak:
    scene makerspaceout
    m "YAY MORE SEEKING!!!!!"
    menu mik:
        "Floor 1" if not mf1:
            $ mf1=True
            jump mf1
        "Floor 2" if not mf2:
            $ mf2=True
            jump mf2
        "Floor 3" if not mf3:
            $ mf3=True
            jump mf3
        "Leave":
            jump GITC
        
label mf1:
    scene maker1
    m "where are ya?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "this place is so much prettier than before."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "nope."
        $ pulls += 1
        jump mik

label mf2:
    scene maker3d 
    m "where are ya!"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "3D printing my duderoni!"
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "nope!"
        $ pulls += 1
        jump mik

label mf3:
    scene maker2
    m "where are ya!?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "Trotec Speedy 100, more like Trotec Stupid 100."
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "nope!!"
        $ pulls += 1
        jump mik

label mie:
    scene meche
    m "prolly not here."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "comin back from gios BAYBEE!!"
        c "you found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "nuh uh."
        $ pulls += 1
        jump gitcc

define lf1 = False
define lf2 = False
define lf3 = False
define lf4 = False


label lib:
    scene libout
    m "is he studying?"
    m "studious little boy."
    menu libab:
        "Floor 0" if not lf1:
            $ lf1 = True
            jump lf1
        "Floor 1" if not lf2:
            $ lf2 = True
            jump lf2
        "Floor 2" if not lf3:
            $ lf3 = True
            jump lf3
        "Floor 3" if not lf4:
            $ lf4 = True
            jump lf4
        "Leave":
            jump CC

label lf1:
    scene lib0
    m "silence time."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "found me!"
        c "but shhhhhhh"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no calvin."
        $ pulls += 1
        jump libab

label lf2:
    scene lib1
    m "printing time."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "printers are ass here bro."
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no calvini."
        $ pulls += 1
        jump libab

label lf3:
    scene lib2
    m "group time."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "i ain't got no people to work with."
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no calvini."
        $ pulls += 1
        jump libab

label lf4:
    scene lib3
    m "loud place."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "too noisy."
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no calipers."
        $ pulls += 1
        jump libab

define nf1=False
define nf2=False
define nf3=False
define nf4=False
define nf5=False
define nf6=False
define nf7=False

label npd:
    scene parknew1
    m "7 MORE FLOORS OF SUFFERING!"
    menu npdd:
        "Floor 1" if not nf1:
            $ nf1=True
            jump nf1
        "Floor 2" if not nf2:
            $ nf2=True
            jump nf2
        "Floor 3" if not nf3:
            $ nf3=True
            jump nf3
        "Floor 4" if not nf4:
            $ nf4=True
            jump nf4
        "Floor 4" if not nf4:
            $ nf4=True
            jump nf4
        "Floor 5" if not nf5:
            $ nf5=True
            jump nf5
        "Floor 6" if not nf6:
            $ nf6=True
            jump nf6
        "Floor 7" if not nf7:
            $ nf7=True
            jump nf7
        "Leave":
            jump CC
label nf1:
    scene parknew1
    m "staff parking?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "place is boring"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no clavin!"
        $ pulls += 1
        jump npdd

label nf2:
    scene parknew2
    m "2 parking 2 furious?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "place is boringer"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no claviner!"
        $ pulls += 1
        jump npdd
label nf3:
    scene parknew3
    m "trifecta of parking floors!"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "place is boringest"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no korbin!"
        $ pulls += 1
        jump npdd

label nf4:
    scene parknew4
    m "parking 4 me! "
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "place is mildly interesting. Cool car."
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here!"
        $ pulls += 1
        jump npdd

label nf5:
    scene parknew5
    m "5 is his favorite number. remember that."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "place is interesting. Cooler cars."
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here!(!@&#^(!@))"
        $ pulls += 1
        jump npdd

label nf6:
    scene parknew6
    m "too 6y for dis deck"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "place is very interesting. Coolest cars."
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "here he is not."
        $ pulls += 1
        jump npdd

label nf7:
    scene parknew7
    m "7 like the 11?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "yeah, 7 like the 11."
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "here he ain't"
        $ pulls += 1
        jump npdd

define gds = False
define cs = False
define cf2 = False
define cf3=False
define cf4=False
define ba=False
define ra = False


label ccin:
    scene gdsenter
    m "oh god place so big."
    menu ccop:
        "Gourmet Dining Services" if not gds:
            $ gds = True
            jump gds
        "C-store" if not cs:
            $ cs = True
            jump cs
        "Randol" if not ra:
            $ ra = True
            jump ra
        "Check each Floor":
            jump fcheck
        "Keep Going":
            jump njit 
        "Go back":
            jump CC

label ra:
    scene randol
    m "good ol IGDAzon."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "FUCKING PACKIGE"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no calipers, not unbox therapy."
        $ pulls += 1
        jump ccop

label fcheck:
    m "alright what floor to go to..."
    menu fc:
        "Basement" if not ba:
            $ ba = True
            jump ba
        "Floor 2" if not cf2:
            $ cf2=True
            jump cf2
        "Floor 3" if not cf3:
            $ cf3=True
            jump cf3
        "Floor 4" if not cf4:
            $ cf4=True
            jump cf4
        "Go Back":
            jump ccin
label gds:
    scene gds3
    m "godly dining services."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "FOOD POISONING!"
        c "AAAAAAAA"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no calipers, not hungry man."
        $ pulls += 1
        jump ccop
    
label cs:
    scene cstore
    m "1 billion celsius please."
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "CAFFIENE YEAAAAAAA"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "no more caffiene for cal."
        $ pulls += 1
        jump ccop

label cf2:
    scene camp2
    m "study time?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "why am i here?"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "ain't here."
        $ pulls += 1
        jump fc
label cf3:
    scene camp3
    m "kareoke night?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "baka mi-yikes! im dame da not looking forward to this!"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "baka mi-dammit he ain't here."
        $ pulls += 1
        jump fc
label cf4:
    scene camp4
    m "what's even up here"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "pickin up schopenhaur!"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "ain't here?!@?#!?@#?21"
        $ pulls += 1
        jump fc

label ba:
    scene office2
    m "am i allowed in here?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "workin on club stuff!"
        c "one morbillion schopenhaurs!"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "i ain't supposed to be here."
        $ pulls += 1
        jump fc

define fen = False
define cul = False

label njit:
    scene njit
    m "belltower curse ooooooooooooo"
    menu nfuck:
        "Fenster Hall" if not fen:
            $ fen =True
            jump fen
        "Cullimore Hall" if not cul:
            $ cul =True
            jump cul
        "Go back":
            jump ccin


label fen:
    scene fenster
    m "tall ass building dafuq?"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "im on that fenster pack ykwim?"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "fenster more like fent lmao."
        m "he ain't here."
        $ pulls += 1
        jump nfuck

label cul:
    scene cullimore
    m "ew libral arts"
    if gacha == random.randint(1,100):
        if pulls == 0:
            $ winner = True
        show calb up
        c "THE LIBERALS!!!! THEY ARE MAKING THE FROGS GAY!!!!"
        c "found me!"
        m "yey"
        jump finale
    elif pulls == numEnd:
        show calb down
        c "took too long. mad."
        jump finale
    else:
        m "not here :\["
        $ pulls += 1
        jump nfuck

label finale:
    scene black with fade
    show calb neutral
    c "well."
    c "that's it."
    c "that's the whole route."
    c "you've made it."
    c "after all those reels, quizzes, and gacha, you can finally rest."
    c "was it worth it?"
    show calb up
    c "i sure hope so."
    show calb neutral happy
    c "thanks for beating the 'Dark Souls' of the Eboard dating sim."
    c "here's some fun facts about the route."
    c "the 64 reels total to just about 20 minutes."
    c "you liked [score] reels the same as i did."
    if winner:
        c "you found me on your first try, which is some insane luck."
        c "that is a 1% chance of happening."
        c "you should go gambling"
        c "surely if you win this, you can win anything."
    else:
        c "you found me after [pulls] tries."
    c "there are 36 quiz questions."
    c "the ChemE HW is based on real exams and HW i have taken."
    c "there is a 1 percent chance to find me at every location."
    c "at each location, there is unique dialogue for finding me and hitting pity."
    c "and there is a special dialogue you get to see if you find me on your first try."
    c "oh, and 1 more thing."
    if perfect:
        c "you have achieved the true ending."
        c "you literally can not do this game any more perfectly."
        c "you have seen everything, answered everything, and you've done EVERYTHING."
        c "you truly are THE Greatest Of All Time."
        c "you are the true Calvin fan."
        c "a real Calvinism follower."
        c "Thank you for everything."
        c "Have this image, as a promise to our everlasting friendship."
        window hide
        $ quick_menu = False
        show secret
        pause
        c "Goodbye, and good luck to everything you do."
        c "if nobody gotchu, i gotchu."
        return
    c "this is just a regular ending."
    c "there is a TRUE ending for liking/disliking every reel the same as I do, AND getting my quiz perfectly, AND my HW perfectly."
    c "i wish you luck, either in life, or getting that true ending."
    c "Thank you."
    c "Genuinely. Thank you."
    return


    
