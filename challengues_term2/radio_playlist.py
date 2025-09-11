import time
weekly_playlist = ["Blinding Lights", "Levitating", "As It Was", "Heat Waves", "Good 4 u"]
weekly_playlist.append("Drivers License")
weekly_playlist.insert(0, "Bohemian Rhapsody")
weekly_playlist.remove("Good 4 u")
print(weekly_playlist.index("Levitating")) #Index where Levitating is
print(weekly_playlist.count("As It Was")) #I don't really understand this step, there's only one song of him?
throwback_playlist = weekly_playlist.copy()
throwback_playlist.reverse()
print(throwback_playlist) #Throwback
sorted_playlist = weekly_playlist.copy()
sorted_playlist.sort()
print(sorted_playlist) #sorted playlist
print(weekly_playlist) #final result
print(f"There's a total of {len(weekly_playlist)} songs in the final playlist.")
while True:
    #forgot to put that time thing
    time.sleep(2) # 2 seconds just to prove it works :p
    weekly_playlist.insert(6, weekly_playlist[0])
    weekly_playlist.remove(weekly_playlist[0])
    print(weekly_playlist)
    if weekly_playlist[0] == "Bohemian Rhapsody":
        break