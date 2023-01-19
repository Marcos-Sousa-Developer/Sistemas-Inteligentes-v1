---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Sistemas Inteligentes 2021/2022

## Mini-projeto 1: Pacman comilão

<img src="pacman.png" alt="Drawing" style="width: 100px;"/>


## Grupo: 02

### Elementos do Grupo

Número: 55852       Nome: Marcos Leitão

Número: 56909       Nome: Miguel Fernandes       



## Representação dos estados


Vamos formular um problema de navegação, numa grelha 2D em que algumas posições são obstáculos que impedem o nosso Pacman comlião de avançar.
O **estado vai ser um tuplo de tuplos em que cada tuplo contém a sua identificação e a sua representação**.
Portanto o nosso estado que é tuplo, irá conter um tuplo com identificação 'posicaoPacman' e cordenadas (x,y), em que x corresponde à coluna e y à linha, um tuplo com identificação 'pacmanPassagens' e as passagens do nosso Pacman comilão, um tuplo com identificação 'pastilhasEmCampo' e as pastilhas em campo, um tuplo com identificação 'ponto' e os pontos ja conquistados e por fim um tuplo com identificação 't' e um valor que corresponde ao tempo decorrido até a pastilha ser apanhada.



Assim um estado inicial, por exemplo ficará com a seguinte representação:

* ( ('posicaoPacman',(1,1)), ('pacmanPassagens' ,tuple([(1,1)])), ('pastilhasEmCampo', tuple({})), ('ponto',0), ('t',0) )

em que a posição inicial do Pacman comilão é (1,1), as passagens do pacman apenas contém a posição inicial, pois foi a primeira passagem, as pastilhas em campo neste caso não há, pontos a 0 e t a 0.


## Formulação do problema


**Estados:** ( (Posicao Pacman comilão (x,y)), (Passagens do Pacman comilão), (Pastilhas em Campo), (pontos), (t) )

**Estado Inicial:** ( (Posicao Pacman comilão,(x,y)), (Passagens do Pacman comilão, tuple([(x,y)])) , (Pastilhas em Campo, tuple(O conjunto de pastilhas) ), (pontos,0), (t,0) ) 

**Estado Final:** ( (Posicao Pacman comilão,(x,y)), (Passagens do Pacman comilão, tuple([Passagens])) , (Pastilhas em Campo, tuple(O conjunto de pastilhas em Campo) ), <span style='color:green'> **(pontos,goal)**</span>, (t,t+=1) ) 

**Ações:** (N,O,E,S) de acordo com a possibilidade de navegação

**Sucessor:** Nova localização se possível, adiciona a posicão anterior as passagens do Pacman, retira a pastilha do campo(1), incrementa ponto(2) e incrementa t(3)

    (1) retira a pastilha do campo caso tenha consumido essa mesma pastilha
    (2) incrementa ponto se comer pastilha N, D ou C, em que as pastilhas normais (N) que valem 1 ponto, as pastilhas de         desgaste (D) que valem max(0,5-t) pontos e as pastilhas de crescimento (C) que valem t pontos
    (3) incrementa t apenas se o Pacman estiver numa nova localização

**Custo:** Custos das acções dependem da frequência com que visita as células que delas resultam. Quando visita uma célula pela primeira vez o custo é de 1, mas quando a visita pela n-ésima vez o custo é de n.

**Teste de objetivo:** Ponto >= Goal


         




## Definição da classe PacmanPastilhas
<span style='color:red'> **Importante !!**</span> 

Para criação de um problema **PacmanPastilhas**, o construtor deve receber como parâmetros:  

* A posição do pacman, 
* O número de pontos M a atingir o objetivo do problema), 
* O conjunto de pastilhas, 
* O conjunto de obstáculos,
* A dimensão do mundo.

O problema PacmanPastilhas trata de construir um estado inicial a partir dos parametros introduzidos pelo utilizador e é obrigatório a inserção dos parâmetros. 

```python
from searchPlus import *
   
class PacmanPastilhas(Problem):
    
    def __init__(self,pacman,goal,pastilhas,obstacles,dim): 
        
        lista = list()
        for key,value in pastilhas.items(): 
            
            if type(value) == tuple:
                lista.append((key,value))
            else:
                lista.append((key,tuple(value))) 
        
        passagens = tuple([pacman])
            
        initial = ( ('posicaoPacman',pacman), ('pacmanPassagens', passagens ), ('pastilhasEmCampo', tuple(lista)), ('ponto',0), ('t',0) )
        
        super().__init__(initial,goal)
        
        self.obstacles = obstacles
        self.dim = dim
    
    def actions(self,state):
        
        state = dict(state)
        state = state['posicaoPacman']
        
        canMove = [ ('N',(state[0],state[1]-1)),('W',(state[0]-1,state[1])), ('E',(state[0]+1,state[1])), 
                   ('S',(state[0],state[1]+1))] 
        
        return list(filter(lambda x: x[1] not in self.obstacles, canMove))
    
    def result(self, state, action): 

        action = action[1]
        
        estado = dict(state).copy() 
        
        pacmanPassagens = list(estado['pacmanPassagens'])

        dic = dict()

        estado['t'] += 1
                
        for key, value in dict(estado['pastilhasEmCampo']).items(): 
            flag = False
            if action in value:
                flag = True
                valores = list((value)) 
                valores.remove(action) 

                if len(valores) != 0: 

                    dic[key] = tuple(valores)
                
            elif action == value:
                flag = True 
            
            else:
                dic[key] = value
            
            if flag ==  True:
                
                if key == 'N':
                    estado['ponto'] += 1
                elif key == 'D':
                    estado['ponto'] += max(0,5-estado['t'])
                elif key == 'C':
                    estado['ponto'] += estado['t'] 
        
        estado['posicaoPacman'] = action
        pacmanPassagens +=  [action] 
        
        estado['pastilhasEmCampo'] = tuple(dic.items())
        
        estado['pacmanPassagens'] = tuple(pacmanPassagens)

        return tuple(estado.items())
    
    def goal_test(self, state):
        
        state = dict(state)
            
        return state['ponto'] >= self.goal 
    
    def path_cost(self, c, state1, action, state2):
        
        state1 = dict(state1)
        
        state2 = dict(state2)
        
        if action[1] not in state1['pacmanPassagens']:
             return c+1 
        else:
            return c + state2['pacmanPassagens'].count(action[1])

    def display(self,state): 
        
        state = dict(state)
        
        pastilhasEmCampo = dict(state['pastilhasEmCampo'])
        
        for y in range(self.dim):

            for x in range(self.dim):
                
                dicPastilhas = dict()

                if( (x,y) in self.obstacles):
                    print("=", end=' ')

                elif( (x,y) == state['posicaoPacman']):
                    print("@", end=' ')

                elif( "N" in pastilhasEmCampo and ((x,y) in pastilhasEmCampo['N'] or (x,y) == pastilhasEmCampo['N'])):
                    print("N", end=' ')

                elif( "D" in pastilhasEmCampo and ((x,y) in pastilhasEmCampo['D'] or (x,y) == pastilhasEmCampo['D'])):
                    print("D", end=' ')

                elif( "C" in pastilhasEmCampo and ((x,y) in pastilhasEmCampo['C'] or (x,y) == pastilhasEmCampo['C'])):
                    print("C", end=' ')

                elif( (x,y) not in state['pacmanPassagens']):
                    print(".",end=' ')
                
                else:
                    print("+",end=' ')
                
            print()

```

As funções seguintes permitem ajudar a construir os obstáculos e a fronteira do mundo respetivamente.

```python
def line(x, y, dx, dy, length):
    """Uma linha de células de comprimento 'length' começando em (x, y) na direcção (dx, dy)."""
    return {(x + i * dx, y + i * dy) for i in range(length)} 
    
def quadro(x, y, length):
    """Uma moldura quadrada de células de comprimento 'length' começando no topo esquerdo (x, y)."""
    return line(x,y,0,1,length) | line(x+length-1,y,0,1,length) | line(x,y,1,0,length) | line(x,y+length-1,1,0,length) 

```

## Criação de estados e do problema
Comecemos por criar uma instância da classe do problema e visualizar o estado inicial do problema. <br>
O código a seguir deve permitir construir um problema com um mundo 10x10 com o pacman na posição (1,1), com pastilhas N na posição (2,1),(3,7), pastilha D na posição (4,5), pastilha C na posição (8,3) e o objetivo é ter pelo menos 8 pontos.

```python
l = line(2,2,1,0,6)
c = line(2,3,0,1,4)
fronteira = quadro(0,0,10)

p = PacmanPastilhas(pacman=(1,1),goal=8,pastilhas={'N':[(2,1),(3,7)],'D':(4,5),'C':(8,3)},obstacles=fronteira | l | c,dim=10)

print("O meu estado inicial é:", p.initial)
print()
print("O objetivo é atingir pelo menos:",p.goal,"pontos")
print()
p.display(p.initial)
```

Vamos verificar quais são as acções que podemos aplicar ao estado inicial

```python
print("As ações que podemos aplicar:",p.actions(p.initial))
```

<span style='color:red'> **Note:**</span> que cada ação (x,y), é acompanhada pelo seu ponto cardial de modo a ser mais facil controlar os movimentos do nosso Pacman comilão.


Vamos aplicar uma ação (primeira ação) ao nosso estado e obter um novo estado

```python
e1 = p.result(p.initial,('E', (2, 1)))
print(e1)
```

Repare que o ponto aumentou para 1 e t aumentou para 1, o que indica que o nosso Pacman comeu uma pastilha, consequentemente deixou de ter uma pastilha em campo e também andou uma célula.


Note também que não houve alteração do estado anterior, simplesmente foi gerado um novo estado

```python
print("Estado Inicial:",p.initial)
print()
```

Vamos visualizar o nosso novo estado.

```python
p.display(e1)
```

Repare que a posição do pacman mudou e consequentemente deixou um rasto sobre a ultima posição que passou


Verifiquemos agora quais as ações aplicáveis a esse novo estado

```python
p.actions(e1)
```

Vamos aplicar uma ação (segunda ação) a esse novo estado e obter um novo estado

```python
e2 = p.result(e1,('E', (3, 1)))
print(e2)
```

Vamos visualizar o nosso novo estado.

```python
p.display(e2)
```

Qual foi o custo da ação e1 para e2? 

Vamos testar a função path_cost. 

```python
custo = 0 

print("Comecemos:",p.initial)
print("Com custo =",custo)
print()

acao = p.actions(p.initial)
custo = p.path_cost(custo,p.initial,acao[0],e1)

print("Vamos para:",e1)
print("Com custo =",custo)
print()

acao = p.actions(e1)
custo = p.path_cost(custo,e1,acao[1],e2)

print("Vamos para:",e2)
print("Com custo =",custo)
print()
```

E se houver um caso em que ande para trás ? 

```python
acao = p.actions(e2)
e3 = p.result(e2,acao[0])
custo = p.path_cost(custo,e2,acao[0],e3)

print("Vamos para:",e3)
print("Com custo =",custo)
print()
```

**Porque o custo é 4 e não 3 ?**<br>
Repare que tal como dito na formulação do problema o pacman não gosta de visitar as células muitas vezes e por isso os custos das ações dependem da frequência com que visita as células que delas resultam. 
Quando visita uma célula pela primeira vez o custo é de 1, mas quando a visita pela n-ésima vez o custo é de n.



Vamos aplicar uma sequência de ações a partir de nosso estado inicial. <br>
Para isso vamos usar a função **exc()**, que permite executar uma sequência de ações a partir de um estado qualquer, devolvendo o estado resultante e o custo acumulado num par `(estadoResultante,custoTotal)`.


```python
def exec(p,estado,accoes):
    custo = 0
    for a in accoes:
        seg = p.result(estado,a)
        custo = p.path_cost(custo,estado,a,seg)
        estado = seg
    p.display(estado)
    print('Custo:',custo)
    print('Goal?',p.goal_test(estado))
    return (estado,custo)
```

```python
exect = exec(p,p.initial,[ ('E',(2,1)) , ('E',(3,1)) , ('E',(4,1)) , ('E',(5,1)) , ('E',(6,1)) , ('E',(7,1)) , ('E',(8,1)) , ('S',(8,2)) ,
            ('S',(8,3)), ('W',(7,3))])
print(exect)
```

Embora tenhamos visto um goal teste com a função exec, vamos experimentar fazer um goal teste em caso de False e True

```python
print("Atingimos o objetivo em e3:",p.goal_test(e3))
```

```python
print("Atingimos o objetivo em exec:",p.goal_test(exect[0]))
```

Verifiquemos agora a comparação entre estado. <br>
Como vimos anteriormente o estado e1 surgiu a partir de p.initial e e2 surgiu a partir de e1, portanto é previsivel que e1 > p.initial, e2 > e1.

```python
e0 = p.initial
print("e1 é maior que e0:", e1 > e0)
print("e2 é maior que e1:",e2 > e1)
```

<span style='color:red'> **Note**:</span> Apesar de se criar um estado a partir de outro, não quer dizer que o estado criado tenha de ser obrigatoriamente maior que o estado anterior, por exemplo e2 > e3.

Isto acontece porque se tivermos em casos como um resultado de novo estado em que houve retrocesso, ou seja, voltar para uma célula anterior estamos perante um destes casos, como no caso e3 gerado a apartir de e2.

```python
print("e2 é maior que e3:",e2 > e3)
```

# Teste de procura de solução
Mais abaixo vai haver testes de procura sobre o nosso problema definido anteriormente. <br>
Assim poderemos comparar o tempo de execução dos algoritmos e ver qual dos algoritmos é o mais rápido. <br>
Também iremos responder as perguntas como por exemplo **"Porque é que a nossa procura entra em ciclo?"**.

<span style='color:red'>Note:</span> Se a não houver pastilhas em campo inicialmente ou o tipo de problema não tenha solução, qualquer algoritmo entra em loop infinito.


### Profundidade-Primeiro (árvore)
O algoritmo de profundidade primeiro, **dá preferência aos nós da fronteira que estejam mais afastados da raíz (maior número de acções).** <br>
Se executarmos a procura em profundidade primeiro, podemos **entrar em ciclo, porque este método de procura não faz controlo de ciclos.** <br>
A procura em profundidade quando devolve uma solução não garante que ela seja a de menor custo, não sendo optimal. **Só garante a solução óptima se todas as soluções estiverem à mesma profundidade e os custos são homogéneos.**

Vamos aplicar a procura em Profundidade-Primeiro (árvore) sobre o nosso problema anterior.

```python
dfts = depth_first_tree_search(p) 
p.display(dfts.state)
```

### Porque a profundidade primeiro entra em ciclo?
Para vermos porque é que a procura em profundidade entrou em ciclo, vamos renomear a funcao tree_search() e depth_first_tree_search() para **tree_search_teste()** e **depth_first_tree_search_teste()** respetivamente e de seguida inspecionar o seu funcionamento. <br>
Iremos fazer 20 simulações e ver em que nós a nossa procura passa.

```python
def tree_search_teste(problem, frontier):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Don't worry about repeated paths to a state. [Figure 3.7]"""
    frontier.append(Node(problem.initial))
    count = 1
    while frontier:
        if count == 20:
            break
        node = frontier.pop()
        print(node)
        print()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
        count +=1
    return None

def depth_first_tree_search_teste(problem):
    """Search the deepest nodes in the search tree first."""
    return tree_search_teste(problem, Stack())

dfts = depth_first_tree_search_teste(p) 
```

Como podemos ver, assim que chegamos a posicao (8,8) a nossa procura fica num loop infinito, variado entre os estados de posição (8,8) e de posição (7,8), não saindo daí. <br>
Ao empilharmos os sucessores, as ordens invertem-se dando origem ao ciclo.


### Largura-Primeiro (árvore)
Vamos executar uma procura em largura primeiro que **dá preferência aos nós da fronteira que estão mais à superfície (menor número de acções)** e que nos dará uma solução óptima em termos do número de acções, e não em termos do custo. **Só garante a optimalidade quando os custos são homogéneos**, o que não é o caso. <br>
**A procura em largura, numa árvore, não entra em ciclo** porque primeiro explora todos os estados à distância de uma acção do estado inicial, depois todos os estados à distância de duas acções do estado inicial, etc., ultrapassando assim um ciclo infinito desde que haja uma solução.

Vamos aplicar a procura em Largura-Primeiro (árvore) sobre o nosso problema anterior e posteriormente aplicar o display de modo a visualizarmos o estado inicial e a solução.

```python
bfts = breadth_first_tree_search(p) 
p.display(p.initial)
print()
print("O nó resultante da procura em largura primeiro é:",bfts)
print()
print("As ações aplicadas ao estado foram:",bfts.solution())
print()
p.display(bfts.state)
```

### Profundidade-Primeiro (grafo)
Na procura em profundidade primeiro em grafo, é preciso guardar os estados expandidos num conjunto e também filtrar os estados sucessores, evitando os já expandidos ou aqueles que são terminais dos caminhos na fronteira, ou seja, os não expandidos mas na fronteira). <br>
Tal como acontecia na profundidade primeiro em arvore, e executarmos a procura em profundidade primeiro em grafo, **entraremos em ciclo.**

Vamos aplicar a procura em Profundidade-Primeiro (grafo) sobre o nosso problema anterior.

```python
dfgs = depth_first_graph_search(p) 
p.display(dfgs.state)
```

### Porque a profundidade primeiro em grafo entra em ciclo?
Para vermos porque é que a procura em profundidade primeiro em grafo entrou em ciclo, vamos renomear a funcao graph_search() e depth_first_graph_search() para **graph_search_teste()** e **depth_first_graph_search_teste()** respetivamente e de seguida inspecionar o seu funcionamento. <br>
Fazer 5 simulações e ver a nossa fronteira.

```python
def graph_search_teste(problem, frontier):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    If two paths reach a state, only use the first one. [Figure 3.7]"""
    frontier.append(Node(problem.initial))
    explored = set()
    count = 1
    while frontier:
        if count == 5:
            break
        node = frontier.pop()
        print()
        print(node,"Este é Nó")
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        print()
        print(explored,"Este é explorado")
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and
                        child not in frontier)
        print(frontier,"Esta é a fronteira")
        count +=1
        print()
    return None

def depth_first_graph_search_teste(problem):
    """Search the deepest nodes in the search tree first."""
    return graph_search_teste(problem, Stack())

dfgs = depth_first_graph_search_teste(p)
```

Como podemos ver, o nosso Pacman comilão ja passou pela posição (1,1) com certos atributos num certa altura, mas é possivel ver que ele **acrescenta a fronteira outra vez porque essa mesma posição contém outros atributos completamente diferentes**, logo esses dois nós não são iguais. <br>
É este o indicativo que nos permite ver que a profundidade primeiro em grafo pode entrar num ciclo infinito, algo que normalmente não costuma acontecer. 


### Largura-Primeiro em (grafo)
Na procura em largura primeiro em grafo, tal como na profundidade primeiro em grafo é preciso guardar os estados expandidos num conjunto e também filtrar os estados sucessores, evitando os já expandidos ou aqueles que são terminais dos caminhos na fronteira, ou seja, os não expandidos mas na fronteira).

Vamos aplicar a procura Largura-Primeiro em (grafo) sobre o nosso problema anterior e posteriormente aplicar o display de modo a visualizarmos o estado inicial e a solução..

```python
def breadth_first_graph_search(problem):
    """Search the deepest nodes in the search tree first."""
    return graph_search(problem, FIFOQueue())

bfgs = breadth_first_graph_search(p) 
p.display(p.initial)
print()
print("O nó resultante da procura em Aprofundamento progressivo é:",bfgs)
print()
print("As ações aplicadas ao estado foram:",bfgs.solution())
print()
p.display(bfgs.state)
```

### Aprofundamento Progressivo
Se aplicarmos o aprofundamento progressivo não teremos também a garantia de encontrar a solução óptima porque os custos não são homogéneos. <br>
**Este algoritmo garante a solução mais próxima do estado inicial, em termos de número de acções,** como a procura em largura, mas com um custo menor do que a largura em termos de memória utilizada.
Ele começa por fazer uma procura limitada ao estado inicial e à profundidade 0, depois limitada à profundidade 1, a seguir limitada à profundidade 2, etc. etc., evitando os ciclos até encontrar uma solução que esteja mais próxima da raíz da árvore em termos do número de movimentos ou acções.

Vamos aplicar a procura em Aprofundamento Progressivo sobre o nosso problema anterior e posteriormente aplicar o display de modo a visualizarmos o estado inicial e a solução.

```python
ids = iterative_deepening_search(p) 
p.display(p.initial)
print()
print("O nó resultante da procura em Aprofundamento progressivo é:",ids)
print()
print("As ações aplicadas ao estado foram:",ids.solution())
print()
p.display(ids.state)
```

### Custo Uniforme
Se aplicarmos a procura de custo uniforme **teremos sempre a solução óptima**. 

```python
ucs = uniform_cost_search(p) 
p.display(p.initial)
print()
print("O nó resultante da procura em Aprofundamento progressivo é:",ids)
print()
print("As ações aplicadas ao estado foram:",ucs.solution())
print()
p.display(ucs.state)
```

### Comparação dos resultados ao nível de tempo de execução

Dentro dos algoritmos de procura que vimos anteriormente, vamos comparar aqueles que não entram em loop em termos de tempo, ou seja, vamos descobrir quem é o mais rápido.


#### Tempo de execução do algoritmo Largura-Primeiro (árvore)

```python
import timeit

start = timeit.default_timer()
bfts = breadth_first_tree_search(p) 
final_bfts = timeit.default_timer() - start 

print("O tempo de execução da Largura-Primeiro (árvore):",final_bfts)

```

#### Tempo de execução do algoritmo Largura-Primeiro (grafo)

```python
start = timeit.default_timer()
bfgs = breadth_first_graph_search(p)
final_bfgs = timeit.default_timer() - start 

print("O tempo de execução do Largura-Primeiro (grafo):",final_bfgs) 
```

#### Tempo de execução do algoritmo Aprofundamento-Progressivo (grafo)

```python
start = timeit.default_timer()
ids = iterative_deepening_search(p) 
final_ids = timeit.default_timer() - start 

print("O tempo de execução do Aprofundamento-Progressivo (árvore):",final_ids) 
```

#### Tempo de execução do algoritmo Custo uniforme

```python
start = timeit.default_timer()
ucs = uniform_cost_search(p) 
final_ucs = timeit.default_timer() - start 

print("O tempo de execução do custo uniforme:",final_ucs) 

```

### Quem é o mais eficiente ?
Depois desta análise, conseguimos afirmar que para obter a solução ideal para um determinado problema o uso do algoritmo do custo uniforme é a melhor solução.
A nível do tempo de execução do programa, o custo uniforme também é melhor. 
