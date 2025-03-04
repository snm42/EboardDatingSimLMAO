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
        jump myDinnerWithAlex

label myDinnerWithAlex:
    play music "Kevin MacLeod - Erik Satie_ Gymnopedie No 1.mp3"
    show my_dinner_with_alex
    pause
    scene dinner_bg2
    show dinner_alex_fanservice
    show dinner_fg2
    a "Oh, joining me for dinner?"
    a "Well.."
    a "Okay yeah take a seat."
    m "I thought you could use some company."
    a "Sure. It's been a miserable day. What a sour waste of life."
    m "(I think he's sad)"
    return

label aleDay1:
    scene black
    "I messaged Alex."
    "While waiting for him to respond, I found myself trawling the campus."
    show office2
    show alex neutral at left
    m "Oh! Hi!"
    a "Hey."

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
    a "It's just the state of my life. The state of the world. A flower petal from a tree today."
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
    "This boy..."
    stop music
    jump checkDay

