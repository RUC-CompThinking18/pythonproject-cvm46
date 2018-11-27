#PROJECT Riley
import time
import random

class Game():#The class where everything goes down




    def __init__(self):
        self


    def name(self):#The name is important for the sake of immersion so that way people feel connected to Riley
        player_name= input("Enter your name.")
        print("Are you certain that,", player_name, ",is your name?")
        checker=input("please answer y or n.")
        if checker == 'n':
            player_name=input("Enter your ACTUAL name.")
        else:
            print(player_name, "is a lovely name. Anyway", player_name, "The game you are about to play is about suicide."+
              "I attempted suicide on October 10th 2018, and I wanted to make a game to show that society does little to help those", "\n" "who commit suicide before it happens"+
              ", but to also serve as a memorial to those who actually commited suicide.")#by the way this is actually my beliefs and yes I did actually attempt suicide on that date. This is why this project is both personal and draining for me.
        self.name=player_name
        return self.name

    def questions(self):#this determines the path and will eventually alter the player's experience, however I might just pull a ha your choices don't matter thing to add on to the hopelessness, I honestly haven't decided.
        print("Before you play this game I have a few questions. Please be honest and answer using y and n" "\n with y for yes and n for no.")
        question1=input("Do you think those who commit suicide are just doing this to seek attention? ")
        if question1=="y":
            question1=1
        else:
            question1=0
        question2=input("Have you ever had suicidal thoughts? ")
        if question2 == "n":
            question2=1
        else:
            question2=0
        question3=input("Have you lost a friend or loved one to suicide? ")
        if question3=="n":
            question3=1
        else:
            question3=0
        question4=input("Do you, or someone you care about, have depression? ")
        if question4 == "n":
            question4=1
        else:
            question4=0
        question5=input("Finally, are you currently contemplating suicide? " )
        if question5=="y":
            print("Please stop playing this game and call 1-800-273-8255. ")
            return
        questionTotal=(question1+question2+question3+question4)
        if questionTotal == 0:
            self.path=1
        elif questionTotal==1:
            self.path=2
        elif questionTotal==2:
            self.path=3
        elif questionTotal==3:
            self.path=4
        else:
            self.path=5

    def paths(self):
        #print (self.path)
        if self.path==1:
            self.path1()
        #if self.path==2:
            #path2()
        #if self.path==3:
            #path3()
        #if self.path==4:
            #path4()
        #if self.path==5:
            #path5()
        else:
            print("The following path is not yet avaliable.")#I don't have enough time to create a whole new path
    def path1(self):#Alright I'll be honest this needs to be fleshed out more. I was honestly focused on other things and this project is just naturally draining to me for obvious reasons.
        print('You are,', self.name, ',and your dear friend, Riley, is currently messaging you. How about we check in on them? \n “Hey', self.name, "How's it going?”")
        choice1=input("1: It's going good, dude. What about you?" + "\n2: I'm doing alright. What about you?" +"\n3: I'll be honest with you I ain't doing so good. You doing any better?")
        if choice1==3:
               print(" “Oh really,", self.name,  ",tell me about it?” From there you proceed to discuss your problems all through the night, but only your problems. In a normal turn of events you asked if they had any problems of their own. They simply responded, “I'm fine.”")
               choice2=input("Do you \n1: go to bed and think nothing of it \nor do you \n2: try to pry further")
               if choice2==1:
                   print("You end your conversation with them and go to bed. Unfortunately for you their last message to you was stuck in your head leaving your mind to echo it and to wake up to something horrid.")
                   ending()
               else:
                    print("You try to delve deeper but they keep insisting that they're fine no matter what. The more you pry the more fed up with you they become. Suddenly they just stop texting you. You try and go to sleep but their insistence on stating that they're fine when they clearly weren't haunts you. It's all you can think about through the night.")
                    ending()

        else:
                print("“I'm fine.” Their short response was a bit weird because normally they would talk your ear off for hours upon hours. In fact they've been acting a little off as of late.")
                choice2=input("Do you \n1: pry further \nor do you \n2: ignore it")
                if choice2==2:
                        print("You choose to ignore your friend's shifting behavior and just reply with a simple that's good. Riley is silent for a few moments but then he messages back," + "\n“You know that painting I made a few years ago, the one you said was life changing? You can have it.”"
                                  + "My mom will probably give it to you sometime this week”."+ "\nWait why would their mom give it to you? Riley moved out of their parents' house two years ago. Something was definitely wrong.")
                        choice3=input("Do you \n1: ask if your friend is okay? \nor do you \n2: still ignore it")
                        if choice3==2:
                            print("Against your better judgement you still decide the odd behavior of Riley. You simply send a message saying thanks for the painting, yet your conscience is ridden with guilt," +
                                          "after all Riley has been one of your closest friends ever since preschool. You cannot abandon them now.")
                            choice4=input('Do you \n1: ask them if they are okay. \nor do you \n2: tell them you notice something is up.')
                            if choice4 == 1 or 2:
                                print("After a few minutes of silence you send a message of concern to Riley. They respond with one phrase,“I'm fine.”, you can clearly tell that they are not fine in any way, shape, or form.")
                                choice5=input("1:“Riley, please tell me what's wrong. I can tell that you aren't fine.”"+ "\n2:“Dude, I know you're not okay. Please stop lying to the both of us and tell me what's wrong.”")
                                if choice5 == 1 or 2:
                                    print("As soon as you are about to send your message your phone dies. You scramble to find an outlet to plug in your charger, but all of them are taken by depressed and stressed looking people typing up a storm on their laptops." +
                                                  "You sigh as you decide to leave campus and go home. By the time you get back home and plug in your charger the last message you see is “I'm fine.”, and it just rings around in your head and all you can think is, “I'm fine.”")
                                    ending()
                        else:
                            print("You send a simple message but they only respond with “I'm fine.” and as they respond your phone dies. Thus ends the conversation, but that last remark dances through your head and echoes through your very mind.")
                            ending()
                else:
                    print("You pry further and yet they don't respond right away. You wait for them and wait for them until finally a message sends. It reads “I'm fine.” but they clearly aren't. You respond to them constantly trying to get their attetion but they never answer. Suddenly your phone dies and you're left thinking about their message, “I'm fine.”")
                    ending()
#yes a lot of that is if else statements and long strings but given that I don't really have visuals to aid me these long strings are 200% necessary.


    def ending(self):#the ending code is actually derived from the twitterbot I planned to make. I repurposed it into this as to not waste code.
        s=0
        m=0

        while s<=40:
            time.sleep(1)
            s+=1
            if s==40:
                print("I'm fine.")
                s=0
                m +=1
            if m == 40:#40 is for the fact that every 40 seconds someone either attempts or commits suicide according to the World Health Organization. I will put a citation and a quote for that in the readme.
                s=1
                print("After talking to your friend, they still didn't feel comfortable about addressing their issues with you."+
              "Unfortunately they felt they had no where to turn to and their issues began to pile up and overhwhelm them."+
              "This morning you found out they had commited suicide.")
                return

x=Game()
x.name()
x.questions()
x.paths()
