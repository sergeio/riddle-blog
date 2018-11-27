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

<p align="center"><img alt="$$ \frac{1}{4} + \frac{2}{8} + \frac{3}{16} + \frac{4}{32} + \frac{5}{64} + \frac{6}{128} + \frac{7}{256} + \frac{8}{512} + \frac{9}{1024} = .99 girls/fam $$" src="svgs/64912ade791bb3255eea3920db3eb4ee.svg" align="middle" width="485.8491pt" height="32.9901pt"/></p>

Whoa!  They're making a comeback, and we're only 9 terms into this infinite
sum.  I renounce my intuition and would now guess that somehow, the amount of
girls precisely equals the amount of boys in the country.  Well, on average.


But why? How?
-------------

Since we're here, this seems like a reasonable time to stop guessing and
approximating, and "do math".

The amount of boys per family is 1 by definition, but since we're doing math,
and we wouldn't want someone to accidentally understand us -- I mean, how then
would we derive our sense of self-worth? -- let us obfuscate:

<p align="center"><img alt="$$ boys per family = S_{b}(n) = \sum\limits_{n=1}^\infty \frac{1}{2^n} = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... $$" src="svgs/e8932725786aea573106ed38b650b2a8.svg" align="middle" width="371.8308pt" height="44.69883pt"/></p>

And here comes the magic.  We can multiply every term in the sequence by 1/2:
<p align="center"><img alt="$$ 2 \cdot S_{b}(n) = \sum\limits_{n=0}^\infty \frac{1}{2^n} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... $$" src="svgs/920527dff6b7df80d3e007343f3e6962.svg" align="middle" width="290.65905pt" height="44.69883pt"/></p>

We can see that the nth element of <img alt="$S_{b}(n)$" src="svgs/524a91476d58c91811ce94f302e83099.svg" align="middle" width="39.33501pt" height="24.6576pt"/> equals the (n+1)th element of
<img alt="$2 \cdot S_{b}(n)$" src="svgs/be7c2f1cfe8d61e254cd709dd2078450.svg" align="middle" width="59.426235pt" height="24.6576pt"/>.

And being a little clever, we eliminate all those pesky infinite terms:
<p align="center"><img alt="$$ 2 \cdot S_{b}(n) - S_{b}(n) = 1 + \frac{1}{2} - \frac{1}{2} + \frac{1}{4} - \frac{1}{4} + \frac{1}{8} - \frac{1}{8} + ... = 1 $$" src="svgs/525251e7b095f7b750a749582d537ae5.svg" align="middle" width="406.44945pt" height="32.9901pt"/></p>

<p align="center"><img alt="$$S_{b}(n) = 1$$" src="svgs/4c4ccc9f2de2ad744a0b34270f627a0c.svg" align="middle" width="69.471765pt" height="16.438356pt"/></p>




<img alt="$E = \frac{mc^2}{\sqrt{1-\frac{v^2}{c^2}}}$" src="svgs/bd03775d716dc07295041dad665bb7bc.svg" align="middle" width="83.313285pt" height="36.29604pt"/>

another one

<p align="center"><img alt="$$$$" src="svgs/f1fd19f04d53a15bbc21f4179282c5d5.svg" align="middle" width="0.0pt" height="0.0pt"/></p>

<p align="center"><img alt="$$\sum\limits_{n=2}^\infty \frac{n}{2^n} $$" src="svgs/37d30664d7eea87fa863b1116c16f402.svg" align="middle" width="46.649295pt" height="44.69883pt"/></p>



boys per family = 1

Similarly,

girls per family = sum(n/(2^(n+1))) for n = (1, infinity)
girls per family = 1/2 * sum(n/(2^n)) for n = (1, infinity)


[riddle]: https://quomodocumque.wordpress.com/2011/01/10/the-google-puzzle-and-the-perils-of-averaging-ratios/
