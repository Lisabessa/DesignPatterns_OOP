# Visitable - object to be visited by visitors with the accept() operation
class GymActivities:
    def accept(self, visitor):
        visitor.visit(self)

    def working_out(self, visitor):
        print(self, visitor, 'is working out')

    def training_people(self, visitor):
        print(self, visitor, 'is training others')

    def __str__(self):
        return self.__class__.__name__


# Concrete GymActivities classes: Concrete visitable classes
class Stretching(GymActivities):
    pass


class Strength_Training(GymActivities):
    pass


class Dance(GymActivities):
    pass


# Abstract Visitor class
class Visitor:
    def __str__(self):
        return self.__class__.__name__


# Concrete Visitor classes
# These classes have a visit() method which is called by the accept() method of the Concrete visitable classes
class Trainer(Visitor):
    def visit(self, activity):
        activity.training_people(self)


class Sportsman(Visitor):
    def visit(self, activity):
        activity.working_out(self)


stretching = Stretching()
strength_training = Strength_Training()
dance = Dance()

trainer = Trainer()
sportsman = Sportsman()

stretching.accept(trainer)
stretching.accept(sportsman)
strength_training.accept(trainer)
strength_training.accept(sportsman)
dance.accept(trainer)
dance.accept(sportsman)
