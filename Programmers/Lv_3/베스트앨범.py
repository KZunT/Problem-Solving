# def solution(genres, plays):
#     answer = []
#     album = dict()

#     for genre , play in zip (genres,plays):
#         if genre in album:
#             album[genre] += play
#         else:
#             album[genre] = play

#     genres_score = sorted(album.items() , key = lambda x : x[1] , reverse = True)

#     for genres_name in genres_score:
#         song = []

#         for i,p in enumerate(zip(genres,plays)):
#             if genres_name[0] == p[0]:
#                 song.append((i,p))

#         song.sort(key = lambda x:x[1][1], reverse = True)

#         if len(song) == 1:
#             answer.append(song[0][0])
#         else:
#             answer.append(song[0][0])
#             answer.append(song[1][0])

#     return answer

def solution(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    genreSort = sorted(list(d.keys()), key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]
    return answer