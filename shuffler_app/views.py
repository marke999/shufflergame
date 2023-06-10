# -*- coding: utf-8 -*-,
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from shuffler_app.shuffler3 import definition, shuffled_word, random_word
import shuffler_app.shuffler3 as shuffler3
import subprocess
import signal
import importlib
import os

process = None

def my_view(request):
      #Store the data in variables      
      meanings_p = definition
      shuffled_word_p = shuffled_word
      original_word_p = random_word
      
      #Construct the template context with many variables
      context = {
            'meanings_p': meanings_p,
            'original_word_p': original_word_p,
            'shuffled_word_p': shuffled_word_p
      }
      
      return render(request, 'shuffler_html.html', context)
      
# def restart_script(request):
      
#       global process

#       if process is not None and process.poll() is None:
#             process.send_signal(signal.SIGTERM)
#             process.terminate()
#             process.wait()

#       process = subprocess.run(['python3', "/home/lgucebu1/Tasks/Python3/shuffler/shuffler_app/shuffler3.py"])
#       importlib.reload(shuffler3)

#       return HttpResponse("Script restarted")

def restart_script(request):
            
      # Terminate the existing process, if any
      global process

      #Store the data in variables      
      meanings_p = definition
      shuffled_word_p = shuffled_word
      original_word_p = random_word
      
      #Construct the template context with many variables
      context = {
            'meanings_p': meanings_p,
            'original_word_p': original_word_p,
            'shuffled_word_p': shuffled_word_p
      }      
      
      if process is not None and process.poll() is None:
            
            process.send_signal(signal.SIGTERM)
            process.terminate()
            process.wait()
                    
            subprocess.call("pkill -f /home/lgucebu1/Tasks/Python3/shuffler/shuffler_app/shuffler3.py", shell=True)
            subprocess.run(['pkill', 'python'])
                    
            # Start a new process
            subprocess.run(["python3", "/home/lgucebu1/Tasks/Python3/shuffler/shuffler_app/shuffler3.py"])
                 
      #return HttpResponse("Script restarted")
      return render(request, 'shuffler_html.html', context)

# def restart_script(request):
#       # subprocess.call(['python3', '/home/lgucebu1/Tasks/Python3/shuffler/shuffler_app/kill.sh'])
#       

#       return HttpResponse("All python Killed!")

# def restart_script(request):
#     try:
#         subprocess.run(['pkill', 'python'])
#         message = 'All python have been killed'
#     except subprocess.CalledProcessError:
#         message = 'Failed to kill Python process'

#     context = {'message': message}
#     return render(request, 'shuffler_html.html', context)