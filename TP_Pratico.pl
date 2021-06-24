% O número X já foi sorteado alguma vez?
% Primeiramente, cria-se uma lista de listas com todos elementos, utilizando-se "findall"
% O "flatten" foi utilizado para se transformar a lista de listas em uma única lista total
% Após isto, utiliza-se a cláusula "member" para ver se um número qualquer já foi sorteado
% Coloca-se o comando de stop para, quando o Prolog achar o número dos jogos apresentados, ele parar a execução
has_number_sorted(A) :- findall([X, Y, Z, W, Q, E], game([X, Y, Z, W, Q, E], _), List), flatten(List, L) , (member(A, L) , !).



% Qual número nunca foi sorteado? Encotrar os que falta na ordem missing
% Criei uma lista de listas com todos os elementos usando o findall, usei o flatten para tranformar em uma lista só e ordenei,
%então criei uma lista que contém todos os elementos e subtrai a lista gerada por uma lista com todos elementos, se a subtração
%retornar uma lista vazia é false, se não a lista dos não encontrados é printada. O is_empty verifico se qualquer coisa faz parte
%da lista caso faça é true e para a execução, se não false.
%Exemplo: never_sort(X). Lfinal = Lista com os não sorteados.
never_sort(Lfinal) :- findall([X, Y, Z, W, Q, E], game([X, Y, Z, W, Q, E], _), List), flatten(List, L), sort(L, LS), numlist(1, 60, Lall), 
                subtract(Lall, LS, Lfinal), is_empty(Lfinal).
is_empty(List):- member(_,List), !.

% O jogo (X1,X2,X3,X4,X5,X6) já foi contemplado alguma vez?
% Primeiramente cria-se uma lista de lista com todos os elementos utilizando-se o findall.
% Então, usa-se a cláusula "member" para verificar se os 6 números já foram escolhidos em alguns dos jogos
% Caso sejam, verifica também se ele já foi contemplado. Para isto, verifica-se se o número indicando suas contemplações é mais que zero
% Se for, o jogo já foi contemplado, caso contrário, ele não foi.
has_jogo_contemplado(X1, X2, X3, X4, X5, X6) :- findall([[X, Y, Z, W, Q, E], N1], game([X, Y, Z, W, Q, E], N1), List) , write(List) , 
                                                (member([[X1, X2, X3, X4, X5, X6], N2], List) , N2 > 0 , !).




% Algum jogo completo já foi contemplado mais de uma vez? Qual?
% Uso a função findall para printar todos os fatos e após feito isso chamo a função duplicate que verica se há 
%algum jogo duplicado na lista de fatos. Ele usa um para ir quebrando a lista em pedaços e depois vai verificando se enconta
%um elemento igual na duas partes da lista atrás da função member quando encontra printa. 
%Exemplo: game_sort_N(V, N). V = Jogo contemplado mais de 1 vez. N = Numero de vezes
game_sort_N(V, N) :- findall([X, Y, Z, W, Q, E, R], game([X, Y, Z, W, Q, E], R), L), aggregate(count,member(M,L),N), N > 1,
last(M, Last), Last > 0, delete(M, Last, V).

% Um número X foi sorteado quantas vezes?
% Uso a função findall para encontrar quantas vezes um numero foi sorteado em game e 
%após isso uso a função length para verificar o tamanho do array de resposta
%Exemplo: qtde_X(12, N). N = numero de vezes sorteado
qtde_X(X, N) :- findall(X, (game([X, _, _, _, _, _], _); game([_, X, _, _, _, _], _); game([_, _, X, _, _, _], _); 
        game([_, _, _, X, _, _], _); game([_, _, _, _, X, _], _); game([_, _, _, _, _, X], _)), L), length(L,N).

% Qual o número foi mais sorteado?
% Uso o findall para gerar uma lista de listas de todos os elementos existentes nos fatos e flatten para transformar essa lista em 
%uma lista unica. Por fim chama a max_element_count para contar e mostra qual é o elemento mais usado. A max_element_count chama uma
%função sencundaria element count que atras do aggregate mostra a quantidade todos os numeros usado, então também atraves da função 
%aggregate ele conta o numero maximo da resposta gerada pelo o element_count.
%game_sort_Q(N, X). N = Numero mais sorteado, X = Vezes que foi sorteado.
element_count(X,N,L) :- aggregate(count,member(X,L),N).
max_element_count(X,N,L) :- aggregate(max(N1,X1),element_count(X1,N1,L),max(N,X)).
game_sort_Q(R1, R2) :- findall([X, Y, Z, W, Q, E], game([X, Y, Z, W, Q, E], _), List), flatten(List, L), max_element_count(R1, R2, L).
