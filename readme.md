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

Let's try looking at the values of <img alt="$ f(n) = \frac{n}{2^n} $" src="svgs/7064a75d9914205d6af48b46a08ac6e5.svg" align="middle" width="70.973925pt" height="24.6576pt"/> for n = 2, 3,..

If we think about it, we can show that each term
<img alt="$ f(n) = \frac{f(n-1)}{2} + \frac{1}{2^n} $" src="svgs/a2f7e337fef90a35244afeab47f7f71f.svg" align="middle" width="137.9367pt" height="33.20559pt"/>

So that's how I'll calculate each line below: take the previous line, divide
by 2, and add the next power of 1/2:

<img alt="$ \frac{1}{4} $" src="svgs/a01ae6d9e2cde028961d1d3790596f76.svg" align="middle" width="6.552645pt" height="27.77577pt"/>
<img alt="$ \frac{1}{8} + \frac{1}{8} = \frac{1}{4} $" src="svgs/4ef4cec6052018c5a3be4f93515f3f76.svg" align="middle" width="69.556905pt" height="27.77577pt"/>
<img alt="$ \frac{1}{8} + \frac{1}{16} $" src="svgs/f589ba46bddb6f6ae209e3073b17a75d.svg" align="middle" width="43.694145pt" height="27.77577pt"/>
<img alt="$ \frac{1}{16} + \frac{1}{32} + \frac{1}{32} = \frac{1}{8} $" src="svgs/dbf713a664e947656c4548c25b8d852d.svg" align="middle" width="119.80353pt" height="27.77577pt"/>
<img alt="$ \frac{1}{16} + \frac{1}{64} $" src="svgs/37e06f17f2c4090984bcb2c2646e0452.svg" align="middle" width="50.246625pt" height="27.77577pt"/>
<img alt="$ \frac{1}{32} + \frac{1}{128} + \frac{1}{128} = \frac{1}{32} + \frac{1}{64} $" src="svgs/0b319c817ea2c41e1a1788066b0b1581.svg" align="middle" width="176.60313pt" height="27.77577pt"/>
<img alt="$ \frac{1}{64} + \frac{1}{128} + \frac{1}{256} $" src="svgs/fd7412447fb69e5e193f9c071edb42a2.svg" align="middle" width="100.49325pt" height="27.77577pt"/>
<img alt="$ \frac{1}{128} + \frac{1}{256} + \frac{1}{512} + \frac{1}{512} = \frac{1}{64} $" src="svgs/ad496a8aca9b553ff0e5fe86ae7aa360.svg" align="middle" width="189.70743pt" height="27.77577pt"/>
<img alt="$ \frac{1}{128} + \frac{1}{1024} $" src="svgs/a0605559efbdf8ea8ea6228c494b9ae1.svg" align="middle" width="69.90423pt" height="27.77577pt"/>
<img alt="$ \frac{1}{256} + \frac{1}{2048} + \frac{1}{2048} = \frac{1}{256} + \frac{1}{1024} $" src="svgs/8d09c62db74e97e2c88980e160a0b878.svg" align="middle" width="215.91768pt" height="27.77577pt"/>
<img alt="$ \frac{1}{512} + \frac{1}{2048} + \frac{1}{4096} $" src="svgs/0866a0f9670a2d772387f381a8a96dbb.svg" align="middle" width="120.150855pt" height="27.77577pt"/>

And now we stare.

Somehow when we sum all the lines together, (in the reduced form) there are
exactly 2 <img alt="$\frac{1}{4}$" src="svgs/56ea6e9aad5379d31310f1b27831a265.svg" align="middle" width="6.552645pt" height="27.77577pt"/>s, adding up to <img alt="$\frac{1}{2}$" src="svgs/47d54de4e337a06266c0e1d22c9b417b.svg" align="middle" width="6.552645pt" height="27.77577pt"/>, 2 <img alt="$\frac{1}{8}$" src="svgs/9d1730c1a86e4200a94d2cdc3c0ce16b.svg" align="middle" width="6.552645pt" height="27.77577pt"/>s, adding
up to <img alt="$\frac{1}{4}$" src="svgs/56ea6e9aad5379d31310f1b27831a265.svg" align="middle" width="6.552645pt" height="27.77577pt"/>, 2 <img alt="$\frac{1}{16}$" src="svgs/98709d8535132dfcec87760d6670b180.svg" align="middle" width="13.105125pt" height="27.77577pt"/>s, 1 <img alt="$\frac{1}{32}$" src="svgs/14e3e7a756f90321fd697daf02511579.svg" align="middle" width="13.105125pt" height="27.77577pt"/>, but 3 <img alt="$\frac{1}{64}$" src="svgs/756e354024ac13b6afedaa3474c46428.svg" align="middle" width="13.105125pt" height="27.77577pt"/>s
to make up for it.

I see how this is mimicing <img alt="$\sum\limits_{n=2}^\infty \frac{1}{2^n}$" src="svgs/197559dff969f5df6ceecf196eb555b1.svg" align="middle" width="44.096085pt" height="41.14176pt"/>, and I get
another little kick of dopamine from my brain, having somehow connected two
seemingly unconnected things.  But for all that, I just don't see the pattern.
I see that it works, but I don't understand why it must.

But why? How? (Round 3)
-----------------------

Let's draw.


Thank You
---------
... to [leegao/readme2tex], because github doesn't natively support latex in
readmes.

[riddle]: https://quomodocumque.wordpress.com/2011/01/10/the-google-puzzle-and-the-perils-of-averaging-ratios/
[leegao/readme2tex]: https://github.com/leegao/readme2tex


