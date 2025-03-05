init python:
    import math
    import random

    class SnekEater(renpy.Displayable):
        
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.me = Solid("#009933", xsize=60, ysize=60)
            self.you = Image("images/sebsprite/snek.png")
            self.appledraw = Solid("#FF0000", xsize=32, ysize=32)
            self.hwall = Solid("#FFFFFF", xsize=32 * 32, ysize=32)
            self.vwall = Solid("#FFFFFF", xsize=32, ysize=32 * 32)

            self.direction = (1, 0)
            self.snake = [(3,3)]

            self.apple = (random.randint(0, 20), random.randint(0, 20))

            self.alpha = 1
            self.width = 1024
            self.height = 1024

            self.lose = False

            self.active_time = 0
            self.score = 0
            
            return

        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            thing = renpy.render(self.you, width, height, st, at)
            applerender = renpy.render(self.appledraw, width, height, st, at)
            hwallrender = renpy.render(self.hwall, width, height, st, at)
            vwallrender = renpy.render(self.vwall, width, height, st, at)
            
            r.blit(hwallrender, (0, 0))
            r.blit(hwallrender, (0, 992))
            r.blit(vwallrender, (0, 0))
            r.blit(vwallrender, (992, 0))

            r.blit(thing, (0, 0))
            newhead = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
            
            for point in self.snake:
                if newhead[0] == point[0] and newhead[1] == point[1]:
                    self.lose = True
                    return r

            if newhead[0] < 0 or newhead[0] > 29 or newhead[1] < 0 or newhead[1] > 29:
                self.lose = True
                return r

            if newhead[0] == self.apple[0] and newhead[1] == self.apple[1]:
                self.snake.insert(0, newhead)
                self.score += 1
                self.apple = (random.randint(0, 29), random.randint(0, 29))
            else:
                self.snake.pop()
                self.snake.insert(0, newhead)


            for point in self.snake:
                r.blit(thing, (32 * point[0] + 32, 32 * point[1] + 32))
            r.blit(applerender, (32 * self.apple[0] + 32, 32 * self.apple[1] + 32))

            self.active_time += 0.04
            renpy.redraw(self, 0.04)
            return r

        def event(self, ev, x, y, st):

            # Compute the distance between the center of this displayable and
            # the mouse pointer. The mouse pointer is supplied in x and y,
            # relative to the upper-left corner of the displayable.
            if (renpy.map_event(ev, 'focus_left') and self.direction[0] != 1):
                self.direction = (-1, 0)
            elif (renpy.map_event(ev, 'focus_right') and self.direction[0] != -1):
                self.direction = (1, 0)
            elif (renpy.map_event(ev, 'focus_up') and self.direction[1] != 1):
                self.direction = (0, -1)
            elif (renpy.map_event(ev, 'focus_down') and self.direction[1] != -1):
                self.direction = (0, 1)
            
            if self.lose:
                return 1

            # Pass the event to our child.
            return None
    
    drink_ratings = {
        "alani": "ftier",
        "celsius green": "ftier",
        "redbull": "ftier",
        "celsius mango": "ftier",
        "celsius bluerasp": "ftier",
        "celsius kiwi": "ftier",
        "celsius watermelon": "ftier",
        "monster rehab": "ftier",
        "ultra rosa": "ftier",
        "venom": "ftier",
        "venom black": "ftier"
    }

    def drink_dragged(drags, drop):
        if not drop:
            return

        drink_ratings[drags[0].drag_name] = drop.drag_name

default snek = SnekEater()
default sebDaysPicked = 0
default sebMood = 0
default sebScore = 0

screen samplescreen:
    add snek

screen tierlist:
    draggroup:
        drag:
            drag_name "stier"
            xpos 0 ypos 0
            drag_raise True
            draggable False
            child "images/sebsprite/drinks/stier.png"
        drag:
            drag_name "atier"
            xpos 0 ypos 0.166
            drag_raise True
            draggable False
            child "images/sebsprite/drinks/atier.png"
        drag:
            drag_name "btier"
            xpos 0 ypos 0.333
            drag_raise True
            draggable False
            child "images/sebsprite/drinks/btier.png"
        drag:
            drag_name "ctier"
            xpos 0 ypos 0.5
            drag_raise True
            draggable False
            child "images/sebsprite/drinks/ctier.png"
        drag:
            drag_name "dtier"
            xpos 0 ypos 0.666
            drag_raise True
            draggable False
            child "images/sebsprite/drinks/dtier.png"
        drag:
            drag_name "ftier"
            xpos 0 ypos 0.833
            drag_raise True
            draggable False
            child "images/sebsprite/drinks/ftier.png"
        drag:
            drag_name "alani"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/alani (Small) (Custom) (Custom).jpg"
        drag:
            drag_name "celsius green"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/celsiusgreen (Small) (Custom) (Custom).jpg"
        drag:
            drag_name "celsius kiwi"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/celsiuskiwiguava (Small) (Custom) (Custom).jpg"
        drag:
            drag_name "monster rehab"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/kiwistrawberry (Small) (Custom) (Custom).jpg"
        drag:
            drag_name "ultra rosa"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/ultrarosa (Small) (Custom) (Custom).jpg"
        drag:
            drag_name "venom"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/venom (Small) (Custom) (Custom).jpg"
        drag:
            drag_name "redbull"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/redbull (Small) (Custom) (Custom).jpg"
        drag:
            drag_name "celsius bluerasp"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/bluerasp (Custom).jpg"
        drag:
            drag_name "celsius mango"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/mangopassion (Custom).png"
        drag:
            drag_name "celsius watermelon"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/celsiuswatermelon (Custom).png"
        drag:
            drag_name "venom black"
            xpos 0.25 ypos 0.25
            drag_raise True
            droppable False
            dragged drink_dragged
            child "images/sebsprite/drinks/venomblack (Custom).png"
    frame:
        xpadding 50
        ypadding 50
        textbutton "DONE" action [ToggleScreen("tierlist"), Jump("posttierlist")]
        

label seb:
    $ sebDaysPicked += 1
    if sebDaysPicked == 1:
        jump sebDay1
    elif sebDaysPicked == 2:
        jump sebDay2
    else:
        jump sebDay3

label sebDay1:
    scene gds
    show sebneutral
    with dissolve
    s "Yo what's good"
    s "I'm Ch- Sebastian"
    menu:
        "You look like Charlie moistcr1tikal":
            hide sebneutral
            show sebcheekysmile
            $ sebMood += 20
            ""
            hide sebcheekysmile
            show sebneutral
        "Sup loser":
            s "Damn... didn't have to remind me bro"
            $ sebMood -= 20
        "Nothing much, you?":
            s "Meh meh"
    
    s "Anyway I got some errands to run if you wanna come with"
    s "Wanna hit the Dollar Tree?"
            
    menu:
        "Uhhh sure?":
            jump dollartreeoutside
        "Nah":
            s "okay"
            s "..."
            s "bye loser"
            jump checkDay


label dollartreeoutside:
    scene dollatree
    show sebneutral
    with slidedown
    s "Damn, that was a 20 minute walk"
    menu:
        "This was your idea dawg":
            hide sebneutral
            show sebdeadass
            s "..."
            s "when I'm done either they won't find you, or they *will* find you in 20 different places"
            s "what?"
            $ sebMood -= 10
            hide sebdeadass
            show sebneutral
        "Yeah bro, idk why 7/11 gotta be so far":
            s "It is what it is"
    
    "Anyway I'm sure you're wondering why we're here"

    menu:
        "No":
            s "okay"
            s "well I don't care if you're gonna be an ass about it, I'll just tell you anyway"
            $ sebMood -= 2
        "Yeah what's going on?":
            s "so here's the situation dawg"

    s "I got a lotta work to do, need me some energy drinks"
    menu:
        "Aren't those bad for you?":
            s "Nah I'm sure it's fine"
        "You so real for that":
            hide sebneutral
            show sebcheekysmile
            s "Gotta get on that 48 hour grind"
            s "You know what I'm saying"  
            hide sebcheekysmile
            show sebneutral

    s "Alright, let's go in"          
    
    jump dollartreeinside

label dollartreeinside:
    scene dollatreeinside
    show sebcheekysmile
    with dissolve
    s "YOOOO NO WAY!"
    menu:
        "What what what's happening?":
            "Chat you're not gonna believe this"
    hide sebcheekysmile
    show sebpoint at right
    s "It's Arthur Schopenhauer!"
    show sebpenhauer at left
    "Talent hits a target no one else can hit. Genius hits a target no one else can see"
    hide sebpoint
    show sebcheekysmile
    s "Yo Arthur, what are your opinions on energy drinks?"
    "A man can be himself only so long as he is alone; and if he does not love solitude, he will not love freedom; for it is only when he is alone that he is really free"
    s "That's what I'm saying bro"
    s "How bout you? Got any opinions on energy drinks?"
    menu:
        "Not particularly":
            s "Welp, I don't care, make one now"
        "Yeah I got a few":
            s "Sweet, I'd be curious to hear what you think"
    s "I got a tierlist, I will judge you based on your opinions"

    scene tierlist
    hide sebcheekysmile
    hide sebpenhauer
    call screen tierlist

label posttierlist:
    scene dollatreeinside
    show sebneutral
    show sebpenhauer at left

    if drink_ratings['celsius green'] == "stier":
        $ sebScore += 1

    if drink_ratings['celsius kiwi'] == "stier":
        $ sebScore += 1

    if drink_ratings['alani'] == "atier":
        $ sebScore += 1
    
    if drink_ratings['venom'] == "atier":
        $ sebScore += 1
    
    if drink_ratings['ultra rosa'] == "atier":
        $ sebScore += 1

    if drink_ratings['celsius mango'] == "btier":
        $ sebScore += 1
    
    if drink_ratings['venom black'] == "btier":
        $ sebScore += 1

    if drink_ratings['celsius bluerasp'] == "btier":
        $ sebScore += 1

    if drink_ratings['monster rehab'] == "ctier":
        $ sebScore += 1

    if drink_ratings['celsius watermelon'] == "ctier":
        $ sebScore += 1

    if drink_ratings['redbull'] == "ftier":
        $ sebScore += 1
    s "..."
    
    if not drink_ratings['redbull'] == "ftier":
        hide sebpenhauer
        hide sebneutral
        show sebdeadass
        s "..."
        s "So about your opinion on red bull"
        s "I see you gave it [drink_ratings['redbull']]"
        s "I have one thing to say to you"
        hide sebdeadass
        scene lightning
        show sebkiller
        s "Your taste is nothing"
        s "It serves zero purpose"
        s "You should reconsider your taste NOW"
        s "And give somebody else a piece of that oxygen in the ozone layer that's covered up so we can breathe inside this blue trap bubble"
        s "Cuz what are you here for?"
        s "To worship redbull?"
        s "Throw that shit out NOW!"
        s "I mean that with a HUNDRED percent"
        s "with a THOUSAND percent"
        $ sebMood -= 100
        jump checkDay
    elif sebScore < 5:
        s "Sooo you share [sebScore] opinions with me"
        s "I'm gonna be honest"
        s "Your opinions are trashier than the villager CGI in the Minecraft movie"
        s "Yeah I don't think I want you picking my energy drinks for me"
        s "Bye"
        $ sebMood -= 10
        jump checkDay
    elif sebScore < 11:
        s "Sooo you share [sebScore] opinions with me"
        s "You have some pretty good takes honestly"
        s "I trust you with drink decisions, let's go grab some energy drinks"
        s "Whaddya say Arthur?"
        "The greatest of follies is to sacrifice health for any other kind of happiness."
        hide sebneutral
        show sebcheekysmile
        s "Haha you said it best bud"
        $ sebMood += 10
        jump checkDay
    elif sebScore == 11:
        hide sebneutral
        show sebcheekysmile
        s "WOW"
        s "Yeah we are literally the same person, 11/11"
        s "Okay yeah let's uh make ou- I mean get some energy drinks"
        s "Whaddya say Arthur?"
        "Great men are like eagles, and build their nest on some lofty solitude,"
        s "Haha you said it best bud"
        jump checkDay
    jump checkDay

label sebDay2:
    scene dorm
    show sebneutral
    with dissolve
    s "Yo what's good?"
    menu:
        "I'm alright":
            s "ai"

    jump sebDay3

label sebDay3:
    show bigmoistcheeky
    s "Hey wanna go out for some karaoke?"
    hide bigmoistcheeky
    call screen samplescreen

    if snek.lose:
        show bigmoistsad
        s "What? You egg?"
        s "You suck ass, be better"
        $ sebMood -= 30
    elif snek.score < 30:
        show bigmoistneutral
        s "..."
        hide bigmoistneutral
        show bigmoistsad
        s "Damn"
        s "I have never heard a worse singer in my life"
        s "It's like when Ninja ruined the low taper fade joke"
        s "Like damn bro I haven't seen shit this bad since Joker 2 came out"
        s "Be better dawg"
        $ sebMood -= 20
    else:
        show bigmoistneutral
        s "..."
        hide bigmoistneutral
        show bigmoistcheeky
        s "Zamn!"
        s "Not half bad!"
        s "You cooked that harder than Gordon Ramsay on Kitchen Nightmares"
        s "Bro brought the Beef Wellington to the Super Bowl cookout"
        $ sebMood += 20

    jump checkDay

label sebEnding:
    