import math
from scipy.io.wavfile import read, write
import sounddevice as sd

def findMax(source):
    tempx = 0
    tempy = 0
    for i in range( len( source ) ):
        if (tempx < source[i]):
            tempx = source[i]
            tempy = i
    return tempx, tempy

def switchToString(i):
    switcher = {
        0:'Boşluk',
        1:'Çıktı',
        2:'Düğme',
        3:'Elma',
        4:'Fil',
        5:'Kağit',
        6:'Poz',
        7:'Sandal',
        8:'Telefon',
        9:'Yeni',
    }
    return switcher.get(i,"Error")




fs = 44100  # Sample rate
seconds = 1  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2,dtype = 'int16')

sd.wait()  # Wait until recording is finished
write('Output.wav', fs, myrecording)  # Save as WAV file

Fs, data = read( "Output.wav" )
sesOutput = data[:, 0]

x2,y2 = findMax( sesOutput )



Fs, data = read( "toInclude/Boşluk.wav" )
sesBosluk= data[:, 0]
Fs, data = read( "toInclude/Düğme.wav" )
sesDügme = data[:, 0]
Fs, data = read( "toInclude/Elma.wav" )
sesElma = data[:, 0]
Fs, data = read( "toInclude/Fil.wav" )
sesFil = data[:, 0]
Fs, data = read( "toInclude/Kağıt.wav" )
sesKagit= data[:, 0]
Fs, data = read( "toInclude/Poz.wav" )
sesPoz = data[:, 0]
Fs, data = read( "toInclude/Sandal.wav" )
sesSandal = data[:, 0]
Fs, data = read( "toInclude/Telefon.wav" )
sesTelefon = data[:, 0]
Fs, data = read( "toInclude/Yeni.wav" )
sesYeni = data[:, 0]
Fs, data = read( "toInclude/Çıktı.wav" )
sesCikti = data[:, 0]



tempHolder =0
minRangeToRecorded =10000000
ses = sesBosluk,sesCikti, sesDügme,sesElma,sesFil,sesKagit,sesPoz,sesSandal,sesTelefon,sesYeni #Alphabetical order



for i in range( 10 ):
    x1, y1 = findMax( ses[i] )
    rangeToRecorded = math.sqrt(abs((x1-x2)^2 + (y1-y2)^2))
    print(switchToString(i)," : ", rangeToRecorded)
    if(minRangeToRecorded > rangeToRecorded):
        minRangeToRecorded = rangeToRecorded
        tempHolder = i


print("Söylediğiniz kelime :",switchToString(tempHolder),"Olabilir mi ? : ", minRangeToRecorded)

