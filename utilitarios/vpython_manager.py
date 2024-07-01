import vpython as vp
import time
from utilitarios.conversoes import Conversoes

class VpythonManager():

    def __init__(self) -> None:

        self.__configuracao_inicial()
        self._posicao_y = 1
        self._posicao_x = 0
        self._posicao_z = 0

    def __configuracao_inicial(self):

        # Set the scene properties
        vp.scene.background = vp.color.white
        vp.scene.center = vp.vector(0, 0, 0)  # Centering the scene to show both objects
        vp.scene.autoscale = True
        vp.scene.width = 700
        vp.scene.title = 'Simulação de Cinemática e Dinâmica de uma Partícula'
    
    def __acrescer_posicao_y(self):

        self._posicao_y -= 4
    
    def adicionar_titulo(self, titulo : str, cor=vp.color.black, caption = "") -> None:

        t = vp.canvas()
        # Set the scene properties
        t.background = vp.color.white
        t.center = vp.vector(0, 0, 0)  # Centering the scene to show both objects
        t.autoscale = True
        t.caption = caption


        novo_titulo = vp.text(text=titulo, align='center', color=cor, pos= vp.vector(0, 0, 0), height=1, canvas=t)
        
        self.__acrescer_posicao_y()
    
    def adicionar_titulo_com_texto(self, titulo : str, cor=vp.color.black, descricao="") -> None:

        t = vp.canvas()
        # Set the scene properties
        t.background = None #vp.color.white
        t.center = vp.vector(0, 0, 0)  # Centering the scene to show both objects
        t.autoscale = True


        novo_titulo = vp.text(text=titulo, align='center', color=cor, pos= vp.vector(0, 0, 0), height=1, canvas=t)
        
        wtext = vp.wtext(text=descricao, background= vp.color.white)
        
        self.__acrescer_posicao_y()

    def adicionar_texto(self, texto : str, cor=vp.color.black):
        
        novaCena = vp.canvas(background= vp.color.white, autoscale = True)
        novaCena.center = vp.vector(0, 0, 0)
        
        wtext = vp.text(text=texto, color=cor, height= 1, align='center', canvas=novaCena, pos= vp.vector(0, 0, 0))
        
    def adicionar_wtexto(self, texto : str, cor=vp.color.black):
        
        novaCena = vp.canvas(background= vp.color.white, autoscale = True)
        novaCena.center = vp.vector(0, 0, 0)
        
        wtext = vp.wtext(text=texto, color=cor, height= 1, align='center', canvas=novaCena, pos= vp.vector(0, 0, 0))
        
    def plotar_grafico(self):
        
        # Dados do problema
        t_standing_start = 0
        t_standing_end = Conversoes.from_minutos_para_segundos(5)  # Convertendo 5 min para segundos
        t_walking_start = t_standing_end
        t_walking_end = Conversoes.from_minutos_para_segundos(10)  # Convertendo 10 min para segundos

        v_caminhada = 2.2  # m/s
        dt = 1  # Intervalo de tempo em segundos para a simulação

        # Inicializando variáveis
        time = 0
        x = 0
        v = 0

        # Listas para armazenar os dados
        time_values = []
        x_values = []
        v_values = []

        # Simulação
        while time <= t_walking_end:
            time_values.append(time)
            x_values.append(x)
            v_values.append(v)
            
            if t_standing_start <= time < t_standing_end:
                # O homem está parado
                v = 0
            elif t_walking_start <= time <= t_walking_end:
                # O homem está caminhando com velocidade constante
                v = v_caminhada
                x += v * dt  # Atualizando a posição

            time += dt

        # Gráficos em VPython
        graph_x = vp.graph(title='Posição (x) em função do Tempo (t)',
                        xtitle='Tempo (s)', ytitle='Posição (m)')
        
        graph_v = vp.graph(title='Velocidade (v) em função do Tempo (t)',
                        xtitle='Tempo (s)', ytitle='Velocidade (m/s)')

        # Curvas
        curve_x = vp.gcurve(graph=graph_x, color=vp.color.blue)
        curve_v = vp.gcurve(graph=graph_v, color=vp.color.red)

        # Plotando os pontos
        for i in range(len(time_values)):
            curve_x.plot(time_values[i], x_values[i])
            curve_v.plot(time_values[i], v_values[i])
        