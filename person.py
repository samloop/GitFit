# Class for person

class Person:

    def __init__(self, gender="F", creditsTaken=0, major="CS", age=0, injury=False, enthusiasm=1, experience=1, goal="health"):
        self.gender = gender
        self.creditsTaken = creditsTaken
        self.major = major
        self.age = age
        self.injury = injury
        self.enthusiasm = enthusiasm
        self.experience = experience
        self.goal = goal

    def interview(self):
        # self.generateGender()
        # self.generateCredits()
        # self.generateMajor()
        # self.generateAge()
        # self.generateInjury()
        self.generateEnthusiasm()
        self.generateExperience()
        self.generateGoal()

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

    def generateInjury(self):
        self.injury = input("Are you injured? True or False: ")
        return self.injury

    def generateEnthusiasm(self):
        self.enthusiasm = input("Please enter your level of enthusiasm about working out on a scale of 1 (low) to 3 (high): ")
        return self.enthusiasm

    def generateExperience(self):
        self.experience = input("Please enter your level of experience in working out on a scale of 1 (beginner) to 3 (expert): ")
        return self.experience

    def generateGoal(self):
        self.goal = input("What is your workout goal? 1 (health), 2 (image), 3 (performance), 4 (weightlifting): ")
        return self.goal

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
        print("injury")
        print(self.injury)
        print("enthusiasm")
        print(self.enthusiasm)
        print("experience")
        print(self.experience)
        print("goal")
        print(self.goal)



