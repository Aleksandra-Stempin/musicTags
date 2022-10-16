import classMusicTags
import classAccantusTags
# music directory path
# musicDir = r"C:\Users\Olenka\Downloads\new4"
musicDir = r"C:\Users\Oleńka\Downloads\newMusic"

# cower image path
# coverImg = r"C:\Users\Olenka\Downloads\dog.jpg"
# coverImg = r"C:\Users\Olenka\Downloads\accantusLogo.jpg"
coverImg = r"C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\music\dog2.jpg"
coverImg = r"C:\Users\aleksandra.stempin\OneDrive - Accenture\!Sync\Downloads\music\cat.jpg"
voyageDir = r"C:\Users\Oleńka\Music\Voyage"
voyageCover = r"C:\Users\Oleńka\Downloads\voyage.jpg"
# album name
album = "Voyage"
# artist name
artist = "ABBA"

startTrackNo = 1
# mt = classMusicTags.MusicTags()
# mt.SetCoverOnly(musicDirectory=voyageDir
#                 ,coverImg=voyageCover
#                 )

# mt.SetMusicTags(
#     musicDirectory=voyageDir
#     , albumName=album
#     , artistName=artist
#     , initTrackNumber=startTrackNo
#     , coverImg=voyageCover
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

