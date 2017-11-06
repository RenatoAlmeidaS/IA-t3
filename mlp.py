from entradas2 import entradas

class perceptron(object):
	def __init__(self, final):
		self.perceptron_values(final)

	def perceptron_values(self, final):
		self.pesos = []
		inp = input("Entre com o peso 0: ")
		inp = float(inp)
		self.pesos.append(inp)
		inp = input("Entre com o peso 1: ")
		inp = float(inp)
		self.pesos.append(inp)

		eta = input("Entre com a taxa de aprendizado: ")
		self.eta = float(eta)
		self.delta=0
		if(final==True):
			self.entrada=0
			self.ent=[]

	def perceptron_train(self, final, valor):
		self.amostra = entradas[valor]
		u = self.pesos[0] * self.amostra[0] + self.pesos[1]*self.amostra[1]
		self.y = self.ativacao(u)
		if(final.entrada==0):
			final.entrada+=self.y*final.pesos[0]
			final.ent.append(self.amostra[0])
		else:
			final.entrada+=self.y*final.pesos[1]
			final.ent.append(self.amostra[1])

	def backpropagation(self, p1, p2, valor):
		self.amostra = entradas[valor]
		self.delta = self.entrada - self.amostra[2]
		print ("\n\nDelta pFinal: ", self.delta)
		if (self.delta<0.05):
			return False
		p1.delta = self.delta*self.pesos[0]
		p2.delta = self.delta*self.pesos[1]
		print ("Delta p1: " , p1.delta)
		print ("Delta p2: " , p2.delta, "\n\n")
		return True

	def pesos(self):
		return self.pesos

	def ativacao(self, soma):
		euler=2.718281828459045
		return 1.0/(1+(euler**(-soma)))


	def hebb(self, peso_atual, d, entrada):
		return peso_atual + self.eta * (d - self.y) * entrada


	def ajustePesos(self, final, valor):
		amostra = entradas[valor]
		if (final==True):	
			self.pesos[0] = self.pesos[0] + self.eta*self.ent[0]*self.delta
			self.pesos[1] = self.pesos[1] + self.eta*self.ent[1]*self.delta	
			print("PFinal - Pesos Novos:", self.pesos[0], " e ", self.pesos[1], "\n\n")			
		else:	
			self.pesos[0] = self.pesos[0] + self.eta*self.amostra[0]*self.delta
			self.pesos[1] = self.pesos[1] + self.eta*self.amostra[1]*self.delta
			print("p - Pesos Novos:", self.pesos[0], " e ", self.pesos[1])	

	def solucao(self,final, valor):
		u = self.pesos[0] * valor[0] + self.pesos[1]*valor[1]
		y = self.ativacao(u)

	def setNull(self):
		self.entrada=0
		self.ent=[]

final = perceptron(final = True)
p1 = perceptron(final = False)
p2 = perceptron(final = False)


erro = True
while erro is True:
	erro = False
	for i in range(0,len(entradas)):
		final.setNull()
		p1.perceptron_train(final,i)
		p2.perceptron_train(final,i)
		erro=final.backpropagation(p1,p2, i)
		p1.ajustePesos(False,i)
		p2.ajustePesos(False,i)
		final.ajustePesos(True,i)

p = []
p.append(p1.pesos)
p.append(p2.pesos)
p.append(final.pesos)
print("  SOLUÇÃO  \n")
print("Pesos finais p1: ",p1.pesos)
print("Pesos finais p2: ",p2.pesos)
print("Pesos finais pFinal: ",final.pesos)

teclado=1
while(teclado!='-1'):
	x=[]
	x.append(float(input("Entre com o primeiro valor X0 = ")))
	x.append(float(input("Entre com o segundo valor X1 = ")))
	print(p[2][0],p[0][0],x[0], p[0][1],x[1], p[2][1],p[1][0],x[0],p[1][1],x[1])
	print("Saída: ", resposta)
