class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        x, y = len(s), len(p)
        mm = [[False] * (y + 1) for _ in range(x + 1)]
        mm[0][0] = True

        #Regex com '*' remove caractere anterior ex: 'a*'
        for j in range(2, y + 1):
            if p[j - 1] == '*':
                mm[0][j] = mm[0][j - 2] #gap em x

        for i in range(1, x + 1):
            for j in range(1, y + 1):
                #Caracteres iguais: diagonal
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    mm[i][j] = mm[i - 1][j - 1] # match
                #Repetição de caracteres
                #1 gap e eliminar o caractere anterior (`mm[i][j - 2]`)
                #2 repetir o caractere anterior se não houver mismatch (`mm[i - 1][j]`)
                elif p[j - 1] == '*':
                    mm[i][j] = mm[i][j - 2] or (mm[i - 1][j] if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False)

        return mm[x][y]

'''
      x1 |x2 |x3     
       0 | a | b
  | 0  T   F   F
y1| .  F   T   F
y2| *  T   T   T

'''