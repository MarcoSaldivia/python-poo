import math

class FuncionTrigonometrica:
    def __init__(self, tipo, amplitud=1, periodo=2*math.pi):
        self.tipo = tipo
        self.amplitud = amplitud
        self.periodo = periodo

    # Evaluar la función
    def evaluar(self, x):
        w = (2*math.pi) / self.periodo   

        if self.tipo == "seno":
            return self.amplitud * math.sin(w * x)
        elif self.tipo == "coseno":
            return self.amplitud * math.cos(w * x)
        elif self.tipo == "tangente":
            return self.amplitud * math.tan(w * x)

    #  "Graficar" mostrando valores
    def graficar(self, inicio, fin, pasos=10):
        x = inicio
        salto = (fin - inicio) / pasos
        valores = []

        while x <= fin:
            valores.append((x, self.evaluar(x)))
            x += salto

        return valores  

    # Representación de texto
    def __str__(self):
        return f"Función {self.tipo} con amplitud={self.amplitud} y periodo={self.periodo}"

    # Valor crítico
    def valor_critico(self):
        if self.tipo in ["seno", "coseno"]:
            return {"maximo": self.amplitud, "minimo": -self.amplitud}
        else:
            return "La tangente no tiene máximos ni mínimos."
