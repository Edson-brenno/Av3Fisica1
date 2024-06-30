from utilitarios.vpython_manager import VpythonManager
import vpython as vp

if __name__ == '__main__':
    
    sistema = VpythonManager()

    sistema.adicionar_titulo("Av3 Fisica 1")
    
    sistema.adicionar_titulo("O Problema: ")
    
    sistema.adicionar_texto("""De t = 0 a t = 5,00 min, um homem fica em pé sem se mover; de t
    = 5,00 min a t = 10,0 min, caminha em linha reta com uma
    velocidade de 2,2 m/s.
    """)
    
    sistema.adicionar_titulo("teste")
    # Display text input prompt in the console
    user_input = input("Enter something: ")