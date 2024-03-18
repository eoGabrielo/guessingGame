# Jogo de Adivinhação

Um simples jogo em Python onde o usuário tenta adivinhar um número sorteado entre 1 e 10.

## Funcionalidades

- Gera um número aleatório entre 1 e 10.
- Solicita ao usuário para adivinhar o número.
- Valida a entrada do usuário para garantir que seja um número inteiro.
- Fornece feedback ao usuário sobre se o palpite está correto.
- Continua pedindo ao usuário para tentar novamente até que o palpite seja correto.

## Instruções de Uso

1. Execute o script Python.
2. Digite um número para adivinhar.
3. O programa fornecerá feedback e pedirá novas tentativas até que o número correto seja adivinhado.

## Explicação do codigo

Este código em Python é um simples jogo de adivinhação, onde o jogador tenta adivinhar um número sorteado aleatoriamente entre 1 e 10.

1. Importar o módulo `random` para gerar números aleatórios:

   ```python
   import random
   ```

2. Gerar um número aleatório entre 1 e 10 e atribuí-lo à variável `numSorteado`:

   ```python
   numSorteado = random.randint(1,10)
   ```

3. Definir duas funções para lidar com a entrada do usuário:

   - A função `contraCaracter()` solicita ao usuário que adivinhe o número e retorna o valor inteiro inserido. Se o usuário digitar algo que não pode ser convertido para um número inteiro, uma exceção `ValueError` é tratada e uma mensagem de aviso é exibida.
   
   - A função `contraCaracterSecond()` é semelhante à primeira, mas é usada para lidar com tentativas subsequentes se o usuário inserir um valor inválido.

4. Solicitar ao usuário que adivinhe o número sorteado chamando a função `contraCaracter()` e atribuir o valor à variável `numeroUsuario`.

   ```python
   numeroUsuario = contraCaracter()
   ```

5. Entrar em um loop `while` que continua executando enquanto o número inserido pelo usuário for diferente do número sorteado.

6. Dentro do loop, verificar se o número inserido pelo usuário está dentro do intervalo válido de 1 a 10. Se estiver, imprimir uma mensagem informando que não é o número sorteado e chamar a função `contraCaracterSecond()` para permitir que o usuário tente novamente. Se o número inserido for maior que 10, informar que o número é inválido e chamar `contraCaracterSecond()` novamente.

   ```python
   while numeroUsuario != numSorteado:
       if numeroUsuario <= 10:
           print(f"Não é o número {numeroUsuario}!")
           numeroUsuario = contraCaracterSecond()
       elif numeroUsuario > 10:
           print(f"O número {numeroUsuario} é maior que 10. Escolha um número entre 1 e 10!")
           numeroUsuario = contraCaracterSecond()
   ```

7. Quando o número correto for adivinhado, imprimir uma mensagem de parabéns e informar qual era o número sorteado.

   ```python
   print(f"ACERTOU!!!, O número {numSorteado} era o sorteado. PARABÉNS!!")
   ```

Esse é o funcionamento básico do jogo de adivinhação implementado neste código Python. Ele continua solicitando que o usuário adivinhe o número sorteado até que o número correto seja adivinhado. Se o usuário inserir um valor inválido, será solicitado que insira um novo valor.
