# Class for person

class Person:

    def __init__(self, gender="F", creditsTaken=0, major="CS", age=0, enthusiasm=1, experience=1, goal="health", zip=30332):
        print("In person class")
        self.gender = gender
        self.creditsTaken = creditsTaken
        self.major = major
        self.age = age
        self.enthusiasm = enthusiasm
        self.experience = experience
        self.goal = goal
        self.zip = zip

    def interview(self):
        # self.generateGender()
        # self.generateCredits()
        # self.generateMajor()
        # self.generateAge()
        self.generateEnthusiasm()
        self.generateExperience()
        self.generateGoal()
        self.getZipCode()

    # method to generate attribute gender
    def generateGender(self):
        self.gender = input("Please enter your gender (M or F): ")
        return self.gender

    def generateCredits(self):
        self.creditsTaken = input("Please enter your current # of credit hours: ")
        return self.creditsTaken

    def generateMajor(self):
        self.major = input("Please enter your major: ")
        return self.major

    def generateAge(self):
        self.age = input("Please enter your age: ")
        return self.age

    def generateEnthusiasm(self):
        self.enthusiasm = input("Please enter your level of enthusiasm about working out on a scale of 1 (low) to 3 (high): ")
        return self.enthusiasm

    def generateExperience(self):
        self.experience = input("Please enter your level of experience in working out on a scale of 1 (beginner) to 3 (expert): ")
        return self.experience

    def generateGoal(self):
        self.goal = input("What is your workout goal? 1 (health / cardio), 2 (image / full body toning), 3 (strength / weightlifting): ")
        return self.goal

    def getZipCode(self):
        self.zip = input("What is the zip code of where you are working out? (5 digits only)")
        return self.zip

    def test(self):
        print("Person")
        print("gender")
        print(self.gender)
        print("creditsTaken")
        print(self.creditsTaken)
        print("major")
        print(self.major)
        print("age")
        print(self.age)
        print("enthusiasm")
        print(self.enthusiasm)
        print("experience")
        print(self.experience)
        print("goal")
        print(self.goal)



