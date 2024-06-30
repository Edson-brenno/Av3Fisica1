class MetodosEspeciaisHtml:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def para_bold(text : str) -> str:
        
        return "<b>" + text + "</b>"
    
    @staticmethod
    def para_delta(text: str) -> str:
        
        return f"&Delta;{text}"
    
    @staticmethod
    def hr() -> str:
        
        return f"<hr>"
    
    @staticmethod    
    def para_exponenciacao_esquerda(texto_do_expoente : str, texto: str) -> str:
        
        return f"<sup>{MetodosEspeciaisHtml.para_bold(texto_do_expoente)}</sup>{texto}"
    
    @staticmethod
    def para_exponenciacao_direita(texto_do_expoente : str, texto: str) -> str:
        
        return f"{texto}<sup>{MetodosEspeciaisHtml.para_bold(texto_do_expoente)}</sup>"
    
    @staticmethod    
    def para_exponenciacao_em_baixo_esquerda(texto_do_expoente : str, texto: str) -> str:
        
        return f"<sub>{MetodosEspeciaisHtml.para_bold(texto_do_expoente)}</sub>{texto}"
    
    @staticmethod
    def para_exponenciacao_em_baixo_direita(texto_do_expoente : str, texto: str) -> str:
        
        return f"{texto}<sub>{MetodosEspeciaisHtml.para_bold(texto_do_expoente)}</sub>"