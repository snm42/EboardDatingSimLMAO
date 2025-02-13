default samDaysPicked = 0
default samEnd = "none"

label sam:
    $ samDaysPicked += 1
    if samDaysPicked == 1:
        jump samDay1
    elif samDaysPicked == 2:
        jump samDay2
    else:
        jump samDay3

label samDay1:
    "..."

    "???" "I hope you haven't been waiting too long!"

    "You turn around and see Sam walking towards you."

    j "I'm sure you haven't had too much experience with the food on campus, as a newly transferred student."
    j "Not like there's many options on campus anyways."
    j "In any case, I'd say it's best to talk over some of the barely acceptable food around the campus."

    m "That doesn't exactly make me excited to eat anything."

    j "Guess you'll have to suck it up."
    j "Anyways, I'll leave the final decision up to you."
    j "Since we're already here in campus center, I guess you can feel free to pick anything that's within 200 feet or so."
    j "It's pretty cold outside, so I'd rather not have to go back outside if we can help it."

    "You take a quick glance at your surroundings."
    "There's nothing particularly of note about any of the places that are in your immediate vicinity."

    m "Umm..."
    m "Could you limit it down to less places for me?"
    m "Like, what two places would you recommend eating at?"

    j "I've really only eaten from the Taco Bell and the dining hall."
    j "I wouldn't recommend the dining hall per se, but it does come free with your fucking Xbox, so that's probably a good thing to consider."

    m "Hmm..."

    menu:
        m "I guess I'll go for the..."
        "Taco Bell":
            m "...Taco Bell."
            $ diningHall = False
        "Dining hall":
            m "...Dining hall."
            $ diningHall = True
    
    if not diningHall:
        j "Real."

        "You walk together with Sam to the Taco Bell."
        "You both order food and sit down in the general seating area located a little behind the place."

        j "God I love Taco Bell."
        j "I'd die a happy man if I could have Taco Bell for the rest of my life."

        m "The rest of your life?"
        m "Isn't that a bit excessive?"

        "You notice that Sam hasn't taken notice of your concern over his Taco Bell obsession."
        "You stare at him as he devours a Crunchwrap whole."
        "Like, completely devours it."
        "Holy crap."

        m "Umm..."
        m "I think you should take it easy there."
        m "You might choke on it if you're eating that quickly."

        "Sam suddenly stops eating and stares at you."

        j "Are you, perhaps, implying that this wonderous Crunchwrap not be eaten at such a brisk pace?"
        j "If I eat any slower, the wrap would become soggy."
        j "A soggy tortilla would bring the value of the meal down several notches."
        j "The difference between a fresh Crunchwrap and a Crunchwrap of even 3 minutes old is enormous."
        j "In fact, by saying that I should slow down, you would be implying that Taco Bell should be eaten mid."
        j "That would imply that you think Taco Bell, by extension, is a mid fast food chain."
        j "Is that what you're trying to say?"

        "He continues staring at you, intensely."
        "You feel the intense pressure of his words fill the air around you."

        m "Not at all!"
        m "I don't think Taco Bell is mid at all."
        m "It's just that-"

        j "I don't think you understand the gravity of the situation."
        j "You are looking at the resident Taco Bell eater of the campus."
        j "I have over 6 million rewards points available in my account."
        j "I think I'd know if I was eating this Crunchwrap at a reasonable pace."
        j "How DARE you even assume otherwise?!"

        "This fucking guy."

        m "Look man, I'm just worried-"

        j "YOU are the one who should be worried."
        j "The sheer disrespect coming from this uneducated idiot."
        j "If I weren't eating this Crunchwrap right now, I'd-"

        "He takes a deep breath and calms down."

        j "You know what?"
        j "You aren't even worth talking to, lest my beloved meal grow even colder."
        j "I'll let you off the hook for now, since you're a new transfer student."
        j "But don't you dare talk to me or my Crunchwrap ever again."
        j "Get the fuck out of my sight."

        m "Okay."

        "You stand up and exit the campus center, not willing to even turn back at the absolute monster named 'Sam'."

        m "This guy's got issues."
        m "Thankfully I just don't have to talk to him ever again!"

        jump checkDay
    else:
        j "Yeah, I get it."
        j "Food is pretty expensive."
        j "That being said..."
        j "Can I bum a guest swipe?"

        m "A what?"

        "You walk together with Sam to the dining hall, and use one of your very limited guest swipes."

        j "Damn, I haven't been here in years!"
        j "I remember the last time I was here, I got insane food poisoning."
        j "I was knocked on my ass for the rest of the day."

        m "You couldn't have mentioned that before we decided to eat here?"

        "You see him laugh a little."

        j "Well it's probably nothing serious."
        j "I'm sure they've improved in the past few years."
        j "After all, what else would they be spending our precious tuition on?"
        j "A presidential suite?"
        j "Of course not!"

        "The both of you grab whatever food was available and find a seat."

        j "The choices today weren't too bad, huh?"
        j "The chicken parmesan seems to be pretty good."

        m "Well, I don't exactly have a basis of comparison considering this is my first time at the dining hall."

        j "Oh I guess that's right."

        "You see Sam start to eat the thing he calls 'food' on his plate."
        "If anything, that chicken looked severely undercooked."
        "May God save this poor guy's soul."

        m "So I called you up today because I wanted to learn more about the campus."

        j "Oh word."
        j "What did you want to know more about?"

        m "I actually have a lot of electives that I still need to take, since most of my credits didn't transfer correctly from where I went to school before."
        m "Do you have any recommendations on what classes are fairly easy?"
        
        "You stare at Sam, expecting an answer."
        "However, he just stares back blankly, as if he didn't hear a single word you said."

        m "Uhh..."
        m "Hello?"

        "No reaction."

        m "Hey!"
        m "Earth to Sam!"

        "Suddenly, you see Sam fall face forward, his head slamming into the plate of food in front of him."

        m "What the?"

        "You try tapping him on the shoulder, but there is no reaction."

        m "This doesn't look good."

        "You look around and try to explain the situation to some random stranger nearby."

        m "Uhh, yeah so this guy just kinda passed out while I was talking to him."
        m "Do you think he's gonna be okay?"
        m "Should I call for public safety or something?"

        "The stranger looks at you for a second, before looking over at mister out cold."
        "He lifts Sam's head up, as if to inspect the contents of his plate, before dropping it and having Sam's face slam down again."

        "???" "Nah, it's probably fine."
        "???" "Everyone who eats the chicken parmesan just knocks out cold after a few."
        "???" "It's like fast acting poison."
        "???" "That shit is so ass, I'm shocked they can still be serving that shit to the public."

        "You see the stranger just shrug his shoulders as he picks up his plate and walks away."

        m "I guess that's a normal occurrence."

        "You pick up your plate, not willing to ingest any more potential toxins from this dining hall."

        m "He should be fine."
        m "I can always check on him another day and see if he's recovering okay."

        "You stand up and exit the dining hall, leaving it's most recent casualty knocked out at the table."

        jump checkDay

label samDay2:
    # Plan out a full frontal assault on GDS (library breakout room)
    "goon 2"

    # Ending 2 - Snitch on Sam
    # Locks out of visiting for the rest of the days
    # Sam is forcibly removed from the library.
    
    jump checkDay

label samDay3:
    # Fight against public safety (club penguin card-jitsu)
    "goon 3"

    # Ending 3 - Sam dies

    # Ending 4 - Sam lives
    jump checkDay

label samEnding:
    # If sam dead, visit gravestone
    # If sam alive, he gets assassinated
    jump checkDay