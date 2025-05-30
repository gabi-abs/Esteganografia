Relatório Técnico – Esteganografia com LSB (Least Significant Bit)

A esteganografia é a arte de esconder informações dentro de outros arquivos, como imagens, áudios ou vídeos, de modo que a existência da informação passe despercebida. Um dos métodos mais utilizados para ocultar dados em imagens é o LSB – Least Significant Bit, ou "bit menos significativo".

O presente relatório descreve o funcionamento dessa técnica e a implementação prática realizada em Python utilizando a biblioteca PIL (Python Imaging Library), com foco na codificação e decodificação de mensagens de texto embutidas em imagens.

Conceito de LSB
Em qualquer valor binário, o último bit é chamado de "menos significativo". Em valores RGB de uma imagem, que vão de 0 a 255, o LSB representa uma mudança mínima no tom da cor, muitas vezes imperceptível visualmente.

Por exemplo, alterar o valor de vermelho de 100 para 101 ou 102 não causa diferença visível ao olho humano. Essa sutileza é explorada para armazenar bits de informação.

Para esconder uma letra (como a letra "A"), ela é primeiro convertida para seu valor binário. Cada caractere ocupa 8 bits. A técnica consiste em alterar o último bit de cada um dos 8 valores RGB utilizados para que eles representem fielmente esses 8 bits.

Funcionamento da Implementação
O processo foi dividido em etapas bem definidas, para garantir clareza e organização na manipulação dos dados.

Etapa 1 – Conversão da Mensagem
A mensagem de texto a ser escondida é convertida para uma lista de sequências binárias. Cada caractere da mensagem é representado por uma string de 8 bits, obtida por meio da função ord() e da formatação binária.

Etapa 2 – Iteração pelos Pixels
A imagem é percorrida pixel a pixel. Para cada caractere (ou sequência de 8 bits), são lidos 3 pixels consecutivos, totalizando 9 valores RGB. O motivo é que 8 valores serão utilizados para armazenar os bits do caractere, e o 9º valor será utilizado como uma marca de controle para indicar se há mais caracteres a serem lidos.

Etapa 3 – Modificação dos Bits
Para cada um dos 8 primeiros valores RGB extraídos, é verificado se o bit da mensagem correspondente é 0 ou 1. Se o bit for 0, o valor RGB é ajustado para ser par (se já for par, permanece). Se o bit for 1, o valor RGB é ajustado para ser ímpar. Esses ajustes são feitos com somas ou subtrações de 1, desde que o novo valor permaneça dentro do intervalo válido (0–255).

Etapa 4 – Controle de Término
O último valor de cada grupo de 9 valores RGB serve como um marcador. Se ainda existem caracteres a serem processados, ele é forçado a ser um número par. Caso seja o último caractere da mensagem, esse valor é tornado ímpar. Com isso, a função de decodificação saberá exatamente onde parar.

Decodificação
O processo de leitura dos dados segue a mesma lógica da codificação, porém no sentido inverso. A imagem é lida em blocos de 3 pixels. Para cada grupo, os 8 primeiros valores RGB são verificados, e seus bits menos significativos (LSBs) são extraídos para formar uma sequência binária. Essa sequência é convertida novamente para um caractere utilizando a função chr(). O processo continua até que o 9º valor de um grupo seja ímpar, o que indica o fim da mensagem.

Considerações Finais
A técnica de LSB é simples, mas bastante eficiente para esconder pequenas quantidades de dados em arquivos de imagem. A vantagem principal está na sutileza das alterações realizadas, que não geram impacto visual perceptível na imagem original.

A implementação descrita neste relatório mostra uma forma prática e funcional de aplicar esse conceito, com uso mínimo de recursos e alta eficiência. Contudo, é importante lembrar que, embora a esteganografia esconda a informação, ela não a protege criptograficamente. Portanto, para maior segurança, recomenda-se utilizar criptografia combinada com esteganografia em aplicações reais.