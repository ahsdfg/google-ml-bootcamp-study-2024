from questions import *


class RuleBasedQuestions:
    def __init__(self):
        """
        Attributes:
            log (list): A list to store the user's answers.
            count (int): The count of questions asked.
            enabled (bool): Indicates if all questions have been asked.
            category (str): The current category of questions.
        """
        self.log = []
        self.count = 0
        self.enabled = True
        self.category = "basic"

    def getQuestion(self):
        """
        Returns the next question based on the current state of the game.

        Returns:
            str: The next question to be asked.
        """
        if self.enabled:
            return "No more available questions."
        if self.count < len(BasicQuestions):  # Basic
            return BasicQuestions[self.count]
        elif self.category == "place":  # Place
            return PlaceQuestions[self.count - len(BasicQuestions)]
        elif self.category == "things":  # Thing
            return ThingsQuestions[self.count - len(BasicQuestions)]

    def logAnswer(self, answer):
        """
        Logs the user's answer and updates the category and count based on the answer.

        Parameters:
        - answer (str): The user's answer, either "yes" or "no".

        Returns:
        None
        """
        answer_yes = True
        if "no" in answer.lower():
            answer_yes = False
        self.log.append(answer_yes)

        # determine the category by first answer
        if self.count == 0:
            self.category = "place" if answer_yes else "things"
        self.count += 1

        if self.count <= len(BasicQuestions):  # Basic
            pass
        elif self.category == "place":  # Place
            if answer_yes or self.count == len(BasicQuestions) + len(PlaceQuestions):  #
                self.enabled = True

        elif self.category == "things":  # Thing
            if self.count == len(BasicQuestions) + len(ThingsQuestions):
                self.enabled = True

    def reset(self):
        self.log = []
        self.count = 0
        self.enabled = False
        self.category = "basic"
