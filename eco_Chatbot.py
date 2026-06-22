#Name: Prisha
'''
This is the eco-friendly Chatbot that I created for my coding class.
It was a very interesting beginner-friendly project to do.
'''

#Idea: Eco-Chatbot that interacts with people and gives advice about
#ecological effects of GenAI tools.

#Ecology topics and GenAI topics:

#Pre-defined lists:

ecology_topics = ["mountain", "lake", "tree", "ocean"]
genAI_topics = ["carbon footprint", "water shortage"]

#Welcome and breif introduction:

print("Hello user!")
print("I am Kayla, your favourite Eco-Chatbot.")
print()
print("I am here to talk with you about different topics of ecology, \nand also the impacts of GenAI on ecology.")
print()

print("But before we get started, let me get to know your name!")
name=input("What is your name? ==> ").strip().capitalize()
  #used strip() to remove white spaces and capitalize() to capitalize the input
  #used two string methods.
print("It is a pleasure to meet you,", name,"!")
print()


#Asking the user about their interest in ecology:

print("Tell me about your favourite ecology topics from the below options")
print("(mountain, lake, tree, ocean)")
topic = str(input("==> ")).lower()
  #used lower() to make all characters lowercase, so it will match the list.
  #used one string method
  #Python is case sensitive. 
print()

if topic in ecology_topics:
    print("Oh!", topic , "is an interesting choice and it is important for our planet.")
else:
    print(topic, "is not one the list. Choose one from the list")

#Asking the user how many number of GenAI tools they have used before:

print("Now, tell me how many number of GenAI tools you have used so far")
tools = int(input("==> "))
if tools >= 3:
    print("That is quite a lot of GenAI tools!")
    if "carbon footprint" in genAI_topics:
        print("Do you know that using GenAI causes higher carbon footprint because \nit requires large amounts of electricity and water, leading to \nincreased greenhouse emissions from data centers?")
  #used nested if
else:
    print("Your usage seems to be moderate or lower than the average rate.")
    if "water shortage" in genAI_topics:
        print("You should know that GenAI tools consume large amounts of water. \nThe data centers require water to cool the servers, indirectly causing water shortage.")
print()
  #used nested if

#Listing the environmental issues caused by GenAI:
print("These are some of the issues caused by GenAI:")
for issue in genAI_topics:
    print("*", issue.upper())
  #used one of the string methods
print()
  #used for loop

#Goodbye message:
print("If you want to learn more about the impacts , then contact:")
print("         =>+12421124134")
print()
print("It was great chatting with you,", name,"!")
print()
