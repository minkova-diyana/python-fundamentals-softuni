def pokemon_capturing(pokemons, index):
    if index < 0:
        captured_pokemon = pokemons[0]
        pokemons.pop(0)
        pokemons.insert(0, pokemons[-1])
    elif index > len(pokemons) - 1:
        captured_pokemon = pokemons[-1]
        pokemons.pop(-1)
        pokemons.append(pokemons[0])
    else:
        captured_pokemon = pokemons[index]
        pokemons.pop(index)
    for i in range(len(pokemons)):
        pokemon = pokemons[i]
        if pokemon > captured_pokemon:
            pokemon -= captured_pokemon
            pokemons[i] = pokemon
        elif pokemon <= captured_pokemon:
            pokemon += captured_pokemon
            pokemons[i] = pokemon
    return pokemons, captured_pokemon


pokemon_distance = [int(s) for s in input().split()]
result_sum = []
while pokemon_distance:
    index_pokemon = int(input())
    pokemon_distance, results = (pokemon_capturing(pokemon_distance, index_pokemon))
    result_sum.append(results)
print(sum(result_sum))
