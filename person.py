# Class for person

class Person:

    def __init__(self, gender="F", creditsTaken=0, major="CS", age=0, injury=False, enthusiasm=1, experience=1, goal="lose weight"):
        self.gender = gender    # do we need this variable?
        self.creditsTaken = creditsTaken    # do we need this variable?  
        self.major = major  # do we need this variable?
        self.age = age  # do we need this variable?
        self.injury = injury
        self.enthusiasm = enthusiasm
        self.experience = experience
        self.goal = goal    # needs a class

# add testing interview functions
    def interview_test1(self):
    # gender = ...
    # credits = ...

# workout call from recommender to test

    def interview(self):
        self.generateGender()
        self.generateCredits()
        self.generateMajor()
        self.generateAge()
        self.generateInjury()
        self.generateEnthusiasm()
        self.generateExperience()
        self.generateGoal()

    # method to generate attribute gender
    def generateGender(self):
        gender = input("Please enter your gender (M or F): ")
        return gender

    def generateCredits(self):
        creditsTaken = input("Please enter your current # of credit hours: ")
        return creditsTaken

    def generateMajor(self):
        major = input("Please enter your major: ")
        return major

    def generateAge(self):
        age = input("Please enter your age: ")
        return age

    def generateInjury(self):
        injury = input("Are you injured? True or False: ")
        return injury

    def generateEnthusiasm(self):
        enthusiasm = input("Please enter your level of enthusiasm about working out on a scale of 1 (low) to 3 (high): ")
        return enthusiasm

    def generateExperience(self):
        experience = input("Please enter your level of experience in working out on a scale of 1 (beginner) to 3 (expert): ")
        return experience

    def generateGoal(self):
        goal = input("What is your workout goal? 1 (health), 2 (image), 3 (performance), 4 (weightlighting): ")
        return goal

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

    # in an ideal world, we have a builder class of some sort that calls this with all of the logic. is that correct?
    # def createPlan():

    # same with this method
    # def refreshPlan():

