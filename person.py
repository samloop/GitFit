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

    # imagining this as method the builder calls to populate their person
    def populate():
        gender = input("Please enter your gender (M or F):")
        creditsTaken = input("Please enter your current # of credit hours:")
        major = input("Please enter your major:")
        age = input("Please enter your age:")
        injury = input("Are you injured? True or False:")
        enthusiasm = input("Please enter your level of enthusiasm about working out on a scale of 1 (low) to 3 (high):")
        experience = input("Please enter your level of experience in working out on a scale of 1 (beginner) to 3 (expert):")
        goal = input("What is your workout goal?")
        return Person(gender, creditsTaken, major, age, injury, enthusiasm, experience, goal)


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

