from asyncio.windows_events import NULL
import random
import sys
import time

########### global variables

dataList = []
currentEntry = NULL
currentAttraction = NULL

################### general functions
def showDatList(dataList):
    if currentEntry.WelcomeCenter == True and currentEntry.Timeless == True and currentEntry.Agile == True and currentEntry.Innovative == True and currentEntry.Reliable == True and currentEntry.Driven == True:
        currentEntry.Complete = True
    #bases cases, lengths 0,1,2
    if len(dataList) == 0:
        return NULL
    elif len(dataList) == 1:
        dataList[0].printDatShort()
        print("")
    elif len(dataList) == 2:
        dataList[0].printDatShort()
        print("   :::   ", end="")
        dataList[1].printDatShort()
        print("")
    else:
        dataList[0].printDatShort()
        print("   :::   ", end="")
        dataList[1].printDatShort()
        print("   :::   ", end="")
        dataList[2].printDatShort()
        print("")
        showDatList(dataList[3:])

def showrfid(dataList):
    if len(dataList) == 0:
        return NULL
    elif len(dataList) == 1:
        dataList[0].printNameRfid()
        print("")
    elif len(dataList) == 2:
        dataList[0].printNameRfid()
        print("   :::   ", end="")
        dataList[1].printNameRfid()
        print("")
    else:
        dataList[0].printNameRfid()
        print("   :::   ", end="")
        dataList[1].printNameRfid()
        print("   :::   ", end="")
        dataList[2].printNameRfid()
        print("")
        showrfid(dataList[3:])
        
        
def searchDatRfid(dataList, x):
    for i in dataList:
        if i.rfid == x:
            return dataList.index(i)
    return False

def swap(x):
    global currentEntry
    currentEntry = dataList[x]

########################## data entry class  
    
class dataEntry:
    def __init__(self, name, email):
        self.name = name
        self.rfid = random.randint(100, 200)
        self.email = email
        self.WelcomeCenter = False
        self.Timeless = False
        self.Innovative = False
        self.Agile = False
        self.Reliable = False
        self.Driven = False
        self.Complete = False
        #this at bottom
        self.addToList()
    
    
    
    def addToList(self):
        global dataList
        dataList.append(self)
    
    def printNameRfid(self):
        print("Name: " + str(self.name) + " | RFID: " + str(self.rfid), end="")
    
    def printDatShort(self):
        if self.WelcomeCenter == True and self.Timeless == True and self.Innovative == True and self.Reliable == True and self.Driven == True and self.Agile == True:
            self.Complete == True
        print("Name: " + str(self.name) + " | RFID: " + str(self.rfid) + " | E-mail: " + str(self.email) + " | Complete: " + str(self.Complete), end="")
        
    def printDatEnt(self):
        print("Name: " + str(self.name) + " | RFID: " + str(self.rfid) + " | E-mail: " + str(self.email) +" | Current Attraction: " + str(currentAttraction.name) + " | Status: " + str(currentAttraction.status) + " -->  ") #+ self.printadds(self.adds)) # + currentAttraction.showAtt())
        self.printadds()

    def printadds(self):
        print("\t WelcomeCenter: " + str(self.WelcomeCenter) + " | Timeless: " + str(self.Timeless) + " | Innovative: " + str(self.Innovative))
        print("\t Agile: " + str(self.Agile) + " | Reliable: " + str(self.Reliable) + " | Driven: " + str(self.Driven))
        
        
        
        
############################### Attraction class

class Attractions:
    def __init__(self, name, status):
        self.name = name
        self.status = status
    
    def updateEnt(self):
        global currentEntry
        global currentAttraction
        x = currentAttraction.name
        match x:
            case "WelcomeCenter":
                currentEntry.WelcomeCenter = True
                self.status = True
            case "Timeless":
                currentEntry.Timeless = True
                self.status = True
            case "Innovative":
                currentEntry.Innovative = True
                self.status = True
            case "Agile":
                currentEntry.Agile = True
                self.status = True
            case "Reliable":
                currentEntry.Reliable = True
                self.status = True
            case "Driven":
                currentEntry.Driven = True
                self.status = True
    
    def showAtt(self):
        print("Current Attraction: " + str(self.name) + " | Status: " + str(self.status))
       
    def returnToHub(self):
        global currentAttraction
        currentAttraction = WelcomeCenter()
        currentAttraction.updateEnt()
        print("")
        print("travelling to welcome center")
        time.sleep(2.0)
        currentAttraction.WCdesc()
        
        
       ############ WELCOME CENTER            
class WelcomeCenter(Attractions):        
    def __init__(self):
        Attractions.__init__(self,"WelcomeCenter", currentEntry.WelcomeCenter)
    
    def WCdesc(self):
        print("------------------------------------------------------------")
        print("This is the welcome center, the hub of the building. From here you can go to any other attraction, view all user data entries, switch to another entry, or exit the building (close the program).")
        print("")
        currentEntry.printadds()
        print("")
        print("Inputting another attraction name (from list above) will transport you to said attraction.")
        print("Other commands include exit or quit to close the program, database to see all user data entries, create to make a new entry (and set as current entry), current to see the current entry info and switch to transfer to another user data entry. (please ensure command entered is one word with no space after)")
        print("")
        temp = input("Enter Welcome Center Command: ")
        self.procWCcommand(temp)
    
    def procWCcommand(self, x):
        global currentEntry
        global currentAttraction
        match x:
            case "WelcomeCenter":
                print("travelling to welcome center")
                time.sleep(2.0)
                self.WCdesc()
                
            case "Timeless":
                print("")
                print("Travelling to Timeless Exhibit")
                currentAttraction = Timeless()
                currentAttraction.updateEnt()
                time.sleep(2.0)
                currentAttraction.Timedesc()
                
            case "Innovative":    
                print("")
                print("Travelling to Innovative Exhibit")
                currentAttraction = Innovative()
                currentAttraction.updateEnt()
                time.sleep(2.0)
                currentAttraction.Innovdesc()
                
            case "Agile":
                print("")
                print("Travelling to Agile Exhibit")
                currentAttraction = Agile()
                currentAttraction.updateEnt()
                time.sleep(2.0)
                currentAttraction.Agdesc()
                
            case "Reliable":
                print("")
                print("Travelling to Reliable Exhibit")
                currentAttraction = Reliable()
                currentAttraction.updateEnt()
                time.sleep(2.0)
                currentAttraction.Reldesc()
                
            case "Driven":
                print("")
                print("Travelling to Driven Exhibit")
                currentAttraction = Driven()
                currentAttraction.updateEnt()
                time.sleep(2.0)
                currentAttraction.Drivdesc()
                
            case "exit":
                sys.exit()
                
            case "quit":
                sys.exit()
                
            case "database":
                print("")
                showDatList(dataList)
                print("")
                input("Press anything to continue: ")
                print("")
                time.sleep(2.0)
                self.WCdesc()
                
            case "create":
                print("")
                print("Incorrectly entering commands (for example to few) will cause the program to crash")
                temp = (input("Enter: Name (space) E-mail: ")).split(" ")
                print("")
                currentEntry = dataEntry(temp[0], temp[1])
                currentAttraction = WelcomeCenter()
                currentAttraction.updateEnt()
                time.sleep(2.0)
                currentAttraction.WCdesc()
                
            case "switch":
                print("")
                showrfid(dataList)
                print("")
                print("Counting the list starts at 1 in the top left, 2 is one to the right of it and so on, counting them progressively in the same pattern you read books.")
                x = input("Please input the position in the list of the entry tag you want to swtich to from list above (input numbers outside range of list will result in program crash): ")
                y = int(x)-1
                swap(y)
                print("")
                currentEntry.printDatEnt()
                self.WCdesc()
                    
            case "current":
                print("")
                print("displaying info for current entry")
                currentEntry.printDatEnt()
                print("")
                time.sleep(2.0)
                self.WCdesc()
                
            case _:
                print("invalid command, please retry")
                time.sleep(2.0)
                self.WCdesc()
        
    ##################### TIMELESS     
class Timeless(Attractions):
    def __init__(self):
        Attractions.__init__(self,"Timeless", currentEntry.Timeless)
        self.cars = [1943,1946,1958,1971,1985,1999,2009,2021] 
        
    def Timedesc(self):
        print("------------------------------------------------------------")
        print("This is the timeless exhibit. Select a car from the following list and place it on ")
        print("the pad to see a video about the history of this era of Jeep or input returnToHub to go back to the Welcome Center.")
        print("")
        print(self.cars)
        print("")
        temp = input("Enter a Timeless exhibit command: ")
        self.procTimecommand(temp)
    
    def procTimecommand(self, x):
        if x == "returnToHub":
            print("")
            time.sleep(2.0)
            self.returnToHub()
            
        elif self.cars.count(int(x)) == 1:
            print("")
            print("A video displaying the history of the " + str(x) + " Jeep is displayed.")
            print("After the video concludes you have the opportunity to choose another Jeep time period.")
            print("")
            time.sleep(2.0)
            self.Timedesc()
            
        else:
            print("")
            print("invalid command, please retry")
            time.sleep(2.0)
            self.Timedesc()
            
   ############### INNOVATIVE
class Innovative(Attractions):
    def __init__(self):
        Attractions.__init__(self,"Innovative", currentEntry.Innovative)
        
    def Innovdesc(self):
        print("------------------------------------------------------------")
        print("This is the Innovative exhibit. It shows Edward's Creative dedication to pushing boundaries to make the best products.")
        time.sleep(3.0)
        print("")
        print("There are no extra options here. Input anything to return to the Welcome Center")
        temp = input("Enter anything to return: ")
        self.returnToHub()  
    
    
    
    ################ AGILE
class Agile(Attractions):
    def __init__(self):
        Attractions.__init__(self,"Agile", currentEntry.Agile)
        
        
    def Agdesc(self):
        print("------------------------------------------------------------")
        print("This is the Agile exhibit. It shows Edward's Creative use of lightweight and mobile materials to make the best products for any event.")
        time.sleep(3.0)
        print("")
        print("There are no extra options here. Input anything to return to the Welcome Center")
        temp = input("Enter anything to return: ")
        self.returnToHub()
        
   ################ RELIABLE
class Reliable(Attractions):
    def __init__(self):
        Attractions.__init__(self,"Reliable", currentEntry.Reliable)
        
    def Reldesc(self):
        print("------------------------------------------------------------")
        print("This is the Reliable exhibit. There is a restoration of an old Jeep engine, but it doesn't seem to do anything.")
        time.sleep(3.0)
        print("")
        print("You can either get closer (getCloser command) or returnToHub")
        temp = input("Enter anything to return: ")
        self.procRelcommand(temp)
        
    def procRelcommand(self, x):
        match x:
            case "getCloser":
                print("")
                print("A motion sensor on the engine goes off causing it to roar to life.")
                print("Now there is nothing left to do at this exhibit. Enter anything to return to the Welcome Desk.")
                temp = input("Input anything to return to Hub: ")
                self.returnToHub()
                
            case "returnToHub":
                self.returnToHub()
                
            case _:
                print("")
                print("Unrecognized command, returning to hub.")
                self.returnToHub
    
    
        
    ################ DRIVEN       
class Driven(Attractions):
    def __init__(self):
        Attractions.__init__(self,"Driven", currentEntry.Driven)    
    
    def Drivdesc(self):
        print("------------------------------------------------------------")
        print("This is the Driven exhibit. It is a restoration of an old jeep with an accompanying interactive touch pad.")
        print("")
        time.sleep(3.0)
        print("")
        print("The tablet has a light, horn and engine command. Your other option is to returnToHub")
        temp = input("Input Driven exhibit command: ")
        self.procDrivcommand(temp)
        
    def procDrivcommand(self, x):
        match x:
            case "light":
                print("")
                print("The headlights of the jeep flash on and off.")
                time.sleep(2.0)
                print("Returning to the start of the exhibit to explore all it has to offer.")
                self.Drivdesc()
                
            case "horn":
                print("")
                print("The old horn beeps a few times.")
                time.sleep(2.0)
                print("Returning to the start of the exhibit to explore all it has to offer.")
                self.Drivdesc()
                
            case "engine":
                print("")
                print("The engine roars to life just like the Reliable exhibit engine.")
                time.sleep(2.0)
                print("Returning to the start of the exhibit to explore all it has to offer.")
                self.Drivdesc()
                
            case "returnToHub":
                self.returnToHub()
    
    
    
    
######################## MAIN BLOCK

def main():
    random.seed(0)
    global currentEntry
    global currentAttraction
    print("")
    print("Incorrectly entering commands (for example to few) will cause the program to crash")
    temp = (input("Enter: Name (space) E-mail: ")).split(" ")
    print("")
    currentEntry = dataEntry(temp[0], temp[1])
    currentAttraction = WelcomeCenter()
    currentAttraction.updateEnt()
    time.sleep(2.0)
    currentAttraction.WCdesc()
    print("Main completed")
    
    
if __name__ == '__main__':
    main()