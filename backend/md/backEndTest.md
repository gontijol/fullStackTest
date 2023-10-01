### :speaking_head: Instructions

<p align="left"> 
  Choose a quiet and peaceful place to perform the tests. The main objective is that we can understand the level of knowledge of the candidate. Be honest with your answers. There is no pre-established time for completing the tests, <strong>do your best</strong>.<br>
</p>


## <img width="45" alt="about" src="https://raw.github.com/elizarov/elizarov/master/about.png"> Good luck !

<img align="right" width="300" src="https://i2.wp.com/allhtaccess.info/wp-content/uploads/2018/03/programming.gif?fit=1281%2C716&ssl=1" />

```python
## 1) Access Yahoo Finance APIs! load the data into a Mysql database. 
## Use the symbol "PETR4.SA" as a filter and identify the dividends.
## To validate the numbers presented use the link https://www.investidorpetrobras.com.br/acoes-dividendos-e-dividas/dividendos-e-jcp/
  
## 2) To finish. Develop an api whose return is the amount of dividends 
## summarized per year. The API must receive the symbol and the year 
## as filter parameters.
    
```



## Documentação utilizada:

- https://algotrading101.com/learn/yahoo-finance-api-guide/


- Projeto Executado: [![Pratical Test](github.png)](../python/)

### Projeto Desenvolvedor Fullstack - Desafio Ouronova Backend

Este projeto consiste em desenvolver uma aplicação web que acessa as APIs do Yahoo Finance, carrega os dados relacionados ao símbolo "PETR4.SA" em um banco de dados MySQL e, em seguida, desenvolve uma API que retorna o montante de dividendos resumidos por ano, com base nos parâmetros de símbolo e ano.

#### Rotas da API

**`/v1/dividendos-load (HTTP GET)`:** Esta rota é usada para carregar os dados do Yahoo Finance para o símbolo "PETR4.SA" no banco de dados MySQL. Os dados mais recentes, incluindo a data e o montante do dividendo, são retornados em formato JSON.

**`/v1/filtrar-dividendos (HTTP POST)`:** Esta rota é usada para filtrar e resumir o montante de dividendos com base nos parâmetros de símbolo e ano fornecidos. Os parâmetros são enviados no corpo da solicitação JSON. O montante de dividendos resumidos é retornado como resposta JSON.

#### Observações:

Certifique-se de configurar corretamente o banco de dados MySQL para que a aplicação possa armazenar os dados do Yahoo Finance.


