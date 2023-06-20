class Grafos:
    def __init__(self):
        while True:
            num = input('Insira o número de vértices:')
            try:
                self.num = int(num)
                if 1 <= self.num <= 20:
                    break
                else:
                    print('Número inválido, insira um número entre 1 e 20')
            except ValueError:
                print('Entrada inválida. Insira um número inteiro válido.')

        self.grafos = [[0] * self.num for _ in range(self.num)]

    def addAresta(self):
        x = input('Insira os vértices que deseja ligar por uma aresta e o peso (ou -1 para sair): ')
        if x == "-1":
            return

        try:
            x = int(x)
            if x <= 0 or x > self.num:
                print("Vértice inválido")
                self.addAresta()
                return

            y = input()
            y = int(y)
            if y <= 0 or y > self.num:
                print("Vértice inválido")
                self.addAresta()
                return

            weight = input()
            weight = int(weight)
            if weight <= 0:
                print("Número inválido, insira um peso maior que zero")
                self.addAresta()
                return

            self.grafos[x - 1][y - 1] = weight
            self.printMatriz()
            self.addAresta()

        except ValueError:
            print("Entrada inválida. Insira um número inteiro válido.")

    def printMatriz(self):
        print('A matriz de adjacência é:')
        for i in range(self.num):
            print(self.grafos[i])


g = Grafos()
g.printMatriz()
g.addAresta()
