


BasicQuestions = [
    "Is it a place?",
    "Does the length of the keyword exceed 10 characters?",
    "Is the first letter of the keyword one of the following letters: 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', or 'm'? Please consider both upper and lower case as the same when checking the first letter.",
]

BasicAnswers = [
    ["Keyword is a place. ", "Keyword is a thing. "],
    ["Keyword length > 10. ", "Keyword length <= 10. "],
    [
        "The first letter of the keyword is one of the following letters: 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', or 'm'. ",
        "The first letter of the keyword is one of the following letters: 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', or 'z'. ",
    ],
]

PlaceQuestions = [
    "Is it a country?",
    "Is it a city?",
    "Is it a mountain?",
    "Is it a river?",
]

PlaceAnswers = [
    "Keyword is a country. ",
    "Keyword is a city. ",
    "Keyword is a mountain. ",
    "Keyword is a river. ",
    "Keyword is not a country, city, mountain, or river. ",
]

ThingsQuestions = [
    "Is it a living thing?",
    "Is it edible?",
    "Is it a tool?",
    "Is it something that can be help in your hand?",
    # "Does it require electricity to operate?",
]

ThingsAnswers = [
    ["Keyword is a living thing. ", "Keyword is not a living thing. "],
    ["Keyword is edible. ", "Keyword is not edible. "],
    ["Keyword is a tool. ", "Keyword is not a tool. "],
    ["Keyword is something that can be held in your hand. ", "Keyword is something that cannot be held in your hand. "],
    # ["Keyword requires electricity to operate. ", "Keyword does not require electricity to operate. "],
]

class RuleBasedQuestions:
    """
    Rule-based 20 Questions
    
    1. Basic Questions

    2. Place or Thing Questions
    
    """
    def __init__(self):
        """
        Initialize the context, log, count, and done.
        """
        self.context = "Hint: "
        self.log = []
        self.count = 0
        self.done = False
    
    def getQuestion(self):
        """
        Get the next question. Return the question based on the count.
        If there is no more hard-coded question, return "No more available questions."
        """
        if self.done:
            return "No more available questions."
        if self.count < 3:          # Basic
            return BasicQuestions[self.count]
        elif self.log[0] == True:   # Place
            return PlaceQuestions[self.count-3]
        else:                       # Thing
            return ThingsQuestions[self.count-3]
        
    def putAnswer(self, answer_yes=True):
        """
        Put the answer to the question.
        If the answer is yes, append the context with the yes answer.
        If the answer is no, append the context with the no answer.
        
        If the count is less than 3, it is a basic question.
        There will be just one answer for ThingsQuestions."""
        if self.count < 3:          # Basic
            self.context += BasicAnswers[self.count][0 if answer_yes else 1]
            
        elif self.log[0] == True:   # Place
            if answer_yes:
                self.context += PlaceAnswers[self.count-3]
                self.done = True
            
            if self.count == len(BasicQuestions) + len(PlaceQuestions) - 1: 
                self.context += PlaceAnswers[4] # Keyword is not a country, city, mountain, or river.
                self.done = True
                
        else:                       # Thing
            self.context += ThingsAnswers[self.count-3][0 if answer_yes else 1]
            
            if self.count == len(BasicQuestions) + len(ThingsQuestions) - 1:
                self.done = True
            
        self.log.append(answer_yes)
        self.count += 1            

    def reset(self):
        self.context = ""
        self.log = []
        self.count = 0
        self.done = False
    
    @property
    def context(self):
        return self.context