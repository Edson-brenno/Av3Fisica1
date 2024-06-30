from utilitarios.vpython_manager import VpythonManager
import vpython as vp

if __name__ == '__main__':
    
    sistema = VpythonManager()
    
    sistema.adicionar_titulo("Av3 Fisica 1", caption="<hr>" +
    "<h1> O Problema: </h1> " +
    "<strong> De t = 0 a t = 5,00 min </strong>, um homem fica em pé sem se mover; de <b>t = 5,00 min a t = 10,0 min</b>, caminha em linha reta com uma velocidade de 2,2 m/s." +
    "<br><br> " + "<hr>" + 
    "<b>(A) Velocidade média(<sup>v</sup>méd) no intervalo de tempo de 2,00 min a 8,00 min?</b>" +
    "<ol>" +
        # Item numero 1 intervalor de tempo
        "<li><b>intervalo de Tempo</b>: 2,00 <b>min</b> e 8,00 <b>min</b>" +
            "<ul>" +
                "<li><sup>t</sup>inicial = 2 min = 120 =120 s.</li>" +
            "</ul>" +
        "</li>" +
        # Fim Item numero 1 intervalor de tempo
    "</ol>"
  )
    
    sistema.adicionar_titulo("a")
    # Display text input prompt in the console
    user_input = input("Enter something: ")