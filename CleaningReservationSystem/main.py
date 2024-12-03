class Citizen:
    clients = []
    workers = []
    def __init__(self, name, surname, username, balance):
        self.name = name
        self.surname = surname
        self.username = username
        self.balance = balance

    @classmethod
    def signIn(cls, username):
        Citizens = cls.clients + cls.workers
        for Citizen in Citizens:
            if (Citizen.username == username):
                if Citizen in cls.clients:
                    print(username, ", welcome client")
                    clientScreen(Citizen)
                elif Citizen in cls.workers:
                    print(username, ", welcom worker")
                    workerScreen(Citizen)
                return
        print("Cannot found user. Type 1 for register: ")
        button = int(input())
        if button == 1:
            register()
        else:
            print("Exiting...")

def register():
    print("### REGISTER ###")
    print("Username: ")
    username = str(input())
    print("Name: ")
    name = str(input())
    print("Surname: ")
    surname = str(input())
    print("Type 1 for register as a client, Type 2 for register as a worker")
    choice = int(input())
    if(choice == 1):
        newCitizen = client(0, username, name, surname, 0)
        client.clients.append(newCitizen)
        mainScreen()
    elif(choice == 2):
        newCitizen = worker(0, 0,username, name, surname, 0)
        worker.workers.append(newCitizen)
        mainScreen()
    else:
        print("Type 1 or 2!")
        register()

class client(Citizen):
    def __init__(self, calledWorker, username, name, surname, balance, serviceReceivedUser, serviceType):
        self.__calledWorker = calledWorker
        self.__serviceReceivedUser = serviceReceivedUser
        self.__serviceType = serviceType
        super().__init__(name, surname, username, balance)

    def setcWorker(self, cWorker):
        self.__calledWorker = cWorker
    def getcWorker(self):
        return self.__calledWorker
    def getSReceivedUser(self):
        return self.__serviceReceivedUser
    def setSReceivedUser(self, SReceivedUser):
        self.__serviceReceivedUser = SReceivedUser
    def getserviceType(self):
        return self.__serviceType
    def setserviceType(self, serviceType):
        self.__serviceType = serviceType

class worker(Citizen):
    def __init__(self, value, experience, username, name, surname, balance, howManyPeopleStarred, sumStar):
        self.__value = value
        self.__experience = experience
        self.__howManyPeopleStarred = howManyPeopleStarred
        self.__sumStar = sumStar
        super().__init__(name, surname, username, balance)

    def getvalue(self):
        return self.__value
    def getexperience(self):
        return self.__experience
    def setexperience(self, experience):
        self.__experience = experience
    def gethowManyPeopleStarred(self):
        return self.__howManyPeopleStarred
    def sethowManyPeopleStarred(self, howManyPeopleStarred):
        self.__howManyPeopleStarred += howManyPeopleStarred
    def setsumStar(self, starSayi):
        self.__sumStar += starSayi
    def getsumStar(self):
        return self.__sumStar

def printStar(starCount):
    stars = ""
    star = "★"
    for x in range(1, starCount + 1):
        stars += star + " "
    return stars

def workerScreen(username):
    print("-------------------------\n### Welcome Worker", username.name, "###\n-------------------------")
    print("Balance:", username.balance)
    print("Value:", username.getvalue())
    print("Stars:", printStar(username.getexperience()))
    for client in Citizen.clients:
        if(client.getSReceivedUser() == username.username):
            print("------------------------------")
            print("Client currently being server: ", client.name, client.surname)
            if(client.getserviceType() == 1):
                print("Given service type: ", "normal")
            else:
                print("Given service type: ", "full")
            if(client.getserviceType() == 1):
                print("Earning:", username.getvalue())
                break
            elif(client.getserviceType() == 2):
                print("Earning:", username.getvalue()*2)
                break
    print("Type -1 for exiting")
    button = int(input())
    if(button == -1):
        mainScreen()
def clientScreen(username):
    print("-------------------------\n### Client Welcome", username.name, "###\n-------------------------")
    print("Balance:", username.balance)
    print("Until this time", username.getcWorker(), "called workers.")
    print("-------------------------\n## Worker List ##\n-------------------------")
    count = 1
    for worker in Citizen.workers:
        print(count, ")", "Name:", worker.name, "| Surname:", worker.surname, "| Username:", worker.username, "| Price:", worker.getvalue(), "| Stars:", printStar(worker.getexperience()))
        count += 1
    print("-------------------------")

    print("1. Buy Service")
    print("2. Buyed Services")
    print("3. Exit")
    choice = int(input())
    if(choice == 1):
        hizmetSatinAlma(username)
    elif(choice == 2):
        satinAlinanHizmet(username)
    elif(choice == 3):
        mainScreen()
        
def satinAlinanHizmet(username):
    print("-------------------------\n## Buyed Services ##\n-------------------------")
    if(username.getcWorker() == 0):
        print("There are no buyed services!")
        clientScreen(username)
    elif(username.getserviceType() == 1):
        for worker in Citizen.workers:
            if(username.getSReceivedUser() == worker.username):
                print(username.getSReceivedUser(), "buyed from user named", worker.getvalue(), "price of normal service")
    elif(username.getserviceType() == 2):
        for worker in Citizen.workers:
            if(username.getSReceivedUser() == worker.username):
                print(username.getSReceivedUser(), "buyed from user named", worker.getvalue()*2, "price of full service")
    print("Press 1 to delete and star the buyed service or press any key to go back: ")
    button = int(input())
    if(button == 1):
        print("You can leave a star by writing numbers from 1 to 5: ")
        star = int(input())
        if(star >= 1 and star <= 5):
            for worker in Citizen.workers:
                if(username.getSReceivedUser() == worker.username):
                    worker.sethowManyPeopleStarred(1)
                    worker.setsumStar(star)
                    worker.setexperience(round(worker.getsumStar() / worker.gethowManyPeopleStarred()))
                    print("Your stars are in the system.")
                    username.setcWorker(username.getcWorker() - 1)
                    username.setSReceivedUser("")
                    clientScreen(username)
        else:
            print("Please enter a number between 1 and 5!")
            satinAlinanHizmet(username)
    else:
        clientScreen(username)


def hizmetSatinAlma(username):
        print("Type the username of the person whose service you want to purchase: ")
        cWanted = str(input())
        for worker in Citizen.workers:
            if(cWanted != worker.username):
                print("Please type the username of the person whose service you want to buy!")
                clientScreen(username)
            else:
                if(len(username.getSReceivedUser()) > 0):
                    print("You already have a purchased service. Rate from 1 to 5 to terminate!")
                else:
                    print(cWanted, "type full to get full service or normal to get normal service (full service is 2 times the normal service):  ")
                    serviceType = str(input())
                    if (serviceType == "full"):
                        if(username.balance < worker.getvalue()*2):
                            print("full service could not be purchased due to insufficient balance!")
                            clientScreen(username)
                        else:
                            username.balance -= worker.getvalue()*2
                            username.setcWorker(username.getcWorker() + 1)
                            username.setSReceivedUser(cWanted)
                            username.setserviceType(2)
                            worker.balance += 2*worker.getvalue()
                            print("Successfully", cWanted, "from worker with user name", 2*worker.getvalue(), "priced full service has been purchased.")
                            clientScreen(username)
                    elif(serviceType == "normal"):
                        if(username.balance < worker.getvalue()):
                            print("normal service could not be purchased because your balance is insufficient!")
                            clientScreen(username)
                        else:
                            username.balance -= worker.getvalue()
                            username.setcWorker(username.getcWorker() + 1)
                            username.setSReceivedUser(cWanted)
                            username.setserviceType(1)
                            worker.balance += worker.getvalue()
                            print("Successfully", cWanted, "from worker with user name", worker.getvalue(), "priced normal service has been purchased.")
                            clientScreen(username)
                    else:
                        print("Please type the service you want to use as full or normal!")
                        clientScreen(username)

def mainScreen():
    print("-------------------------\n### CLEANING SYSTEM ###\n-------------------------")
    print("Username:")
    username = str(input())
    Citizen.signIn(username)

#Ready-made classes for quick check
worker.workers.append(worker(10, 0, "veliz", "Veli", "Zezar", 0, 0, 0))
worker.workers.append(worker(5, 0, "meliş", "Melih", "Erşan", 0, 0, 0))
client.clients.append(client(0, "emir", "Emircan", "Sezer", 100, "", 0))

mainScreen()
