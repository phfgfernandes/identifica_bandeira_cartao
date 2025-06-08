# Identificação e Validação de Cartões de Crédito

Este projeto é uma aplicação em Python que realiza a identificação da bandeira e validação de números de cartões de crédito utilizando o algoritmo de Luhn.

## Estrutura do Projeto

```
images/
    base.png
src/
    identifica_bandeira.py
```

## Funcionalidades

### Identificação de Bandeira

A função [`identificar_bandeira`](src/identifica_bandeira.py) identifica a bandeira do cartão de crédito com base no número inicial do cartão. As bandeiras suportadas incluem:

- Visa
- MasterCard
- Elo
- American Express
- Discover
- Hipercard
- Diners Club
- EnRoute
- JCB
- Voyager
- Aura

### Validação de Cartão

A função [`validar_cartao`](src/identifica_bandeira.py) valida o número do cartão de crédito utilizando o algoritmo de Luhn, garantindo que o número seja válido.

### Validação Completa

A função [`validar_cartao_completo`](src/identifica_bandeira.py) combina a validação do número do cartão com a identificação da bandeira, retornando um dicionário com os seguintes campos:

- `valido`: Indica se o número do cartão é válido.
- `bandeira`: Identifica a bandeira do cartão ou informa que é inválido.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório `src` no terminal.
3. Execute o arquivo `identifica_bandeira.py`:
   ```bash
   python identifica_bandeira.py
   ```
4. O resultado será exibido no terminal, mostrando se o cartão é válido e sua bandeira.

## Exemplo de Uso

Entrada:

```python
numero_cartao = "5088 3526 0051 2916"
```

Saída:

```json
{
  "valido": true,
  "bandeira": "Aura"
}
```

## Dependências

Este projeto não possui dependências externas e utiliza apenas bibliotecas padrão do Python.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou adicionar suporte a novas bandeiras de cartões. Para isso:

1. Faça um fork deste repositório.
2. Crie uma branch para suas alterações.
3. Envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: `phfg@yahoo.com`.
