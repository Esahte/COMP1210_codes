class HospitalPersonsInfo:
    # Construct a hospital object
    def __init__(self, name='', phoneNum=0, ID=0):
        self.name = name
        self.phoneNum = phoneNum
        self.ID = ID


class Patient(HospitalPersonsInfo):
    def __init__(self, name, phoneNum, ID, gender='', age=0, address=0, DOB=0, weight=0.0, height=0.0):
        super().__init__(name, phoneNum, ID)
        self.gender = gender
        self.age = age
        self.address = address
        self.DOB = DOB
        self.weight = weight
        self.height = height

    def addAge(self, newAge):
        self.age = newAge

    def NewAddress(self, newAddi):
        self.address = newAddi

    def weightGained(self, gained):
        self.weight += gained

    def weightLose(self, lose):
        self.weight -= lose

    def heightIncrease(self, increase):
        self.height += increase

class Doctor(HospitalPersonsInfo):
    def __init__(self, name, phoneNum, ID, qualifications, specialization, officeHrs, officeLocation):
        super().__init__(name, phoneNum, ID)
        self.qualifications = qualifications
        self.specialization = specialization
        self.officeHrs = officeHrs
        self.officeLocation = officeLocation

    def newOfficeHrs(self, newTime):
        self.officeHrs = newTime

    def newLocation(self, location):
        self.officeLocation = location

class Records:
    def __init__(self, last_checkup, doctoID, patientID, health_problems, proscriptions, cost, report):
        self.lastCheckup = last_checkup
        self.doctorID = doctoID
        self.patientID = patientID
        self.healthProblems = health_problems
        self.proscriptions = proscriptions
        self.cost = cost
        self.report = report

    def date_of_last_checkup(self, date):
        self.lastCheckup = date

    def addHP(self, problem):
        self.healthProblems.append(problem)

    def removeHP(self, problem):
        self.healthProblems.remove(problem)

    def addProscriptions(self, proscription):
        self.proscriptions.append(proscription)

    def removeProscription(self, proscription):
        self.proscriptions.remove(proscription)

    def newCost(self, price):
        self.cost = price

    def newReport(self, report):
        self.report = report
