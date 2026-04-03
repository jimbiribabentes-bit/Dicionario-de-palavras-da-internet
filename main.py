meme_dict = {
    "CRINGE": "Algo constrangedor",
    "STALKEAR": "Investigar informações e vida de alguém na rede",
    "SPAM": "Repetir a mesma mensagem no chat sem parar",
    "GG": "Good Game, no português significa bom jogo",
    "MB": "My bad, no português é como um minha culpa"
            }

word = input("Digite uma palavra moderna: ").upper()


if word in meme_dict.keys():
    print ("O significado de", word, "é:", meme_dict[word])
