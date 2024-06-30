import vpython as vp
import time

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
    
    def adicionar_titulo(self, titulo : str, cor=vp.color.black) -> None:

        t = vp.canvas()
        # Set the scene properties
        t.background = vp.color.white
        t.center = vp.vector(0, 0, 0)  # Centering the scene to show both objects
        t.autoscale = True


        novo_titulo = vp.text(text=titulo, align='center', color=cor, pos= vp.vector(0, 0, 0), height=1, canvas=t)
        
        self.__acrescer_posicao_y()

    def adicionar_texto(self, texto : str, cor=vp.color.black):
        
        novaCena = vp.canvas(background= vp.color.white, autoscale = True)
        
        wtext = vp.text(text=texto, color=cor, height= 0.5, canvas=novaCena)