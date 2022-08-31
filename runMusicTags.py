import classMusicTags
import classAccantusTags
# music directory path
# musicDir = r"C:\Users\Olenka\Downloads\new4"
musicDir = r"C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\music"

# cower image path
# coverImg = r"C:\Users\Olenka\Downloads\dog.jpg"
# coverImg = r"C:\Users\Olenka\Downloads\accantusLogo.jpg"
# coverImg = r"C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\music\cover.jpg"
# album name
album = "pieselowo"
# artist name
artist = "piesely"

startTrackNo = 1
mt = classMusicTags.MusicTags()

# mt.SetMusicTags(
#     musicDirectory=musicDir
#     , albumName=album
#     , artistName=artist
#     , initTrackNumber=startTrackNo
#     , coverImg=coverImg
# )
# mt.SetMusicTagsCoverInTheDir(
#     musicDirectory=musicDir
#     # , albumName=album
#     # , artistName=artist
#     # , initTrackNumber=startTrackNo
# )

# mt.SetMusicTagsTagsInFileCoverInTheDir(musicDirectory=musicDir)
mta = classAccantusTags.MusicTagsForAccantus()
mta.AccantusMusicTags(musicDir)