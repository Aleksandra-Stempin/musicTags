import os
import eyed3


class MusicTags():
    """sets tags as album, artist, album artist, track name and album cover image to mp3 files in given directory.
    Cover image must be a jpg file. Do not use latin extended characters"""

    def __init__(self):
        pass

    def _CheckDirectory(self, dir):
        """checks if given directory is a valid directory path"""
        if len(dir) == 0:
            print("Specify music directory")
            return False
        elif os.path.isdir(dir):
            return True
        else:
            print("Path {} doesn't match any directory on your machine".format(dir))
            return False

    def _ValidateArgs(self, argAlbum, argArtist):
        """checks if given arguments are valid (album and artist can not be empty"""
        albumOk = False
        artistOk = False
        errStr = ""
        if len(argAlbum) > 0:
            albumOk = True
        else:
            errStr = errStr + "You must specify album name\n"

        if len(argArtist) > 0:
            artistOk = True
        else:
            errStr = errStr + "You must specify artist name\n"

        if artistOk and albumOk:
            return True
        else:
            print(errStr)
            return False

    def _ListFilesInDirectory(self, dir):
        """creating list of images in directory"""
        songsList = []
        songsExtensions = ["mp3"]
        for song in os.listdir(dir):
            extension = (song[-3:]).lower()
            if extension in songsExtensions:
                songsList.append(song)
        return songsList

    # def _ChooseCoverImageFromDirectory(self, musicDirectory=""):
    #     if MusicTags._CheckDirectory(self, musicDirectory):
    #         # finding all images in directory
    #         imageList = []
    #         imgDic = {}
    #         imgExtensions = ["jpg"]
    #         imgNo = 1
    #         for img in os.listdir(musicDirectory):
    #             extension = (img[-3:]).lower()
    #             if extension in imgExtensions:
    #                 imageList.append(img)
    #                 # print(img)
    #                 imgDic[imgNo] = img
    #                 imgNo = imgNo + 1
    #         dictionaryText = ""
    #         dictionaryTextPartA = "\nChoose picture for album cover for directory {}\n".format(musicDirectory)
    #         dictionaryTextPartB = ""
    #         noList = list(imgDic.keys())
    #         for no, image in imgDic.items():
    #             dictionaryTextPartB = dictionaryTextPartB + "{} - {}\n".format(no, image)
    #         dictionaryText = "{}{}type here: ".format(dictionaryTextPartA, dictionaryTextPartB)
    #         usersConfirmation = ""
    #         while usersConfirmation.lower() not in ["y"]:
    #             chosenImgNo = 0
    #             while chosenImgNo not in noList:
    #                 chosenImgNo = input(dictionaryText)
    #                 try:
    #                     chosenImgNo = int(chosenImgNo)
    #                 except:
    #                     chosenImgNo = 0
    #             chosenImg = imgDic[chosenImgNo]
    #             userQuestion = '\nDo you want to set cover image for directory {} to {}?\n' \
    #                            'answer "y" for yes and "n" for no.\nType here: '.format(musicDirectory, chosenImg)
    #             usersConfirmation = input(userQuestion)
    #         confirmationText = "Tou have chosen image {} for album cower for directory {}.\n" \
    #                            "".format(chosenImg, musicDirectory)
    #         print(confirmationText)
    #         coverImage = "{}\{}".format(musicDirectory, chosenImg)
    #         return coverImage

    def SetMusicTags(self, musicDirectory="", albumName="no album", artistName="no artist", initTrackNumber=1,
                     coverImg=""):
        """add tags to mp3 files"""
        try:
            if MusicTags._CheckDirectory(self, musicDirectory) and MusicTags._ValidateArgs(self, albumName, artistName):
                songsList = MusicTags._ListFilesInDirectory(self, musicDirectory)
                if len(songsList) > 0:
                    trackNo = initTrackNumber
                    if not str(trackNo).isdigit():
                        trackNo = 1
                    for song in songsList:
                        try:
                            songName = song[0:-4]
                            song = "{}\{}".format(musicDirectory, song)
                            songTags = eyed3.load(song)
                            songTags.initTag()
                            # setting album nane
                            songTags.tag.album = albumName
                            # setting artist and album artist
                            songTags.tag.artist = ""
                            songTags.tag.artist = artistName
                            songTags.tag.album_artist = ''
                            songTags.tag.album_artist = artistName
                            # setting file name as song tittle
                            songTags.tag.title = songName
                            # setting track number beginning from given number or from 1 if initTrackNumber wasn't given
                            songTags.tag.track_num = trackNo
                            songTags.tag.images.remove('')
                            songTags.tag.images.remove(u"FRONT_COVER")

                            try:
                                if len((str(coverImg))) > 0:
                                    if os.path.isfile(coverImg) and coverImg.endswith(".jpg"):
                                        songTags.tag.images.set(3, open(coverImg, "rb").read(), "image/jpeg")
                                    else:
                                        print("Image {} is not a right cover image".format(coverImg))
                            except Exception as err:
                                print("Fail to set cover image:\n{}".format(err))
                            songTags.tag.save(version=eyed3.id3.ID3_V2_3)
                        except UnicodeEncodeError as e:
                            print("Please, do not use latin extended characters\nUnicodeEncodeError:\n{}\n".format(e))
                            break
                        except Exception as e:
                            print("Something went wrong in loop in function SetMusicTags:\n{}\n".format(str(e)))
                            continue
                        finally:
                            trackNo = trackNo + 1
                    print("Job is done.")
                else:
                    print("List of songs is empty\n")
        except Exception as err:
            print("Something went wrong if function SetMusicTags:\n{}\n".format(str(err)))

    def SetMusicTagsCoverInTheDir(self, musicDirectory="", albumName="no album", artistName="no artist", initTrackNumber=1):
        """add tags to mp3 files and set image from directory named cover as an album cover"""
        coverImagePath = "{}\cover.jpg".format(musicDirectory)
        if not os.path.isfile(coverImagePath):
            coverImagePath = ""
            print("There is no cover image in directory {}".format(musicDirectory))
        MusicTags.SetMusicTags(self, musicDirectory, albumName, artistName, initTrackNumber, coverImagePath)

    def SetMusicTagsTagsInFileCoverInTheDir(self, musicDirectory):
        """add tags to mp3 files and set image from directory named cover as an album cover.jpg, tags are read from a
        file named tags.txt from the same directory.
        Album is in first line of the file and artist is in the second line of the file"""
        filePath = "{}\\tags.txt".format(musicDirectory)
        coverPath = "{}\cover.jpg".format(musicDirectory)
        cover = ""
        album = ""
        artist = ""
        # check if musicDir is a valid directory
        if os.path.isdir(musicDirectory):
            # check if there is a tags.txt file in musicDir
            if os.path.isfile(filePath):
                # check if there is a cover.jpg file in musicDir
                # if os.path.isfile(coverPath):
                #     cover = coverPath
                # reading album name and artist name from file
                tagFile = open(filePath, "r")
                album = (tagFile.readline()).strip()
                artist = (tagFile.readline()).strip()
                # setting tags to mp3 files in directory
                print(musicDirectory, album, artist)
                MusicTags.SetMusicTagsCoverInTheDir(self, musicDirectory=musicDirectory, albumName=album,
                                                    artistName=artist, initTrackNumber=1)


            else:
                errMsg = "File tags.txt could not be found in directory {}.".format(musicDirectory)
                print(errMsg)
        else:
            print("{} in not a valid directory".format(musicDirectory))
