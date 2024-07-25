


BasicQuestions = [
    "is it a place?",
    "does the length of the keyword exceed 10 characters?",
    "is the first letter of the keyword one of the following letters: 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', or 'm'? Please consider both upper and lower case as the same when checking the first letter.",
]

BasicAnswers = [
    ["keyword is a place. ", "keyword is a thing. "],
    ["keyword length > 10. ", "keyword length <= 10. "],
    [
        "the first letter of the keyword is one of the following letters: 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', or 'm'. ",
        "the first letter of the keyword is one of the following letters: 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', or 'z'. ",
    ],
]

PlaceQuestions = [
    "is it a country?",
    "is it a city?",
    "is it a mountain?",
    "is it a river?",
]

PlaceAnswers = [
    "keyword is a country. ",
    "keyword is a city. ",
    "keyword is a mountain. ",
    "keyword is a river. ",
    "keyword is not a country, city, mountain, or river. ",
]

ThingsQuestions = [
    "is it a living thing?",
    "is it edible?",
    "is it a tool?",
    "is it something that can be help in your hand?",
    # "Does it require electricity to operate?",
]

ThingsAnswers = [
    ["keyword is a living thing. ", "keyword is not a living thing. "],
    ["keyword is edible. ", "keyword is not edible. "],
    ["keyword is a tool. ", "keyword is not a tool. "],
    ["keyword is something that can be held in your hand. ", "keyword is something that cannot be held in your hand. "],
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
        self.context = "hint: "
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
    
    @property
    def count(self):
        return self.count