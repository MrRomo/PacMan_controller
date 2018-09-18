import pygame


def readPad():
    pygame.init()

    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Initialize the joysticks
    pygame.joystick.init()
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()

        pads = joystick.get_numhats()

        padStr = joystick.get_hat(0)
        print(padStr)
        if(padStr[1]!=0):
            if(padStr[1]==1):
               
                return 0
            else:               
                return 1
        else:
            if(padStr[0]!=0):
                if(padStr[0]==1):
                    return 2
                else:               
                    return 3
            else:
                return 4

    clock.tick(20)