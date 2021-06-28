import os, sys
import os.path
import song as s
from mutagen.id3 import USLT, Encoding
import time

repetir = True

while repetir:

    total = 0
    archivo_ini = 0
    error = 0
    agregado_lyric = 0

    os.system('clear')
    ruta = str(input("Ingrese la ruta de la cancion(es): "))


    if os.path.exists(ruta):

        if ".mp3" in ruta or ".flac" in ruta:

            song = s.Cancion(ruta, True)

            if not song.letra[0] == 'archivoInvalido' and not song.letra[0] == 'archivoTieneLetra':
                if song.esFlac:

                    song.archivo_cancion['LYRICS'] = song.letra[0]
                    song.archivo_cancion.save()

                elif song.esMp3:

                    song.archivo_cancion.setall("USLT", [USLT(encoding=Encoding.UTF8, text=song.letra[0])])
                    song.archivo_cancion.save()
                    
                agregado_lyric += 1
            
            else:
                error += 1

        else:

            os.system('clear')
            for root, dir, files in os.walk(ruta):
                for file in files:

                    archivo = os.path.join(root, file)

                    song = s.Cancion(archivo, True)

                    if ".ini" in file:
                        archivo_ini += 1
                        continue

                    if song.letra[0] == 'archivoInvalido':
                        error += 1
                        continue

                    elif song.letra[0] == 'archivoTieneLetra':
                        error += 1
                        continue

                    elif song.letra[0] == 'letraNoEncontrada':
                        error += 1
                        continue

                    else:
                        if song.esFlac:

                            song.archivo_cancion['LYRICS'] = song.letra[0]
                            song.archivo_cancion.save()

                        elif song.esMp3:

                            song.archivo_cancion.setall("USLT", [USLT(encoding=Encoding.UTF8, text=song.letra[0])])
                            song.archivo_cancion.save()
                        
                        agregado_lyric += 1
        
        
        print("")
        print("Letra agregada a {} canciones desde Genius" .format(agregado_lyric))
        print("Letra no fue agregada a {} canciones" .format(error))
        print("Archivos ini: {}" .format(archivo_ini))
        print("---------------------")
        print("Total: {}" .format(error+archivo_ini+agregado_lyric))
        print("")

        loopError = True

        while loopError:

            resp = input("¿Desea agregar letra a otras canciones? (S/N) ")

            print(resp)

            if resp.upper() == "S":
                break

            elif resp.upper() == "N":
               sys.exit()

            else:
                continue

    else:
        print('')
        print("El directorio o archivo no existe.")
        time.sleep(1.5)
        continue