from abc import ABC, abstractmethod

class Chatbot(ABC):

    @abstractmethod
    def greeting(self):
        pass

    @abstractmethod
    def introduction(self):
        pass

    @abstractmethod
    def redirection(self):
        pass

    def serviceUrl(self):
        pass

    def exit(self):
        pass
    
class GreetingBot(Chatbot):

    def greeting(self):
        pass

    def introduction(self):
        pass 

    def redirection(self):
        pass

    def emailSubscription(self):
        pass

class ActionsBot(Chatbot):

    def greeting(self):
        pass

    def introduction(self):
        pass 

    def redirection(self):
        pass

    def serviceUrl(self):
        pass

    def exit(self):
        pass

class OperatorsBot(Chatbot):

    def greeting(self):
        pass

    def introduction(self):
        pass 

    def redirection(self):
        pass

    def serviceUrl(self):
        pass

    def exit(self):
        pass

class ProBot(Chatbot):

    def greeting(self):
        pass

    def introduction(self):
        pass 

    def redirection(self):
        pass

    def serviceUrl(self):
        pass

    def exit(self):
        pass