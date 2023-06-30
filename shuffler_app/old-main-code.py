
import random
import requests

#Path to the text file/
file_path = "/home/lgucebu1/Tasks/Python3/shuffler/shuffler_app/templates/words10.txt"

#Read the words from the file
with open(file_path, "r") as file:
    words = file.read().split()

#Select a random word from the list
random_word = random.choice(words)

#Shuffle the letters in the word
shuffled_word = "".join(random.sample(random_word, len(random_word)))

def get_word(random_word):
   url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(random_word)

   response = requests.get(url)
   if response.status_code == 200:
          data = response.json()

          if  len(data) > 0:
            meanings = data[0]['meanings']
            if  len(meanings) > 0:
                meaning = meanings[0]['definitions'][0]['definition']
                #print(meaning)
                return meaning
            else:
                print("No meanings found.")
          else:
            print("No meanings found.")
   else:
        print("Failed to retrieve meaning.")

definition = get_word(random_word)

#For terminal use
#Print the meaning of the original word and the shuffled word
# get_word(random_word)
# print("Definition: ", definition)
# print("Shuffled Word: ", shuffled_word)
# user_input = input("Original Word:  ")
# original_word = user_input.upper()

# #Print the results
# if random_word == original_word:
#     print("Correct. You got it right!")
# else:
#     print("Wrong. The correct answer is", random_word)
