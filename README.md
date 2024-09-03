# Gatito

Gatito é um bot para Discord que envia imagens e GIFs de gatos, além de um arquivo de áudio com um som de miau!

![Gatito](gatito.png)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

2. **Instale as dependências:**

   ```bash
   pip install discord.py requests
   ```

3. **Configure o bot:**

   1. **Crie uma aplicação no Discord Developer Portal:**
   
      - Acesse [Discord Developer Portal](https://discord.com/developers/applications).
      - Clique em "New Application" e dê um nome à sua aplicação.
      - No menu à esquerda, selecione "Bot" e clique em "Add Bot". Confirme clicando em "Yes, do it!".

   2. **Obtenha o token do bot:**

      - Na página do bot, copie o token clicando em "Copy" ao lado do campo "TOKEN". 
      - **Importante:** Mantenha este token em segredo.

   3. **Configure o bot:**

      - Substitua `'Seu_token'` no arquivo `bot.py` com o token copiado do Discord Developer Portal.

4. **Execute o bot:**

   ```bash
   python bot.py
   ```

## Dependências

- `discord.py` - Biblioteca para interagir com a API do Discord.
- `requests` - Biblioteca para fazer requisições HTTP.

## Contribuição

Este projeto é apenas para diversão e aprendizado. Sinta-se à vontade para explorar e experimentar com o código!
