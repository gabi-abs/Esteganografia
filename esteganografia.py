from PIL import Image

def gerar_dados(texto):
    """Converte o texto de entrada em uma lista de strings binárias de 8 bits."""
    return [format(ord(caractere), '08b') for caractere in texto]

def modificar_pixels(pixels, dados):
    """Modifica os valores dos pixels para codificar os dados binários."""
    lista_dados = gerar_dados(dados)
    tamanho_dados = len(lista_dados)
    dados_imagem = iter(pixels)
    
    for i in range(tamanho_dados):
        valores = [valor for valor in next(dados_imagem)[:3] + next(dados_imagem)[:3] + next(dados_imagem)[:3]]
        
        # Modifica os valores dos pixels com base nos dados binários
        for j in range(8):
            if lista_dados[i][j] == '0' and valores[j] % 2 != 0:
                valores[j] -= 1
            elif lista_dados[i][j] == '1' and valores[j] % 2 == 0:
                valores[j] = valores[j] - 1 if valores[j] != 0 else valores[j] + 1
        
        # Define o pixel de parada (último pixel ímpar = fim dos dados)
        if i == tamanho_dados - 1:
            valores[-1] |= 1  # Torna ímpar (sinal de parada)
        else:
            valores[-1] &= ~1  # Torna par (continuar)
        
        yield tuple(valores[:3])
        yield tuple(valores[3:6])
        yield tuple(valores[6:9])
        
def codificar_imagem(nova_imagem, dados):
    """Codifica os dados modificados na nova imagem."""
    largura = nova_imagem.size[0]
    (x, y) = (0, 0)
    
    for pixel in modificar_pixels(nova_imagem.getdata(), dados):
        nova_imagem.putpixel((x, y), pixel)
        x = 0 if x == largura - 1 else x + 1
        y += 1 if x == 0 else 0

def codificar():
    """Recebe entrada do usuário e chama as funções de codificação."""
    imagem_nome = input("Digite o nome da imagem (com extensão): ")
    imagem = Image.open(imagem_nome, 'r')
    dados = input("Digite os dados a serem codificados: ")
    
    if not dados:
        raise ValueError("Os dados estão vazios.")
    
    nova_imagem = imagem.copy()
    codificar_imagem(nova_imagem, dados)
    novo_nome_imagem = input("Digite o nome da nova imagem (com extensão): ")
    nova_imagem.save(novo_nome_imagem, novo_nome_imagem.split(".")[-1].upper())

def decodificar():
    """Decodifica o texto oculto de uma imagem."""
    imagem_nome = input("Digite o nome da imagem (com extensão): ")
    imagem = Image.open(imagem_nome, 'r')
    dados_imagem = iter(imagem.getdata())
    mensagem = ""
    
    while True:
        valores = [valor for valor in next(dados_imagem)[:3] + next(dados_imagem)[:3] + next(dados_imagem)[:3]]
        binario = ''.join(['1' if valor % 2 else '0' for valor in valores[:8]])
        mensagem += chr(int(binario, 2))
        
        if valores[-1] % 2 != 0:
            break
    
    return mensagem


