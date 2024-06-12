# Zadani: Z prilozeneho tsv souboru vytvor pomoci JSON seznam slovniku,
# kde u kazdeho filmu te budou zajimat jen urcite polozky.
# Kazdy film prirad k dekade


import json

data = []
with open('netflix_titles.tsv', mode='r', encoding='utf-8') as file:
    for line in file:
        data.append(line.strip().split('\t'))

# nacte soubor a po radku jej ulozi do seznamu data
# vycisteni o prebytecne znaky, rozdeli radky pomoci '\t' delimiteru

header = data[0]
data = data[1:]

# oddeli hlavicku od dat

title_index = header.index('PRIMARYTITLE')
director_index = header.index('DIRECTOR')
cast_index = header.index('CAST')
genre_index = header.index('GENRES')
decade_index = header.index('STARTYEAR')

# najde indexy sloupcu specifikovanych v zadani

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

# vytvori seznam slovniku s klici podle zadani

with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(movies_info, file, ensure_ascii=False, indent=4)

# ulozi data do JSON souboru