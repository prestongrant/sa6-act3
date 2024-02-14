pokemon_list_1 = ['Lugia', 'Rayquaza', 'Dragonite', 'Sylveon']
pokemon_list_2 = ['Rayquaza', 'Sylveon', 'Spheal', 'Espeon']
intersection_list = list(filter(lambda x: x in pokemon_list_1, pokemon_list_2))

print(intersection_list)