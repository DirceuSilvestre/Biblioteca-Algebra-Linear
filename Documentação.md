<h1 align="center"  size="40px">
Documentação
</h1>

# Paradigma

O paradigma utilizado para o arquivo que trata dos vetores foi POO (programação orientada a objeto).
A classe Vetor, que leva o mesmo nome do arquivo, tem seus metodos que fazem os calculos de vetor.
Foi programado desta forma para a pratica do paradigma e de args* e kargs*, podendo alguns métodos receber diversos vetores como parâmetro e calcular em uma chamada todos eles.

Para o arquivo que trata das matrizes foi utilizado o paradigma estruturado. Todos os dois arquivos tinham sido iniciados neste paradigma, porém pelo motivo acima uma parte foi refatorada em POO.

Antes havia um arquivo só com todas as funções em paradigma estruturado. Porém ao cursar a matéria de Estrutura de Dados aprendi que a modularização é o melhor a se fazer durante a programação de qualquer projeto.

# Vetor

A seguir serão tratados as funções do arquivo responsavel pelos calculos de vetores, suas funções, parâmetros, o que retornam.

## Criar Vetor

### criar_vetor_nulo(dimensão=2)

cria e retorna um vetor nulo, somente com o numero 0, da dimensão passada por parâmetro.
caso não indique a dimensão desejada, retornará um vetor de dimensão 2, aquele com x e y.

### criar_vetor_unitario(dimensao=2):

cria e retorna um vetor unitário, somente com o numero 1, da dimensão passada por parâmetro.
caso não indique a dimensão desejada, retornará um vetor de dimensão 2, aquele com x e y.

### criar_vetor_aleatorio(dimensao=2)

cria e retorna um vetor com numeros sorteados entre 0 e 9 por um algoritmo pseudo-aleatório da biblioteca random, da dimensão passada por parâmetro.
caso não indique a dimensão desejada, retornará um vetor de dimensão 2, aquele com x e y.

### criar_vetor_oposto(vetor)

cria e retorna um vetor com sinal oposto ao que foi passado no parâmetro e de mesma dimensão.
todo elemento positivo se torna negativo, e todo negativo fica positivo.
caso não passe um vetor como parâmetro retornará um erro.

### imprimir_vetor(plural=False, \*args):

imprime de forma bonita, da mesma que escrevemos no caderno, um vetor, dentro do parenteses e com suas vírgulas separando os elementos.
pode passar um ou mais vetores como parâmetro, caso passe mais de um vetor, colocar True no parâmetro plurar.

### igualdade_de_vetores(\*args):

verifica se todos os vetores passados para a função são igualdade.
como na algebra linear ele compara cada elemento do vetor na determinada posição com o elemento da exata posição em outro vetor.
havendo igualdade retorna uma mensagem dizendo que é igual, ou retorna uma mensagem dizendo que não é igual.
e se todos os vetores passados para a função não forem da mesma dimensão retorna uma mensagem dizendo que não são iguais exatamente por esse motivo.

### subtracao_de_vetor(\*args):

retorna um vetor da mesma dimensão dos vetores passados por parametro, que é a subtração de todos os vetores que foram passados.
podendo passar uma lista com todos os vetores dentro.
caso os vetores passados sejam de tamanhos diferentes o código retornará uma mensagem de erro, dizendo não ser possível subtrair vetores de diferentes dimensões.
