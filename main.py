from utilitarios.vpython_manager import VpythonManager
from utilitarios.conversoes import Conversoes
from utilitarios.metodos_especiais_html import MetodosEspeciaisHtml
import vpython as vp

if __name__ == '__main__':
    
    sistema = VpythonManager()
    
    minutos_inciais = 2
    minutos_inciais_2 = 3
    minuto_inicio_movimento = 5
    minutos_finais = 8
    minutos_finais_2 = 9
    velocidade_movimento = 2.2
    
    sistema.adicionar_titulo("Av3 Fisica 1", caption="<hr>" +
    "<h1> O Problema: </h1> " +
    "<strong> De t = 0 a t = 5,00 min </strong>, um homem fica em pé sem se mover; de <b>t = 5,00 min a t = 10,0 min</b>, caminha em linha reta com uma velocidade de 2,2 m/s." +
    "<br><br> " + "<hr>" + 
    # Resolução opção A
    "<b>(A) Velocidade média(<sup>v</sup>méd) no intervalo de tempo de 2,00 min a 8,00 min?</b>" +
    "<ol>" +
        # Item numero 1 intervalor de tempo
        "<li><b>intervalo de Tempo</b>: 2,00 <b>min</b> e 8,00 <b>min</b>" +
            "<ul>" +
                f"<li><sup>t</sup>inicial = {minutos_inciais} min = {Conversoes.from_minutos_para_segundos(minutos_inciais)} = {Conversoes.from_minutos_para_segundos(minutos_inciais)}s.</li>" +
                f"<li><sup>t</sup>final = 8 min = {Conversoes.from_minutos_para_segundos(minutos_finais)} = {Conversoes.from_minutos_para_segundos(minutos_finais)}s.</li>" +
                f"<li>&Delta;t = <sup>t</sup>final - <sup>t</sup>inicial = "+
                    f"{Conversoes.from_minutos_para_segundos(minutos_finais)} - {Conversoes.from_minutos_para_segundos(minutos_inciais)} = "+ 
                    f"{Conversoes.from_minutos_para_segundos(minutos_finais) - Conversoes.from_minutos_para_segundos(minutos_inciais)}s.</li>" +
            "</ul>" +
        "</li>" +
        # Fim Item numero 1 intervalor de tempo
        
        # Item numero 2 Divisão de intervalo
        "<li><b>Divisão de intervalo</b>:" +
            "<ul>" +
                f"<li> De {minutos_inciais} min ({Conversoes.from_minutos_para_segundos(minutos_inciais)} s) a " +
                    f"{minuto_inicio_movimento} min ({Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)} s): o homem está parado.</li>" +
                
                f"<li> De {minuto_inicio_movimento} min ({Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)} s) a " +
                    f"{minutos_finais} min ({Conversoes.from_minutos_para_segundos(minutos_finais)} s): o homem está se movendo a {velocidade_movimento}m/s.</li>" +
            "</ul>" +
        "</li>" +
        # Fim Item numero 2 Divisão de intervalo
        
        # Item numero 3 Deslocamento total
        "<li><b>Deslocamento total</b>:" +
            "<ul>" +
                f"<li> De {minutos_inciais} min a " +
                    f"{minuto_inicio_movimento} min: {MetodosEspeciaisHtml.para_exponenciacao_em_baixo_direita("1", MetodosEspeciaisHtml.para_delta("X"))} = 0 (o homem está parado.)</li>" +
                
                f"<li> De {minuto_inicio_movimento} min a " +
                    f"{minutos_finais} min: {MetodosEspeciaisHtml.para_exponenciacao_em_baixo_direita("2", MetodosEspeciaisHtml.para_delta("X"))} = v x t = "+
                        f"{velocidade_movimento} m/s x ({Conversoes.from_minutos_para_segundos(minutos_finais)} - {Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)}) = "+ 
                        f"{velocidade_movimento} m/s x ({Conversoes.from_minutos_para_segundos(minutos_finais) - Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)})s = "+
                        f"{velocidade_movimento * (Conversoes.from_minutos_para_segundos(minutos_finais) - Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)):.2f} m"+
            "</ul>" +
        "</li>" +
        # Fim Item numero 3 Deslocamento total
        
        # Item numero 4 Velocidade Média
        f"<li>{MetodosEspeciaisHtml.para_bold("Velocidade Média")} ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "média")}):" +
            "<ul>" +
                f"<li> {MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "média")} = " +
                    f" {MetodosEspeciaisHtml.para_delta("x")} {MetodosEspeciaisHtml.simbolo_divisao()} {MetodosEspeciaisHtml.para_delta("t")} = "+
                    f"{velocidade_movimento * (Conversoes.from_minutos_para_segundos(minutos_finais) - Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)):.2f} m "+ f"{MetodosEspeciaisHtml.simbolo_divisao()} " +
                    f"{MetodosEspeciaisHtml.simbolo_divisao} " + f"{Conversoes.from_minutos_para_segundos(minutos_finais) - Conversoes.from_minutos_para_segundos(minutos_inciais)}s = " +
                    f" {(velocidade_movimento * (Conversoes.from_minutos_para_segundos(minutos_finais) - Conversoes.from_minutos_para_segundos(minuto_inicio_movimento))) / (Conversoes.from_minutos_para_segundos(minutos_finais) - Conversoes.from_minutos_para_segundos(minutos_inciais)) }"+
                    f" m/s"
                "</li>" +
                
                "</ul>" +
        "</li>" +
        # Fim Item numero 4 Velocidade Média
    "</ol>" + 
    # Fim Resolução opção a
    
    # Resolução opção b
    "<b>(B) Aceleração média(<sup>A</sup>méd) no intervalo de tempo de 2,00 min a 8,00 min?</b>" +
    "<ol>" +
        # Item numero 1 velocidade inicial
        f"<li>{MetodosEspeciaisHtml.para_bold("Velocidade Inicial")} ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "inicial")}): " +
                f"0 m/s (parado)"+
        "</li>" +
        # Fim Item numero 1 velocidade inicial
        
        # Item numero 2 velocidade Final
        f"<li>{MetodosEspeciaisHtml.para_bold("Velocidade Final")} ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "final")}): " +
                f" {velocidade_movimento} m/s (após {minuto_inicio_movimento} min)"+
        "</li>" +
        # Fim Item numero 2 velocidade Final
        
        # Item numero 3 Aceleração media
        f"<li>{MetodosEspeciaisHtml.para_bold("Aceleração média")} ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("a", "méd")}): " +
                f"<br>"+
                f"{MetodosEspeciaisHtml.para_exponenciacao_esquerda("a", "méd")} = ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "final")} - "+
                    f"{MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "inicial")}) {MetodosEspeciaisHtml.simbolo_divisao()} " +
                    f"({MetodosEspeciaisHtml.para_exponenciacao_esquerda("t", "final")} - {MetodosEspeciaisHtml.para_exponenciacao_esquerda("t", "incial")})"+
                    f" &asymp; " + f"{(velocidade_movimento - 0) / (Conversoes.from_minutos_para_segundos(minutos_finais) - Conversoes.from_minutos_para_segundos(minutos_inciais)):.4f} m/s²"
                    
        "</li>" +
        # Fim Item numero 3 Aceleração media
        
    "</ol>"
    # Fim Resolução opção b
    
    # Resolução opção C
    "<b>(C) Velocidade média(<sup>v</sup>méd) no intervalo de tempo de 3,00 min a 9,00 min?</b>" +
    "<ol>" +
        # Item numero 1 intervalor de tempo
        "<li><b>intervalo de Tempo</b>: 3,00 <b>min</b> e 9,00 <b>min</b>" +
            "<ul>" +
                f"<li><sup>t</sup>inicial = {minutos_inciais_2} min = {Conversoes.from_minutos_para_segundos(minutos_inciais_2)} = {Conversoes.from_minutos_para_segundos(minutos_inciais_2)}s.</li>" +
                f"<li><sup>t</sup>final = 9 min = {Conversoes.from_minutos_para_segundos(minutos_finais_2)} = {Conversoes.from_minutos_para_segundos(minutos_finais_2)}s.</li>" +
                f"<li>&Delta;t = <sup>t</sup>final - <sup>t</sup>inicial = "+
                    f"{Conversoes.from_minutos_para_segundos(minutos_finais_2)} - {Conversoes.from_minutos_para_segundos(minutos_inciais_2)} = "+ 
                    f"{Conversoes.from_minutos_para_segundos(minutos_finais_2) - Conversoes.from_minutos_para_segundos(minutos_inciais_2)}s.</li>" +
            "</ul>" +
        "</li>" +
        # Fim Item numero 1 intervalor de tempo
        
        # Item numero 2 Divisão de intervalo
        "<li><b>Divisão de intervalo</b>:" +
            "<ul>" +
                f"<li> De {minutos_inciais_2} min ({Conversoes.from_minutos_para_segundos(minutos_inciais_2)} s) a " +
                    f"{minuto_inicio_movimento} min ({Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)} s): o homem está parado.</li>" +
                
                f"<li> De {minuto_inicio_movimento} min ({Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)} s) a " +
                    f"{minutos_finais_2} min ({Conversoes.from_minutos_para_segundos(minutos_finais_2)} s): o homem está se movendo a {velocidade_movimento}m/s.</li>" +
            "</ul>" +
        "</li>" +
        # Fim Item numero 2 Divisão de intervalo
        
        # Item numero 3 Deslocamento total
        "<li><b>Deslocamento total</b>:" +
            "<ul>" +
                f"<li> De {minutos_inciais_2} min a " +
                    f"{minuto_inicio_movimento} min: {MetodosEspeciaisHtml.para_exponenciacao_em_baixo_direita("1", MetodosEspeciaisHtml.para_delta("X"))} = 0 (o homem está parado.)</li>" +
                
                f"<li> De {minuto_inicio_movimento} min a " +
                    f"{minutos_finais_2} min: {MetodosEspeciaisHtml.para_exponenciacao_em_baixo_direita("2", MetodosEspeciaisHtml.para_delta("X"))} = v x t = "+
                        f"{velocidade_movimento} m/s x ({Conversoes.from_minutos_para_segundos(minutos_finais_2)} - {Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)}) = "+ 
                        f"{velocidade_movimento} m/s x ({Conversoes.from_minutos_para_segundos(minutos_finais_2) - Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)})s = "+
                        f"{velocidade_movimento * (Conversoes.from_minutos_para_segundos(minutos_finais_2) - Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)):.2f} m"+
            "</ul>" +
        "</li>" +
        # Fim Item numero 3 Deslocamento total
        
        # Item numero 4 Velocidade Média
        f"<li>{MetodosEspeciaisHtml.para_bold("Velocidade Média")} ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "média")}):" +
            "<ul>" +
                f"<li> {MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "média")} = " +
                    f" {MetodosEspeciaisHtml.para_delta("x")} {MetodosEspeciaisHtml.simbolo_divisao()} {MetodosEspeciaisHtml.para_delta("t")} = "+
                    f"{velocidade_movimento * (Conversoes.from_minutos_para_segundos(minutos_finais_2) - Conversoes.from_minutos_para_segundos(minuto_inicio_movimento)):.2f} m "+ f"{MetodosEspeciaisHtml.simbolo_divisao()} " +
                    f"{MetodosEspeciaisHtml.simbolo_divisao} " + f"{Conversoes.from_minutos_para_segundos(minutos_finais_2) - Conversoes.from_minutos_para_segundos(minutos_inciais_2)}s &asymp; " +
                    f" {(velocidade_movimento * (Conversoes.from_minutos_para_segundos(minutos_finais_2) - Conversoes.from_minutos_para_segundos(minuto_inicio_movimento))) / (Conversoes.from_minutos_para_segundos(minutos_finais) - Conversoes.from_minutos_para_segundos(minutos_inciais)) }"+
                    f" m/s"
                "</li>" +
                
                "</ul>" +
        "</li>" +
        # Fim Item numero 4 Velocidade Média
    "</ol>" + 
    # Fim Resolução opção C
    
    # Resolução opção d
    "<b>(D) Aceleração média(<sup>A</sup>méd) no intervalo de tempo de 3,00 min a 9,00 min?</b>" +
    "<ol>" +
        # Item numero 1 velocidade inicial
        f"<li>{MetodosEspeciaisHtml.para_bold("Velocidade Inicial")} ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "inicial")}): " +
                f"0 m/s (parado)"+
        "</li>" +
        # Fim Item numero 1 velocidade inicial
        
        # Item numero 2 velocidade Final
        f"<li>{MetodosEspeciaisHtml.para_bold("Velocidade Final")} ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "final")}): " +
                f" {velocidade_movimento} m/s (após {minuto_inicio_movimento} min)"+
        "</li>" +
        # Fim Item numero 2 velocidade Final
        
        # Item numero 3 Aceleração media
        f"<li>{MetodosEspeciaisHtml.para_bold("Aceleração média")} ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("a", "méd")}): " +
                f"<br>"+
                f"{MetodosEspeciaisHtml.para_exponenciacao_esquerda("a", "méd")} = ({MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "final")} - "+
                    f"{MetodosEspeciaisHtml.para_exponenciacao_esquerda("v", "inicial")}) {MetodosEspeciaisHtml.simbolo_divisao()} " +
                    f"({MetodosEspeciaisHtml.para_exponenciacao_esquerda("t", "final")} - {MetodosEspeciaisHtml.para_exponenciacao_esquerda("t", "incial")})"+
                    f" &asymp; " + f"{(velocidade_movimento - 0) / (Conversoes.from_minutos_para_segundos(minutos_finais_2) - Conversoes.from_minutos_para_segundos(minutos_inciais_2)):.4f} m/s²"
                    
        "</li>" +
        # Fim Item numero 3 Aceleração media
        
    "</ol>"
    # Fim Resolução opção d
  )
    
    sistema.adicionar_titulo("a")
    # Display text input prompt in the console
    user_input = input("Enter something: ")