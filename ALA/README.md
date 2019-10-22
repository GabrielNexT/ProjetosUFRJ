# Recorrência Linear


#### Gabriel Oliveira de Março - 118147655
Email: gmarco@dcc.ufrj.br


## Escopo

A recursão é uma forma de resolver problemas que visa quebrar o problema em sub problemas menores, muitas pessoas possuem dificuldade em pensar de forma recursiva ou descobrir a recursão que existe em um problema. Existem vagas em abudância na área da ciência da computação, isso ocorre porque as faculdades, em 4 anos, não conseguem qualificar o aluno para o mercado de trabalho. A melhor forma de aproveitar o máximo possível da faculdade e se formar pronto para o mercado de trabalho é praticando a programação regulamente por conta própria. Da mesma forma que você não precisar saber tudo de mecânica para dirigir um carro, você não precisa saber de toda ciência por trás do computador para ser um bom programador. 


O projeto será desenvolvido com fins educacionais para ensinar uma forma mais eficiente de resolver problemas que envolvem recursão, a partir de matriz de transformação e exponenciação rápida de matrizes. Com isso, será possível mostrar aos estudantes uma grande aplicação da matriz de recursão para resolver problemas de programação competitiva.

Será criado um slide, com explicações teórica sobre a recursão linear e um código com a resolução dos problemas citados no slide. O código estará disponível em **Python e C++** e será comentado, para que uma pessoa iniciante na programação consiga entender o seu funcionamento.

O primeiro exemplo a ser utilizado, será o de Fibonacci. Será desenvolvido um algoritmo com complexidade $O(2^n$), $O(n$) e $O(b^3*log(n)$). Além disso, será apresentado o algoritmo de **Tribonacci**, que é uma generalização do algoritmo de Fibonacci. Ele é uma recorrência de terceira ordem e segue os mesmo príncipios que o Fib.

O segundo exemplo é a recursão da torre de Hanói, a fórmula fechada desse algoritmo não é um problema para o computador, visto que ela não trabalha com números complexos. Com isso, será possível observar que em alguns casos, a matriz de recorrência não é possível.

## Benefícios e malefícios

Benefícios da recursão:
1. Problemas difícieis podem ser tornar mais simples.
2. Em alguns casos, a versão recursiva é mais otimizada que a versão iterativa.
3. Um função escrita de forma recursiva, em geral, é menos verbosa do que uma função iterativa.

Malefícios da recursão:
1. Podem produzir códigos mais difícil de entender.
2. Podem causar Stackoverflow após estourar o empilhamento máximo.
3. Em geral, gastam mais memória.

Apesar desses malefícios, a recursão usando algebra linear evita a maior parte deles, visto que o número de chamadar recursivas será nula. Usando transformações lineares, nós podemos reduzir o problema para apenas uma multiplicação de matrizes. Todavia, como foi dito no tópico anterior, nem todos os problemas recursivos podem ser resolvidos usando está técnica.

Além disso, será mostrada a solução de alguns problemas de programação competitiva que usam recorrência linear.
* [SEQ](https://www.spoj.com/problems/SEQ/)
* [Codeforces Educacional Div 2](https://codeforces.com/contest/1117/problem/D)

## Bibliografia e referências
* [Hackerearth - Prinkesh Sharma](https://www.hackerearth.com/pt-br/practice/notes/solving-linear-recurrence-relation/)
* [Medium - Andrew Chamberlain](https://medium.com/@andrew.chamberlain/the-linear-algebra-view-of-the-fibonacci-sequence-4e81f78935a3)
* [Adriano Cattai](http://www.alunospgmat.ufba.br/adrianocattai/construcoes/maple/seq-fibonacci/seq-fibonacci.html)
