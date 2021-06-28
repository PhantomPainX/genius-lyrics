#Code to verify if the song has lyrics.

import os, sys
import os.path
import song as s

repetir = True
ruta_error = ""
rec = False

while repetir:

    os.system('clear')

    if rec:
        print(ruta_error)
        print('')

    print("Formatos: .mp3 .flac")
    print("Si el archivo tiene letra, esta se mostrara")
    print('')
    ruta_cancion = input("Ingrese la ruta de la cancion (debe terminar en los formatos): ")
    print('')

    if ".mp3" in ruta_cancion or ".flac" in ruta_cancion:

        if os.path.exists(ruta_cancion):

            archivo = s.Cancion(ruta_cancion, False)

            val = archivo.letra[0]

            if val == "archivoTieneLetra":

                print(archivo.lyrics)

            else:
                print("No tiene letra")

            rec = False

        else:
            rec = True
            ruta_error = "El archivo no existe"
            continue

    else:
        rec = True
        ruta_error = "La ruta no es un archivo valido"
        continue

    print('')

    loopError = True

    while loopError:

        resp = input("¿Desea verificar otra canción? (S/N) ")

        print(resp)

        if resp.upper() == "S":
            break

        elif resp.upper() == "N":
            sys.exit()

        else:
            continue
