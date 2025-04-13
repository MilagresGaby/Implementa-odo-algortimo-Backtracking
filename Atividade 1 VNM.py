def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|" + "|".join(linha) + "|")
    print()

def movimento_valido(tabuleiro, linha, coluna, n):
    return 0 <= linha < n and 0 <= coluna < n and tabuleiro[linha][coluna] in (' ', 'D')

def chegou_destino(linha, coluna, destino):
    return (linha, coluna) == destino

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade, n, destino, visitados):
    melhor_profundidade = float('inf')
    melhor_linha, melhor_coluna = linha_atual, coluna_atual
    
    # Define as 4 direções possíveis: direita, esquerda, baixo, cima
    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for dl, dc in direcoes:
        nova_linha, nova_coluna = linha_atual + dl, coluna_atual + dc
        
        if movimento_valido(tabuleiro, nova_linha, nova_coluna, n) and (nova_linha, nova_coluna) not in visitados:
            if chegou_destino(nova_linha, nova_coluna, destino):
                return (nova_linha, nova_coluna, profundidade + 1)
            
            # Marca como visitado
            visitados.add((nova_linha, nova_coluna))
            tabuleiro[nova_linha][nova_coluna] = '*'
            
            # Chama recursivamente
            l, c, p = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1, n, destino, visitados)
            
            # Desmarca
            visitados.remove((nova_linha, nova_coluna))
            tabuleiro[nova_linha][nova_coluna] = ' '
            
            if p < melhor_profundidade:
                melhor_linha, melhor_coluna, melhor_profundidade = l, c, p
    
    return (melhor_linha, melhor_coluna, melhor_profundidade)

def main():
    # Definindo o tabuleiro
    tabuleiro = [
        [' ', ' ', ' ', 'D'],
        [' ', 'X', ' ', 'X'],
        [' ', 'X', ' ', ' '],
        ['*', ' ', ' ', ' ']
    ]
    n = len(tabuleiro)  # Tamanho do tabuleiro NxN
    
    # Posições inicial e destino
    inicio = (3, 0)
    destino = (0, 3)
    
    # Marca a posição inicial
    linha_atual, coluna_atual = inicio
    tabuleiro[linha_atual][coluna_atual] = '*'
    visitados = set()
    visitados.add((linha_atual, coluna_atual))
    
    print("Tabuleiro Inicial:")
    mostrar_tabuleiro(tabuleiro)
    
    while True:
        # Encontra o próximo movimento
        l, c, p = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0, n, destino, visitados)
        
        if p == float('inf'):
            print("Não foi possível encontrar um caminho até o destino!")
            break
        
        # Atualiza a posição atual
        linha_atual, coluna_atual = l, c
        tabuleiro[linha_atual][coluna_atual] = '*'
        visitados.add((linha_atual, coluna_atual))
        
        print(f"Movendo para ({linha_atual}, {coluna_atual})")
        mostrar_tabuleiro(tabuleiro)
        
        if chegou_destino(linha_atual, coluna_atual, destino):
            print("Destino alcançado!")
            break
        
        # Para fins de demonstração, vamos limitar a 10 movimentos
        if len(visitados) > 10:
            print("Limite de movimentos atingido!")
            break

if __name__ == "__main__":
    main()