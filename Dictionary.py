from PyDictionary import PyDictionary

dictionary=PyDictionary()

inp1=input("Hello, I am PyDictionary. How can I help you today? (Antonyms, Synonyms or Definitions?)    ")

if inp1 == "antonyms" :
    inp2=input("Which word would you like to find the antonym of?     ")
    print (dictionary.antonym(inp2))
elif inp1 == "Antonyms" :
    inp2=input("Which word would you like to find the antonym of?     ")
    print (dictionary.antonym(inp2))
elif inp1 == "Synonyms" :
    inp3=input("Which word would you like to find the synonym of?    ")
    print (dictionary.synonym(inp3))
elif inp1 == "synonyms" :
    inp3=input("Which word would you like to find the synonym of?    ")
    print (dictionary.synonym(inp3))
elif inp1 == "definitions" :
    inp4=input("Which word would you like to find the definition of?    ")
    print (dictionary.meaning(inp4))
elif inp1== "Definitions":
     inp4=input("Which word would you like to find the definition of?    ")
     print (dictionary.meaning(inp4))
else:
    print ("Whoops. That didn't work. Try typing either one of the three the next time you run this : Antonyms, Synonyms or Definitions.")
        