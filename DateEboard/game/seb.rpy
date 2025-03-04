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


default snek = SnekEater()
default sebDaysPicked = 0

screen samplescreen:
    add snek

label seb:
    
    $ sebDaysPicked += 1
    if sebDaysPicked == 1:
        jump sebDay1
    elif sebDaysPicked == 2:
        jump sebDay2
    else:
        jump sebDay3

label sebDay1:
    show bigmoistcheeky
    s "Hey wanna go out for some karaoke?"
    hide bigmoistcheeky
    call screen samplescreen

    if snek.lose:
        show bigmoistsad
        s "What? You egg?"
        s "You suck ass, be better"
    jump checkDay

label sebDay2:
    s "Let's play uhh"
    jump checkDay

label sebDay3:
    s "What it's like to be drank"
    jump checkDay