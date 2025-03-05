label myDinnerWithAlex:
    scene black
    "I was in despair."
    "Giving up all hope, I headed to that place all men fear."
    "Gourmet Dining Services."
    "And by an odd series of circumstances, I had dinner with a man who had been avoiding me literally for a week."
    play music "Kevin MacLeod - Erik Satie_ Gymnopedie No 1.mp3"
    show my_dinner_with_alex
    pause
    scene dinner_bg2
    show alex dinner contemplation
    show dinner_fg2
    m "May I sit with you?"
    show alex dinner neutral
    a "Oh, joining me for dinner?"
    show alex dinner looking away
    a "Well.."
    show alex dinner neutral
    a "Okay yeah take a seat."
    m "I thought you could use some company."
    show alex dinner contemplation
    a "Sure. It's been a miserable day. What a sour waste of life."
    m "Oh, are you melancholy again?"
    show alex dinner neutral
    a "I'm always melancholy, heheh."
    a "You know, it's a lot to be a human being in the 21st century."
    show alex dinner contemplation
    a "I get overwhelmed by it really."
    show alex dinner questioning
    a "All this technology. All this modern thought. Rationalism, atheism, capitalism, wow."
    a "And what's it for? It feels like everyone's spiritually dead."
    a "What have our been technologies actually been built to accomplish, other than make some rich man richer?"
    show alex dinner looking away
    a "I hate my phone. I almost didn't want to buy a new one."
    show alex dinner point
    a "I turn on my phone and I get sucked into this stream of nonstop noise. The emails, the notifications..."
    show alex dinner contemplation
    a "Each one some new opportunity for you to prostitute yourself or some demand from some boss somewhere."
    show alex dinner looking away
    a "When my phone was dead, there was so much silence. And in that silence I could focus."
    show alex dinner neutral
    a "And in that focus, I felt less like a zombie and more like a human."
    menu:
        "\"I don't like my phone either.\"":
            show alex dinner neutral
            a "Right? They suck!"
        "\"I think you're exaggerating.\"":
            show alex dinner point
            a "I don't know. I really do think I mean this."
            show alex dinner looking away
            a "How am I supposed to know what I really want?"
            show alex dinner neutral
            a "Exaggerated or not, I feel something. I think that counts for something. I can't stand apathy."
            a "God, you see that so often these days. So many people have no opinions at all."
            show alex dinner questioning
            a "And they get shocked if you have opinions!"
            m "You're exaggerating again!"
            a "Am I? My friend, April, she says that to me all the time."
            show alex dinner point
            a "\"Wow, Alex. You have... opinions.\""
            show alex dinner questioning
            a "Of course I do. I'm alive."
            m "And the people with no opinions aren't?"
            show alex dinner neutral
            a "I don't know."
        "\"Is every conversation with you so... verbose?\"":
            show alex dinner questioning
            a "You've been hounding me all week looking to talk to me."
            a "Well! I'm here! We're talking!"
            a "Yes, I like to talk at length and I like to talk \"intellectually\", whatever that means. So what? I like it."
            a "I'm sorry if you don't. You can leave at any time. But if you're going to sit with me, this is how I am."
            a "This is what you signed up for."
            menu:
                "Continue.":
                    m "Alright. I'll keep an open mind. Let's keep going."
                    a "Okay."
                "Man, fuck this nerd.":
                    m "Maybe I could sit around and talk to you if you spoke like a normal human being."
                    m "Do you hear yourself? You're insane!"
                    a "What, do you think I'm pretentious?"
                    m "Pretentious doesn't even cut it!"
                    m "I'm getting out of here. I wasted my time with you."
                    scene black
                    "So ended my dinner with Alex."
                    "He's not a bad guy. Just ridiculous."
                    "I wish him well in life, but I don't want to talk to him ever again."
                    jump checkDay
    m "Sure, phones might not be great, but don't you like their convenience?"
    show alex dinner questioning
    a "What's with that? This modern obsession with \"convenience?\""
    show alex dinner looking away
    a "Is that really so valuable?"
    show alex dinner contemplation
    a "Well, I do actually like my phone. I shouldn't lie."
    a "Things are complicated."
    show alex dinner looking away
    a "It's not all just emails and notifications."
    show alex dinner neutral
    a "But most of the other things you view on phones is... slop."
    a "Meaningless. Vapid distraction."
    show alex dinner questioning
    a "I mean, how many of those shorts or memes or whatever do you even remember 5 seconds after you've stopped looking?"
    a "Undoubtedly some, but 99 percent you probably don't remember. And even the ones you do aren't earth-shattering."
    a "You can't even build a meaningful connection with any of them. They're gone before you even consider them."
    menu:
        "\"Tell me more.\"":
            show alex dinner point
            a "I really do think that all that noise coming at you will destory your brain. Like using a strong hose on a fragile wall."
            a "I don't think it was made to destroy minds. I think it was just made to make money. But that's the a side effect that corporations like."
            a "If somebody has their capacity for thought or individuality eroded away by constant distraction, then it's easier to profit off of them."
            a "I bet dictators would like that."
            show alex dinner looking away
            a "What's an antidote to fascism if not love? And how can a distracted person love?"
        "(Trenchant Insight)":
            m "Ah, but every so often, one of those does in fact change people's lives."
            m "You can't say they don't. Somebody will testify to it. Maybe even somebody right behind us."
            show alex dinner contemplation
            a "I guess you're right."
            m "And a lot of those are expressions of people. You will privilege older mediums over them?"
            show alex dinner looking away
            a "They're shallow expressions. There's just not enough time to do anything more."
            show alex dinner neutral
            a "And if there was, there's no guarantee anyone will appreciate it. You're given the viewer's attention, but not their focus."
            m "There's still something there."
            pause
        "(Bon mot)":
            m "I don't know. I saw the Earth shatter in a few of them."
            m "In one of them, the Earth was a slice of highly detailed cake. And the knife cut right through it."
            show alex dinner neutral
            a "You're funny."
    show alex dinner looking away
    a "I think about people today."
    a "Everyone's so lonely. So separate."
    a "People long for a connection."
    show alex dinner neutral
    a "I mean, you said the same to me yesterday."
    m "You actually heard me?"
    show alex dinner looking away
    a "Well, I think I was more absorbed in the song you reminded me of."
    show alex dinner neutral
    a "\"O My God\" by the Police. \"Everyone I know is lonely. And God is so far away.\""
    a "It rings true though, doesn't it? Everyone I know IS lonely."
    a "Art is one of those things that's supposed to connect us to each other. Especially when you really engage with it."
    a "But you need to engage with it. And the art needs to be true and have depth."
    a "I just don't think you get that with online \"content.\""
    show alex dinner looking away
    a "You know, when I went to Italy with the school years ago, we went to Vatican City, to St. Peter's."
    show alex dinner contemplation
    a "And I was there, walking through the rooms, all those rooms those Popes lived in for centuries."
    a "All adorned with frescoes and murals."
    show alex dinner neutral
    a "And I walk through this doorway and I look up and I see the School of Athens."
    show alex dinner questioning
    a "THE School of Athens. You know, that painting with Plato and Aristotle."
    show alex dinner point
    a "And Plato has his finger up to gesture to his Forms."
    show alex dinner questioning
    a "Right, I saw that painting in person. And it's huge. It's massive."
    show alex dinner neutral
    a "Plato and Aristotle are practically life-size."
    a "Our guide for the group — who I didn't even really like that much to be honest — was explaining to us the painting."
    a "She told us about how the artist used models of real people they knew for Plato and Arisotle."
    a "Their friends — painters and intellectuals."
    show alex dinner questioning
    a "And I start thinking about warm this painting is."
    a "About how it creates a community out of disparate elements."
    a "The philosophers painted are all from different centuries and countries. And the real people too who modeled for them."
    show alex dinner neutral
    a "And they're all united by their commitment to philosophy. Their contribution to a shared pool of knowledge."
    a "Almost two millennia of Western intellectualism, united in a single painting, drawing a thread through all of that."
    a "It makes you think."
    show alex dinner looking away
    a "It really moved me. I had tears in my eyes, honest! Not just from the painting, but from that meaning of it."
    show alex dinner contemplation
    a "I had a similar experience too another year when I saw Caravaggio's Calling of St. Matthew in person."
    show alex dinner questioning
    a "That's my favorite painting. It's wonderful. It's monumental. It stopped me cold dead."
    show alex dinner contemplation
    a "I look at that painting and I get this whole sense of the grandeur of life and the beauty of destiny."
    a "Matthew! I mean, there's a man who knew what to do with his life and THAT'S the moment he knew it."
    show alex dinner neutral
    a "I mean, that's a real experience with art, isn't it?"
    a "I connected with those paintings. With those people, people long dead, from a wholly different culture."
    show alex dinner looking away
    a "Do people have that with games?"
    menu:
        "Haven't you?":
            show alex dinner neutral
            a "Clever."
            a "Yeah, I guess maybe once or twice."
        "Of course.":
            m "People make connections all the time"
            "If all of gaming was Genshin Impact, I'd say throw it all away. It'd be rubbish. The world would be better off not having it."
    show alex dinner questioning
    a "I watched Andrei Tarkovsky's Stalker. It was incredible. I was absorbed to the screen. I could not look away, not for a moment."
    show alex dinner neutral
    a "And by the end, I was on the floor, sobbing. I'm not afraid to say it. I've never connected with any film like that before."
    show alex dinner contemplation
    a "I was sobbing because Tarkovksy's shots and characters could articulate my deepest pain and struggles. And they could do it better than I could."
    a "This man, who lived in another country and died decades before I was born knew the exact pitch of my life."
    show alex dinner neutral
    a "And he shared it. We were connected and united, across time and space."
    show alex dinner looking away
    a "I love games, but I don't think I've had a connection that deep yet."
    show alex dinner neutral
    a "But maybe one day, if we keep developing the medium, we'll have that connection."
    show alex dinner looking away
    a "At least that's what I tell myself."
    m "Is that why you make games?"
    show alex dinner neutral
    a "Yes. That's why."
    a "That, and also they do fascinate me. These simulacrums of space, portals to another world."
    show alex dinner contemplation
    a "Stalker knows me as if it was me. Yet, when I close my eyes, I see the hills of Shadow of the Colossus and the town of Pathologic."
    a "Those spaces have imprinted upon me."
    show alex dinner neutral
    a "Have you ever had a deep experience like that with a game?"
    menu: 
        '"Yes."':
            a "Really?"
            show alex dinner questioning
            a "What was it like?"
            menu:
                "It's personal. I couldn't tell you.":
                    show alex dinner contemplation
                    a "I understand."
                    jump regularEnding
                "I cannot express it.":
                    jump cannotExpress
        '"No."':
            jump regularEnding
        '"I cannot say."':
            show alex dinner questioning
            a "Why not?"
            menu:
                "I just don't think I've had that kind of experience.":
                    jump regularEnding
                "I cannot express it.":
                    jump cannotExpress

label cannotExpress:
    a "Why not?"
    menu:
        "It's difficult.":
            jump regularEnding
        "I do not have the words.":
            jump noWords

label noWords:
    show alex dinner looking away
    a "Take your time."
    menu:
        "I just can't do it right now.":
            a "I understand."
            jump regularEnding
        "You are imposing your limits upon me.":
            jump pathologic

label regularEnding:
    m "Aren't you going to eat more of your food?"
    show alex dinner contemplation
    a "I don't think think that's possible."
    m "So..?"
    show alex dinner neutral
    a "Well, I think that's it."
    m "That's it?"
    show alex dinner point
    a "What else need there be?"
    m "I guess I just expected more."
    show alex dinner neutral
    a "If you want more, maybe we should talk again."
    m "This was an odd experience."
    show alex dinner looking away
    a "Haters will say the whole thing is just yapping. But I think there's something there."
    m "Bye."
    show alex dinner neutral
    a "Bye-bye."
    jump checkDay

label pathologic:
    m "This isn't a real conversation."
    m "I can't actually respond to you."
    m "Sure, you give me a choice every now and then."
    m "And I pick whichever one I like best."
    m "But I can't pick any words you didn't write."
    m "You're just talking to yourself."
    m "What can I actually do?"
    m "You are imposing your limits upon me."
    show alex dinner neutral
    a "Did I hear you right? Who is it speaking?"
    menu:
        "It's Me.":
            show alex dinner contemplation
            a "...false alarm."
            jump regularEnding
        "It's the Player.":
            a "Our protagonist has lost their battle for freedom since the very day they were born. What about you?"
            menu:
                "I wanted to get to know my eboard. Even a make-believe one.":
                    a "But did you understand what these days all really were?"
                    menu:
                        "A parody of dating sims.":
                            a "And a pastiche of My Dinner with Andre!"
                            a "And now I've used it commentate on the nature of games."
                            menu:
                                "And who are you?":
                                    a "\"I am exactly what you think I am. A collection of poorly rendered pixels on a screen."
                                    show alex dinner neutral
                                    a "Why are you giving me that look?"
                                    a "Do not ascribe a more important role to me than the one I have been assigned from the very beginning."
                                    a "I'll fail a bigger role. The mask isn't expressive enough.\""
    p "Pathologic."
    a "Yep."
    p "You're plagiarizing it?"
    show alex dinner questioning
    a "What? No, no!"
    show alex dinner point
    a "This is a quotation."
    show alex dinner looking away
    a "I stand on the shoulders of giants. I always have. I'm making it plain now."
    show alex dinner neutral
    a "I want to continue the conversation they started. So why not use their words?"
    show alex dinner questioning
    a "And besides, those words? \"The mask isn't expressive enough?\""
    show alex dinner neutral
    a "I wanted somebody else to see those words."
    show alex dinner contemplation
    a "I remember when I first read them. They shook me to my very core."
    show alex dinner looking away
    a "They're beautiful. I could never get them out of my head since."
    a "We were talking about having a connection with games."
    a "Well, that was a connection I had."
    a "The exact kind that keeps me playing them and the exact kind that keeps me making them."
    show alex dinner neutral
    a "So I could one day have a connection with a player."
    hide window
    pause
    m "This was some dinner, huh?"
    stop music fadeout 2.0
    a "Yes."
    m "It's all over now, right?"
    a "Yeah."
    m "You barely ate your food."
    show alex dinner contemplation
    a "I have appetite issues."
    p "Goodbye Alex."
    show alex dinner neutral
    a "Goodbye."
    scene black
    p "I went home."
    p "And I looked at my games."
    p "I stared at screenshots and videos."
    p "And there wasn't some area..."
    p "there wasn't some character..."
    p "...that wasn't connected to some memory in my mind."
    "The End"
    return