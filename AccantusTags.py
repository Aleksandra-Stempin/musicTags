import classMusicTags
import os
def ReadNumberAndIncrease():
    trackNoFilePath = r"AccantusTrackNo.txt"
    if os.path.isfile(trackNoFilePath):
        trackNoFile = open(trackNoFilePath, "r")
        trackNo = trackNoFile.read()
        trackNoFile.close()
        try:
            trackNoInt = int(trackNo)
            newTrackNoInt = trackNoInt + 1
            newTrackNoStr = str(newTrackNoInt)
            trackNoFile = open(trackNoFilePath, "w")
            trackNoFile.write(newTrackNoStr)
            trackNoFile.close()
        except Exception as e:
            print("ReadNumberAndIncrease\n{}".format(e))
            trackNoInt = 1
        finally:
            return trackNoInt
    else:
        print("File {} doesn't exists".format(trackNoFilePath))
        return 1

musicDir = r"C:\Users\Olenka\Downloads\new4"
coverPath = r"images/accantusLogo.jpg"
album = "Accantus"
artist = "Studio Accantus"
trackNo = ReadNumberAndIncrease()
mt = classMusicTags.MusicTags()
mt.SetMusicTags(musicDirectory=musicDir
                ,albumName=album
                ,artistName=artist
                ,initTrackNumber=trackNo
                ,coverImg=coverPath)




