import subprocess
import os
import datetime

processes = []

def download_video(url, index):
    # Crea el directorio de destino si no existe
    base_path = os.path.join(os.getcwd(), 'videos', 'TS')
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    # Lanza el proceso ffmpeg para descargar el video
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'panic', '-i', url, '-c', 'copy', '-b:v', '5M', os.path.join(base_path, f'video_{index}.ts')])
    # Añade el proceso a la lista de procesos
    processes.append(process)

def convert_to_mp4(index):
    # Establece los paths para los archivos
    base_path = os.path.join(os.getcwd(), 'videos')
    ts_path = os.path.join(base_path, 'TS')
    input_filename = f'video_{index}.ts'
    input_path = os.path.join(ts_path, input_filename)
    # Si el archivo no existe, sale de la función
    if not os.path.exists(input_path):
        return
    # Pide al usuario el nombre deseado del archivo
    filename = input("Introduce el nombre deseado del archivo: ")
    # Concatena el nombre del archivo personalizado con la fecha actual en el formato deseado
    output_filename = f'{filename}_{datetime.datetime.now().strftime("%d-%m-%Y")}.mp4'
    output_path = os.path.join(base_path, output_filename)
    # Si el archivo ya existe, agrega un número al final del nombre del archivo
    i = 2
    while os.path.exists(output_path):
        output_filename = f'{filename}_{datetime.datetime.now().strftime("%d-%m-%Y")}_{i}.mp4'
        output_path = os.path.join(base_path, output_filename)
        i += 1
    # Lanza el proceso ffmpeg para convertir el archivo
    subprocess.run(['ffmpeg', '-loglevel', 'panic', '-i', input_path, '-c', 'copy', output_path])
    # Borra el archivo .ts
    os.remove(input_path)


def stop_download(index):
    # Obtiene el proceso en la posición "index" de la lista de procesos
    process = processes[index]
    # Si el proceso existe, lo detiene y espera a que termine
    if process is not None:
        process.terminate()
        process.wait()
        processes[index] = None
    # Convierte el archivo descargado a mp4
    convert_to_mp4(index)
    # Imprime un mensaje informando al usuario que la descarga ha sido detenida y convertida a mp4
    print(f"La descarga del video {index} ha sido detenida y convertida a un archivo mp4.")
