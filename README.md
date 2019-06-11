
## Como usar?
Necessário python 3.7.2

Para rodar o programa:

`$ python3 main.py <nomedoarquivo>.json>`

Na pasta [Automatos](/Automatos) possuem exemplos para testar.

`$ python3 main.py Automatos/input_1.json`

Nesta mesma pasta possui um arquivo [modelo](/Automatos/modelo.json) para facilitar a criacao de novos automatos.

#### ⚠️ Atenção as letras usadas nos nomes dos estados nao poderão ser usadas como transição  ⚠️
#### Ex.(❌Estado ["A1"] transição["a"] ❌)

Após a execução a saida deverá ser parecida com isso:

~~~~
$ python main.py Automatos/input_2.json
Começando pelo estado final <s1> :
        g(<s1>,a) = $
        g(<s1>,b) = <s0|s1>
Um novo estado apareceu,entao vamos mapear <s0|s1> :
        g(<s0|s1>,a) = $
        g(<s0|s1>,b) = <s0|s1|s2>
Um novo estado apareceu,entao vamos mapear <s0|s1|s2> :
        g(<s0|s1|s2>,a) = <s0|s1|s2>
        g(<s0|s1|s2>,b) = <s0|s1|s2>
Não ocorreu mais nenhum estado novo
Juntando as esquações equivalentes chegamos em:`
Juntando as esquações equivalentes chegamos em:
=========================================================
<s0|s1|s2>=<s0|s1|s2>a+<s0|s1|s2>b+$
<s0|s1>=<s0|s1|s2>b+$
<s1>=<s0|s1>b
=========================================================

Simplificando a equacao <s0|s1|s2>=<s0|s1|s2>a+<s0|s1|s2>b+$
        Obtemos: <s0|s1|s2>=$+<s0|s1|s2>(a+b)
        Aplicando Arden a equacao <s0|s1|s2>=$+<s0|s1|s2>(a+b)
        Obtemos: <s0|s1|s2>=(a+b)*
Substituindo <s0|s1|s2> em <s0|s1>:
        <s0|s1|s2>=(a+b)*
        <s0|s1>=<s0|s1|s2>b+$
        <s0|s1>=(a+b)*b+$
Substituindo <s0|s1> em <s1>:
        <s0|s1>=(a+b)*b+$
        <s1>=<s0|s1>b
        <s1>=(a+b)*bb+b
Logo como não possuem mais vaiaveis a serem substituidas.
Nossa expressao regular para este AFD é equivalente à:
(a+b)*bb+b`
~~~~

