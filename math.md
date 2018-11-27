I recently came across a [riddle]:

> There’s a certain country where everybody wants to have a son. Therefore each
> couple keeps having children until they have a boy; then they stop.  What
> fraction of the population is female?


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

$$ \frac{1}{4} + \frac{2}{8} + \frac{3}{16} + \frac{4}{32} + \frac{5}{64} + \frac{6}{128} + \frac{7}{256} + \frac{8}{512} + \frac{9}{1024} = .99\ \mathrm{girls\ per\ family} $$

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

$$ \mathrm{boys\ per\ family} = S_{b} = \sum\limits_{n=1}^\infty \frac{1}{2^n} = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... $$

And here comes the magic.  We can multiply every term in the sequence by 1/2:

$$ 2 \cdot S_{b} = \sum\limits_{n=0}^\infty \frac{1}{2^n} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... $$

We can see that the nth element of $S_{b}$ equals the (n+1)th element of
$2 \cdot S_{b}$.

And being a little clever, we eliminate all those pesky infinite terms:

$$ 2 \cdot S_{b} - S_{b} = 1 + \frac{1}{2} - \frac{1}{2} + \frac{1}{4} - \frac{1}{4} + \frac{1}{8} - \frac{1}{8} + ... = 1 $$

$$S_{b} = 1$$

So now we're back where we started, with the added benefit of alienating some
people.  Let's keep going; maybe it'll be useful.

We can use the exact same reasoning as above to get a more general formula for
the sum of an infinite sum:

$$ \sum\limits_{n=0}^\infty x^n = \frac{1}{1-x} $$

> so long as the series converges, it'll converge to this.

Now let's formalize the amount of girls in this country:

$$ \mathrm{girls\ per\ family} = S_{g} = \sum\limits_{n=2}^\infty \frac{n}{2^n} = \frac{1}{4} + \frac{2}{8} + \frac{3}{16} + ... $$

This sum has a slightly different form, so we can't use the general formula we
just came up with.  But, you might notice that $\frac{d}{dx} x^n = n x^{n-1}$,
which _does_ match the form of $S_{g}$.

So let's follow that clue:

$$ \sum\limits_{n=0}^\infty x^n = \frac{1}{1-x} $$
$$ \frac{d}{dx} \sum\limits_{n=0}^\infty x^n = \frac{d}{dx} \frac{1}{1-x} $$
$$ \sum\limits_{n=0}^\infty n x^{n-1} = \frac{1}{(x-1)^2} $$

And shuffling some things around:

$$ S_{g} = 1 $$

So here we are.  We've been good.  We didn't just take formulas from an oracle
and plug things in; we derived them.  I feel confident that the answer is
correct, and that I would get a ✓ if this were math homework.  Still, doing all
this symbol manipulation brings me no intuitive satisfaction as to _why_ or
_how_ those two infinite sequences converge to the same value.

Let's try something less fancy.


But why? How? (Round 2)
-----------------------

Test

$ \frac{1}{4} $
$ \frac{1}{8} + \frac{1}{8} = \frac{1}{4} $
$ \frac{1}{8} + \frac{1}{16} $
$ \frac{1}{16} + \frac{1}{32} + \frac{1}{32} = \frac{1}{8} $
$ \frac{1}{16} + \frac{1}{64} $
$ \frac{1}{32} + \frac{1}{128} + \frac{1}{128} = \frac{1}{32} + \frac{1}{64} $
$ \frac{1}{64} + \frac{1}{128} + \frac{1}{256} $
$ \frac{1}{128} + \frac{1}{256} + \frac{1}{512} + \frac{1}{512} = \frac{1}{64} $
$ \frac{1}{128} + \frac{1}{1024} $
$ \frac{1}{256} + \frac{1}{2048} + \frac{1}{2048} = \frac{1}{256} + \frac{1}{1024} $
$ \frac{1}{512} + \frac{1}{2048} + \frac{1}{4096} $


Thank You
---------
... to [leegao/readme2tex], because github doesn't natively support latex in
readmes.

[riddle]: https://quomodocumque.wordpress.com/2011/01/10/the-google-puzzle-and-the-perils-of-averaging-ratios/
[leegao/readme2tex]: https://github.com/leegao/readme2tex


