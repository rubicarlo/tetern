import funciones

while True:
    user_input = input("¿Qué deseas hacer? (d - descargar video, s - detener descarga, q - salir): ")

    if user_input == "q":
        break
    elif user_input == "d":
        url = input("Introduce el enlace m3u8 para el video: ")
        index = len(funciones.processes)
        funciones.download_video(url, index)
    elif user_input == "s":
        print("Videos descargándose:")
        for i, process in enumerate(funciones.processes):
            if process is not None:
                print(f"{i}: video_{i}.mp4")
        index = int(input("Introduce el índice del video que deseas detener: "))
        funciones.stop_download(index)
    else:
        print("Opción no válida")


