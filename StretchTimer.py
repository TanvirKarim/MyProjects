
import datetime as dt
import winsound

# startTime = 0

# increment time until a certain amount time has passed

# when the timer reaches a certain time notify the user to stretch

# After stretching restart the timer by making the start time zero

# program closes when the user closes it

userInput=input("Start the stretch timer? Type Yes Or No: ")

while userInput=="yes":

    startTime = dt.datetime.now()

    stopTime = startTime + dt.timedelta(minutes=30)

    def passTime():

        currentTime = dt.datetime.now()

        return currentTime

    print("Counting down time ...")

    while startTime <= stopTime:
        currentTime=passTime()
        if currentTime >= stopTime:
            winsound.Beep(440,1000)
            print("Stretch!")
            break

    userInput=input("Restart the stretch timer? Type Yes Or No: ")
    if userInput == "No":
        print("Stretch timer closed.")