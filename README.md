# gravity-simulation 🌎

# Introdução 📜
O programa se propõe a fazer uma simulação da interação gravitacional entre diversos planetas, O programa conta com uma simulação já pronta de um sistema análogo ao nosso sistema solar, ou o usuário pode definir o programa para funcionar apartir de um arquivo ```input.data```, onde podem ser definidas massa, posição no eixo x e y do corpo, o nome do corpo, sua velocidade inicial e seu raio. Para os calculos foi utilizado como base a lei de newton para gravitação:


<img src="img\formula.jpg" alt="formula" width="300" style="display: block; margin: auto;">


Onde  M  e  m  é a massa dos dois corpos que sofrem a interação, G é a gravidade do meio, e dé a distância entre os 2 corpos.

# Exemplo de execução 📌
<img src="img\Simulação de Órbita.png" alt="Simulation" width="400" style="display: block; margin: auto;">


Para esse exemplo temos como entrada:

+ Saturno. 
+ Sol.
+ Terra.
+ Marte.
+ Mercurio.
+ Vênus.

Todos objetos da classe ```BodiesInit```, que tem o objetivo apenas de inicializar as posições, velocidades e cores dos planetas citados acima.

É possível alterar a velocidade dos planetas,e o sentido da mesma; basta apertar a tecla ```SPACE```, oquê vai pausar a simulação, durante esse processo é possível fazer as alterações na velocidade, é necessário 'clicar' em um planeta e arrastar para um ponto que queira, quanto mais 'longe' maior será o módulo da velocidade e também o sentido é importante.


exemplo de alteração de velocidade e sentido:


<img src="img\vetores orbitas.png" alt="Simulation" width="400" style="display: block; margin: auto;">


Após apertar a tecla ```SPACE``` denovo, despausamos a simulação.



<img src="img\execução orbitas.png" alt="Simulation" width="400" style="display: block; margin: auto;">



## Exemplo de arquivo de entrada (```input.data```):


<img src="img\Inputdata exemplo.png" alt="Simulation" width="600" style="display: block; margin: auto;">


Para a inclusão de novos corpos no programa deve-se seguir as seguintes diretivas.

+ ```nome``` 
+ ```posição em X```.
+ ```posição em Y```.
+ ```Massa do corpo```.
+ ```Velocidade em X```.
+ ```Velocidade em Y```.
+ ```Cor```.
+ ```Raio do corpo```.


De maneira mais direta: nome: ```nome_desejado``` x:```posição_x desejada``` y:```posição_y desejada``` massa:```massa desejada``` vx:```velocidade_x desejada``` vy:```velocidade_y desejada``` cor:```cor desejada``` raio:```raio desejado```.

Exemplo de execução do arquivo de entrada:

<img src="img\Simulação de Órbita inputdata.png" alt="Simulation" width="400" style="display: block; margin: auto;">




# Resultados de execução
Para cada planeta selecionado durante a execução do programa é mostrado no terminal: a velocidade no eixo X e a velocidade no eixo Y, bem como a massa do planeta
\\ <img src="img\Output.png" alt="output" width="400" style="display: block; margin: auto;"> \\


Semelhantemente para o arquivo de entrada definido pelo usuário:


<img src="img\Output inputdata.png" alt="output" width="400" style="display: block; margin: auto;">

# Compilação e execução 
O programa se Utiliza do Python e da biblioteca Pygame. Para a execução é recomendado que tenha o Python 3.9, pip e o pygame instalados em seu computador.
Instalação (Python e Pygame): \\

<table border="1">
      <tr><td><u>sudo apt-get install python3.9</u></td></tr>
      <tr><td><u>sudo apt-get install python3-pip</u></td></tr>
      <tr><td><u>pip install pygame</u></td></tr>
</table>


Após a instalação basta clonar este repositório, pelo comando:
<table border="1">
      <tr><td><u>git clone git@github.com:Getulio-Mendes/gravity-simulation.git</u></td></tr>
</table>


Agora basta utilizar da linha de comando, para executar o programa:
<table border="1">
      <tr><td><u>python3 main.py</u></td></tr>
</table>

# Autores 
+ Leandro Sousa Costa  
+ Getúlio Santos Mendes 
+ João Pedro Freitas 
+ Gabriel Vitor Silva


