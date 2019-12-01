import random
import string


class Robot():

    existingNames = set()
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.name = self.getRandomName()
        self.existingNames.add(self.name)

    def getRandomName(self):
        while True:
            newName = self.computeRandomName()
            if newName not in self.existingNames:
                return newName
    
    def computeRandomName(self):
        computedName = ""
        computedName += random.choice(string.ascii_uppercase)
        computedName += random.choice(string.ascii_uppercase) 
        computedName += str(random.randrange(0,9)) 
        computedName += str(random.randrange(0,9)) 
        computedName += str(random.randrange(0,9))
        return computedName