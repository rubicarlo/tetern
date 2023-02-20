import subprocess

processes = []

def download_video(url, index):
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'panic', '-i', url, '-b:v', '2M', f'video_{index}.ts'])

    processes.append(process)

def stop_download(index):
    process = processes[index]
    if process is not None:
        process.terminate()
        process.wait()
        processes[index] = None
        print(f"La descarga del video {index} ha sido detenida.")