I recently came across a [riddle]:

    There’s a certain country where everybody wants to have a son. Therefore
    each couple keeps having children until they have a boy; then they stop.
    What fraction of the population is female?


Guess and test
--------------

It immediately tickled me.  Just the notion that I apparently have enough
information to answer the question surprises me.

Maybe the wording "everybody wants to have a son" biased me, but I was pretty
sure that such a country would have more sons than daughters.  But I was also
skeptical of my intuition, since Ellenberg's bread and butter is making you
confident you understand something, and then pulling the rug out from under
you.  He's basically a bully, but we all have Stockholm syndrome.

So let's do some mental napkin math: there's 100 families in this country.  50
of them will have a boy and no girls.  Another 25 will have one of each.  And
there we are: 75 boys to 25 girls, and only 25 families left to consider, and
all of them will have boys too.  It seems difficult for the girls to make a
comeback.  That's the feeling.

Next up, I'd approximate the answer with a simulation.  Since all families have
a boy (it seems like people generally ignore the possibility of families that
have daughters, but haven't yet conceived a son), we can say that there is 1
boy per family.  Look at us.  We're doing math.  Girls are a tiny bit more
complicated.  One quarter of families have one girl, an eighth have two girls,
and so on.

1/4 + 2/8 + 3/16 + 4/32 + 5/64 + 6/128 + 7/256 + 8/512 + 9/1024 = .99 girls/fam

Whoa!  They're making a comeback, and we're only 9 terms into this infinite
sum.  I renounce my intuition and would now guess that somehow, the amount of
girls precisely equals the amount of boys in the country.  Well, on average.


But why? How?
-------------

since we're here, this seems like a reasonable time to stop guessing and
approximating, and "do math".

The amount of boys per family is 1 by definition, but since we're doing math,
and we wouldn't want someone to accidentally understand us -- I mean, how then
would we derive our sense of self-worth? -- let us obfuscate:

boys/family = Sb(n) = sum(.5^n) for n in (1, infinity) = 1/2 + 1/4 + 1/8 + ...

And here comes the magic.  We can multiply every term in the sequence by 1/2:
2 * Sb(n) = sum(.5^n) for n in (0, infinity) = 1 + 1/2 + 1/4 + 1/8 + ...
<img alt="$2 * Sb(n) = sum(.5^n) for n in (0, infinity) = 1 + 1/2 + 1/4 + 1/8 + ...$" src="svgs/e03ffa0c1c47c9b6cf40b00ff897ed7c.svg?invert_in_darkmode" align="middle" width="491.128605pt" height="24.6576pt"/>

We can see that the nth element of Sb(n) equals the (n+1)th element of
2 * Sb(n).

And being a little clever, we eliminate all those pesky infinite terms:
2 * Sb(n) - Sb(n) = 1 + 1/2 - 1/2 + 1/4 - 1/4 + 1/8 - 1/8 + ... = 1
Sb(n) = 1




<img alt="$E = \frac{mc^2}{\sqrt{1-\frac{v^2}{c^2}}}$" src="svgs/bd03775d716dc07295041dad665bb7bc.svg?invert_in_darkmode" align="middle" width="83.313285pt" height="36.29604pt"/>

another one

<p align="center"><img alt="$$\sum\limits_{n=1}^\infty \frac{1}{2^n} $$" src="svgs/c30f5d7a05b80c41ecd23d4109765b9a.svg?invert_in_darkmode" align="middle" width="46.649295pt" height="44.69883pt"/></p>



boys per family = 1

Similarly,

girls per family = sum(n/(2^(n+1))) for n = (1, infinity)
girls per family = 1/2 * sum(n/(2^n)) for n = (1, infinity)


[riddle]: https://quomodocumque.wordpress.com/2011/01/10/the-google-puzzle-and-the-perils-of-averaging-ratios/
