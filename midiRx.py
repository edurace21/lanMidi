# leer comandos midi
from pygame import midi
# enviar request http
import requests
import json

# iniciar modulo MIDI
midi.init()

# obtener info de dispositivos
devCount = midi.get_count()
for devId in range(devCount):
    devInfo = midi.get_device_info(devId)
    print(f"{devId}\t{devInfo[1]}", end='')
    if devInfo[2] == 1:
        print('\tINPUT', end='')
    if devInfo[3] == 1:
        print('\tOUTPUT', end='')
    if devInfo[4] == 1:
        print('\tOPENED')
    else:
        print()

# seleccionar dispositivos
selectDev = int(input("Seleccione dispositivo:"))
midiIn = midi.Input(selectDev)

# Requests
url = 'http://192.168.0.129:8080/midi'

class MIDIMessage:
    def __init__(self, channel, note, value):
        self.channel = channel
        self.note = note
        self.value = value

# leer datos MIDI
while True:
    try:
        if midiIn.poll():
            midiMessage = midiIn.read(1)[0][0]
            requestData = {"channel":midiMessage[0],
                           "note":midiMessage[1],
                           "value":midiMessage[2]}
            dataJson = json.dumps(requestData, indent=4)
            print(dataJson)
            requests.post(url=url, data=dataJson, 
                          headers={"Content-Type":"application/json"}, 
                          timeout=0.5)

    except requests.exceptions.Timeout:
        pass
    except requests.exceptions.ChunkedEncodingError:
        pass
    except requests.exceptions.ConnectionError:
        pass

    # terminar programa
    except KeyboardInterrupt:
        midiIn.close()
        break

