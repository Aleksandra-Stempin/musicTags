import classMusicTags
import os

trackNoFilePath = r"AccantusTrackNo.txt"
musicDir = r"C:\Users\Olenka\Downloads\new4"
coverPath = r"images/accantusLogo.jpg"
album = "Accantus"
artist = "Studio Accantus"
def ReadNumber():
    trackNoInt = 1
    if os.path.isfile(trackNoFilePath):
        trackNoFile = open(trackNoFilePath, "r")
        trackNo = trackNoFile.read()
        trackNoFile.close()
        try:
            trackNoInt = int(trackNo)
        except Exception as e:
            print("ReadNumber\n{}".format(e))
        finally:
            return trackNoInt
    else:
        print("File {} doesn't exists".format(trackNoFilePath))
        return 1

def WriteNumber(intNo):
    try:
        no = int(intNo)
        no = no + 1
        noStr = str(no)
        if os.path.isfile(trackNoFilePath):
            trackNoFile = open(trackNoFilePath, "w")
            trackNoFile.write(noStr)
            trackNoFile.close()
        else:
            print("File {} doesn't exists".format(trackNoFilePath))
    except Exception as e:
        print("WriteNumber\n{}".format(e))


def MusicTagsForAccantus():
    trackNo = ReadNumber()
    mt = classMusicTags.MusicTags()
    tn = mt.SetMusicTags(musicDirectory=musicDir
                    ,albumName=album
                    ,artistName=artist
                    ,initTrackNumber=trackNo
                    ,coverImg=coverPath)
    WriteNumber(tn)




