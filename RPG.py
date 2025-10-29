from random import randint

lista_npcs = []

def criar_npc():
    level = randint(0, 50)

    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
    }

    return novo_npc


def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        npc = criar_npc()
        lista_npcs.append(npc)


def exibir_npcs():
    for npc in lista_npcs:
        print(
            f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']}"
        )





gerar_npcs(5)
exibir_npcs()

