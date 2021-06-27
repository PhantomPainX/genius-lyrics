#Code to verify if the song has lyrics.

import os, sys
import song as s

repetir = True

while repetir:

    os.system('clear')

    print("Formatos: .mp3 .flac")
    print("Si el archivo tiene letra, esta se mostrara")
    print('')
    ruta_cancion = input("Ingrese la ruta de la cancion (debe terminar en los formatos): ")
    print('')

    if ".mp3" in ruta_cancion or ".flac" in ruta_cancion:

        archivo = s.Cancion(ruta_cancion, False)

        val = archivo.letra[0]

        if val == "archivoTieneLetra":

            print(archivo.lyrics)

        else:
            print("No tiene letra")

    else:
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
