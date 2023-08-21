with open('env.conf', 'r') as file:
    for line in file:
        if line.startswith('app_ip'):
            app_ip = line.split('=')[1].strip()
            print("Content-Type: text/plain")
            print()
            print(app_ip)
            break
