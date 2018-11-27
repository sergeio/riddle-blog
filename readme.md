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

<p align="center"><img alt="$$ \frac{1}{4} + \frac{2}{8} + \frac{3}{16} + \frac{4}{32} + \frac{5}{64} + \frac{6}{128} + \frac{7}{256} + \frac{8}{512} + \frac{9}{1024} = .99\ \mathrm{girls\ per\ family} $$" src="svgs/237f0c714ed9520af3d7038e551559d8.svg" align="middle" width="524.8122pt" height="32.9901pt"/></p>

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

<p align="center"><img alt="$$ \mathrm{boys\ per\ family} = S_{b} = \sum\limits_{n=1}^\infty \frac{1}{2^n} = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... $$" src="svgs/82ec63b44a1141a7cdd27542d87f3c00.svg" align="middle" width="353.3046pt" height="44.69883pt"/></p>

And here comes the magic.  We can multiply every term in the sequence by 1/2:

<p align="center"><img alt="$$ 2 \cdot S_{b} = \sum\limits_{n=0}^\infty \frac{1}{2^n} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... $$" src="svgs/985fe21125c26508e9480a1f6e88f971.svg" align="middle" width="268.0062pt" height="44.69883pt"/></p>

We can see that the nth element of <img alt="$S_{b}$" src="svgs/c4a75d21c4e375d513e6c8d7db547012.svg" align="middle" width="15.86079pt" height="22.46574pt"/> equals the (n+1)th element of
<img alt="$2 \cdot S_{b}$" src="svgs/953eed524506c9a1fef161f7a97489e0.svg" align="middle" width="35.952015pt" height="22.46574pt"/>.

And being a little clever, we eliminate all those pesky infinite terms:

<p align="center"><img alt="$$ 2 \cdot S_{b} - S_{b} = 1 + \frac{1}{2} - \frac{1}{2} + \frac{1}{4} - \frac{1}{4} + \frac{1}{8} - \frac{1}{8} + ... = 1 $$" src="svgs/fe01fd285b080a7198f5aad637d909fb.svg" align="middle" width="361.1454pt" height="32.9901pt"/></p>

<p align="center"><img alt="$$S_{b} = 1$$" src="svgs/69f709cece5a8c9da7288ebfe4a4fb49.svg" align="middle" width="46.819575pt" height="13.698597pt"/></p>

So now we're back where we started, with the added benefit of alienating some
people.  Let's keep going; maybe it'll be useful.

We can use the exact same reasoning as above to get a more general formula for
the sum of an infinite sum:

<p align="center"><img alt="$$ \sum\limits_{n=0}^\infty x^n = \frac{1}{1-x} $$" src="svgs/5804112b234b942dc2184f91669a6d00.svg" align="middle" width="107.448165pt" height="44.69883pt"/></p>

> so long as the series converges, it'll converge to this.

Now let's formalize the amount of girls in this country:

<p align="center"><img alt="$$ \mathrm{girls\ per\ family} = S_{g} = \sum\limits_{n=2}^\infty \frac{n}{2^n} = \frac{1}{4} + \frac{2}{8} + \frac{3}{16} + ... $$" src="svgs/fc41bf32a52515b5393b385ac4eb385d.svg" align="middle" width="360.3303pt" height="44.69883pt"/></p>

This sum has a slightly different form, so we can't use the general formula we
just came up with.  But, you might notice that <img alt="$\frac{d}{dx} x^n = n x^{n-1}$" src="svgs/30cf0c20cb6e6569c2bb27d7fea5bf20.svg" align="middle" width="100.745205pt" height="28.92648pt"/>,
which _does_ match the form of <img alt="$S_{g}$" src="svgs/76ec708901184af488b1203c510733ca.svg" align="middle" width="16.9059pt" height="22.46574pt"/>.

So let's follow that clue:

<p align="center"><img alt="$$ \sum\limits_{n=0}^\infty x^n = \frac{1}{1-x} $$" src="svgs/5804112b234b942dc2184f91669a6d00.svg" align="middle" width="107.448165pt" height="44.69883pt"/></p>
<p align="center"><img alt="$$ \frac{d}{dx} \sum\limits_{n=0}^\infty x^n = \frac{d}{dx} \frac{1}{1-x} $$" src="svgs/f165f54d8d32d9b3054535f7dee18798.svg" align="middle" width="152.007405pt" height="44.69883pt"/></p>
<p align="center"><img alt="$$ \sum\limits_{n=0}^\infty n x^{n-1} = \frac{1}{(x-1)^2} $$" src="svgs/4346fd43032207a3545bc2126f1e63ad.svg" align="middle" width="154.3014pt" height="44.69883pt"/></p>

And shuffling some things around:

<p align="center"><img alt="$$ S_{g} = 1 $$" src="svgs/08ca43336175c9f6bb34139b3df7e938.svg" align="middle" width="47.864685pt" height="15.93603pt"/></p>

So here we are.  We've been good.  We didn't just take formulas from an oracle
and plug things in; we derived them.  I feel confident that the answer is
correct, and that I would get a ✓ if this were math homework.  Still, doing all
this symbol manipulation brings me no intuitive satisfaction as to _why_ or
_how_ those two infinite sequences converge to the same value.

Let's try something less fancy.


But why? How? (Round 2)
-----------------------

Test

<img alt="$ \fraction{1}{4} $" src="svgs/39d6d090ff091f9d21016d4901bd98ff.svg" align="middle" width="16.438455pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{8} + \fraction{1}{8} = \fraction{1}{4} $" src="svgs/0fd4c213fcd61c0dcedf6f8feefec458.svg" align="middle" width="91.3242pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{8} + \fraction{1}{16} $" src="svgs/45eeb59c49ac9838db86ce0877f3d1d2.svg" align="middle" width="61.18728pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{16} + \fraction{1}{32} + \fraction{1}{32} = \fraction{1}{8} $" src="svgs/93b71f96157b65defd74604ebcb0c488.svg" align="middle" width="152.511315pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{16} + \fraction{1}{64} $" src="svgs/2da600fec7bc9426411e536a40b122d1.svg" align="middle" width="69.406425pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{32} + \fraction{1}{128} + \fraction{1}{128} = \fraction{1}{32} + \fraction{1}{64} $" src="svgs/ebf73e9a59c81700cdee2daa161ce2ef.svg" align="middle" width="221.917905pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{64} + \fraction{1}{128} + \fraction{1}{256} $" src="svgs/8d17e11bf93701b6217f5280561603ff.svg" align="middle" width="130.593705pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{128} + \fraction{1}{256} + \fraction{1}{512} + \fraction{1}{512} = \fraction{1}{64} $" src="svgs/eb946fdbea4ced05b86f1f05384ea4f3.svg" align="middle" width="238.356855pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{128} + \fraction{1}{1024} $" src="svgs/f106c199b167d93db535b50c67b73d5b.svg" align="middle" width="94.06419pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{256} + \fraction{1}{2048} + \fraction{1}{2048} = \fraction{1}{256} + \fraction{1}{1024} $" src="svgs/f7b195a4f4256a07d6e406a7b58227a4.svg" align="middle" width="271.233105pt" height="21.18732pt"/>
<img alt="$ \fraction{1}{512} + \fraction{1}{2048} + \fraction{1}{4096} $" src="svgs/05bdb31d93e6fbe701597c007ccfcf3a.svg" align="middle" width="155.251305pt" height="21.18732pt"/>


Thank You
---------
... to [leegao/readme2tex], because github doesn't natively support latex in
readmes.

[riddle]: https://quomodocumque.wordpress.com/2011/01/10/the-google-puzzle-and-the-perils-of-averaging-ratios/
[leegao/readme2tex]: https://github.com/leegao/readme2tex


