from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.db import connection
from django.contrib.auth.hashers import check_password
from .forms import LoginForm
from .models import User
from datetime import datetime
import random
import requests
import logging


# Main Home Page
def homepage(request):
      return render(request, 'signin.html')

# Main Python Logic
def shuffleword(request):
      # Path to the CSV file
      file_path = "/home/lgucebu1/Tasks/Python3/shufflergame/shuffler_app/templates/words10.txt"

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

#Guess Another Word Button
def game(request):
      return shuffleword(request)

#For Register Button
def register(request):
      return render(request, 'register.html')

#Store Details from Register webpage to MySQL
def process_form(request):
      if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            country = request.POST.get('country')
            city = request.POST.get('city')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                  #Check if the username already exists
                  with connection.cursor() as cursor:
                        sql = "SELECT COUNT(*) FROM shuffler_app_user WHERE Username = %s"
                        cursor.execute(sql, [username])
                        count = cursor.fetchone()[0]
                        if count > 0:
                              return render(request, 'existacct.html')

                  #Insert the form data into the database
                  with connection.cursor() as cursor:
                        sql = "INSERT INTO players (FirstName, LastName, Country, City, Email, Mobile, Username, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, [firstname, lastname, country, city, email, mobile, username, password])

                  #When form is successfully submitted
                  return render(request, 'success.html')
            except Exception as e:
                  #When the form submission failed
                  return render(request, 'fail.html')
      else:
            return JsonResponse({'message': "Invalid request method."})

#Logging in to Shufflergame
def login(request):
      if request.method == 'POST':
            form = LoginForm (request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password']
                  try:
                        user = User.objects.get(username=username)
                        if user.password == password:
                              return shuffleword(request)
                        else:
                              return render(request, 'wrongpw.html')
                  except User.DoesNotExist:
                        return render(request, 'noaccount.html')
            else:
                  messages.error(request, 'Invalid form data')
      else:
            form = LoginForm()
      return render(request, 'noaccount.html', {'form': form})


###########To check again this line of code
#Store game details from the game page to MySQL
def store_input(request):
      if request.method == 'POST':
            inputValue = request.POST.get('UserInput')
            
            # Get the username of the currently logged-in user 
            # Put the code here.

            #Get the curren date and time
            play_date = datetime.now().date()
            play_time = datetime.now().time()

            try:
                  #Insert the answer to the database
                  with connection.cursor() as cursor:
                        sql = "INSERT INTO output (username, PlayDate, PlayTime, WordClass, OrigWord, ShufWord, UserInput, Result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, ["M.ARNOCO", play_date, play_time, "NOUN", "{{random_word}}", "{{shuffled_word}}", inputValue, "RESULT"])
                        connection.commit()
                  #When the answer is successfully stored in the database
                  return JsonResponse({'message': "Successfully stored in MySQL"})
            except Exception as e:
                  logging.error(f"Failed to store in MySQL. Error: {e}")
                  return JsonResponse({'message': "Failed to store in MySQL"})
      else:
            return JsonResponse({'message': "Invalid request method"})
      