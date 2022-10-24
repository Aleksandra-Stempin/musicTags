import classMusicTags
import os
class MusicTagsForAccantus():
    """sets tags (album and artist name and sets cover image) for Accantus songs"""
    global _trackNoFilePath
    global trackNumber
    trackNumber = 1
    _trackNoFilePath = r"AccantusTrackNo.txt"

    def _ReadNumber(self):
        """reads track number from file"""
        trackNoInt = 1
        if os.path.isfile(_trackNoFilePath):
            trackNoFile = open(_trackNoFilePath, "r")
            trackNo = trackNoFile.read()
            trackNoFile.close()
            try:
                trackNoInt = int(trackNo)
            except Exception as e:
                print("ReadNumber\n{}".format(e))
            finally:
                return trackNoInt
        else:
            print("File {} doesn't exists".format(_trackNoFilePath))
            return 1

    def _WriteNumber(self, intNo):
        """writes track number to file"""
        try:
            no = int(intNo)
            noStr = str(no)
            if os.path.isfile(_trackNoFilePath):
                trackNoFile = open(_trackNoFilePath, "w")
                trackNoFile.write(noStr)
                trackNoFile.close()
            else:
                print("File {} doesn't exists".format(_trackNoFilePath))
        except Exception as e:
            print("WriteNumber\n{}".format(e))


    def AccantusMusicTags(self, musicDirectory):
        """sets tags to mp3 files in directory"""
        coverPath = r"images/accantusLogo.jpg"
        album = "Accantus"
        artist = "Studio Accantus"
        trackNo = MusicTagsForAccantus._ReadNumber(self)

        mt = classMusicTags.MusicTags()
        trackNumber = mt.SetMusicTags(musicDirectory=musicDirectory
                        ,albumName=album
                        ,artistName=artist
                        ,initTrackNumber= trackNo
                        ,coverImg=coverPath)
        trackNumberStr = str(trackNumber)
        MusicTagsForAccantus._WriteNumber(self, trackNumberStr)





