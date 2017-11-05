from entradas import entradas

class perceptron(object):
	def __init__(self):
		self.perceptron_trein()

	def perceptron_trein(self):
		self.pesos = []
		inp = input("Entre com o peso 0: ")
		inp = float(inp)
		self.pesos.append(inp)
		inp = input("Entre com o peso 1: ")
		inp = float(inp)
		self.pesos.append(inp)

		eta = input("Entre com a taxa de aprendizado: ")
		self.eta = float(eta)
		limiar = input("Entre com o limiar: ")
		self.limiar = float(limiar)
		self.epoca = 0

		erro = True;
		while erro is True:
			erro = False
			for i in range(0,len(entradas)):
				amostra = entradas[i]
				u = self.pesos[0] * amostra[0] + self.pesos[1]*amostra[1]
				self.y = self.ativacao(u)
				if(self.y != amostra[2]):
					self.pesos[0] = self.hebb(peso_atual = self.pesos[0], d = amostra[2], entrada = amostra[0])
					self.pesos[1] = self.hebb(peso_atual = self.pesos[1], d = amostra[2], entrada = amostra[1])
					erro = True
			print("Época: ", self.epoca, "		Peso 1: ", self.pesos[0], "		Peso 2: ", self.pesos[1])
			self.epoca += 1

		print("Épocas: ", self.epoca, "		Peso 1: ", self.pesos[0], "		Peso 2: ", self.pesos[1])

	def ativacao(self, soma):
		if(self.limiar + soma < 2):
			return 0
		return 1


	def hebb(self, peso_atual, d, entrada):
		return peso_atual + self.eta * (d - self.y) * entrada

	def classificar(self):
		x0 = float(input("Entre com o primeiro valor X0 = "))
		x1 = float(input("Entre com o segundo valor X1 = "))

		soma = x0*self.pesos[0] + x1*self.pesos[1]
		self.y = self.ativacao(soma)

	

a = perceptron()
a.classificar()
print(a.y)