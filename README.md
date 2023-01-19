
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light"><div id="MathJax_Message" style="display: none;"></div>

<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h1 id="Sistemas-Inteligentes-2021/2022">Sistemas Inteligentes 2021/2022<a class="anchor-link" href="#Sistemas-Inteligentes-2021/2022">¶</a></h1><h2 id="Mini-projeto-1:-Pacman-comil%C3%A3o">Mini-projeto 1: Pacman comilão<a class="anchor-link" href="#Mini-projeto-1:-Pacman-comil%C3%A3o">¶</a></h2><p><img src="pacman.png" alt="Drawing" style="width: 100px;"></p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Grupo:-02">Grupo: 02<a class="anchor-link" href="#Grupo:-02">¶</a></h2><h3 id="Elementos-do-Grupo">Elementos do Grupo<a class="anchor-link" href="#Elementos-do-Grupo">¶</a></h3><p>Número: 55852       Nome: Marcos Leitão</p>
<p>Número: 56909       Nome: Miguel Fernandes</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Representa%C3%A7%C3%A3o-dos-estados">Representação dos estados<a class="anchor-link" href="#Representa%C3%A7%C3%A3o-dos-estados">¶</a></h2>
</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Vamos formular um problema de navegação, numa grelha 2D em que algumas posições são obstáculos que impedem o nosso Pacman comlião de avançar.
O <strong>estado vai ser um tuplo de tuplos em que cada tuplo contém a sua identificação e a sua representação</strong>.
Portanto o nosso estado que é tuplo, irá conter um tuplo com identificação 'posicaoPacman' e cordenadas (x,y), em que x corresponde à coluna e y à linha, um tuplo com identificação 'pacmanPassagens' e as passagens do nosso Pacman comilão, um tuplo com identificação 'pastilhasEmCampo' e as pastilhas em campo, um tuplo com identificação 'ponto' e os pontos ja conquistados e por fim um tuplo com identificação 't' e um valor que corresponde ao tempo decorrido até a pastilha ser apanhada.</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Assim um estado inicial, por exemplo ficará com a seguinte representação:</p>
<ul>
<li>( ('posicaoPacman',(1,1)), ('pacmanPassagens' ,tuple([(1,1)])), ('pastilhasEmCampo', tuple({})), ('ponto',0), ('t',0) )</li>
</ul>
<p>em que a posição inicial do Pacman comilão é (1,1), as passagens do pacman apenas contém a posição inicial, pois foi a primeira passagem, as pastilhas em campo neste caso não há, pontos a 0 e t a 0.</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Formula%C3%A7%C3%A3o-do-problema">Formulação do problema<a class="anchor-link" href="#Formula%C3%A7%C3%A3o-do-problema">¶</a></h2>
</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Estados:</strong> ( (Posicao Pacman comilão (x,y)), (Passagens do Pacman comilão), (Pastilhas em Campo), (pontos), (t) )</p>
<p><strong>Estado Inicial:</strong> ( (Posicao Pacman comilão,(x,y)), (Passagens do Pacman comilão, tuple([(x,y)])) , (Pastilhas em Campo, tuple(O conjunto de pastilhas) ), (pontos,0), (t,0) )</p>
<p><strong>Estado Final:</strong> ( (Posicao Pacman comilão,(x,y)), (Passagens do Pacman comilão, tuple([Passagens])) , (Pastilhas em Campo, tuple(O conjunto de pastilhas em Campo) ), <span style="color:green"> **(pontos,goal)**</span>, (t,t+=1) )</p>
<p><strong>Ações:</strong> (N,O,E,S) de acordo com a possibilidade de navegação</p>
<p><strong>Sucessor:</strong> Nova localização se possível, adiciona a posicão anterior as passagens do Pacman, retira a pastilha do campo(1), incrementa ponto(2) e incrementa t(3)</p>

<pre><code>(1) retira a pastilha do campo caso tenha consumido essa mesma pastilha
(2) incrementa ponto se comer pastilha N, D ou C, em que as pastilhas normais (N) que valem 1 ponto, as pastilhas de         desgaste (D) que valem max(0,5-t) pontos e as pastilhas de crescimento (C) que valem t pontos
(3) incrementa t apenas se o Pacman estiver numa nova localização

</code></pre>
<p><strong>Custo:</strong> Custos das acções dependem da frequência com que visita as células que delas resultam. Quando visita uma célula pela primeira vez o custo é de 1, mas quando a visita pela n-ésima vez o custo é de n.</p>
<p><strong>Teste de objetivo:</strong> Ponto &gt;= Goal</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Defini%C3%A7%C3%A3o-da-classe-PacmanPastilhas">Definição da classe PacmanPastilhas<a class="anchor-link" href="#Defini%C3%A7%C3%A3o-da-classe-PacmanPastilhas">¶</a></h2><p><span style="color:red"> **Importante !!**</span></p>
<p>Para criação de um problema <strong>PacmanPastilhas</strong>, o construtor deve receber como parâmetros:</p>
<ul>
<li>A posição do pacman, </li>
<li>O número de pontos M a atingir o objetivo do problema), </li>
<li>O conjunto de pastilhas, </li>
<li>O conjunto de obstáculos,</li>
<li>A dimensão do mundo.</li>
</ul>
<p>O problema PacmanPastilhas trata de construir um estado inicial a partir dos parametros introduzidos pelo utilizador e é obrigatório a inserção dos parâmetros.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[5]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">searchPlus</span> <span class="kn">import</span> <span class="o">*</span>
   
<span class="k">class</span> <span class="nc">PacmanPastilhas</span><span class="p">(</span><span class="n">Problem</span><span class="p">):</span>
    
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">pacman</span><span class="p">,</span><span class="n">goal</span><span class="p">,</span><span class="n">pastilhas</span><span class="p">,</span><span class="n">obstacles</span><span class="p">,</span><span class="n">dim</span><span class="p">):</span> 
        
        <span class="n">lista</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span><span class="n">value</span> <span class="ow">in</span> <span class="n">pastilhas</span><span class="o">.</span><span class="n">items</span><span class="p">():</span> 
            
            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">)</span> <span class="o">==</span> <span class="nb">tuple</span><span class="p">:</span>
                <span class="n">lista</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">key</span><span class="p">,</span><span class="n">value</span><span class="p">))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">lista</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">key</span><span class="p">,</span><span class="nb">tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)))</span> 
        
        <span class="n">passagens</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">([</span><span class="n">pacman</span><span class="p">])</span>
            
        <span class="n">initial</span> <span class="o">=</span> <span class="p">(</span> <span class="p">(</span><span class="s1">'posicaoPacman'</span><span class="p">,</span><span class="n">pacman</span><span class="p">),</span> <span class="p">(</span><span class="s1">'pacmanPassagens'</span><span class="p">,</span> <span class="n">passagens</span> <span class="p">),</span> <span class="p">(</span><span class="s1">'pastilhasEmCampo'</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">lista</span><span class="p">)),</span> <span class="p">(</span><span class="s1">'ponto'</span><span class="p">,</span><span class="mi">0</span><span class="p">),</span> <span class="p">(</span><span class="s1">'t'</span><span class="p">,</span><span class="mi">0</span><span class="p">)</span> <span class="p">)</span>
        
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">initial</span><span class="p">,</span><span class="n">goal</span><span class="p">)</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">obstacles</span> <span class="o">=</span> <span class="n">obstacles</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">dim</span> <span class="o">=</span> <span class="n">dim</span>
    
    <span class="k">def</span> <span class="nf">actions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">state</span><span class="p">):</span>
        
        <span class="n">state</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
        <span class="n">state</span> <span class="o">=</span> <span class="n">state</span><span class="p">[</span><span class="s1">'posicaoPacman'</span><span class="p">]</span>
        
        <span class="n">canMove</span> <span class="o">=</span> <span class="p">[</span> <span class="p">(</span><span class="s1">'N'</span><span class="p">,(</span><span class="n">state</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">state</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">-</span><span class="mi">1</span><span class="p">)),(</span><span class="s1">'W'</span><span class="p">,(</span><span class="n">state</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="n">state</span><span class="p">[</span><span class="mi">1</span><span class="p">])),</span> <span class="p">(</span><span class="s1">'E'</span><span class="p">,(</span><span class="n">state</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span><span class="n">state</span><span class="p">[</span><span class="mi">1</span><span class="p">])),</span> 
                   <span class="p">(</span><span class="s1">'S'</span><span class="p">,(</span><span class="n">state</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">state</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">+</span><span class="mi">1</span><span class="p">))]</span> 
        
        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="nb">filter</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">obstacles</span><span class="p">,</span> <span class="n">canMove</span><span class="p">))</span>
    
    <span class="k">def</span> <span class="nf">result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span> 

        <span class="n">action</span> <span class="o">=</span> <span class="n">action</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
        
        <span class="n">estado</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">state</span><span class="p">)</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> 
        
        <span class="n">pacmanPassagens</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">estado</span><span class="p">[</span><span class="s1">'pacmanPassagens'</span><span class="p">])</span>

        <span class="n">dic</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>

        <span class="n">estado</span><span class="p">[</span><span class="s1">'t'</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
                
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nb">dict</span><span class="p">(</span><span class="n">estado</span><span class="p">[</span><span class="s1">'pastilhasEmCampo'</span><span class="p">])</span><span class="o">.</span><span class="n">items</span><span class="p">():</span> 
            <span class="n">flag</span> <span class="o">=</span> <span class="kc">False</span>
            <span class="k">if</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">value</span><span class="p">:</span>
                <span class="n">flag</span> <span class="o">=</span> <span class="kc">True</span>
                <span class="n">valores</span> <span class="o">=</span> <span class="nb">list</span><span class="p">((</span><span class="n">value</span><span class="p">))</span> 
                <span class="n">valores</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">action</span><span class="p">)</span> 

                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">valores</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span> 

                    <span class="n">dic</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">valores</span><span class="p">)</span>
                
            <span class="k">elif</span> <span class="n">action</span> <span class="o">==</span> <span class="n">value</span><span class="p">:</span>
                <span class="n">flag</span> <span class="o">=</span> <span class="kc">True</span> 
            
            <span class="k">else</span><span class="p">:</span>
                <span class="n">dic</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
            
            <span class="k">if</span> <span class="n">flag</span> <span class="o">==</span>  <span class="kc">True</span><span class="p">:</span>
                
                <span class="k">if</span> <span class="n">key</span> <span class="o">==</span> <span class="s1">'N'</span><span class="p">:</span>
                    <span class="n">estado</span><span class="p">[</span><span class="s1">'ponto'</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="k">elif</span> <span class="n">key</span> <span class="o">==</span> <span class="s1">'D'</span><span class="p">:</span>
                    <span class="n">estado</span><span class="p">[</span><span class="s1">'ponto'</span><span class="p">]</span> <span class="o">+=</span> <span class="nb">max</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">5</span><span class="o">-</span><span class="n">estado</span><span class="p">[</span><span class="s1">'t'</span><span class="p">])</span>
                <span class="k">elif</span> <span class="n">key</span> <span class="o">==</span> <span class="s1">'C'</span><span class="p">:</span>
                    <span class="n">estado</span><span class="p">[</span><span class="s1">'ponto'</span><span class="p">]</span> <span class="o">+=</span> <span class="n">estado</span><span class="p">[</span><span class="s1">'t'</span><span class="p">]</span> 
        
        <span class="n">estado</span><span class="p">[</span><span class="s1">'posicaoPacman'</span><span class="p">]</span> <span class="o">=</span> <span class="n">action</span>
        <span class="n">pacmanPassagens</span> <span class="o">+=</span>  <span class="p">[</span><span class="n">action</span><span class="p">]</span> 
        
        <span class="n">estado</span><span class="p">[</span><span class="s1">'pastilhasEmCampo'</span><span class="p">]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">dic</span><span class="o">.</span><span class="n">items</span><span class="p">())</span>
        
        <span class="n">estado</span><span class="p">[</span><span class="s1">'pacmanPassagens'</span><span class="p">]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">pacmanPassagens</span><span class="p">)</span>

        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">estado</span><span class="o">.</span><span class="n">items</span><span class="p">())</span>
    
    <span class="k">def</span> <span class="nf">goal_test</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        
        <span class="n">state</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
            
        <span class="k">return</span> <span class="n">state</span><span class="p">[</span><span class="s1">'ponto'</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">goal</span> 
    
    <span class="k">def</span> <span class="nf">path_cost</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">c</span><span class="p">,</span> <span class="n">state1</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">state2</span><span class="p">):</span>
        
        <span class="n">state1</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">state1</span><span class="p">)</span>
        
        <span class="n">state2</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">state2</span><span class="p">)</span>
        
        <span class="k">if</span> <span class="n">action</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">state1</span><span class="p">[</span><span class="s1">'pacmanPassagens'</span><span class="p">]:</span>
             <span class="k">return</span> <span class="n">c</span><span class="o">+</span><span class="mi">1</span> 
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">c</span> <span class="o">+</span> <span class="n">state2</span><span class="p">[</span><span class="s1">'pacmanPassagens'</span><span class="p">]</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">action</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">display</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">state</span><span class="p">):</span> 
        
        <span class="n">state</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
        
        <span class="n">pastilhasEmCampo</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">state</span><span class="p">[</span><span class="s1">'pastilhasEmCampo'</span><span class="p">])</span>
        
        <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">):</span>

            <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">):</span>
                
                <span class="n">dicPastilhas</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>

                <span class="k">if</span><span class="p">(</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">obstacles</span><span class="p">):</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"="</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">' '</span><span class="p">)</span>

                <span class="k">elif</span><span class="p">(</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="o">==</span> <span class="n">state</span><span class="p">[</span><span class="s1">'posicaoPacman'</span><span class="p">]):</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"@"</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">' '</span><span class="p">)</span>

                <span class="k">elif</span><span class="p">(</span> <span class="s2">"N"</span> <span class="ow">in</span> <span class="n">pastilhasEmCampo</span> <span class="ow">and</span> <span class="p">((</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="ow">in</span> <span class="n">pastilhasEmCampo</span><span class="p">[</span><span class="s1">'N'</span><span class="p">]</span> <span class="ow">or</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="o">==</span> <span class="n">pastilhasEmCampo</span><span class="p">[</span><span class="s1">'N'</span><span class="p">])):</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"N"</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">' '</span><span class="p">)</span>

                <span class="k">elif</span><span class="p">(</span> <span class="s2">"D"</span> <span class="ow">in</span> <span class="n">pastilhasEmCampo</span> <span class="ow">and</span> <span class="p">((</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="ow">in</span> <span class="n">pastilhasEmCampo</span><span class="p">[</span><span class="s1">'D'</span><span class="p">]</span> <span class="ow">or</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="o">==</span> <span class="n">pastilhasEmCampo</span><span class="p">[</span><span class="s1">'D'</span><span class="p">])):</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"D"</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">' '</span><span class="p">)</span>

                <span class="k">elif</span><span class="p">(</span> <span class="s2">"C"</span> <span class="ow">in</span> <span class="n">pastilhasEmCampo</span> <span class="ow">and</span> <span class="p">((</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="ow">in</span> <span class="n">pastilhasEmCampo</span><span class="p">[</span><span class="s1">'C'</span><span class="p">]</span> <span class="ow">or</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="o">==</span> <span class="n">pastilhasEmCampo</span><span class="p">[</span><span class="s1">'C'</span><span class="p">])):</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"C"</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">' '</span><span class="p">)</span>

                <span class="k">elif</span><span class="p">(</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">state</span><span class="p">[</span><span class="s1">'pacmanPassagens'</span><span class="p">]):</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"."</span><span class="p">,</span><span class="n">end</span><span class="o">=</span><span class="s1">' '</span><span class="p">)</span>
                
                <span class="k">else</span><span class="p">:</span>
                    <span class="nb">print</span><span class="p">(</span><span class="s2">"+"</span><span class="p">,</span><span class="n">end</span><span class="o">=</span><span class="s1">' '</span><span class="p">)</span>
                
            <span class="nb">print</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>As funções seguintes permitem ajudar a construir os obstáculos e a fronteira do mundo respetivamente.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[6]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">line</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span><span class="p">,</span> <span class="n">length</span><span class="p">):</span>
    <span class="sd">"""Uma linha de células de comprimento 'length' começando em (x, y) na direcção (dx, dy)."""</span>
    <span class="k">return</span> <span class="p">{(</span><span class="n">x</span> <span class="o">+</span> <span class="n">i</span> <span class="o">*</span> <span class="n">dx</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">i</span> <span class="o">*</span> <span class="n">dy</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">length</span><span class="p">)}</span> 
    
<span class="k">def</span> <span class="nf">quadro</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">length</span><span class="p">):</span>
    <span class="sd">"""Uma moldura quadrada de células de comprimento 'length' começando no topo esquerdo (x, y)."""</span>
    <span class="k">return</span> <span class="n">line</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="n">length</span><span class="p">)</span> <span class="o">|</span> <span class="n">line</span><span class="p">(</span><span class="n">x</span><span class="o">+</span><span class="n">length</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="n">y</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="n">length</span><span class="p">)</span> <span class="o">|</span> <span class="n">line</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="n">length</span><span class="p">)</span> <span class="o">|</span> <span class="n">line</span><span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="o">+</span><span class="n">length</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="n">length</span><span class="p">)</span> 
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Cria%C3%A7%C3%A3o-de-estados-e-do-problema">Criação de estados e do problema<a class="anchor-link" href="#Cria%C3%A7%C3%A3o-de-estados-e-do-problema">¶</a></h2><p>Comecemos por criar uma instância da classe do problema e visualizar o estado inicial do problema. <br>
O código a seguir deve permitir construir um problema com um mundo 10x10 com o pacman na posição (1,1), com pastilhas N na posição (2,1),(3,7), pastilha D na posição (4,5), pastilha C na posição (8,3) e o objetivo é ter pelo menos 8 pontos.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[7]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">l</span> <span class="o">=</span> <span class="n">line</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">6</span><span class="p">)</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">line</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">4</span><span class="p">)</span>
<span class="n">fronteira</span> <span class="o">=</span> <span class="n">quadro</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">10</span><span class="p">)</span>

<span class="n">p</span> <span class="o">=</span> <span class="n">PacmanPastilhas</span><span class="p">(</span><span class="n">pacman</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span><span class="n">goal</span><span class="o">=</span><span class="mi">8</span><span class="p">,</span><span class="n">pastilhas</span><span class="o">=</span><span class="p">{</span><span class="s1">'N'</span><span class="p">:[(</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">),(</span><span class="mi">3</span><span class="p">,</span><span class="mi">7</span><span class="p">)],</span><span class="s1">'D'</span><span class="p">:(</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">),</span><span class="s1">'C'</span><span class="p">:(</span><span class="mi">8</span><span class="p">,</span><span class="mi">3</span><span class="p">)},</span><span class="n">obstacles</span><span class="o">=</span><span class="n">fronteira</span> <span class="o">|</span> <span class="n">l</span> <span class="o">|</span> <span class="n">c</span><span class="p">,</span><span class="n">dim</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"O meu estado inicial é:"</span><span class="p">,</span> <span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"O objetivo é atingir pelo menos:"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">goal</span><span class="p">,</span><span class="s2">"pontos"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>O meu estado inicial é: (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0))

O objetivo é atingir pelo menos: 8 pontos

= = = = = = = = = = 
= @ N . . . . . . = 
= . = = = = = = . = 
= . = . . . . . C = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Vamos verificar quais são as acções que podemos aplicar ao estado inicial</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[8]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">"As ações que podemos aplicar:"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>As ações que podemos aplicar: [('E', (2, 1)), ('S', (1, 2))]
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><span style="color:red"> **Note:**</span> que cada ação (x,y), é acompanhada pelo seu ponto cardial de modo a ser mais facil controlar os movimentos do nosso Pacman comilão.</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Vamos aplicar uma ação (primeira ação) ao nosso estado e obter um novo estado</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[9]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">e1</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">,(</span><span class="s1">'E'</span><span class="p">,</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">)))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">e1</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>(('posicaoPacman', (2, 1)), ('pacmanPassagens', ((1, 1), (2, 1))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 1), ('t', 1))
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Repare que o ponto aumentou para 1 e t aumentou para 1, o que indica que o nosso Pacman comeu uma pastilha, consequentemente deixou de ter uma pastilha em campo e também andou uma célula.</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Note também que não houve alteração do estado anterior, simplesmente foi gerado um novo estado</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[10]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">"Estado Inicial:"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Estado Inicial: (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0))

</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Vamos visualizar o nosso novo estado.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[11]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">e1</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>= = = = = = = = = = 
= + @ . . . . . . = 
= . = = = = = = . = 
= . = . . . . . C = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Repare que a posição do pacman mudou e consequentemente deixou um rasto sobre a ultima posição que passou</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Verifiquemos agora quais as ações aplicáveis a esse novo estado</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[12]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">e1</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[12]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>[('W', (1, 1)), ('E', (3, 1))]</pre>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Vamos aplicar uma ação (segunda ação) a esse novo estado e obter um novo estado</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[13]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">e2</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">e1</span><span class="p">,(</span><span class="s1">'E'</span><span class="p">,</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">)))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">e2</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>(('posicaoPacman', (3, 1)), ('pacmanPassagens', ((1, 1), (2, 1), (3, 1))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 1), ('t', 2))
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Vamos visualizar o nosso novo estado.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[14]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">e2</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>= = = = = = = = = = 
= + + @ . . . . . = 
= . = = = = = = . = 
= . = . . . . . C = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Qual foi o custo da ação e1 para e2?</p>
<p>Vamos testar a função path_cost.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[15]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">custo</span> <span class="o">=</span> <span class="mi">0</span> 

<span class="nb">print</span><span class="p">(</span><span class="s2">"Comecemos:"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Com custo ="</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>

<span class="n">acao</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="n">custo</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="n">custo</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">,</span><span class="n">acao</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">e1</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"Vamos para:"</span><span class="p">,</span><span class="n">e1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Com custo ="</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>

<span class="n">acao</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">e1</span><span class="p">)</span>
<span class="n">custo</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="n">custo</span><span class="p">,</span><span class="n">e1</span><span class="p">,</span><span class="n">acao</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span><span class="n">e2</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"Vamos para:"</span><span class="p">,</span><span class="n">e2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Com custo ="</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Comecemos: (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0))
Com custo = 0

Vamos para: (('posicaoPacman', (2, 1)), ('pacmanPassagens', ((1, 1), (2, 1))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 1), ('t', 1))
Com custo = 1

Vamos para: (('posicaoPacman', (3, 1)), ('pacmanPassagens', ((1, 1), (2, 1), (3, 1))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 1), ('t', 2))
Com custo = 2

</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>E se houver um caso em que ande para trás ?</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[16]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">acao</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">e2</span><span class="p">)</span>
<span class="n">e3</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">e2</span><span class="p">,</span><span class="n">acao</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="n">custo</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="n">custo</span><span class="p">,</span><span class="n">e2</span><span class="p">,</span><span class="n">acao</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">e3</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"Vamos para:"</span><span class="p">,</span><span class="n">e3</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Com custo ="</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Vamos para: (('posicaoPacman', (2, 1)), ('pacmanPassagens', ((1, 1), (2, 1), (3, 1), (2, 1))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 1), ('t', 3))
Com custo = 4

</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Porque o custo é 4 e não 3 ?</strong><br>
Repare que tal como dito na formulação do problema o pacman não gosta de visitar as células muitas vezes e por isso os custos das ações dependem da frequência com que visita as células que delas resultam. 
Quando visita uma célula pela primeira vez o custo é de 1, mas quando a visita pela n-ésima vez o custo é de n.</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Vamos aplicar uma sequência de ações a partir de nosso estado inicial. <br>
Para isso vamos usar a função <strong>exc()</strong>, que permite executar uma sequência de ações a partir de um estado qualquer, devolvendo o estado resultante e o custo acumulado num par <code>(estadoResultante,custoTotal)</code>.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[17]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">exec</span><span class="p">(</span><span class="n">p</span><span class="p">,</span><span class="n">estado</span><span class="p">,</span><span class="n">accoes</span><span class="p">):</span>
    <span class="n">custo</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">accoes</span><span class="p">:</span>
        <span class="n">seg</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">estado</span><span class="p">,</span><span class="n">a</span><span class="p">)</span>
        <span class="n">custo</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="n">custo</span><span class="p">,</span><span class="n">estado</span><span class="p">,</span><span class="n">a</span><span class="p">,</span><span class="n">seg</span><span class="p">)</span>
        <span class="n">estado</span> <span class="o">=</span> <span class="n">seg</span>
    <span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">estado</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">'Custo:'</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">'Goal?'</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">estado</span><span class="p">))</span>
    <span class="k">return</span> <span class="p">(</span><span class="n">estado</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[18]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">exect</span> <span class="o">=</span> <span class="n">exec</span><span class="p">(</span><span class="n">p</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">,[</span> <span class="p">(</span><span class="s1">'E'</span><span class="p">,(</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span> <span class="p">,</span> <span class="p">(</span><span class="s1">'E'</span><span class="p">,(</span><span class="mi">3</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span> <span class="p">,</span> <span class="p">(</span><span class="s1">'E'</span><span class="p">,(</span><span class="mi">4</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span> <span class="p">,</span> <span class="p">(</span><span class="s1">'E'</span><span class="p">,(</span><span class="mi">5</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span> <span class="p">,</span> <span class="p">(</span><span class="s1">'E'</span><span class="p">,(</span><span class="mi">6</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span> <span class="p">,</span> <span class="p">(</span><span class="s1">'E'</span><span class="p">,(</span><span class="mi">7</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span> <span class="p">,</span> <span class="p">(</span><span class="s1">'E'</span><span class="p">,(</span><span class="mi">8</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span> <span class="p">,</span> <span class="p">(</span><span class="s1">'S'</span><span class="p">,(</span><span class="mi">8</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span> <span class="p">,</span>
            <span class="p">(</span><span class="s1">'S'</span><span class="p">,(</span><span class="mi">8</span><span class="p">,</span><span class="mi">3</span><span class="p">)),</span> <span class="p">(</span><span class="s1">'W'</span><span class="p">,(</span><span class="mi">7</span><span class="p">,</span><span class="mi">3</span><span class="p">))])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">exect</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>= = = = = = = = = = 
= + + + + + + + + = 
= . = = = = = = + = 
= . = . . . . @ + = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 
Custo: 10
Goal? True
((('posicaoPacman', (7, 3)), ('pacmanPassagens', ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (7, 3))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)))), ('ponto', 10), ('t', 10)), 10)
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Embora tenhamos visto um goal teste com a função exec, vamos experimentar fazer um goal teste em caso de False e True</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[19]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">"Atingimos o objetivo em e3:"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">e3</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Atingimos o objetivo em e3: False
</pre>
</div>
</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[20]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">"Atingimos o objetivo em exec:"</span><span class="p">,</span><span class="n">p</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">exect</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Atingimos o objetivo em exec: True
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Verifiquemos agora a comparação entre estado. <br>
Como vimos anteriormente o estado e1 surgiu a partir de p.initial e e2 surgiu a partir de e1, portanto é previsivel que e1 &gt; p.initial, e2 &gt; e1.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[21]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">e0</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">initial</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"e1 é maior que e0:"</span><span class="p">,</span> <span class="n">e1</span> <span class="o">&gt;</span> <span class="n">e0</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"e2 é maior que e1:"</span><span class="p">,</span><span class="n">e2</span> <span class="o">&gt;</span> <span class="n">e1</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>e1 é maior que e0: True
e2 é maior que e1: True
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><span style="color:red"> **Note**:</span> Apesar de se criar um estado a partir de outro, não quer dizer que o estado criado tenha de ser obrigatoriamente maior que o estado anterior, por exemplo e2 &gt; e3.</p>
<p>Isto acontece porque se tivermos em casos como um resultado de novo estado em que houve retrocesso, ou seja, voltar para uma célula anterior estamos perante um destes casos, como no caso e3 gerado a apartir de e2.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[25]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">"e2 é maior que e3:"</span><span class="p">,</span><span class="n">e2</span> <span class="o">&gt;</span> <span class="n">e3</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>e2 é maior que e3: True
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h1 id="Teste-de-procura-de-solu%C3%A7%C3%A3o">Teste de procura de solução<a class="anchor-link" href="#Teste-de-procura-de-solu%C3%A7%C3%A3o">¶</a></h1><p>Mais abaixo vai haver testes de procura sobre o nosso problema definido anteriormente. <br>
Assim poderemos comparar o tempo de execução dos algoritmos e ver qual dos algoritmos é o mais rápido. <br>
Também iremos responder as perguntas como por exemplo <strong>"Porque é que a nossa procura entra em ciclo?"</strong>.</p>
<p><span style="color:red">Note:</span> Se a não houver pastilhas em campo inicialmente ou o tipo de problema não tenha solução, qualquer algoritmo entra em loop infinito.</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Profundidade-Primeiro-(%C3%A1rvore)">Profundidade-Primeiro (árvore)<a class="anchor-link" href="#Profundidade-Primeiro-(%C3%A1rvore)">¶</a></h3><p>O algoritmo de profundidade primeiro, <strong>dá preferência aos nós da fronteira que estejam mais afastados da raíz (maior número de acções).</strong> <br>
Se executarmos a procura em profundidade primeiro, podemos <strong>entrar em ciclo, porque este método de procura não faz controlo de ciclos.</strong> <br>
A procura em profundidade quando devolve uma solução não garante que ela seja a de menor custo, não sendo optimal. <strong>Só garante a solução óptima se todas as soluções estiverem à mesma profundidade e os custos são homogéneos.</strong></p>
<p>Vamos aplicar a procura em Profundidade-Primeiro (árvore) sobre o nosso problema anterior.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[26]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dfts</span> <span class="o">=</span> <span class="n">depth_first_tree_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">dfts</span><span class="o">.</span><span class="n">state</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr">
<pre><span class="ansi-red-intense-fg ansi-bold">---------------------------------------------------------------------------</span>
<span class="ansi-red-intense-fg ansi-bold">KeyboardInterrupt</span>                         Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">~\AppData\Local\Temp/ipykernel_8924/330208132.py</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 1</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>dfts <span class="ansi-yellow-intense-fg ansi-bold">=</span> depth_first_tree_search<span class="ansi-yellow-intense-fg ansi-bold">(</span>p<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">      2</span> p<span class="ansi-yellow-intense-fg ansi-bold">.</span>display<span class="ansi-yellow-intense-fg ansi-bold">(</span>dfts<span class="ansi-yellow-intense-fg ansi-bold">.</span>state<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\OneDrive - Universidade de Lisboa\2ºAno\2_Sem\Sistemas_Inteligentes\Projeto\P1\searchPlus.py</span> in <span class="ansi-cyan-fg">depth_first_tree_search</span><span class="ansi-blue-intense-fg ansi-bold">(problem)</span>
<span class="ansi-green-fg">    217</span> <span class="ansi-green-intense-fg ansi-bold">def</span> depth_first_tree_search<span class="ansi-yellow-intense-fg ansi-bold">(</span>problem<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    218</span>     <span class="ansi-blue-intense-fg ansi-bold">"""Search the deepest nodes in the search tree first."""</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 219</span><span class="ansi-yellow-intense-fg ansi-bold">     </span><span class="ansi-green-intense-fg ansi-bold">return</span> tree_search<span class="ansi-yellow-intense-fg ansi-bold">(</span>problem<span class="ansi-yellow-intense-fg ansi-bold">,</span> Stack<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    220</span> 
<span class="ansi-green-fg">    221</span> 

<span class="ansi-green-intense-fg ansi-bold">~\OneDrive - Universidade de Lisboa\2ºAno\2_Sem\Sistemas_Inteligentes\Projeto\P1\searchPlus.py</span> in <span class="ansi-cyan-fg">tree_search</span><span class="ansi-blue-intense-fg ansi-bold">(problem, frontier)</span>
<span class="ansi-green-fg">    189</span>         <span class="ansi-green-intense-fg ansi-bold">if</span> problem<span class="ansi-yellow-intense-fg ansi-bold">.</span>goal_test<span class="ansi-yellow-intense-fg ansi-bold">(</span>node<span class="ansi-yellow-intense-fg ansi-bold">.</span>state<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    190</span>             <span class="ansi-green-intense-fg ansi-bold">return</span> node
<span class="ansi-green-intense-fg ansi-bold">--&gt; 191</span><span class="ansi-yellow-intense-fg ansi-bold">         </span>frontier<span class="ansi-yellow-intense-fg ansi-bold">.</span>extend<span class="ansi-yellow-intense-fg ansi-bold">(</span>node<span class="ansi-yellow-intense-fg ansi-bold">.</span>expand<span class="ansi-yellow-intense-fg ansi-bold">(</span>problem<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    192</span>     <span class="ansi-green-intense-fg ansi-bold">return</span> <span class="ansi-green-intense-fg ansi-bold">None</span>
<span class="ansi-green-fg">    193</span> 

<span class="ansi-red-intense-fg ansi-bold">KeyboardInterrupt</span>: </pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Porque-a-profundidade-primeiro-entra-em-ciclo?">Porque a profundidade primeiro entra em ciclo?<a class="anchor-link" href="#Porque-a-profundidade-primeiro-entra-em-ciclo?">¶</a></h3><p>Para vermos porque é que a procura em profundidade entrou em ciclo, vamos renomear a funcao tree_search() e depth_first_tree_search() para <strong>tree_search_teste()</strong> e <strong>depth_first_tree_search_teste()</strong> respetivamente e de seguida inspecionar o seu funcionamento. <br>
Iremos fazer 20 simulações e ver em que nós a nossa procura passa.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[27]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">tree_search_teste</span><span class="p">(</span><span class="n">problem</span><span class="p">,</span> <span class="n">frontier</span><span class="p">):</span>
    <span class="sd">"""Search through the successors of a problem to find a goal.</span>
<span class="sd">    The argument frontier should be an empty queue.</span>
<span class="sd">    Don't worry about repeated paths to a state. [Figure 3.7]"""</span>
    <span class="n">frontier</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Node</span><span class="p">(</span><span class="n">problem</span><span class="o">.</span><span class="n">initial</span><span class="p">))</span>
    <span class="n">count</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="k">while</span> <span class="n">frontier</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">count</span> <span class="o">==</span> <span class="mi">20</span><span class="p">:</span>
            <span class="k">break</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">frontier</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">problem</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">state</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">node</span>
        <span class="n">frontier</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">expand</span><span class="p">(</span><span class="n">problem</span><span class="p">))</span>
        <span class="n">count</span> <span class="o">+=</span><span class="mi">1</span>
    <span class="k">return</span> <span class="kc">None</span>

<span class="k">def</span> <span class="nf">depth_first_tree_search_teste</span><span class="p">(</span><span class="n">problem</span><span class="p">):</span>
    <span class="sd">"""Search the deepest nodes in the search tree first."""</span>
    <span class="k">return</span> <span class="n">tree_search_teste</span><span class="p">(</span><span class="n">problem</span><span class="p">,</span> <span class="n">Stack</span><span class="p">())</span>

<span class="n">dfts</span> <span class="o">=</span> <span class="n">depth_first_tree_search_teste</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>&lt;Node (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0))&gt;

&lt;Node (('posicaoPacman', (1, 2)), ('pacmanPassagens', ((1, 1), (1, 2))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 1))&gt;

&lt;Node (('posicaoPacman', (1, 3)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 2))&gt;

&lt;Node (('posicaoPacman', (1, 4)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 3))&gt;

&lt;Node (('posicaoPacman', (1, 5)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 4))&gt;

&lt;Node (('posicaoPacman', (1, 6)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 5))&gt;

&lt;Node (('posicaoPacman', (1, 7)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 6))&gt;

&lt;Node (('posicaoPacman', (1, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 7))&gt;

&lt;Node (('posicaoPacman', (2, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 8))&gt;

&lt;Node (('posicaoPacman', (3, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 9))&gt;

&lt;Node (('posicaoPacman', (4, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 10))&gt;

&lt;Node (('posicaoPacman', (5, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 11))&gt;

&lt;Node (('posicaoPacman', (6, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 12))&gt;

&lt;Node (('posicaoPacman', (7, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 13))&gt;

&lt;Node (('posicaoPacman', (8, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 14))&gt;

&lt;Node (('posicaoPacman', (7, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (7, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 15))&gt;

&lt;Node (('posicaoPacman', (8, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (7, 8), (8, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 16))&gt;

&lt;Node (('posicaoPacman', (7, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (7, 8), (8, 8), (7, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 17))&gt;

&lt;Node (('posicaoPacman', (8, 8)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (7, 8), (8, 8), (7, 8), (8, 8))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 18))&gt;

</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Como podemos ver, assim que chegamos a posicao (8,8) a nossa procura fica num loop infinito, variado entre os estados de posição (8,8) e de posição (7,8), não saindo daí. <br>
Ao empilharmos os sucessores, as ordens invertem-se dando origem ao ciclo.</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Largura-Primeiro-(%C3%A1rvore)">Largura-Primeiro (árvore)<a class="anchor-link" href="#Largura-Primeiro-(%C3%A1rvore)">¶</a></h3><p>Vamos executar uma procura em largura primeiro que <strong>dá preferência aos nós da fronteira que estão mais à superfície (menor número de acções)</strong> e que nos dará uma solução óptima em termos do número de acções, e não em termos do custo. <strong>Só garante a optimalidade quando os custos são homogéneos</strong>, o que não é o caso. <br>
<strong>A procura em largura, numa árvore, não entra em ciclo</strong> porque primeiro explora todos os estados à distância de uma acção do estado inicial, depois todos os estados à distância de duas acções do estado inicial, etc., ultrapassando assim um ciclo infinito desde que haja uma solução.</p>
<p>Vamos aplicar a procura em Largura-Primeiro (árvore) sobre o nosso problema anterior e posteriormente aplicar o display de modo a visualizarmos o estado inicial e a solução.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[28]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">bfts</span> <span class="o">=</span> <span class="n">breadth_first_tree_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"O nó resultante da procura em largura primeiro é:"</span><span class="p">,</span><span class="n">bfts</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"As ações aplicadas ao estado foram:"</span><span class="p">,</span><span class="n">bfts</span><span class="o">.</span><span class="n">solution</span><span class="p">())</span>
<span class="nb">print</span><span class="p">()</span>
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">bfts</span><span class="o">.</span><span class="n">state</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>= = = = = = = = = = 
= @ N . . . . . . = 
= . = = = = = = . = 
= . = . . . . . C = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 

O nó resultante da procura em largura primeiro é: &lt;Node (('posicaoPacman', (8, 3)), ('pacmanPassagens', ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)))), ('ponto', 10), ('t', 9))&gt;

As ações aplicadas ao estado foram: [('E', (2, 1)), ('E', (3, 1)), ('E', (4, 1)), ('E', (5, 1)), ('E', (6, 1)), ('E', (7, 1)), ('E', (8, 1)), ('S', (8, 2)), ('S', (8, 3))]

= = = = = = = = = = 
= + + + + + + + + = 
= . = = = = = = + = 
= . = . . . . . @ = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Profundidade-Primeiro-(grafo)">Profundidade-Primeiro (grafo)<a class="anchor-link" href="#Profundidade-Primeiro-(grafo)">¶</a></h3><p>Na procura em profundidade primeiro em grafo, é preciso guardar os estados expandidos num conjunto e também filtrar os estados sucessores, evitando os já expandidos ou aqueles que são terminais dos caminhos na fronteira, ou seja, os não expandidos mas na fronteira). <br>
Tal como acontecia na profundidade primeiro em arvore, e executarmos a procura em profundidade primeiro em grafo, <strong>entraremos em ciclo.</strong></p>
<p>Vamos aplicar a procura em Profundidade-Primeiro (grafo) sobre o nosso problema anterior.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[29]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dfgs</span> <span class="o">=</span> <span class="n">depth_first_graph_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">dfgs</span><span class="o">.</span><span class="n">state</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr">
<pre><span class="ansi-red-intense-fg ansi-bold">---------------------------------------------------------------------------</span>
<span class="ansi-red-intense-fg ansi-bold">KeyboardInterrupt</span>                         Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">~\AppData\Local\Temp/ipykernel_8924/1459744273.py</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 1</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>dfgs <span class="ansi-yellow-intense-fg ansi-bold">=</span> depth_first_graph_search<span class="ansi-yellow-intense-fg ansi-bold">(</span>p<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">      2</span> p<span class="ansi-yellow-intense-fg ansi-bold">.</span>display<span class="ansi-yellow-intense-fg ansi-bold">(</span>dfgs<span class="ansi-yellow-intense-fg ansi-bold">.</span>state<span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">~\OneDrive - Universidade de Lisboa\2ºAno\2_Sem\Sistemas_Inteligentes\Projeto\P1\searchPlus.py</span> in <span class="ansi-cyan-fg">depth_first_graph_search</span><span class="ansi-blue-intense-fg ansi-bold">(problem)</span>
<span class="ansi-green-fg">    222</span> <span class="ansi-green-intense-fg ansi-bold">def</span> depth_first_graph_search<span class="ansi-yellow-intense-fg ansi-bold">(</span>problem<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    223</span>     <span class="ansi-blue-intense-fg ansi-bold">"""Search the deepest nodes in the search tree first."""</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 224</span><span class="ansi-yellow-intense-fg ansi-bold">     </span><span class="ansi-green-intense-fg ansi-bold">return</span> graph_search<span class="ansi-yellow-intense-fg ansi-bold">(</span>problem<span class="ansi-yellow-intense-fg ansi-bold">,</span> Stack<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-fg">    225</span> 
<span class="ansi-green-fg">    226</span> 

<span class="ansi-green-intense-fg ansi-bold">~\OneDrive - Universidade de Lisboa\2ºAno\2_Sem\Sistemas_Inteligentes\Projeto\P1\searchPlus.py</span> in <span class="ansi-cyan-fg">graph_search</span><span class="ansi-blue-intense-fg ansi-bold">(problem, frontier)</span>
<span class="ansi-green-fg">    204</span>             <span class="ansi-green-intense-fg ansi-bold">return</span> node
<span class="ansi-green-fg">    205</span>         explored<span class="ansi-yellow-intense-fg ansi-bold">.</span>add<span class="ansi-yellow-intense-fg ansi-bold">(</span>node<span class="ansi-yellow-intense-fg ansi-bold">.</span>state<span class="ansi-yellow-intense-fg ansi-bold">)</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 206</span><span class="ansi-yellow-intense-fg ansi-bold">         frontier.extend(child for child in node.expand(problem)
</span><span class="ansi-green-fg">    207</span>                         <span class="ansi-green-intense-fg ansi-bold">if</span> child<span class="ansi-yellow-intense-fg ansi-bold">.</span>state <span class="ansi-green-intense-fg ansi-bold">not</span> <span class="ansi-green-intense-fg ansi-bold">in</span> explored <span class="ansi-green-intense-fg ansi-bold">and</span>
<span class="ansi-green-fg">    208</span>                         child not in frontier)

<span class="ansi-green-intense-fg ansi-bold">~\OneDrive - Universidade de Lisboa\2ºAno\2_Sem\Sistemas_Inteligentes\Projeto\P1\searchPlus.py</span> in <span class="ansi-cyan-fg">&lt;genexpr&gt;</span><span class="ansi-blue-intense-fg ansi-bold">(.0)</span>
<span class="ansi-green-fg">    206</span>         frontier.extend(child for child in node.expand(problem)
<span class="ansi-green-fg">    207</span>                         <span class="ansi-green-intense-fg ansi-bold">if</span> child<span class="ansi-yellow-intense-fg ansi-bold">.</span>state <span class="ansi-green-intense-fg ansi-bold">not</span> <span class="ansi-green-intense-fg ansi-bold">in</span> explored <span class="ansi-green-intense-fg ansi-bold">and</span>
<span class="ansi-green-intense-fg ansi-bold">--&gt; 208</span><span class="ansi-yellow-intense-fg ansi-bold">                         child not in frontier)
</span><span class="ansi-green-fg">    209</span>     <span class="ansi-green-intense-fg ansi-bold">return</span> <span class="ansi-green-intense-fg ansi-bold">None</span>
<span class="ansi-green-fg">    210</span> 

<span class="ansi-green-intense-fg ansi-bold">~\OneDrive - Universidade de Lisboa\2ºAno\2_Sem\Sistemas_Inteligentes\Projeto\P1\searchPlus.py</span> in <span class="ansi-cyan-fg">__eq__</span><span class="ansi-blue-intense-fg ansi-bold">(self, other)</span>
<span class="ansi-green-fg">    132</span>     <span class="ansi-red-intense-fg ansi-bold"># want in other contexts.]</span>
<span class="ansi-green-fg">    133</span> 
<span class="ansi-green-intense-fg ansi-bold">--&gt; 134</span><span class="ansi-yellow-intense-fg ansi-bold">     </span><span class="ansi-green-intense-fg ansi-bold">def</span> __eq__<span class="ansi-yellow-intense-fg ansi-bold">(</span>self<span class="ansi-yellow-intense-fg ansi-bold">,</span> other<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-fg">    135</span>         <span class="ansi-green-intense-fg ansi-bold">return</span> isinstance<span class="ansi-yellow-intense-fg ansi-bold">(</span>other<span class="ansi-yellow-intense-fg ansi-bold">,</span> Node<span class="ansi-yellow-intense-fg ansi-bold">)</span> <span class="ansi-green-intense-fg ansi-bold">and</span> self<span class="ansi-yellow-intense-fg ansi-bold">.</span>state <span class="ansi-yellow-intense-fg ansi-bold">==</span> other<span class="ansi-yellow-intense-fg ansi-bold">.</span>state
<span class="ansi-green-fg">    136</span> 

<span class="ansi-red-intense-fg ansi-bold">KeyboardInterrupt</span>: </pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Porque-a-profundidade-primeiro-em-grafo-entra-em-ciclo?">Porque a profundidade primeiro em grafo entra em ciclo?<a class="anchor-link" href="#Porque-a-profundidade-primeiro-em-grafo-entra-em-ciclo?">¶</a></h3><p>Para vermos porque é que a procura em profundidade primeiro em grafo entrou em ciclo, vamos renomear a funcao graph_search() e depth_first_graph_search() para <strong>graph_search_teste()</strong> e <strong>depth_first_graph_search_teste()</strong> respetivamente e de seguida inspecionar o seu funcionamento. <br>
Fazer 5 simulações e ver a nossa fronteira.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[33]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">graph_search_teste</span><span class="p">(</span><span class="n">problem</span><span class="p">,</span> <span class="n">frontier</span><span class="p">):</span>
    <span class="sd">"""Search through the successors of a problem to find a goal.</span>
<span class="sd">    The argument frontier should be an empty queue.</span>
<span class="sd">    If two paths reach a state, only use the first one. [Figure 3.7]"""</span>
    <span class="n">frontier</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Node</span><span class="p">(</span><span class="n">problem</span><span class="o">.</span><span class="n">initial</span><span class="p">))</span>
    <span class="n">explored</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
    <span class="n">count</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="k">while</span> <span class="n">frontier</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">count</span> <span class="o">==</span> <span class="mi">5</span><span class="p">:</span>
            <span class="k">break</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">frontier</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
        <span class="nb">print</span><span class="p">()</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">node</span><span class="p">,</span><span class="s2">"Este é Nó"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">problem</span><span class="o">.</span><span class="n">goal_test</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">state</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">node</span>
        <span class="n">explored</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">state</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">()</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">explored</span><span class="p">,</span><span class="s2">"Este é explorado"</span><span class="p">)</span>
        <span class="n">frontier</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">child</span> <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="n">node</span><span class="o">.</span><span class="n">expand</span><span class="p">(</span><span class="n">problem</span><span class="p">)</span>
                        <span class="k">if</span> <span class="n">child</span><span class="o">.</span><span class="n">state</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">explored</span> <span class="ow">and</span>
                        <span class="n">child</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">frontier</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">frontier</span><span class="p">,</span><span class="s2">"Esta é a fronteira"</span><span class="p">)</span>
        <span class="n">count</span> <span class="o">+=</span><span class="mi">1</span>
        <span class="nb">print</span><span class="p">()</span>
    <span class="k">return</span> <span class="kc">None</span>

<span class="k">def</span> <span class="nf">depth_first_graph_search_teste</span><span class="p">(</span><span class="n">problem</span><span class="p">):</span>
    <span class="sd">"""Search the deepest nodes in the search tree first."""</span>
    <span class="k">return</span> <span class="n">graph_search_teste</span><span class="p">(</span><span class="n">problem</span><span class="p">,</span> <span class="n">Stack</span><span class="p">())</span>

<span class="n">dfgs</span> <span class="o">=</span> <span class="n">depth_first_graph_search_teste</span><span class="p">(</span><span class="n">p</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>&lt;Node (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0))&gt; Este é Nó

{(('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0))} Este é explorado
[&lt;Node (('posicaoPacman', (2, 1)), ('pacmanPassagens', ((1, 1), (2, 1))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 1), ('t', 1))&gt;, &lt;Node (('posicaoPacman', (1, 2)), ('pacmanPassagens', ((1, 1), (1, 2))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 1))&gt;] Esta é a fronteira


&lt;Node (('posicaoPacman', (1, 2)), ('pacmanPassagens', ((1, 1), (1, 2))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 1))&gt; Este é Nó

{(('posicaoPacman', (1, 2)), ('pacmanPassagens', ((1, 1), (1, 2))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 1)), (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0))} Este é explorado
[&lt;Node (('posicaoPacman', (2, 1)), ('pacmanPassagens', ((1, 1), (2, 1))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 1), ('t', 1))&gt;, &lt;Node (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 1))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 2))&gt;, &lt;Node (('posicaoPacman', (1, 3)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 2))&gt;] Esta é a fronteira


&lt;Node (('posicaoPacman', (1, 3)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 2))&gt; Este é Nó

{(('posicaoPacman', (1, 2)), ('pacmanPassagens', ((1, 1), (1, 2))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 1)), (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0)), (('posicaoPacman', (1, 3)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 2))} Este é explorado
[&lt;Node (('posicaoPacman', (2, 1)), ('pacmanPassagens', ((1, 1), (2, 1))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 1), ('t', 1))&gt;, &lt;Node (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 1))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 2))&gt;, &lt;Node (('posicaoPacman', (1, 2)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 2))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 3))&gt;, &lt;Node (('posicaoPacman', (1, 4)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 3))&gt;] Esta é a fronteira


&lt;Node (('posicaoPacman', (1, 4)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 3))&gt; Este é Nó

{(('posicaoPacman', (1, 2)), ('pacmanPassagens', ((1, 1), (1, 2))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 1)), (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1),)), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 0)), (('posicaoPacman', (1, 3)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 2)), (('posicaoPacman', (1, 4)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 3))} Este é explorado
[&lt;Node (('posicaoPacman', (2, 1)), ('pacmanPassagens', ((1, 1), (2, 1))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 1), ('t', 1))&gt;, &lt;Node (('posicaoPacman', (1, 1)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 1))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 2))&gt;, &lt;Node (('posicaoPacman', (1, 2)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 2))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 3))&gt;, &lt;Node (('posicaoPacman', (1, 3)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 3))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 4))&gt;, &lt;Node (('posicaoPacman', (1, 5)), ('pacmanPassagens', ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5))), ('pastilhasEmCampo', (('N', ((2, 1), (3, 7))), ('D', (4, 5)), ('C', (8, 3)))), ('ponto', 0), ('t', 4))&gt;] Esta é a fronteira

</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Como podemos ver, o nosso Pacman comilão ja passou pela posição (1,1) com certos atributos num certa altura, mas é possivel ver que ele <strong>acrescenta a fronteira outra vez porque essa mesma posição contém outros atributos completamente diferentes</strong>, logo esses dois nós não são iguais. <br>
É este o indicativo que nos permite ver que a profundidade primeiro em grafo pode entrar num ciclo infinito, algo que normalmente não costuma acontecer.</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Largura-Primeiro-em-(grafo)">Largura-Primeiro em (grafo)<a class="anchor-link" href="#Largura-Primeiro-em-(grafo)">¶</a></h3><p>Na procura em largura primeiro em grafo, tal como na profundidade primeiro em grafo é preciso guardar os estados expandidos num conjunto e também filtrar os estados sucessores, evitando os já expandidos ou aqueles que são terminais dos caminhos na fronteira, ou seja, os não expandidos mas na fronteira).</p>
<p>Vamos aplicar a procura Largura-Primeiro em (grafo) sobre o nosso problema anterior e posteriormente aplicar o display de modo a visualizarmos o estado inicial e a solução..</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[34]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">breadth_first_graph_search</span><span class="p">(</span><span class="n">problem</span><span class="p">):</span>
    <span class="sd">"""Search the deepest nodes in the search tree first."""</span>
    <span class="k">return</span> <span class="n">graph_search</span><span class="p">(</span><span class="n">problem</span><span class="p">,</span> <span class="n">FIFOQueue</span><span class="p">())</span>

<span class="n">bfgs</span> <span class="o">=</span> <span class="n">breadth_first_graph_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"O nó resultante da procura em Aprofundamento progressivo é:"</span><span class="p">,</span><span class="n">bfgs</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"As ações aplicadas ao estado foram:"</span><span class="p">,</span><span class="n">bfgs</span><span class="o">.</span><span class="n">solution</span><span class="p">())</span>
<span class="nb">print</span><span class="p">()</span>
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">bfgs</span><span class="o">.</span><span class="n">state</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>= = = = = = = = = = 
= @ N . . . . . . = 
= . = = = = = = . = 
= . = . . . . . C = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 

O nó resultante da procura em Aprofundamento progressivo é: &lt;Node (('posicaoPacman', (8, 3)), ('pacmanPassagens', ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)))), ('ponto', 10), ('t', 9))&gt;

As ações aplicadas ao estado foram: [('E', (2, 1)), ('E', (3, 1)), ('E', (4, 1)), ('E', (5, 1)), ('E', (6, 1)), ('E', (7, 1)), ('E', (8, 1)), ('S', (8, 2)), ('S', (8, 3))]

= = = = = = = = = = 
= + + + + + + + + = 
= . = = = = = = + = 
= . = . . . . . @ = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Aprofundamento-Progressivo">Aprofundamento Progressivo<a class="anchor-link" href="#Aprofundamento-Progressivo">¶</a></h3><p>Se aplicarmos o aprofundamento progressivo não teremos também a garantia de encontrar a solução óptima porque os custos não são homogéneos. <br>
<strong>Este algoritmo garante a solução mais próxima do estado inicial, em termos de número de acções,</strong> como a procura em largura, mas com um custo menor do que a largura em termos de memória utilizada.
Ele começa por fazer uma procura limitada ao estado inicial e à profundidade 0, depois limitada à profundidade 1, a seguir limitada à profundidade 2, etc. etc., evitando os ciclos até encontrar uma solução que esteja mais próxima da raíz da árvore em termos do número de movimentos ou acções.</p>
<p>Vamos aplicar a procura em Aprofundamento Progressivo sobre o nosso problema anterior e posteriormente aplicar o display de modo a visualizarmos o estado inicial e a solução.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[35]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ids</span> <span class="o">=</span> <span class="n">iterative_deepening_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"O nó resultante da procura em Aprofundamento progressivo é:"</span><span class="p">,</span><span class="n">ids</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"As ações aplicadas ao estado foram:"</span><span class="p">,</span><span class="n">ids</span><span class="o">.</span><span class="n">solution</span><span class="p">())</span>
<span class="nb">print</span><span class="p">()</span>
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">ids</span><span class="o">.</span><span class="n">state</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>= = = = = = = = = = 
= @ N . . . . . . = 
= . = = = = = = . = 
= . = . . . . . C = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 

O nó resultante da procura em Aprofundamento progressivo é: &lt;Node (('posicaoPacman', (8, 3)), ('pacmanPassagens', ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)))), ('ponto', 10), ('t', 9))&gt;

As ações aplicadas ao estado foram: [('E', (2, 1)), ('E', (3, 1)), ('E', (4, 1)), ('E', (5, 1)), ('E', (6, 1)), ('E', (7, 1)), ('E', (8, 1)), ('S', (8, 2)), ('S', (8, 3))]

= = = = = = = = = = 
= + + + + + + + + = 
= . = = = = = = + = 
= . = . . . . . @ = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Custo-Uniforme">Custo Uniforme<a class="anchor-link" href="#Custo-Uniforme">¶</a></h3><p>Se aplicarmos a procura de custo uniforme <strong>teremos sempre a solução óptima</strong>.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[36]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ucs</span> <span class="o">=</span> <span class="n">uniform_cost_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"O nó resultante da procura em Aprofundamento progressivo é:"</span><span class="p">,</span><span class="n">ids</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"As ações aplicadas ao estado foram:"</span><span class="p">,</span><span class="n">ucs</span><span class="o">.</span><span class="n">solution</span><span class="p">())</span>
<span class="nb">print</span><span class="p">()</span>
<span class="n">p</span><span class="o">.</span><span class="n">display</span><span class="p">(</span><span class="n">ucs</span><span class="o">.</span><span class="n">state</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>= = = = = = = = = = 
= @ N . . . . . . = 
= . = = = = = = . = 
= . = . . . . . C = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 

O nó resultante da procura em Aprofundamento progressivo é: &lt;Node (('posicaoPacman', (8, 3)), ('pacmanPassagens', ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3))), ('pastilhasEmCampo', (('N', ((3, 7),)), ('D', (4, 5)))), ('ponto', 10), ('t', 9))&gt;

As ações aplicadas ao estado foram: [('E', (2, 1)), ('E', (3, 1)), ('E', (4, 1)), ('E', (5, 1)), ('E', (6, 1)), ('E', (7, 1)), ('E', (8, 1)), ('S', (8, 2)), ('S', (8, 3))]

= = = = = = = = = = 
= + + + + + + + + = 
= . = = = = = = + = 
= . = . . . . . @ = 
= . = . . . . . . = 
= . = . D . . . . = 
= . = . . . . . . = 
= . . N . . . . . = 
= . . . . . . . . = 
= = = = = = = = = = 
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Compara%C3%A7%C3%A3o-dos-resultados-ao-n%C3%ADvel-de-tempo-de-execu%C3%A7%C3%A3o">Comparação dos resultados ao nível de tempo de execução<a class="anchor-link" href="#Compara%C3%A7%C3%A3o-dos-resultados-ao-n%C3%ADvel-de-tempo-de-execu%C3%A7%C3%A3o">¶</a></h3><p>Dentro dos algoritmos de procura que vimos anteriormente, vamos comparar aqueles que não entram em loop em termos de tempo, ou seja, vamos descobrir quem é o mais rápido.</p>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h4 id="Tempo-de-execu%C3%A7%C3%A3o-do-algoritmo-Largura-Primeiro-(%C3%A1rvore)">Tempo de execução do algoritmo Largura-Primeiro (árvore)<a class="anchor-link" href="#Tempo-de-execu%C3%A7%C3%A3o-do-algoritmo-Largura-Primeiro-(%C3%A1rvore)">¶</a></h4>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[49]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">timeit</span>

<span class="n">start</span> <span class="o">=</span> <span class="n">timeit</span><span class="o">.</span><span class="n">default_timer</span><span class="p">()</span>
<span class="n">bfts</span> <span class="o">=</span> <span class="n">breadth_first_tree_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
<span class="n">final_bfts</span> <span class="o">=</span> <span class="n">timeit</span><span class="o">.</span><span class="n">default_timer</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span> 

<span class="nb">print</span><span class="p">(</span><span class="s2">"O tempo de execução da Largura-Primeiro (árvore):"</span><span class="p">,</span><span class="n">final_bfts</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>O tempo de execução da Largura-Primeiro (árvore): 0.0848599999999351
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h4 id="Tempo-de-execu%C3%A7%C3%A3o-do-algoritmo-Largura-Primeiro-(grafo)">Tempo de execução do algoritmo Largura-Primeiro (grafo)<a class="anchor-link" href="#Tempo-de-execu%C3%A7%C3%A3o-do-algoritmo-Largura-Primeiro-(grafo)">¶</a></h4>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[50]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">start</span> <span class="o">=</span> <span class="n">timeit</span><span class="o">.</span><span class="n">default_timer</span><span class="p">()</span>
<span class="n">bfgs</span> <span class="o">=</span> <span class="n">breadth_first_graph_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span>
<span class="n">final_bfgs</span> <span class="o">=</span> <span class="n">timeit</span><span class="o">.</span><span class="n">default_timer</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span> 

<span class="nb">print</span><span class="p">(</span><span class="s2">"O tempo de execução do Largura-Primeiro (grafo):"</span><span class="p">,</span><span class="n">final_bfgs</span><span class="p">)</span> 
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>O tempo de execução do Largura-Primeiro (grafo): 0.2960712999997668
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h4 id="Tempo-de-execu%C3%A7%C3%A3o-do-algoritmo-Aprofundamento-Progressivo-(grafo)">Tempo de execução do algoritmo Aprofundamento-Progressivo (grafo)<a class="anchor-link" href="#Tempo-de-execu%C3%A7%C3%A3o-do-algoritmo-Aprofundamento-Progressivo-(grafo)">¶</a></h4>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[51]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">start</span> <span class="o">=</span> <span class="n">timeit</span><span class="o">.</span><span class="n">default_timer</span><span class="p">()</span>
<span class="n">ids</span> <span class="o">=</span> <span class="n">iterative_deepening_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
<span class="n">final_ids</span> <span class="o">=</span> <span class="n">timeit</span><span class="o">.</span><span class="n">default_timer</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span> 

<span class="nb">print</span><span class="p">(</span><span class="s2">"O tempo de execução do Aprofundamento-Progressivo (árvore):"</span><span class="p">,</span><span class="n">final_ids</span><span class="p">)</span> 
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>O tempo de execução do Aprofundamento-Progressivo (árvore): 0.0643632000001162
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h4 id="Tempo-de-execu%C3%A7%C3%A3o-do-algoritmo-Custo-uniforme">Tempo de execução do algoritmo Custo uniforme<a class="anchor-link" href="#Tempo-de-execu%C3%A7%C3%A3o-do-algoritmo-Custo-uniforme">¶</a></h4>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[52]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">start</span> <span class="o">=</span> <span class="n">timeit</span><span class="o">.</span><span class="n">default_timer</span><span class="p">()</span>
<span class="n">ucs</span> <span class="o">=</span> <span class="n">uniform_cost_search</span><span class="p">(</span><span class="n">p</span><span class="p">)</span> 
<span class="n">final_ucs</span> <span class="o">=</span> <span class="n">timeit</span><span class="o">.</span><span class="n">default_timer</span><span class="p">()</span> <span class="o">-</span> <span class="n">start</span> 

<span class="nb">print</span><span class="p">(</span><span class="s2">"O tempo de execução do custo uniforme:"</span><span class="p">,</span><span class="n">final_ucs</span><span class="p">)</span> 
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>O tempo de execução do custo uniforme: 0.06069169999955193
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Quem-%C3%A9-o-mais-eficiente-?">Quem é o mais eficiente ?<a class="anchor-link" href="#Quem-%C3%A9-o-mais-eficiente-?">¶</a></h3><p>Depois desta análise, conseguimos afirmar que para obter a solução ideal para um determinado problema o uso do algoritmo do custo uniforme é a melhor solução.
A nível do tempo de execução do programa, o custo uniforme também é melhor.</p>

</div>
</div>









</body>
