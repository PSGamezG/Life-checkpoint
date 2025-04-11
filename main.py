print(
    "You wake up for the first time, your eyes still see fuzzy, all bright colors you don't even know the name of, your surroundings Unknown and the people that are looking at you, Who are they?"
)
print('...')
print('...')

print("Select your gender, our company believes in equality")
print("1) human 2) being")

while True:
    gender = int(input('Please enter 1 or 2: '))

    if gender == 1 or gender == 2:
        print(
            "Perfect! I'm glad you have no gender, you can proceed with the experience"
        )
        break
    else:
        print("Select a valid option")

print('...')
print('...')

print(
    "The memories start comming back, random names you can't quite catch, the name of the colors and some of your surroundings, you focus on some food displayed in front of you"
)
print('...')
print('...')

print("1) sandwich 2) apple 3) knife  4) chocolate")

while True:
    food = int(input('You are craving: '))
    caries = False

    if food == 1 or food == 2:
        print(
        "You bite it, the flavor fills your senses, and then you realize, you are alive, you've just had won your awareness, welcome to society..."
    )
        break
    elif food == 4:
       caries = True
       print(
        "You bite it, the flavor fills your senses, and then you realize, you are alive, you've just had won your awareness, welcome to society..."
    )
       break
    elif food == 3:
       print(
        "Haha, nice try, don't make me call the police"
    )
    else:
       print("Select a valid option")

print("...")
print("...")

print("You look around trying to gather more information")
print("1) ask the figures who they are 2) ask where are you going 3) stay quiet")

while True :
    question=int(input('You decide to: '))
    dementia=False
    
    if question == 1:
      print(
        "'What? who are we? someone must be sleepy still and cant recognize their own dad and mom'"
        )
      print("You nod and sit still, that sounds about right...")
      dementia=True
      break
    elif question == 2:
      print(
        "'Dont play dummy, you know we are going to school'"
    )
      print("You feel your eyes sting a bit, school is no fun...")
      break
    elif question == 3:
      print(
        "'Honey, your dad and I will leave you at school earlier today, we need to run some errands'"
        )
      print("You hmm in understading looking trough the window")
      break
    else: 
      print("enter a valid option")

print("...")
print("...")

print(
    "You are now at school a young 4 year old in the middle of the color activity, a mundane learning experience, other kids running around and screaming, you turn to your colors, what was the best one for the flower?"
)

print("1) blue 2) purple 3) red 4) pink")

while True:
    color=int(input('Obviously: '))

    if color == 1:
        color = "blue"
        break
    elif color == 2:
        color = "purple"
        break
    elif color == 3:
        color = "red"
        break
    elif color == 4:
        color = "pink"
        break
    else:
        print("Enter a valid option")

print("...")
print("...")

print("You start to paint your flower, life is easy and breazy, nothing could go wrong...")

print("...")
print("...")

print("Sweat, an incredible amount of it, a ray of sun sliding between your curtains, the sound of the alarm startle you")
print("'You are gonna be late for school!'")
print("Right, you are now a 14-year-old, teen years haven't been good to you, you can barely get up, the day ahead heavy on you. Down the breakfast is served")

print("1) grab breakfast 2) go to school without eating 3) take an apple")

while True:
    breakfast=int(input('I think today i will: '))
    depression=False

    if breakfast == 1:
        print("A nutritious breakfast!")
        break
    elif breakfast == 2:
        print("'Im not hungry today...'")
        depression=True
        break
    elif breakfast == 3 and caries:
        print("You start feeling your theeth hurt a sting in your mouth, you rush to the dentist")
        print("You have now a fake theeth and are running late for school")
        break
    elif breakfast == 3:
        print("An apple a day keeps the creep away")
        break
    else:
        print("Enter a valid option")

print("...")
print("...")

print(
    "Now you are at the school, you breathe deeply fighting the urge of run away, you see people running around, gossiping, just the cumulus of mindless people and you are a slave of your own conscience, you walk to your first class."
)

print("1) Biology 2) English 3) Maths 4) Art")

while True:
    lecture=int(input('Finally, my favorite class: '))

    if lecture == 1 or lecture == 2 or lecture == 3:
        print("You enter ready to learn, then your Art teacher comes in")
        print("'Your teacher was sick so I'll be giving an extra class to fill in for him'")
        print("'Today we will explore Fibonacci sequence in art and nature, combining mathematics and the beauty of the world, one never further apart from the other...'")
        break
    elif lecture == 4:
        print("You enter ready to learn, exited to see your Art teacher")
        print("Today we will explore Fibonacci sequence in art and nature, combining mathematics and the beauty of the world, one never further apart from the other...")
        break
    else:
        print("Enter a valid option")

print("...")
print("...")

print("1) Listen to it 2) Dissociate 3) Take as many notes as you can 4) Fall sleep")

while True:
    future=int(input('Rightnow I just want to: '))

    if future == 1:
        future = 1
        print("You listen carefuly as the teacher starts explaining the mathematics behid...")
        break
    elif future == 2:
        future = 2
        print("The class continues as you dozz off looking into the distance...")
        break
    elif future == 3:
        future = 3
        print("You start taking notes metodically trying to stay focus...")
        break
    elif future == 4:
        future = 4
        print("The teachers voice slowly fades into the distance as your eyes start to feel heavy...")
        break
    else:
        print("Enter a valid option")

print("...")
print("...")

print(
    "A tiring day of school, you lay on your bed, at least there is little homework, your mom is making a good meal and some game is waiting for you, it's not that bad"
)

print("...")
print("...")

("Time passed just like water it ran trough your fingers, university was hard on you but you managed somehow to fight back and the result of it was...")

print("...")
print("...")

if dementia:
    print("At first it was little details, like the keys, your phone, the name of some friends, but eventually it escalated, you started to lose track of reality, your memory gettig lost bewtween the fantasy, the pills and your pain.")
    print("Society is not designed for broken people, so you ended up being admitted to a mental institution and there you stayed...")

if future == 1 and not depression:
    print(
        "You are standing on the shore, the salty breeze against your face a peaceful ocean stands in front of you, you had a " + color + " shirt, it remembered you of that flower so many years ago"
        )
    print("life was not easy but you managed to make the bes of it and you receive the new day with a smile...")

if future == 1 and depression:
    print(
        "The weather is cold, you hold your " + color + " mug a childood memory attached to it, looking throurg the mirror the memories of life reflected on tiny drops"
    )
    print("you breath deeply, trying to ease your mind from spiriling, its has been days since the relapse and you think you might be too old to feel this way")

if future == 2 or future == 4 and not depression:
    print(
        "The sound of music coming down the street makes you turn around, the possibilities of the day giving you the same rush as wen you were young"
        )
    print("you start walking towards the noise a smile on your face and a " + color + " flower in your pocket")

if future == 2 or future == 4 and depression:
    print(
        "You got the paper on your front door, the heavy weight of another day trying to climb up, there is not much to do today"
    )
    print("you let out a deep breath, the day going by too fast and too slow at the same time")

if future == 3 and not depression:
    print(
        "Working at a call center caused you mental disorders, you are now old trying to live the best you can"
        )
    print("however, you can't answer or make calls")

if future == 3 and depression:
    print(
        "Working at a call center made your mental disorders worst, multiple therapy sessions, spiritual retirements, medical marihuana, all of them helped you exist"
    )
    print("'Never work at a Call Center' human is how the kids on the block call you.")

print("...")
print("...")

print("This is the end of your life, thank you for playing.")
print("created and written by Paula Gamez")