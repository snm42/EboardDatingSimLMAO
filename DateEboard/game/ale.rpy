define aleDaysPicked = 0

label ale:
    $ aleDaysPicked +=1
    if aleDaysPicked == 1:
        jump aleDay1
    if aleDaysPicked == 2:
        jump aleDay2
    if aleDaysPicked == 3:
        jump aleDay3
    if aleDaysPicked == 4:
        jump aleDay4
    if aleDaysPicked == 5:
        jump myDinnerWithAlex

label aleDay1:
    scene black
    "I messaged Alex."
    "While waiting for him to respond, I found myself trawling the campus."
    show ckb
    show alex neutral at left
    m "Oh! Hi!"
    a "Hey."
    m "Funny running into you."
    show alex smirk at left
    a "Funny like a Woody Allen move or funny like a Woody Allen marriage?"
    m "Huh..?"
    show alex neutral at left
    m "I sent you some messages. Did you see them?"
    a "No, not yet."
    m "Well, I wanted to hang out. What are you up to?"
    a "I'm heading to class."
    m "And then?"
    a "I go to the library and grind out projects for the rest of the night."
    m "That's it?"
    a "That's it."
    hide alex with dissolve
    "(He didn't even wait for a reply)"
    scene black
    "Guess I'll have to try again."
    jump checkDay

label aleDay2:
    scene black
    "Alex wasn't responding to my messages today either. I decided to look for him in all his familiar spaces."
    show library
    "After searching for a while with no success, it was late at night and I found myself in the library."
    play music "Kevin MacLeod - J. S. Bach_ Toccata and Fugue in D Minor.mp3"
    show alex dio
    window hide
    pause
    "(...uhh...)"
    "(Is he... posing?)"
    window hide
    pause
    m "Hi."
    a "Hello."
    m "What are you doing?"
    a "Brooding. I'm in another one of my melancholies."
    "... how do you even respond to that?"
    m "You didn't text me back. Did you even see my DMs?"
    a "My apologies. I was busy."
    m "Brooding?"
    a "Working."
    a "They're burying me."
    "(Maybe I should try to lift his spirits)"
    menu:
        "(Commiserate)":
            m "Yeah man I got a lot of work too."
            a "We'll never be free."
            show alex smirk at center
            a "That's just our lot in life, I suppose."
            "(I think he feels a little better)"
        "(Tell a joke)":
            m "Well uhh you should invest in an oxygen tank then..."
            m "...so you can breathe."
            show alex neutral at center
            pause
            show alex ponder at center
            a "Wow you're in even worse melancholy than me."
            show alex neutral at center
            "(At least I shook him out of the pose)"
    "(Okay, now's my chance. I got him!)"
    m "So why are you so sad?"
    a "It's just the state of my life. The state of the world. A flower petal fell from a tree today."
    a "I mean, can you even believe it?"
    show alex dio at center
    pause
    "(And he's right back to his old ways)"
    m "Oh come on. Cheer up."
    m "Things can't be that bad."
    m "I mean, you have friends... you have a club..."
    hide alex dio with dissolve
    m "...you have me."
    m "Wait where did he go?"
    m "DID HE DISAPPEAR!?"
    scene black
    "This boy..."
    stop music
    jump checkDay

label aleDay3:
    scene black
    "Once more I sent Alex some messages. Once more, no reply."
    "At this point, I expected having to look for him."
    show kupfrianbelow2
    show alex neutral at left
    pause
    m "Why don't you ever check your messages?"
    show alex wishywashy at left
    a "...my phone's broken."
    m "...oh."
    m "That's no excuse!"
    show alex neutral at left
    a "What can I say? I'm a busy guy. Busy Guy Alex."
    "(You could say sorry)"
    m "Anyways..."
    m "You come here often?"
    a "No."
    m "..."
    show alex trade offer at center with moveinright
    a "I have a proposition for you."
    "(Is this my big break?)"
    a "I have this box of GDS pizza..."
    m "And you want to eat it together?"
    a "No, I need to get out of here actually."
    m "Oh... what topping?"
    show alex smirk at center
    a "Philly Cheesesteak!"
    m "Oh that sounds pretty good"
    show alex laugh at center
    a "Yeah but they threw Kraft Singles on top!"
    "He opened the box and showed me the pizza."
    "It was godawful."
    show alex trade offer at center
    a "Believe it or not, it's actually pretty good."
    "(I don't)"
    show alex neutral at center
    a "Anyways, you want it or not?"
    menu: 
        "Take the evil pizza":
            "(Maybe this is my way in!)"
            m "Give me the pizza."
            a "Sweet."
            show alex trade offer at center
            a "Pleasure doing buisiness with you."
            hide alex with moveoutright
            m "You're going??"
            "(He didn't even look back)"
            scene black
            "That pizza was crap."
            jump checkDay
        "Politely reject it":
            "(There's bravery and then there's just stupidity)"
            m "Oh I couldn't. It's all yours."
            show alex wishywashy at center
            a "Darn."
            show alex neutral at center
            hide alex with moveoutleft
            a "Alright bye."
            "(He left before I could even say anything)"
            scene black
            "Maybe I should have taken that pizza."
            jump checkDay


    
label aleDay4:
    "I sent Alex more messages. Not like he ever reads them."
    "I prowled around looking for him."
    "Not to brag or anything, but I'm getting good at finding him."
    show tiernan
    show alex neutral at left
    m "Is your phone still broken?"
    a "Actually I got a new one!"
    m "Wait, so why aren't you texting me back now?"
    show alex wishywashy at left
    pause
    m "I'm so lonely, Alex."
    show alex neutral at left
    a "Everyone I know is lonely"
    show alex ponder at left
    m "Please, why can't you just spend some time with me?"
    a "And God's so far away ♩~"
    a "~♩ And my heart belongs to no one ♩~"
    a "~♩ So, now, sometimes, I pray ♩~"
    a "♩ Take the space between us ♩ Fill it up some way ♩"
    hide alex with moveoutleft
    a "♩ Take the space between us..."
    "(He walked away, mid-conversation, absent-mindedly singing)"
    "(Was he even listening?)"
    "(And it wasn't even a good Police song)"
    scene black
    "I can't stand being jerked around like this."
    jump checkDay
