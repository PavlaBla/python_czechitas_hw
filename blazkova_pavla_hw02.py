import json

data = []
with open('netflix_titles.tsv', mode='r', encoding='utf-8') as file:
    for line in file:
        data.append(line.strip().split('\t'))

header = data[0]
data = data[1:]

title_index = header.index('PRIMARYTITLE')
director_index = header.index('DIRECTOR')
cast_index = header.index('CAST')
genre_index = header.index('GENRES')
decade_index = header.index('STARTYEAR')

movies_info = []

for line in data:
    dict_movie = {
        'title': line[title_index],
        'directors': line[director_index].split(', ') if line[director_index] else [],
        'cast': line[cast_index].split(', ') if line[cast_index] else [],
        'genres': line[genre_index].split(',') if line[genre_index] else [],
        'decade': (int(line[decade_index]) // 10) * 10
    }
    movies_info.append(dict_movie)


with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(movies_info, file, ensure_ascii=False, indent=4)
