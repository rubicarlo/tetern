import subprocess
import signal

processes = []

def download_video(url, index):
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'panic', '-i', url, f'video_{index}.mp4'])
    processes.append(process)

def stop_download(index):
    process = processes[index]
    if process is not None:
        process.terminate()
        process.wait()
        processes[index] = None
        print(f"La descarga del video {index} ha sido detenida.")

while True:
    user_input = input("¿Qué deseas hacer? (d - descargar video, s - detener descarga, q - salir): ")

    if user_input == "q":
        break
    elif user_input == "d":
        url = input("Introduce el enlace m3u8 para el video: ")
        index = len(processes)
        download_video(url, index)
    elif user_input == "s":
        print("Videos descargándose:")
        for i, process in enumerate(processes):
            if process is not None:
                print(f"{i}: video_{i}.mp4")
        index = int(input("Introduce el índice del video que deseas detener: "))
        stop_download(index)
    else:
        print("Opción no válida")