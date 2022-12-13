#Mad Libs Generator Project
loop = 1
while (loop < 9):
#All the questions that the program asks the user
    noun = input("Choose a noun: ")
    plural_noun = input("Choose a plural noun: ")
    second_noun = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    third_noun = input("Choose a noun: ")
#Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", plural_noun)
    print ("For a duck may be somebody's", seond_noun,",")
    print ("Be kind to your",plural_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",third_noun,",")
    print ("Well it is.")
    print ("------------------------------------------")
#Loop back to "loop = 1"
    loop = loop + 1
