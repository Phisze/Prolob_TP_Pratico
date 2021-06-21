game(12,14,17,18,19,22).
game(2, 6 ,44,46,53,58).
game(12,13,25,37,39,41).
game(23,24,26,44,49,60).
game(3,19,25,44,46,57).
game(4,15,30,36,39,48).
game(7,31,37,42,44,56).
game(4,9,17,19,37,60).
game(4,7,13,25,36,58).
game(5,23,29,34,53,60).
game(4,27,33,35,38,41).
game(1,17,28,37,44,50).
game(20,33,42,44,51,56).
game(6,14,24,34,39,58).
game(3,20,22,32,35,50).
game(14,21,22,29,35,46).
game(10,15,21,24,29,45).
game(31,32,39,42,43,51).
game(5,9,11,16,43,57).
game(19,28,30,34,40,51).
game(19,28,30,34,40,51).



% O número X já foi sorteado alguma vez?



% Qual número nunca foi sorteado? Encotrar os que falta na ordem missing
% Criei uma lista de listas com todos os elementos usando o findall, usei o flatten para tranformar em uma lista só e ordenei,
%então criei uma lista que contém todos os elementos e subtrai a lista gerada por uma lista com todos elementos, se a subtração
%retornar uma lista vazia é false, se não a lista dos não encontrados é printada. O is_empty verifico se qualquer coisa faz parte
%da lista caso faça é true e para a execução, se não false.
%Exemplo: n_sort. False or os não numeros nunca contemplados
never_sort :- findall([X, Y, Z, W, Q, E], game(X, Y, Z, W, Q, E), List), flatten(List, L), sort(L, LS), numlist(1, 60, Lall), 
                subtract(Lall, LS, Lfinal), is_empty(Lfinal), write(Lfinal).
is_empty(List):- member(_,List), !.

% O jogo (X1,X2,X3,X4,X5,X6) já foi contemplado alguma vez?




% Algum jogo completo já foi contemplado mais de uma vez? Qual?
% Uso a função findall para printar todos os fatos e após feito isso chamo a função duplicate que verica se há 
%algum jogo duplicado na lista de fatos. Ele usa um para ir quebrando a lista em pedaços e depois vai verificando se enconta
%um elemento igual na duas partes da lista atrás da função member quando encontra printa. 
%Exemplo: game_sort_N. jogos que estão contemplados mais de uma vez
game_sort_N :- findall((X, Y, Z, W, Q, E), game(X, Y, Z, W, Q, E), L), duplicate(L).
duplicate(List):- append(X,Y,List), member(M,X), member(M,Y), write(M).

% Um número X foi sorteado quantas vezes?
% Uso a função findall para encontrar quantas vezes um numero foi sorteado em game e 
%após isso uso a função length para verificar o tamanho do array de resposta
%Exemplo: qtde_X(12, N). N = numero de vezes sorteado
qtde_X(X, N) :- findall(X, (game(X, _, _, _, _, _); game(_, X, _, _, _, _); game(_, _, X, _, _, _); 
        game(_, _, _, X, _, _); game(_, _, _, _, X, _); game(_, _, _, _, _, X)), L), length(L,N).

% Qual o número foi mais sorteado?
% Uso o findall para gerar uma lista de listas de todos os elementos existentes nos fatos e flatten para transformar essa lista em 
%uma lista unica. Por fim chama a max_element_count para contar e mostra qual é o elemento mais usado. A max_element_count chama uma
%função sencundaria element count que atras do aggregate mostra a quantidade todos os numeros usado, então também atraves da função 
%aggregate ele conta o numero maximo da resposta gerada pelo o element_count.
%game_sort_Q(N, X). N = Numero mais sorteado, X = Vezes que foi sorteado.
element_count(X,N,L) :- aggregate(count,member(X,L),N).
max_element_count(X,N,L) :- aggregate(max(N1,X1),element_count(X1,N1,L),max(N,X)).
game_sort_Q(R1, R2) :- findall([X, Y, Z, W, Q, E], game(X, Y, Z, W, Q, E), List), flatten(List, L), max_element_count(R1, R2, L).

% Leitura de dados
% Chamar prolog
% Inserir diminamicamente os dados assert