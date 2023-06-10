import subprocess

def restart_script(request):
    try:
        subprocess.run(['pkill', 'python'])
        message = 'All python have been killed'
    except subprocess.CalledProcessError:
        message = 'Failed to kill Python process'

    context = {'message': message}
    return render(request, 'shuffler_html.html', context)