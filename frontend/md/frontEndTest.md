### :speaking_head: Instructions

<p align="left">
  Choose a quiet and peaceful place to perform the tests. The main objective is that we can understand the level of knowledge of the candidate. Be honest with your answers. There is no pre-established time for completing the tests, <strong>do your best</strong>.<br>
</p>

## <img width="45" alt="about" src="https://raw.github.com/elizarov/elizarov/master/about.png"> Good luck

<img align="right" width="300" src="https://i2.wp.com/allhtaccess.info/wp-content/uploads/2018/03/programming.gif?fit=1281%2C716&ssl=1" />

```python
## Using the Referencia 2 mockup, develop a functional interface
## for uploading a file. Check the extension we will only 
## accept specific formats. The design necessarily needs 
## to be responsive.

## Instructions: thinking about a better user experience when uploading, 
## create a progress bar.   
```

### :speaking_head: Reference 1
  
![up_load_file](https://user-images.githubusercontent.com/93677386/220721238-e4b9f1e6-ed3e-457b-90e8-4f4b0ceb308b.png)

  ```python
## A company in the retail segment needs to improve its search bar as many 
## customers are unable to find products. Implement a search bar focused on 
## the consumer's experience, which should bring the images of the 
## products for auto-completion.
```
  
### :speaking_head: Reference 2
  
![search_bar](https://user-images.githubusercontent.com/93677386/220727451-cdcaf85d-9f1c-417f-82da-70962e12d52c.png)

# Documentação do Desafio Frontend

- Projeto Executado: [![Pratical Test](github.png)](../frontend/)

## Arquitetura

- Este projeto utiliza o Vite como ferramenta de construção para criar projetos Vue.js.
- A linguagem de programação principal é o JavaScript.

## Componentes

O projeto possui dois componentes principais:

1. **FileUpload**
   - Este componente permite aos usuários fazer o upload de arquivos ou arrastar e soltar arquivos para carregá-los.
   - Ele também oferece a opção de carregar dados de uma URL da web ou selecionar um conjunto de dados de amostra.
   - O componente é responsável por exibir a barra de progresso durante o carregamento de um arquivo.

2. **SearchBar**
   - Este componente implementa um campo de pesquisa com funcionalidade de autocompletar usando o componente EjsAutocomplete da biblioteca Syncfusion.

## Rotas

- O projeto possui rotas para diferentes referências ou páginas, implementadas usando o Vue Router.
- As rotas são as seguintes:
   1. Rota raiz ("/"): A página inicial exibe um menu onde você pode selecionar qual dos desafios deseja acessar.
   2. Rota "/reference1": Direciona para o componente "FileUpload".
   3. Rota "/reference2": Direciona para o componente "SearchBar".

## Executando o Projeto

Para rodar o projeto, siga estas etapas:

1. Certifique-se de ter o Node.js instalado em seu sistema.
2. Abra o terminal na raiz do projeto.
3. Execute o seguinte comando para instalar as dependências:

#### npm install

4. Execute o seguinte comando para iniciar o servidor de desenvolvimento:

```bash
npm run dev

```
