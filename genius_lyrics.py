import os, sys
import song as s
from tqdm import tqdm
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


    if "\\" in ruta or "/" in ruta:

        if ".mp3" in ruta or ".flac" in ruta:

            song = s.Cancion(ruta)

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

        else:

            os.system('clear')
            for root, dir, files in os.walk(ruta):
                for file in tqdm(files,desc="Procesando", ncols=100):

                    archivo = os.path.join(root, file)

                    song = s.Cancion(archivo)

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

            resp = input("¿Desea agregar letra a otras cancioness? (S/N) ")

            print(resp)

            if resp.upper() == "S":
                break

            elif resp.upper() == "N":
               sys.exit()

            else:
                continue

    else:

        print("Ingrese una ruta valida.")
        time.sleep(1)
        continue