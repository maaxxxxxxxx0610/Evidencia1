import networkx as nx
from mesa import Agent

class Semaforo(Agent): 
    def __init__ (self, model, estadoInicial = "green", tiempoVerde = 10, tiempoAmarillo = 2): 
        super().__init__(model)
        self.estado = estadoInicial
        self.tiempoV = tiempoVerde
        self.tiempoA = tiempoAmarillo
        #tiempo rojo = V + A
        self.tiempoR = tiempoAmarillo + tiempoVerde
        self.timerXpaso = 0

        def step(self): 
            self.tiempoXpaso += 1

            if self.estado == "green" and self.tiempoXpaso >= self.tiempoV:
                self.estado = "yellow"
                self.tiempoXpaso = 0
            elif self.estado == "yellow" and self.tiempoXpaso >= self.tiempoA: 
                self.estado = "red"
                self.tiempoXpaso = 0
            elif self.estado == "red" and self.tiempoXpaso >= self.tiempoR: 
                self.estado = "green"
                self.tiempoXpaso = 0




class Carro(Agent): 
    def __init__ (self, model, origen, destino): 
        super.__init__(model)
        self.orgien = origen
        self.destino = destino
        self.llego = False
        self.pasoActual = 1

        #obtener x y y del diccionario de el modelo
        posInicial = self.model.estacionamientos[self.orgien]
        posFinal = self.model.estacionamiento[self.destino]


        try: 
            self.ruta = nx.shortest_path(self.model.grafo, posInicial, posFinal)
        except: 
            nx.NetworkXNoPath
            print("no hay caminos del estacionamiento de origen a destino")
            self.ruta = [posInicial] 



        def step(self): 

            if self.llego:
              return

            #ver si ya piso el estacionamiento
            if self.pos == self.ruta[-1] or self.pasoActual >= len(self.ruta): 
                self.llego = True
                return

            #checar su sig ruta
            nextPos = self.ruta[self.pasoActual]
            contenido = self.model.grid.get_cell_list_contents([nextPos])


            #revisar si hay un semaforo si hay y esta en verde se detiene 
            for obj in contenido:
             if isinstance (obj, Semaforo):

              if obj.estado != "green": 
                return

            #si hay un carro detenerse para no chocar
            for obj in contenido: 
               if isinstance(obj, Carro) and not obj.llego: 
                 return



            self.model.grid.move_agent(self, nextPos)  
            self.pasoActual +=1








    