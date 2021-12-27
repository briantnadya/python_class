from itertools import cycle

"""b) part of the task 6"""
i = 0
music_genres = ["Retrowave", "House", "Hip-Hop", "Electronic dance"]
for el in cycle(music_genres):
    if i > 5:
        break
    else:
        print(el)

    i += 1
