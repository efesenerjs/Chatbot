from abc import ABC, abstractmethod

# importation for use RegEx
import re

# importation for sleep
import time

# RegEx for email validation
emailValidation = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Templates definition
templates = {"1": ["Nocode Bible - Actions", "Nocode Bible - Bubble Actions template was created to increase your Bubble learning speed with examples and tips from all the actions that come with when you create a new app with Bubble", "https://bubble.io/template/nocode-bible---bubble-actions-1627042650294x983336912496885800"], "2": ["Nocode Bible - Operators", "Nocode Bible - Bubble Operators template was created to increase your Bubble learning speed with examples and tips from all the operators that come with when you create a new app with Bubble", "https://bubble.io/template/nocode-bible--bubble-operators-1627043775944x678850432281608200"], "3": ["Nocode Bible - Pro", "Nocode Bible consists of two free templates that make Bubble easy to learn, and a Pro template that can greatly increase the speed of application development. Constantly updated content includes almost everything you might need when developing a Bubble app, from expert-level tips to Regex patterns.", "https://bubble.io/template/nocode-bible---pro-v12-1619555909664x271005251423698940"]}

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

    def emailSubscription(self):
        pass

    def gotoTemplate(self):
        pass
    
class GreetingBot(Chatbot):

    def greeting(self):
        print("\nWelcome to Nocode Bible Bot!")
        time.sleep(2)
        print("\nCould you take down your name. Thus, I can call you with your name.")
        name = input("")
        print("\nHello, {name}! Glad to see you here!".format(name=name))
        self.introduction()
        return name

    def introduction(self):
        time.sleep(2)
        print("\nWe built Nocode Bible to decrease steep of Bubble learning curve!")
        print("\nNocode Bible is a triology template for Bubble. You can do both learning and testing almost all actions.")
        time.sleep(2)

        self.emailSubscription()

    def redirection(self):
        time.sleep(2)
        print("\nOkey! Let's dig down now.\nWhich information of a template do you want?")
        time.sleep(4)
        print("\n'1' for Nocode Bible - Actions\n'2' for Nocode Bible - Operators\n'3' for Nocode Bible - Pro")
        
        template = str(input())

        return template


    def emailSubscription(self):
        print("\nBefore digging down, could you get emails about news and updates for Nocode Bible? (yes/no)")
        subscription = input("").lower()
        while subscription == "yes":
            time.sleep(2)
            print("\nGreat! Please type your email address:")
            userEmail = input()
            if(re.fullmatch(emailValidation, userEmail)):
                 time.sleep(1)
                 print("Great!\n")
                 subscription = "no"
            else:
               time.sleep(1)
               print("\nInvalid email. Please type again:")

class ServiceBot(Chatbot):

    def __init__(self, templateName, informText, serviceUrl, userName):
        self.templateName = templateName
        self.informText = informText
        self.serviceUrl = serviceUrl
        self.userName = userName

    def greeting(self):
        print("\nHey, {name}! How are you doing?".format(name=self.userName))
        time.sleep(1)
        print("\nLet's talk about {templateName}".format(templateName=self.templateName))
        time.sleep(1)
        self.introduction()

    def introduction(self):
        print(self.informText)
        # If user get informatino about priced template, provide coupon code to call to action
        if self.templateName == templates["3"][0]:
            print("\nAre you interested in {templateName}? You can purchase now with 'DISCOUNT20' coupon code!".format(templateName=self.templateName))
        self.gotoTemplate()

    def redirection(self):
        time.sleep(5)
        print("\nWould you like check out our other templates?\nWhich information of a template do you want?")
        time.sleep(2)
        print("\n'1' for Nocode Bible - Actions\n'2' for Nocode Bible - Operators\n'3' for Nocode Bible - Pro\n'4' for Exit from the app")
        
        template = str(input())

        return template

    def gotoTemplate(self):
        print("Get {templateName} from here: {URL}".format(templateName=self.templateName, URL=self.serviceUrl))
        

def run ():
    firstLoop = True
    
    while firstLoop: 

        greetingBot = GreetingBot()

        userName = greetingBot.greeting()

        redirect = greetingBot.redirection()

        try:
           
           secondLoop = True

           while secondLoop:
                try:
                    if redirect != '4':
                        serviceBot = ServiceBot(templates[redirect][0], templates[redirect][1], templates[redirect][2], userName)

                        serviceBot.greeting()

                        redirect = serviceBot.redirection()
                    else:
                        print("Thank you for the great conversation!\nFollow my creator on twitter: @NocoderEfe")
                        secondLoop = False
                        firstLoop = False

                except:

                    print("Err, something wrong! Please try again")

        except:

            print("Err, something wrong! Please try again")

        

run()