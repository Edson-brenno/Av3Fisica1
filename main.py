from utilitarios.vpython_manager import VpythonManager
import vpython as vp

if __name__ == '__main__':
    
    sistema = VpythonManager()
    
    sistema.adicionar_titulo("Av3 Fisica 1", caption="""<hr>
<h1> O Problema: </h1> 
    <strong> De t = 0 a t = 5,00 min </strong>, um homem fica em pé sem se mover; de <b>t = 5,00 min a t = 10,0 min</b>, caminha em linha reta com uma velocidade de 2,2 m/s.
    
    <b>Qual é (a) a velocidade média vméd e (b) qual a aceleração média améd do homem no intervalo de tempo de 2,00 min a 8,00 min?</b>
    """)
    
    sistema.adicionar_titulo("a")
    # Display text input prompt in the console
    user_input = input("Enter something: ")