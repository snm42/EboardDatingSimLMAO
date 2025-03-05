init python:
    import math
    import random

    drawing_list = [
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 0]],

        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 0, 0, 0]],

        [[0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]],

        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

        [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]],
    ]

    path_list = [
        "images/sebsprite/prompts/prompt1.png",
        "images/sebsprite/prompts/prompt2.png",
        "images/sebsprite/prompts/prompt3.png",
        "images/sebsprite/prompts/prompt4.png",
        "images/sebsprite/prompts/prompt5.png"
    ]

    class DrawMe(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.state = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

            self.randindex = random.randint(0, 4)
            self.prompt = Image(path_list[self.randindex])

            self.whitebox = Solid("#FFFFFF", xsize=100, ysize=100)
            self.blackbox = Solid("#000000", xsize=100, ysize=100)
            self.time = 0
            self.showing_prompt = True
            self.score = 0
            self.done = False

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            if not self.showing_prompt:
                selected = renpy.render(self.blackbox, width, height, st, at)
                unselected = renpy.render(self.whitebox, width, height, st, at)

                for row in range(0, 10):
                    for col in range(0, 10):
                        drawpos = (100 * col, 100 * row)
                        if self.state[row][col] == 1:
                            r.blit(selected, drawpos)
                        else:
                            r.blit(unselected, drawpos)

                bar_size = round((self.time / 15.0) * 1000)
                if bar_size >= 1000:
                    bar_size = 1000
                
                bar = Solid("#FF0000", xsize=bar_size, ysize=100)
                bar_render = renpy.render(bar, width, height, st, at)
                r.blit(bar_render, (0, 1000))

                if self.time >= 15:
                    self.done = True
            else:
                prompt_image = renpy.render(self.prompt, width, height, st, at)
                r.blit(prompt_image, (0, 0))

                bar = Solid("#FF0000", xsize=round((self.time / 2.0) * 640), ysize=64)
                bar_render = renpy.render(bar, width, height, st, at)
                r.blit(bar_render, (0, 640))

                if self.time >= 2:
                    self.showing_prompt = False
                    self.time = 0
                    

            self.time += 0.04
            renpy.redraw(self, 0.04)
            return r

        def event(self, ev, x, y, st):
            if not self.done:
                if (renpy.map_event(ev, 'drag_activate')):
                    row = y // 100
                    col = x // 100
                    if row >= 10 or col >= 10:
                        pass
                    elif (self.state[row][col] == 1):
                        self.state[row][col] = 0
                    else:
                        self.state[row][col] = 1
            else:
                drawing = drawing_list[self.randindex]
                self.score = 0
                for row in range(0, 10):
                    for col in range(0, 10):
                        if drawing[row][col] == self.state[row][col]:
                            self.score += 1
                return 1

    class SnekEater(renpy.Displayable):
        
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.me = Solid("#009933", xsize=60, ysize=60)
            self.you = Image("images/sebsprite/snek.png")
            self.appledraw = Solid("#FF0000", xsize=32, ysize=32)
            self.hwall = Solid("#FFFFFF", xsize=32 * 32, ysize=32)
            self.vwall = Solid("#FFFFFF", xsize=32, ysize=32 * 32)
            self.background = Solid("#0000006d", xsize=32 * 32, ysize=32 * 32)

            self.direction = (1, 0)
            self.snake = [(3,3)]

            self.apple = (random.randint(0, 20), random.randint(0, 20))

            self.alpha = 1
            self.width = 1024
            self.height = 1024

            self.lose = False
            self.done = False

            self.active_time = 0
            self.score = 0

            self.input_in = False
            
            return

        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            thing = renpy.render(self.you, width, height, st, at)
            applerender = renpy.render(self.appledraw, width, height, st, at)
            hwallrender = renpy.render(self.hwall, width, height, st, at)
            vwallrender = renpy.render(self.vwall, width, height, st, at)
            bgrender = renpy.render(self.background, width, height, st, at)
            
            r.blit(bgrender, (0 + 512, 0))
            r.blit(hwallrender, (0 + 512, 0))
            r.blit(hwallrender, (0 + 512, 992))
            r.blit(vwallrender, (0 + 512, 0))
            r.blit(vwallrender, (992 + 512, 0))

            r.blit(thing, (512, 0))
            newhead = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
            
            for point in self.snake:
                if newhead[0] == point[0] and newhead[1] == point[1]:
                    self.lose = True
                    return r

            if newhead[0] < 0 or newhead[0] > 29 or newhead[1] < 0 or newhead[1] > 29:
                self.lose = True
                return r
            
            if self.active_time < 185:
                if newhead[0] == self.apple[0] and newhead[1] == self.apple[1]:
                    self.snake.insert(0, newhead)
                    self.score += 1
                    self.apple = (random.randint(0, 29), random.randint(0, 29))
                else:
                    self.snake.pop()
                    self.snake.insert(0, newhead)
            else:
                self.done = True


            bar_amount = round((self.active_time / 185.0) * 1024)
            if bar_amount > 1024:
                bar_amount = 1024
            bar = Solid("#FF0000", xsize=32, ysize=bar_amount)
            bar_render = renpy.render(bar, width, height, st, at)
            r.blit(bar_render, ( 512 + 992 + 32, 0))

            for point in self.snake:
                r.blit(thing, (32 * point[0] + 32 + 512, 32 * point[1] + 32))
            r.blit(applerender, (32 * self.apple[0] + 32 + 512, 32 * self.apple[1] + 32))

            self.input_in = False
            self.active_time += 0.04
            renpy.redraw(self, 0.04)
            return r

        def event(self, ev, x, y, st):

            # Compute the distance between the center of this displayable and
            # the mouse pointer. The mouse pointer is supplied in x and y,
            # relative to the upper-left corner of the displayable.
            if (renpy.map_event(ev, 'focus_left') and self.direction[0] != 1 and not self.input_in):
                self.direction = (-1, 0)
                self.input_in = True
            elif (renpy.map_event(ev, 'focus_right') and self.direction[0] != -1 and not self.input_in):
                self.direction = (1, 0)
                self.input_in = True
            elif (renpy.map_event(ev, 'focus_up') and self.direction[1] != 1 and not self.input_in):
                self.direction = (0, -1)
                self.input_in = True
            elif (renpy.map_event(ev, 'focus_down') and self.direction[1] != -1 and not self.input_in):
                self.direction = (0, 1)
                self.input_in = True
            
            if self.lose or self.done:
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

init:
    define light = Fade(.25, 0.0, .75, color="#fff")

default snek = SnekEater()
default sebDaysPicked = 0
default sebMood = 0
default sebScore = 0

default drawgame = DrawMe()

define fraudpenhauer = Character("Arthur Sebpenhauer", color="#eb34db")

define random_drawing_num = 0

define perfect_drawings = 0

screen drawgamescreen:
    add drawgame

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
    stop music
    scene gitc3
    show sebneutral
    with dissolve
    
    pause

    "This Sebastian guy seems chill"
    "I should get to know him"

    s "Yo what's good"
    s "I'm Ch- Sebastian"
    menu:
        "You look like Charlie moistcr1tikal":
            hide sebneutral
            show sebcheekysmile
            $ sebMood += 10
            pause
            hide sebcheekysmile
            show sebneutral
        "Sup loser":
            s "Damn..."
            s "You didn't have to remind me bro"
            $ sebMood -= 10
        "Nothing much, you?":
            s "Meh meh"
    
    s "Anyway I got some errands to run"
    s "Wanna hit the Dollar Tree?"
            
    menu:
        "Uhhh sure?":
            jump dollartreeoutside
        "Nah":
            s "Okay"
            s "..."
            s "..."
            s "Bye loser"
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
            s "When I'm done with you, they either won't find you, or they *will* find you in 20 different places"
            s "What?"
            $ sebMood -= 10
            hide sebdeadass
            show sebneutral
        "Yeah bro, idk why 7/11 gotta be so far":
            s "It is what it is"
    
    "*eagull noises*"
    hide sebneutral
    show sebdafoe
    s "Whoa what was that?"
    
    menu:
        "A bird?":
            hide sebdafoe
            show sebneutral
            s "Yeah probably"
        "A plane?":
            hide sebdafoe
            show sebneutral
            s "Nah that looked like a bird"
        "Somebody playing Bloons TD 6 on high def?":
            hide sebdafoe
            show sebcheekysmile
            s "Haha nice, those guys' laptops are always taking off in class"
            hide sebcheekysmile
            show sebneutral

    s "Anyway I'm sure you're wondering why we're here"

    menu:
        "No":
            s "Okay"
            s "Well"
            s "I don't care if you're gonna be an ass about it, I'll just tell you anyway"
            $ sebMood -= 2
        "Yeah what's going on?":
            s "So here's the situation dawg"

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
    pause
    s "YOOOO NO WAY!"
    menu:
        "What what what's happening?":
            s "Chat you're not gonna believe who I just saw at the energy drink aisle"
    hide sebcheekysmile
    show sebpoint at right
    s "It's Arthur Schopenhauer!"
    show sebpenhauer at left
    fraudpenhauer "Talent hits a target no one else can hit. Genius hits a target no one else can see"
    hide sebpoint
    show sebcheekysmile
    s "Yo Arthur, what are your opinions on energy drinks?"
    fraudpenhauer "A man can be himself only so long as he is alone; and if he does not love solitude, he will not love freedom; for it is only when he is alone that he is really free"
    s "That's what I'm saying bro"
    s "How bout you? Got any opinions on energy drinks?"
    menu:
        "Not particularly":
            hide sebcheekysmile
            show sebneutral
            s "Welp, I don't care, form one now"
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
        with light
        play sound thunder
        s "Your taste is nothing"
        s "It serves zero purpose"
        play sound vineboom
        s "You should reconsider your taste NOW"
        play sound vineboom
        s "And give somebody else a piece of that caffeine in the redbull can that's covered up so we don't have to drink that utter trash"
        play sound vineboom
        s "Cuz what are you here for?"
        play sound vineboom
        s "To worship redbull?"
        play sound vineboom
        s "Throw that shit out NOW!"
        play sound vineboom
        s "I mean that with a HUNDRED percent"
        play sound vineboom
        s "With a THOUSAND percent"
        $ sebMood -= 100
        jump checkDay
    elif sebScore < 5:
        s "Sooo you share [sebScore] opinions with me"
        hide sebneutral
        show sebdeadass
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
        fraudpenhauer "The greatest of follies is to sacrifice health for any other kind of happiness."
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
        fraudpenhauer "Great men are like eagles, and build their nest on some lofty solitude,"
        s "Haha you said it best bud"
        jump checkDay
    jump checkDay

label sebDay2:
    stop music
    "I've been meaning to meet with Sebastian again"
    "I hope he didn't actually stay up for 48 hours straight"
    "Then again... all those energy drinks we bought"
    scene honorgreen
    show gothsebside
    with dissolve
    pause
    "Speak of the devil"
    s "Yo je ne suis pas"
    menu:
        "What?":
            s "Don't worry about it"
            s "I just got tired of seeing Duolingo bird's fat cheeks on my notification bar every morning"
        "Je mange l'orange":
            s "Ah j'ai un enfant de poisson"
            $ sebMood += 5
        "Yo":
            s "Yo"
    s "Anyway"
    s "I made something for you"
    menu:
        "Oh?":
            hide gothsebside
            show gothsebdrawing
        "I don't want it":
            hide gothsebside
            show gothsebdisappointed
            s "Damn... okay"
            $ sebMood -= 20
            s "Bye I guess"
            jump checkDay

    s "Peek this"
    window hide
    image random_drawing = "images/sebsprite/drawings/draw" + str(renpy.random.randint(1, 11)) + " (Small).png"
    show random_drawing at truecenter
    with dissolve

    pause

    hide random_drawing
    with dissolve

    hide gothsebdrawing
    show gothsebforward

    menu:
        "What the fuck was that?":
            hide gothsebforward
            show gothsebdisappointed
            s "..."
            s "Soon"
            s "I mean what?"
            s "Anyway"
            $ sebMood -= 10
            show gothsebforward
            hide gothsebdisappointed
        "I-It... it's beautiful *sniffles*":
            s "Yeah it's pretty good right?"
            $ sebMood += 10
        
    
    s "Anyway, I want you to make one for me now"

    menu:
        "Nah":
            stop music
            s "Okay"
            s "Bye"
            $ sebMood -= 20
            jump checkDay
        "Okey":
            s "I want you to draw this for me..."

    $ drawgame.__init__()
    call screen drawgamescreen

    s "..."

    if drawgame.score < 90:
        stop music
        hide gothsebforward
        show gothsebdisgust
        s "Wow, you suck"
        s "Be better"
        $ sebMood -= 5
        jump checkDay
    elif drawgame.score == 100:
        s "Huh! You a mind reader or something?"
        s "Do it again"
        $ sebMood += 10
        $ perfect_drawings += 1
    else:
        s "Okay that's pretty good"
        s "Do it again"

    $ drawgame.__init__()
    call screen drawgamescreen

    if drawgame.score < 90:
        stop music
        hide gothsebforward
        show gothsebdisgust
        s "Guess last time was just a fluke"
        s "Be better"
        $ sebMood -= 5
        jump checkDay
    elif drawgame.score == 100:
        s "Whoa that's like, exactly how I envisioned it"
        s "Do it again"
        $ sebMood += 10
        $ perfect_drawings += 1
    else:
        s "Wow, you're one a roll"
        s "Do it again"

    $ drawgame.__init__()
    call screen drawgamescreen

    s "..."

    if drawgame.score < 90:
        stop music
        hide gothsebforward
        show gothsebdisgust
        s "Damn, I really thought"
        s "Be better"
        $ sebMood -= 5
        jump checkDay
    elif drawgame.score == 100:
        s "DAMN! That's perfect!"
        $ sebMood += 10
        $ perfect_drawings += 1
    else:
        $ sebMood += 20
        s "Wow!"
    
    if perfect_drawings == 3:
        s "You gotta be like, picasso or something"
        s "This is like my hit new comic Mortalslap"
        s "You could make a morbillion dollars outta these"
    else:
        s "Looks like we got quite the artiste here!"

    menu:
        "I mean they're okayyy":
            s "Nah this is art Mr. White"
        "Yeah I'm pretty goated":
            s "No kidding"
            s "I'm feeling like the day my Moby Huge arrived at my doorstep"
            s "It was essentially the second coming"
    
    s "Anyway I got stuff to do so uh"
    s "Yeah that's about it"
    s "Seeya"
    jump checkDay

label sebDay3:
    stop music
    scene njit
    show sebneutral
    with dissolve
    s "Hey"
    s "So what are we doing today?"
    menu:
        "I wanna go home":
            s "Oh okay"
            s "Bye"
            jump checkDay
        "Karaoke?":
            s "Hah! Just what I was thinking"
            $ sebMood += 5
        "I dunno, what do you want to do?":
            s "I was thinking karaoke"
    s "I live at Laurel, pull up!"
    jump sebKaraoke

label sebKaraoke:
    stop music
    scene kupftopins
    show bigmoistcheeky
    with slidedown

    pause

    
    s "You ready for karaoke?"

    menu:
        "Not really":
            s "Oh come on! It'll be fun"
            s "Here's one of my personal favorites, trust me, you'll love it"
        "AYE AYE CAPTAIN":
            s "I CAN'T HEAR YOU"
            s "sorry"
            s "Okay let's do this! I got just the song in mind"

    hide bigmoistcheeky
    with dissolve

    image karaoke_movie = Movie(play="images/sebsprite/sankeeater.webm", stop_music=True)
    show karaoke_movie
    call screen samplescreen
    hide karaoke_movie

    if snek.lose:
        show bigmoistsad
        s "What? You egg?"
        s "You suck ass, be better"
        $ sebMood -= 30
    elif snek.score < 50:
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
        s "Damn!"
        s "Not half bad!"
        s "You cooked so hard you took me to flavortown!"
        s "Bro brought the Beef Wellington to the Sunday afternoon cookout"
        $ sebMood += 20

    scene black
    with dissolve

    s "Alrighty well"
    s "Let's head back to my place, I got something to show you"
    jump sebEnding

label sebEnding:
    stop music
    scene laurelin
    show bigmoistneutral
    with dissolve
    pause
    s "..."
    if sebMood >= 0:
        stop music
        s "You know, it's been an interesting past few days"
        s "I know I'm not normally as eloquent as my fellow e-board members but I can be verbose when I need to be"
        s "And I'll be honest with you, I think the conversation we're about to have calls for a more serious tone"
        s "So I've been thinking a lot"
        s "About the time we've spent together"
        s "It's made me realize something important"
        s "I need to get away from my computer and..."
        s "Well..."
        s "Live more"
        s "I need to take myself away from the hustle bustle that makes every second feel like a dull, rhythmic step along the march of time"
        s "I need to get out and feel the warmth of the summer sun on my skin"
        s "And feel the cool breeze brush against the hair on my arms and legs and tickle me gently"
        s "I need to hear the chatter and laughter of people I love and care about"
        s "I need to take risks, and stumble and fall and get hurt and get back up again"
        s "I need to live my life like there's no tomorrow, I want to live every day with no regrets"
        s "I need to spin myself into a cocoon because while I might now be an ugly ugly caterpillar"
        s "In time I can transform myself into a beautiful beautiful butterfly"
        s "Thank you"
        s "For showing me this"
        s "But man let me tell you"
        s "I'm tired, oh so tired"
        s "I feel the kind of fatigue that sits in the deepest seat of my soul"
        s "It's sunk itself into my heart like a starving parasite feeding off any semblance of hope or happiness I might have"
        s "And I have found no remedy in my time on this planet"
        s "No amount of caffeine will take this burden away from me"
        scene black
        show bigmoistneutral
        with dissolve
        s "But that's where you come in"
        s "You"
        s "So full of color and life"
        s "The more I've gotten to know you, the more I find myself desiring this thing that you have"
        s "This..."
        s "This spirit"
        s "I've been thinking to myself"
        s "How can I capture this?"
        s "Your vivacious, beating heart?"
        s "And then I realized"
        s "The answer has been standing right in front of me"
        s "It's a beautiful thing"
        s "How life"
        s "Always"
        hide bigmoistneutral
        with dissolve
        s "Finds a way"
        pause
        "..."
        "..."
        ".."
        "."
        $ renpy.movie_cutscene("images/sebsprite/meatgrinder.webm")
        pause
        $ renpy.movie_cutscene("images/sebsprite/goodending.webm")
        show youdrink
        "You got the good ending! Probably..."
    else:
        s "I'm gonna be honest with you"
        hide bigmoistneutral
        show bigmoistsad
        s "You're kinda lame"
        s "Sorry not sorry"
        hide bigmoistsad
        show bigmoiststreaming
        s "Anyway I gotta get back to streaming"
        s "That's all"
        s "See ya"
        "Damn, you got the bad ending"
        "I don't even know how that's possible"
        show evilsebastian
        "Do better next time"
    
    