# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rose", who_color="#ff4a71")
define v = Character ("Violet", who_color="#81dff7")
define d = Character("Daisy", who_color="#e9e141")

# Character sprite definitions

# roses sprites
    # neutral
    # frown
    # blush
    # smile
    # surprised
    # just hallucinated

image roseDefault:
    "rdefault"

# violets sprites
    # default
    # frown
    # smile
    # awkward
    # angry

image viDefault:
    "violet_talksprite_default"
    xpos 0.34
    ypos 0.7


# daisys sprites
    # neutral
    # ^_^
    
image daisyDefault:
    "daisy_talksprite"
    xpos 0.56
    ypos 0.7

# The game starts here.

label start:


    scene bg test

    show spritebg zorder 1
    show roseDefault zorder 2
    show template zorder 3
    show viDefault zorder 5

    # notes:
    # background for the sprites is zorder 1
    # rose sprites are zorder 2
    # frame is zorder 3
    # daisy is zorder 4
    # vi is zorder 5
    


    r "Ah, hey, Vi..! You're up early!"
    v "..."
    r "(She didn't laugh... that makes sense, haha.)"
    v "'Hey' yourself. Sleep well?"
    r "Mhmm!"
    v "I'm glad, then."

    show daisyDefault zorder 4 with dissolve

    d "I don't quite appear in the story yet, but I wanted to cut in, regardless."
    "Narration test"

    # This ends the game.

    return
