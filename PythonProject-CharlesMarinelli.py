import time
import random
#alright so here are the three functions I have so far, the issue is I don't really know how to intergrate a large data with this visual novel-esque experience
def name():
    player_name= input("Enter your name.")
    print "Are you certain that,", player_name, ",is your name?"
    checker=input("please answer y or n.")#this will be a recouring theme
    if checker == 'n':
        player_name=input("Enter your ACTUAL name. This is serious project and having a character named Dickbutt will ruin the experience.")#Yes I have to put this here. People are unpredictable after all.
    else:
        print player_name, "is a lovely name. Anyway", player_name, "The game you are about to play is about suicide."+
              "I attempted suicide on October 10th 2018, and I wanted to make a game to show that society does little to help those", "\n" "who commit suicide before it happens"+
              ", but to also serve as a memorial to those who actually commited suicide."#Before you get concerned I have gotten help since then and I am on the road to recovery. This is the reason
              #why I wanted to do this project. I don't want people to feel the way I felt, like they had no one to turn to in such a dire situation. I just need to format the next a little better
def questions():
    print "Before you play this game I have a few questions. Please be honest and answer using y and n with y for yes and n for no."
    #The questions will impact the paths of the games and the sympathy presented in the choices the player makes with 0 being the most sympathetic and 4 being the least sympathetic
    #The reason for picking these questions is that it will determine the relationship between the player and the friend.
    question1=input("Do you think those who commit suicide are just doing this to seek attention?")
    if question1=="y":
        question1=1
    else:
        question1=0
    question2=input("Have you ever had suicidal thoughts?")
    if question2 == "n":
        question2=1
    else:
        question2=0
    question3=input("Have you lost a friend or loved one to suicide?")
    if question3=="n":
        question3=1
    else:
        question3=0
    question4=input("Do you, or someone you care about, have depression?")
    if question4 == "n":
        question4=1
    else:
        question4=0
    question5=input("Finally, are you currently contemplating suicide?")
    if question5=="y":
        print "Please stop playing this game and call 1-800-273-8255."
        return#this will end the prorgam in the event that someone is suicidal
    questionTotal=(question1+question2+question3+question4)
    if questionTotal == 0:
        path=path1#each path will present the player with different options. This is to emulate visual novels and how they present the reader with different options themselves.
    elif questionTotal==1:
        path=path2
    elif questionTotal==2:
        path=path3
    elif questionTotal==3:
        path=path4
    else:
        path=path5
    return path

def ending():
    s=0
    m=0

    while s<=40:
        time.sleep(1)
        s+=1
        if s==40:
            print "I'm fine."
            s=0
            m +=1
        if m == 40:#alright so the reason for 40 is that according to the world health organization every 40 seconds someone commits suicide.
            s=1
            print "After talking to your friend, he/she still didn't feel comfortable about addressing their issues with you."+
          "Unfortunately they felt they had no where to turn to and their issues began to pile up and overhwhelm them."+
          "This morning you found out they had commited suicide." #I plan to vary the ending text based on the path, but they will all end with the friend commiting suicide
            return
