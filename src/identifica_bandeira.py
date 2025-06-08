def identificar_bandeira(numero_cartao: str) -> str:
    """
    Identifica a bandeira do cartão de crédito com base no número inicial.
    """
    numero = numero_cartao.replace(" ", "").replace("-", "")

    if numero.startswith("4"):
        return "Visa"
    elif (
        51 <= int(numero[:2]) <= 55
        or 2221 <= int(numero[:4]) <= 2720
    ):
        return "MasterCard"
    elif (
        numero.startswith("4011")
        or numero.startswith("4312")
        or numero.startswith("4389")
        # Adicione outros intervalos conhecidos de Elo aqui, se necessário
    ):
        return "Elo"
    elif numero.startswith("34") or numero.startswith("37"):
        return "American Express"
    elif (
        numero.startswith("6011")
        or numero.startswith("65")
        or 644 <= int(numero[:3]) <= 649
    ):
        return "Discover"
    elif numero.startswith("6062"):
        return "Hipercard"
    
    elif  ((300 <= int(numero[:3]) <= 305)  or numero.startswith("36") or numero.startswith("38")): 
        return "Diners Club"
    elif numero.startswith("2014") or numero.startswith("2149"):
        return "EnRoute"
    elif numero.startswith("2100") or numero.startswith("1800") or numero.startswith("35"):
        return "JCB"
    elif numero.startswith("8699"):
        return "Voyager"
    elif numero.startswith("50"):
        return "Aura"
    else:
        return "Bandeira desconhecida"
# end def identificar_bandeira

def validar_cartao(numero_cartao: str) -> bool:
    """
    Valida o número do cartão de crédito usando o algoritmo de Luhn.
    """
    numero = numero_cartao.replace(" ", "").replace("-", "")
    
    if not numero.isdigit() or len(numero) < 13 or len(numero) > 19:
        return False

    soma = 0
    for i, digito in enumerate(reversed(numero)):
        n = int(digito)
        if i % 2 == 1:  # Dobre os dígitos em posições ímpares
            n *= 2
            if n > 9:
                n -= 9
        soma += n

    return soma % 10 == 0
# end def validar_cartao

def validar_cartao_completo(numero_cartao: str) -> dict:
    """
    Valida o número do cartão de crédito e identifica sua bandeira.
    Retorna um dicionário com o resultado da validação e a bandeira.
    """
    numero = numero_cartao.replace(" ", "").replace("-", "")
    
    if not validar_cartao(numero):
        return {
            "valido": False,
            "bandeira": "Inválido"
        }
    
    bandeira = identificar_bandeira(numero)
    
    return {
        "valido": True,
        "bandeira": bandeira
    }
# end def validar_cartao_completo


if __name__ == "__main__":
    numero_cartao = "5088 3526 0051 2916" 
    resultado = validar_cartao_completo(numero_cartao) 
    print(resultado)

