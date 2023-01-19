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
        
        
        if action not in state1['pacmanPassagens']:
             return c+1 
        else:
            return c + state2['pacmanPassagens'].count(action)

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

def line(x, y, dx, dy, length):
    """Uma linha de células de comprimento 'length' começando em (x, y) na direcção (dx, dy)."""
    return {(x + i * dx, y + i * dy) for i in range(length)} 
    
def quadro(x, y, length):
    """Uma moldura quadrada de células de comprimento 'length' começando no topo esquerdo (x, y)."""
    return line(x,y,0,1,length) | line(x+length-1,y,0,1,length) | line(x,y,1,0,length) | line(x,y+length-1,1,0,length) 

def exec(p,estado,accoes):
    custo = 0
    for a in accoes:
        seg = p.result(estado,a)
        print(seg)
        custo = p.path_cost(custo,estado,a,seg)
        estado = seg
    p.display(estado)
    print('Custo:',custo)
    print('Goal?',p.goal_test(estado))
    return (estado,custo)



l = line(2,2,1,0,6)
c = line(2,3,0,1,4)
fronteira = quadro(0,0,10) 
g = PacmanPastilhas(pacman=(1,1),goal=15,pastilhas={'N':[(2,1),(3,7)],'D':(4,5),'C':(8,3)},obstacles=fronteira | l | c,dim=10)



e1 = g.initial 

g.display(e1)

#e2 = g.initial

#e2 = (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 1))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 2))

# print(g.__eq__(e2))

# print(e1 == e2)

# print(30*"-")
# print()

#print(e1)
#g.display(e1)

# print("Estado Inicial: ",e1)
# print()
# g.display(estado_inicial)
# print()
# e1_actions = g.actions(e1)
# print("Acoes Possiveis: ", e1_actions)
# print()

# e2 = g.result(e1,e1_actions[0])
# print("Resultado: ", e2)
# print()
# g.display(e2)
# print()

# g.goal_test(e2)

# d1 = (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0))

# d2 = (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0))


#exec(g,e1,[(2,1),(3,1),(4,1),(3,1),(4,1),(3,1)])

def graph_search(problem, frontier):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    If two paths reach a state, only use the first one. [Figure 3.7]"""
    frontier.append(Node(problem.initial))
    explored = set()
    count = 0
    while frontier:
        node = frontier.pop()
        # print()
        # print(node,"no")
        # print()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        #print(node.state)
        #print()
        # print(explored,'explorado')
        # print()
        
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and
                        child not in frontier)
        # print(frontier,'fronteira')
        # print()
        # print(30*'-')
    return None

def depth_first_graph_search(problem):
    """Search the deepest nodes in the search tree first."""
    return graph_search(problem, Stack())

#res=depth_first_graph_search(g)

print()
#resultado = breadth_first_tree_search(g)
resultado = uniform_cost_search(g)
print(resultado)
print(resultado.solution())
g.display(resultado.state)
print()
