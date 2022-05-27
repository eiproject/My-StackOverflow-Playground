import cv2
import random
import time

states = ['alabama','alaska','arizona','arkansas','california',
'colorado','connecticut','deleware','florida','georgia','hawaii',
'idaho','illinois','indiana','iowa','kansas','kentucky','louisiana',
'maine','maryland','massachussets','michigan','minnesota',
'mississipi','missouri','montana','nebraska','nevada',
'new_hampshire','new_jersey','new_mexico','new_york',
'north_carolina','north_dakota','ohio','oklahoma','oregon',
'pennsylvania','rhode_island','south_carolina','south_dakota',
'tennessee','texas','utah','vermont','virginia','washington',
'west_virginia','wisconsin','wyoming']
while True:
    #choose a random state from the states list
    state = random.choice(states)
    #take a picture from the states folder, and display it
    img = cv2.imread('z9hpi.jpg') 
    cv2.imshow('guess the state!', img)
    cv2.waitKey(0)
    print('here')
    #checks if you typed the right state,
    #and gives an appropriate response
    guess = input("guess the state! (type stop to stop!)\n")
    if guess.lower() == state:
        print("Correct!")
        time.sleep(2)
        print("Lets do it again!")
    elif guess.lower() == "stop":
        break
    else:
        print("Nope! It was " + state + ". Keep trying!")
        time.sleep(2)

