# A importação 'randint' foi removida pois não estava sendo usada.

lista_npcs = []

player = {
    'nome': "SungJinWoo",
    'level': 1,
    'exp': 0,
    'exp_max': 30,
    'hp': 100,
    'hp_max': 100,
    'dano': 25,
}

def criar_npc(level):
    """Cria um novo dicionário de NPC com base no level."""
    novo_npc = {
        'nome': f"Monstro #{level}",
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level,
        'hp_max': 100 * level,
        'exp': 7 * level,
    }
    return novo_npc


def gerar_npcs(n_npcs):
    """Gera uma quantidade (n_npcs) de monstros e os adiciona à lista_npcs."""
    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        lista_npcs.append(npc)


def exibir_npcs():
    """Mostra os status de todos os NPCs na lista."""
    for npc in lista_npcs:
        exibir_npc(npc)


# --- CORREÇÃO 1 ---
# A função agora aceita o argumento 'npc' para saber qual NPC exibir.
def exibir_npc(npc):
    """Mostra os status de um único NPC."""
    print(
        f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // HP MAX: {npc['hp_max']} // EXP: {npc['exp']}"
    )


def exibir_player():
    """Mostra os status do jogador."""
    print(
        f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']} // HP MAX: {player['hp_max']} // EXP: {player['exp']} // EXP MAX: {player['exp_max']}"
    )


def reset_player():
    """Restaura o HP do jogador ao máximo."""
    player['hp'] = player['hp_max']


def reset_npc(npc):
    """Restaura o HP de um NPC ao máximo."""
    npc['hp'] = npc['hp_max']


def iniciar_batalha(npc):
    """Inicia um loop de batalha entre o player e um NPC."""
    print(f"{npc['nome']}")
    exibir_player()
    exibir_npc(npc)
    print("--------------------------------------------------\n")

    # O loop continua enquanto ambos estiverem vivos
    while player['hp'] > 0 and npc['hp'] > 0:
        
        # Turno do Jogador
        atacar_npc(npc)
        print(f"{player['nome']} ataca {npc['nome']} causando {player['dano']} de dano.")

        # Verifica se o NPC morreu antes de poder atacar
        if npc['hp'] <= 0:
            npc['hp'] = 0  # Garante que o HP não fique negativo
            exibir_info_batalha(npc)
            break  # Sai do loop da batalha
        
        # Turno do NPC
        atacar_player(npc)
        print(f"{npc['nome']} ataca {player['nome']} causando {npc['dano']} de dano.")
        
        exibir_info_batalha(npc)
        
        # Verifica se o Player morreu
        if player['hp'] <= 0:
            player['hp'] = 0 # Garante que o HP não fique negativo
            break # Sai do loop da batalha

    print("------------------- FIM DA BATALHA -------------------\n")
    # Verifica o resultado
    if player['hp'] > 0:
        print(f"O {player['nome']} venceu e ganhou {npc['exp']} de EXP!")
        player['exp'] += npc['exp']
        # Aqui você poderia adicionar a lógica de 'upar' (level up)
        # ex: if player['exp'] >= player['exp_max']: ...
        
    else:
        print(f"O {npc['nome']} venceu! {player['nome']} foi derrotado.")

    # Exibe os status finais
    exibir_player()
    exibir_npc(npc)
    print("\n")

    # Reseta os HPs para a próxima batalha
    reset_player()
    
    # --- CORREÇÃO 2 ---
    # Agora estamos passando o 'npc' que batalhou para a função de reset.
    reset_npc(npc)


def atacar_npc(npc):
    """Reduz o HP do NPC baseado no dano do player."""
    npc["hp"] -= player["dano"]


def atacar_player(npc):
    """Reduz o HP do player baseado no dano do NPC."""
    player["hp"] -= npc["dano"]


def exibir_info_batalha(npc):
    """Mostra o status atual da batalha."""
    print(f"Vida Player: {player['hp']}/{player['hp_max']}")
    
    # --- CORREÇÃO 3 ---
    # Exibindo o HP atual do NPC (npc['hp']) e não o máximo.
    print(f"Vida NPC: {npc['nome']} - {npc['hp']}/{npc['hp_max']}")
    print("-----------------------\n")


# --- Execução Principal do Jogo ---

# Cria 5 monstros
gerar_npcs(5)

# Pega o primeiro monstro da lista (Monstro #1) para a batalha
npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)