from django.shortcuts import render
from django.http import JsonResponse
import random
import requests

# Main Python Logic
def get_random_word(request):
      # Path to the CSV file
      file_path = "/home/lgucebu1/Tasks/Python3/shuffler/shuffler_app/templates/words10.txt"

      # Read the words from the CSV file
      with open(file_path, "r") as file:
            words = file.read().split()

      # Select a random word from the list
      random_word = random.choice(words)

      # Shuffle the letters in the word
      shuffled_word = "".join(random.sample(random_word, len(random_word)))

      # API dictionary
      url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(random_word)
      response = requests.get(url)

      # Retrieve meaning of the random word
      if response.status_code == 200:     
            data = response.json()

            if len(data) > 0:
                  meanings = data[0]['meanings']
                  if len(meanings) > 0:
                        meaning = meanings[0]['definitions'][0]['definition']
                        return render(request, 'shuffler_html.html', {
                              'meaning': meaning,
                              'shuffled_word': shuffled_word,
                              'random_word': random_word
                              })
                  else:
                        return render(request, 'shuffler_html.html', {
                              'meaning': "No meanings found.",
                              'shuffled_word': shuffled_word,
                              })
            else:
                  return render(request, 'shuffler_html.html', {
                        'meaning': "Failed to retrieve meaning.",
                        'shuffled_word': shuffled_word
                        })
      else:
            return "Failed to retrieve meaning."

def home(request):
      return get_random_word(request)