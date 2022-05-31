# Mock Final Exam
# Q2

# Prints a welcome message
print("Welcome to JukeBox Music Library\n\n")

# Opens MusicLibrary.txt and allows read/write access
with open("MusicLibrary.txt", "r+") as f:
    # Reads the file, splits every record by newline then stores it in a variable
    library = f.read().split("\n")
    # Splits records by delimiter "|" and stores it in a variable
    splitLibrary = []
    for i in range(len(library)):
        splitLibrary.append(library[i].split("|"))
    
    playStatus = True
    dictLibrary = {}
    nowPlayingArtist = ""
    nowPlayingSong = ""
    
    # Loops through the splitLibrary variable and adds the artist and songs to a dictionary
    for i in range(len(splitLibrary)):
        dictLibrary[splitLibrary[i][0]] = splitLibrary[i][1:]

    while playStatus == True:
        # Asks the user for an artist name and stores it in a variable
        artist = input("Please key in artist: ")
        # Upper cases the artist name
        artist = artist.upper()
        # If the artist name is not in the dictionary, adds it to the dictionary
        if not(artist in list(dictLibrary.keys())):
            print("New artist added to library")
            dictLibrary[artist] = []
        
        # Asks the user for a song name and stores it in a variable
        song = input("Title: ")
        # Upper cases the song name
        song = song.upper()
        # If the song name is not in the dictionary, adds it to the dictionary
        if not(song in dictLibrary[artist]):
            print("New song added to library")
            dictLibrary[artist].append(song)

        # Checks if current artist and song are the same as the one the user is searching for
        if nowPlayingArtist == artist and nowPlayingSong == song:
            # Asks the user if they want to replay the song
            toReplay = input("Replay? ")
            if toReplay.lower() == "yes":
                print("Playing...")
                # Asks the user if they want to play another song
                toContinue = input("\nPlay another song? ")
                if toContinue.lower() == "no":
                    playStatus = False
            else:
                # Asks the user if they want to play another song
                toContinue = input("\nPlay another song? ")
                if toContinue.lower() == "no":
                    playStatus = False
        else:
            # Sets the current artist and song to the one the user is searching for
            nowPlayingArtist = artist
            nowPlayingSong = song
            print("Playing...")
            # Asks the user if they want to play another song
            toContinue = input("\nPlay another song? ")
            if toContinue.lower() == "no":
                playStatus = False

    # Syncronises the dictionary with the file
    outputString = ""
    for artist in dictLibrary:
        outputString += artist + "|"
        for song in dictLibrary[artist]:
            outputString += song + "|"
        outputString = outputString[:-1] + "\n"
    outputString = outputString[:-1]
    f.seek(0)
    f.write(outputString)
    f.truncate()

# Prints a goodbye message
print("\n\nThank you for using JukeBox Music Library")
