import subprocess

webots_path = r'C:\Program Files\Webots\msys64\mingw64\bin\webotsw.exe'
webots_world = r'C:\Users\gerar\PycharmProjects\CODIGOS_TESIS\ho_sim\worlds\ho_sim.wbt'
webots_process = None

def start_webots():
    global webots_process
    open_command = [webots_path, "--mode=fast", webots_world]
    webots_process = subprocess.Popen(open_command)

def stop_webots():
    global webots_process
    if webots_process:
        webots_process.terminate()
