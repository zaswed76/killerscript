import psutil

a = [
    'c:\\users\\serg\\appdata\\local\\programs\\python\\python36-32\\python.exe',
    'C:\\Users\\Serg\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts\\stat3-script.py']
b = ['cmd.exe']

for process in psutil.process_iter():
    try:
        proc = process.cmdline()
    except psutil._exceptions.AccessDenied:
        pass
    else:
        for p in proc:
            if "stat3" in p:
                print(p)
                print("   ---")
                process.terminate()
                # print("#####################")




                # print("------------------")
