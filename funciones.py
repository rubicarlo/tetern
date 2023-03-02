import subprocess
import os


processes = []

def download_video(url, index):
    if not os.path.exists('video'):
        os.makedirs('video')
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'panic', '-i', url, '-c', 'copy', '-b:v', '5M', os.path.join('video', f'video_{index}.ts')])
    processes.append(process)

def convert_to_mp4(index):
    if not os.path.exists(os.path.join('video', f'video_{index}.ts')):
        return
    subprocess.run(['ffmpeg', '-loglevel', 'panic', '-i', os.path.join('video', f'video_{index}.ts'), '-c', 'copy', os.path.join('video', f'video_{index}.mp4')])
    os.remove(os.path.join('video', f'video_{index}.ts'))

def stop_download(index):
    process = processes[index]
    if process is not None:
        process.terminate()
        process.wait()
        processes[index] = None
    convert_to_mp4(index)
    print(f"La descarga del video {index} ha sido detenida y convertida a un archivo mp4.")
