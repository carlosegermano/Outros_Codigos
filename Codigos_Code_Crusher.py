#CÓDIGOS CODE_CRUSHER

#PARTE 1 - CRIAR TABULEIRO
def createBoard(nRows, nColumns, n):
    board = [] #Array que representa o tabuleiro
    #Percorre cada linha do tabuleiro
    for rows in range(nRows):
        line = [] #Cada linha do tabuleiro
        #Percorre cada posição da linha e adiciona um elemento
        for colum in range(nColumns):
            line.append(randrange(n))
        #Adiciona a linha ao tabuleiro
        board.append(line)
    return board

#PARTE 2 - SWAP
def swap(board, r1, c1, r2, c2):
    temp = board[r1][c1]
    board[r1][c1] = board[r2][c2]
    board[r2][c2] = temp

#PARTE 3 - A PEÇA ESPECIAL
def clearAll(board, sym):
    # percorre cada linha na matriz
    for line in board:
        x = 0
        # percorre cada símbolo (index) na linha e verifica se é um símbolo ingual ao passado como parâmetro
        # substitui todos os símbolos iguais por um espaço vazio (-1 ou EMPTY)
        for symbol in line:
            if symbol == sym:
                line[x] = EMPTY
            x += 1

#PARTE 4 - LIMITANDO O SWAP
def vLineAt(board, r1, c1, r2, c2):

    # Primeira peça
    if r1 == 0:
        if board[r1+1][c1] == board[r1][c1] and board[r1+2][c1] == board[r1][c1]:
            return True

    elif r1 == len(board)-1:
        if board[r1-1][c1] == board[r1][c1] and board[r1-2][c1] == board[r1][c1]:
            return True

    elif r1 == 1:
        if board[r1-1][c1] == board[r1][c1] and board[r1+1][c1] == board[r1][c1]:
            return True
        elif board[r1+1][c1] == board[r1][c1] and board[r1+2][c1] == board[r1][c1]:
            return True

    elif r1 == len(board)-2:
        if board[r1-1][c1] == board[r1][c1] and board[r1-2][c1] == board[r1][c1]:
          return True
        elif board[r1-1][c1] == board[r1][c1] and board[r1+1][c1] == board[r1][c1]:
          return True

    else:
        if board[r1-1][c1] == board[r1][c1] and board[r1 + 1][c1] == board[r1][c1]:
          return True
        elif board[r1+1][c1] == board[r1][c1] and board[r1+2][c1] == board[r1][c1]:
          return True
        elif board[r1-1][c1] == board[r1][c1] and board[r1-2][c1] == board[r1][c1]:
          return True

    #Segunda peça
    if r2 == 0:
      if board[r2+1][c2] == board[r2][c2] and board[r2+2][c2] == board[r2][c2]:
        return True

    elif r2 == len(board) - 1:
      if board[r2-1][c2] == board[r2][c2] and board[r2-2][c2] == board[r2][c2]:
        return True

    elif r2 == 1:
      if board[r2-1][c2] == board[r2][c2] and board[r2+1][c2] == board[r2][c2]:
        return True
      elif board[r2+1][c2] == board[r2][c2] and board[r2+2][c2] == board[r2][c2]:
        return True

    elif r2 == len(board) - 2:
      if board[r2-1][c2] == board[r2][c2] and board[r2-2][c2] == board[r2][c2]:
        return True
      elif board[r2-1][c2] == board[r2][c2] and board[r2+1][c2] == board[r2][c2]:
        return True

    else:
      if board[r2-1][c2] == board[r2][c2] and board[r2+1][c2] == board[r2][c2]:
        return True
      elif board[r2+1][c2] == board[r2][c2] and board[r2+2][c2] == board[r2][c2]:
        return True
      elif board[r2-1][c2] == board[r2][c2] and board[r2-2][c2] == board[r2][c2]:
        return True

    return False

def hLineAt(board, r1, c1, r2, c2):
  # Primeira peça
  if c1 == 0:
    if board[r1][c1+1] == board[r1][c1] and board[r1][c1+2] == board[r1][c1]:
      return True

  elif c1 == len(board[0]) - 1:
    if board[r1][c1-1] == board[r1][c1] and board[r1][c1-2] == board[r1][c1]:
      return True

  elif c1 == 1:
    if board[r1][c1-1] == board[r1][c1] and board[r1][c1+1] == board[r1][c1]:
      return True
    elif board[r1][c1+1] == board[r1][c1] and board[r1][c1+2] == board[r1][c1]:
      return True

  elif c1 == len(board[0]) - 2:
    if board[r1][c1-1] == board[r1][c1] and board[r1][c1-2] == board[r1][c1]:
      return True
    elif board[r1][c1-1] == board[r1][c1] and board[r1][c1+1] == board[r1][c1]:
      return True

  else:
    if board[r1][c1-1] == board[r1][c1] and board[r1][c1+1] == board[r1][c1]:
      return True
    elif board[r1][c1+1] == board[r1][c1] and board[r1][c1+2] == board[r1][c1]:
      return True
    elif board[r1][c1-1] == board[r1][c1] and board[r1][c1-2] == board[r1][c1]:
      return True

  # Segunda peça
  if c2 == 0:
    if board[r2][c2+1] == board[r2][c2] and board[r2][c2+2] == board[r2][c2]:
      return True

  elif c2 == len(board[0]) - 1:
    if board[r2][c2-1] == board[r2][c2] and board[r2][c2-2] == board[r2][c2]:
      return True

  elif c2 == 1:
    if board[r2][c2-1] == board[r2][c2] and board[r2][c2+1] == board[r2][c2]:
      return True
    elif board[r2][c2+1] == board[r2][c2] and board[r2][c2+2] == board[r2][c2]:
      return True

  elif c2 == len(board[0]) - 2:
    if board[r2][c2-1] == board[r2][c2] and board[r2][c2-2] == board[r2][c2]:
      return True
    elif board[r2][c2-1] == board[r2][c2] and board[r2][c2+1] == board[r2][c2]:
      return True

  else:
    if board[r2][c2-1] == board[r2][c2] and board[r2][c2+1] == board[r2][c2]:
      return True
    elif board[r2][c2+1] == board[r2][c2] and board[r2][c2+2] == board[r2][c2]:
      return True
    elif board[r2][c2-1] == board[r2][c2] and board[r2][c2-2] == board[r2][c2]:
      return True

  return False
  