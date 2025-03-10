default samDaysPicked = 0
default samEnd = "none"
default shoo = ""
default diningHall = True
default pubSec = False
transform real:
    center
    zoom 0.3

image sec attack:
    "images/samsprite/sec gun1.png"
    pause 0.2
    "images/samsprite/sec gun2.png"
    pause 0.1
    "images/samsprite/sec gun3.png"
    pause 2.0

label sam:
    if not diningHall:
        "..."
        "Honestly, I don't think I want to see him after that display at Taco Bell."
        "I should probably just spend the day relaxing."
        jump checkDay
    if pubSec:
        "..."
        "Honestly, I probably shouldn't see this guy after ratting him out to public safety."
        "I should probably avoid seeing him if possible."
        jump checkDay
    $ samDaysPicked += 1
    if samDaysPicked == 1:
        jump samDay1
    elif samDaysPicked == 2:
        jump samDay2
    else:
        jump samDay3

label samDay1:
    play music "Kevin MacLeod - Rollin at 5 - 210 - full.mp3"
    scene njit
    "..."

    "???" "I hope you haven't been waiting too long!"

    "You turn around and see Sam walking towards you."

    show sam normal at real

    j "I'm sure you haven't had too much experience with the food on campus, as a newly transferred student."
    j "Not like there's many options on campus anyways."
    j "In any case, I'd say it's best to talk over some of the barely acceptable food around the campus."

    m "That doesn't exactly make me excited to eat anything."

    show sam idk at real
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

        scene cstore
        show sam normal at real
        "You walk together with Sam to the Taco Bell (depicted as Cstore)."
        "You both order food and sit down in the general seating area located a little behind the place."

        j "God I love Taco Bell."
        j "I'd die a happy man if I could have Taco Bell for the rest of my life."

        m "The rest of your life?"
        m "Isn't that a bit excessive?"

        "You notice that Sam hasn't taken notice of your concern over his Taco Bell obsession."
        show sam taco at real
        "You stare at him as he devours a Crunchwrap whole."
        "Like, completely devours it."
        "Holy crap."

        m "Umm..."
        m "I think you should take it easy there."
        m "You might choke on it if you're eating that quickly."

        show sam stare at real
        "Sam suddenly stops eating and stares at you."

        j "Are you, perhaps, implying that this wonderous Crunchwrap not be eaten at such a brisk pace?"
        j "If I eat any slower, the wrap would become soggy."
        show sam stare at real:
            zoom 1.1
        j "A soggy tortilla would bring the value of the meal down several notches."
        j "The difference between a fresh Crunchwrap and a Crunchwrap of even 3 minutes old is enormous."
        show sam stare at real:
            zoom 1.2
        j "In fact, by saying that I should slow down, you would be implying that Taco Bell should be eaten mid."
        j "That would imply that you think Taco Bell, by extension, is a mid fast food chain."
        show sam stare at real:
            zoom 1.3
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
        show sam angy at real:
            zoom 1.3
        j "How DARE you even assume otherwise?!"

        "This fucking guy."

        m "Look man, I'm just worried-"

        j "YOU are the one who should be worried."
        j "The sheer disrespect coming from this uneducated idiot."
        j "If I weren't eating this Crunchwrap right now, I'd-"

        show sam stare at real
        "He takes a deep breath and calms down."

        j "You know what?"
        j "You aren't even worth talking to, lest my beloved meal grow even colder."
        j "I'll let you off the hook for now, since you're a new transfer student."
        j "But don't you dare talk to me or my Crunchwrap ever again."
        show sam angy at real
        j "Get the fuck out of my sight."
        show sam stare at real

        m "Okay."

        "You stand up and exit the campus center, not willing to even turn back at the absolute monster named 'Sam'."

        m "This guy's got issues."
        m "Thankfully I just don't have to talk to him ever again!"

        hide sam

        jump checkDay
    else:
        j "Yeah, I get it."
        j "Food is pretty expensive."
        j "That being said..."
        j "Can I bum a guest swipe?"

        m "A what?"

        hide sam normal
        scene gds3
        "You walk together with Sam to the dining hall, and use one of your very limited guest swipes."

        show sam shocked at real

        j "Damn, I haven't been here in years!"
        show sam normal at real
        j "I remember the last time I was here, I got insane food poisoning."
        j "I was knocked on my ass for the rest of the day."

        m "You couldn't have mentioned that before we decided to eat here?"

        "You see him laugh a little."

        j "Well it's probably nothing serious."
        show sam good at real
        j "I'm sure they've improved in the past few years."
        j "After all, what else would they be spending our precious tuition on?"
        show sam shocked at real
        j "A presidential suite?"
        show sam normal
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
        show sam stare at real
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

        hide sam stare
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
    play music "Kevin MacLeod - Rollin at 5 - 210 - full.mp3"
    scene maple
    "You are walking through Maple hall, entering Sam's dorm after he invited you over."
    "You walk into the dorm, and see Sam furiously drawing something on his iPad."

    scene sorm

    show sam normal at real

    m "Hey."

    show sam stare at real
    
    "He stops writing and looks up at you."

    j "Hey."

    "He waves you down to sit down across from him in the living room."
    "You sit down."

    show sam normal at real

    m "So..."
    m "You doing alright after that chicken parmesan incident?"
    m "I was worried you were going to die or something."

    show sam good at real

    j "Yeah, I'm doing alright."
    j "Actually, I've never been better!"

    show sam normal at real
    j "That experience has actually inspired me to make a substantial change in this campus."
    j "Usually I'm a pretty passive person."
    j "I don't get riled up by anything, unless someone insults something I'm deeply passionate about."
    
    "You see Sam tense up for a bit."

    show sam angy at real
    j "But this?"
    j "This absolutely sickens me!"
    j "I can't believe such a terrible thing can be allowed to exist unchecked."
    j "This dining hall is the lifeline for all these students, and they simply poison them!"

    show sam ipad at real

    "Sam holds up his iPad, showing his very atrocious art skills."

    j "As such, I have finally decided to take action."
    j "Outlined here is my battle plan."
    j "On this iPad lay the groundwork of my plan to overthrow the dining hall employees and start a rebellion."

    "You take a closer look at the iPad."
    "Detailed on the screen is the entire layout of the dining hall."
    "The positions of each employee are drawn clearly on the screen."
    "All of the furniture and potential obstacles are also detailed."
    "There are lines drawing the best places to walk through and plant... explosives?"
    "You can't even tell what the hell he's trying to draw on this screen."
    "You look back to Sam."

    show sam normal at real
    j "In order to cause change, one must disturb the peace and become noticed."

    m "Are you sure this is a good idea?"
    m "I mean, you're talking about potentially fighting against the administration!"
    m "You could get expelled!"

    j "Tsk, tsk, tsk."
    j "One must take such risks to get things rolling."
    j "Even if I'm expelled, then my actions will resonate among the students."
    j "If I'm to fall, another student will take my place and make a lasting change in this godforsaken campus."

    "Oh boy."
    "This guy has lost it."
    "Maybe the chicken parmesan has done more damage under the surface."
    "..."
    
    menu:
        "Should I report Sam to public safety?"
        "Report him.":
            "You pull out your phone discreetly and text public safety about a potential terrorist in the dorm."
            $ pubSec = True
        "Feed into his delusions":
            "You decide against texting public safety."
            "You think that this could be interesting to watch go down."
            $ pubSec = False
    
    if pubSec:
        show sam shocked at real
        j "Anyways, I'm starving!"
        j "I've been working on this plan ever since I got out of my capstone meeting."
        j "Do you wanna come along?"

        "You realize that you need to keep Sam here in order for public safety to come in."

        m "Actually..."
        m "I had a question regarding your plan."
        
        show sam normal at real
        "You decide to just stall Sam by asking stupid questions, and clarifying things on his drawing."
        "After a while, you see a few public safety people crowding by the entrance."

        m "Oh yeah, sorry for holding you up."
        
        m "Let's go grab some food!"
        show sam good at real
        j "Sure!"
        j "Lemme just pack my things up and let's head out."
        show sam normal at real
        "Before Sam could finish putting his things in his bag, two people barge into the room and walk towards Sam."

        show sam angy at real
        j "Hey!"
        j "Watch where you're putting-"


        "The public safety officer hits Sam swiftly in the back of his head, and he stops struggling."
        hide sam angy
        "Oh shit."
        "The two officers look at you."

        "???" "Thanks for the tip."
        "???" "We'll make sure that he is taken care of."

        "The two of them leave as quickly as they came in, leaving you in the room, alone."

        m "How quaint."

        "You leave the room as well, and exit his dorm."

        jump checkDay
    else:
        m "I think that this plan is pretty well written."
        m "However..."
        m "I do think that there are some flaws in the plan."
        
        j "Oh really?"
        j "Where?"

        m "So if you look over here..."
        show sam ipad at real
        "Together, you refined the plan on the attack on the dining hall."
        "Even with the new changes and modifications you made to the plan, somehow you feel that something will go wrong."
        "After all, this entire thing seems ridiculous to even execute."
        "Oh well, if anything, Sam's the one who will take the blame."

        show sam good at real
        j "You are a life saver!"
        j "I don't think this plan would have come together so nicely without your help!"
        j "Genuinely, I appreciate all the help you've given me so far."

        show sam normal at real
        "Sam seems to stop for a second and think."
        show sam shocked at real
        "Then he suddenly jumps up."

        j "Now that I think about it, I haven't helped you with anything!"
        show sam normal at real
        j "I was originally supposed to help you learn about the campus and the club but I was out cold before I could even get to it."
        j "Was there anything that you needed help with?"

        m "Actually, I remember I wanted to know some easy classes to take for my electives."
        m "A lot of my classes didn't transfer over nicely, so I lost a lot of credits right there."
        m "At this point, I really don't want to take more hard classes."
        m "What are your recommendations?"

        hide sam normal
        "You look at Sam, expecting an answer."
        "However, you see him out cold, lying down on top of his iPad."
        "This time, it looks like he was sleepily happily, however."

        m "I guess he has been working on this for a few hours at this point."
        m "Some sleep before the actual execution of the plan would help the success rate tremendously."
        
        "..."

        m "Not that the success rate is much higher than zero."

        "You leave the room and exit the dorm."

        jump checkDay
    
    jump checkDay

label samDay3:
    play music "Kevin MacLeod - Rollin at 5 - 210 - full.mp3"
    scene gds3
    "..."

    "???" "Today's the day!"

    show sam normal at real
    "You turn around and see Sam walking towards you."
    "He seems oddly excited for what seems to be a grand attempt at a terrorist attack."
    "Note: This is a work of fiction."
    "Sam isn't actually planning on committing a terrorist attack on July 12, 2027."

    m "Hey."
    m "How are you feeling for today?"

    show sam good at real
    j "Never better!"
    show sam normal at real
    j "In fact, all that sleep I got the other day helped me really lock in."
    j "I've been running through the plan all day, just to make sure that everything will work out."

    "You pause a minute."
    "You can barely even remember what the plan was."

    m "So..."
    m "Run me through the plan again?"

    j "Well, the main idea is to just destroy all of the equipment and furniture in the dining hall."
    j "By causing a forced renovation, the administration will have to pay attention to the dining hall for once."
    j "And maybe then they'll see the sorry state of affairs within."
    show sam good at real
    j "Surely there's no way that nothing will come out of this!"
    show sam normal at real

    m "Uh-huh."
    m "Well, I'll be here for moral support."
    m "You can handle this by yourself, right?"

    show sam good at real
    j "Of course!"
    
    "You see him walk past the counter and deeper into the food section."
    "He's not even concealing any weapons or anything."
    "His destruction and wrath will be done solely through adrenaline and willpower alone."
    "..."
    "This guy is so fucked."

    m "Wait up for me!"
    m "I gotta see this all go down."

    "You follow Sam further into the food hall, where he is standing in front of the chicken parmesan."

    show sam angy at real
    j "Take this!"
    
    "You see Sam raise his fist in the air, fully intending to flip the tray and spill the food everywhere."
    "However, his fist is suddenly stopped by someone standing behind him."
    
    m "Look out!"
    m "It's a public safety officer!"
    
    show sec neutral at center
    show sam shocked at real
    j "Oh shit!"

    show sam normal at real
    show sam normal at right
    "You see Sam break free from the officer's grasp and back away."
    show sec neutral at left

    "Officer" "We've been tracking your moves ever since you drafted up that attack plan."

    j "Damn did I forget to use a VPN?"

    "This guy is so stupid."
    "Upon closer inspection, you see that there are far more public safety officers than usual surrounding the area."
    "Seems like a pretty major oversight."

    j "In any case, you couldn't possibly agree with how they're handling things here!"
    j "Surely you see who is in the right here?"

    "The public safety officer shakes their head."

    "Officer" "Unfortunately, I don't make the rules."

    show sec gun3
    "The officer takes out... a gun?"
    "There's no way that they are actually allowed to use that."

    "Officer" "I'll give you one chance to back off."
    "Officer" "If you don't comply, I'll have to use the full force of my ability to prevent any more damage to the area."

    "You see Sam think in his head a little bit before speaking."

    j "How about this?"
    j "If I beat you in rock-paper-scissors, you'll let me enact my plan in peace."
    j "If you win, you get to put me down."

    menu:
        "Is this guy for real?":
            "What a moron."
        "Is this guy for real?":
            "What an idiot."
    
    show sec neutral
    "Officer" "Hmm..."
    "Officer" "Why not?"

    "No shot."

    jump rockPaperScissors

label samDay3Death:
    show sam rock at real
    show sam at right
    show sec rock at left
    "Sam and Officer" "Rock..."
    show sam up at real
    show sam at right
    show sec up at left
    "..."
    show sam rock at real
    show sam at right
    show sec rock at left
    "Sam and Officer" "Paper..."
    show sam up at real
    show sam at right
    show sec up at left
    "..."
    show sam rock at real
    show sam at right
    show sec rock at left
    "Sam and Officer" "Scissors..."
    show sam up at real
    show sam at right
    show sec up at left
    "..."
    "Sam and Officer" "Shoot!"
    if shoo == 'R':
        show sam rock at real
        show sam at right
        show sec paper at left
    elif shoo == 'P':
        show sam paper at real
        show sam at right
        show sec scissors at left
    else:
        show sam scissors at real
        show sam at right
        show sec rock at left
    
    # Cue gun
    pause 0.05
    show sec attack
    pause 0.05
    play sound "gun.mp3"
    
    hide sam
    "You see Sam sprawled out on the ground, bleeding out pretty severely."

    hide sec
    m "Oh shoot, I thought you would have had him in the bag."
    m "My b."
    m "I shoulda picked a different option."

    j "Bro are you blind he literally just started shooting"
    j "Whatever..."
    j "It seems like I've met my end"
    j "..."

    "He looks at you, but his gaze is unfocused."

    j "Guess it's over for me."
    j "."
    j "..."
    j "...."

    m "Oh I guess he's dead."
    m "No cool final words."
    m "..."
    m "womp womp"

    show sec neutral at center
    "Officer" "Don't think you're in the clear either."
    "Officer" "You are an accomplice to his crimes!"
    "Officer" "Eat this!"

    scene black
    play sound "gun.mp3"
    "Bang!"
    "You slowly feel your body go numb as you bleed out in front of Tiernan Lecture Hall 1."
    "..."
    "I guess the game was rigged from the start."

    "The End"

    return

label samEnding:
    scene black
    "Wait, isn't he dead?"

    "Oh well."

    "Guess I get the bad ending."

    return

label rockPaperScissors:
    "Officer" "Let's take this to Tiernan so that we don't have any witnesses."
    scene tierw
    show sam rock at real
    show sam at right
    show sec rock at left
    j "Quick, what should I pick?"

    m "Uhh..."

    menu:
        m "You should do..."
        "Rock":
            $ shoo = "R"
        "Paper":
            $ shoo = "P"
        "Scissors":
            $ shoo = "S"
        
    jump samDay3Death
