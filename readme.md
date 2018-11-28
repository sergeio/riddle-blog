I recently came across a [riddle]:

> There’s a certain country where everybody wants to have a son. Therefore each
> couple keeps having children until they have a boy; then they stop.  What
> fraction of the population is female?


Guess and test
--------------

It immediately tickled me.  Just the notion that I apparently have enough
information to answer the question is neat.  I'd have expected more rules.

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

Next up, I'd approximate the answer with a calculator.  Since all families have
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

And here comes the magic.  We can multiply every term in the sequence by 2:

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

Let's try looking at the values of <img alt="$ f(n) = \frac{n}{2^n} $" src="svgs/7064a75d9914205d6af48b46a08ac6e5.svg" align="middle" width="70.973925pt" height="24.6576pt"/>.  Remember that
<img alt="$ S_{g} = \sum\limits_{n=2}^\infty \frac{n}{2^n} = \sum\limits_{n=2}^\infty f(n) $" src="svgs/d283109e471a27784ba84f8a966efea8.svg" align="middle" width="167.611455pt" height="41.14176pt"/>

If we think about it, we can show that each term
<img alt="$ f(n) = \frac{f(n-1)}{2} + \frac{1}{2^n} $" src="svgs/a2f7e337fef90a35244afeab47f7f71f.svg" align="middle" width="137.9367pt" height="33.20559pt"/>

So that's how I'll calculate each line below: take the previous line, divide
by 2, and add the next power of 1/2:

<img alt="$ f(2) = \frac{1}{4} $" src="svgs/34932512ed36f249e3c73ce1498145f1.svg" align="middle" width="61.26483pt" height="27.77577pt"/>
<img alt="$ f(3) = \frac{1}{8} + \frac{1}{8} = \frac{1}{4} $" src="svgs/3549ec4a11c92577d2d68525627803cd.svg" align="middle" width="124.269255pt" height="27.77577pt"/>
<img alt="$ f(4) = \frac{1}{8} + \frac{1}{16} $" src="svgs/47927f60265f8a30ee7b249699e18b5a.svg" align="middle" width="98.40633pt" height="27.77577pt"/>
<img alt="$ f(5) = \frac{1}{16} + \frac{1}{32} + \frac{1}{32} = \frac{1}{8} $" src="svgs/0500581bf8c1f7842b12b557dfbd08d9.svg" align="middle" width="174.515055pt" height="27.77577pt"/>
<img alt="$ f(6) = \frac{1}{16} + \frac{1}{64} $" src="svgs/7edd375b8435dcede3b204968ea6f1c2.svg" align="middle" width="104.958975pt" height="27.77577pt"/>
<img alt="$ f(7) = \frac{1}{32} + \frac{1}{128} + \frac{1}{128} = \frac{1}{32} + \frac{1}{64} $" src="svgs/f65c40a7cfc3606ff57b6355c9864e92.svg" align="middle" width="231.314655pt" height="27.77577pt"/>
<img alt="$ f(8) = \frac{1}{64} + \frac{1}{128} + \frac{1}{256} $" src="svgs/d15041132d55e13e2a631b580f8ec698.svg" align="middle" width="155.205435pt" height="27.77577pt"/>
<img alt="$ f(9) = \frac{1}{128} + \frac{1}{256} + \frac{1}{512} + \frac{1}{512} = \frac{1}{64} $" src="svgs/04421e642c94b250d8abf5ac561212b9.svg" align="middle" width="244.420605pt" height="27.77577pt"/>
<img alt="$ f(10) = \frac{1}{128} + \frac{1}{1024} $" src="svgs/d5889c09da81f9081d6cf351f60c0c8d.svg" align="middle" width="132.835725pt" height="27.77577pt"/>

And now we stare.

Somehow when we sum all the lines together, (in the reduced form) there are
exactly two 1/4s, adding up to 1/2, two 1/8s, adding up to 1/4, two 1/16s, just
one 1/32, but three 1/64s to make up for it.

I see how this is mimicking <img alt="$\sum\limits_{n=1}^\infty \frac{1}{2^n}$" src="svgs/b3c22d2be0ea06d07531028973594abb.svg" align="middle" width="44.096085pt" height="41.14176pt"/>, and I get
another little kick of dopamine from my brain, having somehow connected two
seemingly unconnected things.  But for all that, I just don't see the pattern.
I see that it works, but I don't understand why it must.


But why? How? (Round 3)
-----------------------

Let's just start drawing things?

I began drawing by hand, but quickly ran into the limits of my ability to
draw straight lines.  So, not unlike Donald Knuth, I made [playbox] to generate
the box images below.

### Starting basic

As before, let's calibrate this tool on something relatively simple (population
of boys), before we move on to the more advanced.

Recall that the number of boys per family can be expressed as
<img alt="$ \sum\limits_{n=1}^\infty \frac{1}{2^n} = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... $" src="svgs/30f4e27c2a6736e4c2ec8863a4d04fc8.svg" align="middle" width="173.452455pt" height="41.14176pt"/>
So if we were to draw a square, we could show it filling up by shading in 1/2
of it, then another 1/4, then 1/8, and so on:

<img src="images/one-half^n-i1.svg" width="512" height="512">

Each subsequent box has half the height of the previous, hence half the area.
And still, we see the box filling up to the point that drawing additional boxes
is difficult even with computer assistance.

Here's another equally valid way to visualize
<img alt="$ \sum\limits_{n=1}^\infty \frac{1}{2^n} $" src="svgs/dd8b88355ca8c6ec10f0e38bacc69fb3.svg" align="middle" width="44.096085pt" height="41.14176pt"/>:

<img src="images/one-half^n-i2.svg" width="512" height="512">

Here, we alternating halving the height and then width of the subsequent boxes,
but the effect is the same:  the whole box is filled with color, and we can
wave our hands and claim this means the sum of the series approaches 1.

### Something a teeny bit different

Let's try visualizing an infinite sum that doesn't converge to 1.  That is to
say, something that won't fill the box up all the way:
<img alt="$ S_{q} = \sum\limits_{n=1}^\infty \frac{1}{4^n} $" src="svgs/183f048910dbdf6127bacf5ec6ab5ca5.svg" align="middle" width="83.35338pt" height="41.14176pt"/>

Now we'll want each subsequent box to have 1/4 the area of the preceding one.

<img src="images/one-fourth^n-bottom.svg" width="512" height="512">

I'm not totally sure what to make of that, and I think we could make a prettier
visualization.  Let's try:

<img src="images/one-fourth^n-middle.svg" width="512" height="512">

At this point, I notice that besides being prettier, this second visualization
of our series is a perfect complement to our first one.  Well, almost perfect.
We'd need a third to completely fill up the box.

<img src="images/one-fourth^n-all.svg" width="512" height="512">

Each of the three colors in the above image represents our sum
<img alt="$ S_{q} = \sum\limits_{n=1}^\infty \frac{1}{4^n} $" src="svgs/183f048910dbdf6127bacf5ec6ab5ca5.svg" align="middle" width="83.35338pt" height="41.14176pt"/>.

And 3 of them fill up the box: <img alt="$ 3 \cdot S_{q} = 1 $" src="svgs/97bd8160f6a5edae549da9a5f180cae4.svg" align="middle" width="67.56783pt" height="22.46574pt"/>.

Therefore <img alt="$ S_{q} = \frac{1}{3} $" src="svgs/0fae6ed3c0ccff59ab9efc80cd648824.svg" align="middle" width="47.782515pt" height="27.77577pt"/>.

My intuition is appeased.  This makes sense.

### Another way

Before we move on, there's another intuitive way to show that
<img alt="$ S_{q} = \frac{1}{3} $" src="svgs/0fae6ed3c0ccff59ab9efc80cd648824.svg" align="middle" width="47.782515pt" height="27.77577pt"/>.

<img src="images/one-fourth^n-middle.svg" width="512" height="512">

Because the images we are using to visualize are self-similar, we can do a
little bit of magic on them.  Notice that the bottom-right quarter of the above
image (and, of each of our other visualizations of <img alt="$ S_{q} $" src="svgs/4f845ae6692add53e6133769b4f7a66b.svg" align="middle" width="16.51782pt" height="22.46574pt"/>) has exactly the
same shape as the whole square, just shrunk by a factor of 4.  In fact, we
could refer to the bottom-right quarter as <img alt="$ \frac{1}{4} S_{q} $" src="svgs/627e7696248f73d31e149a4640dd67b6.svg" align="middle" width="25.04304pt" height="27.77577pt"/>.

Once we've done that, we can get rid of all those infinite boxes.  If we
subtract the areas shaded in the bottom-right quarter from the whole square,
the only thing left shaded is the top-right quarter.  Its area is 1/4.

<p align="center"><img alt="$$ S_{q} - \frac{1}{4} S_{q} = \frac{1}{4} $$" src="svgs/35ff1976a2e671869a8e7b167de62071.svg" align="middle" width="99.044385pt" height="32.9901pt"/></p>
<p align="center"><img alt="$$ \frac{3}{4} S_{q} = \frac{1}{4} $$" src="svgs/0e190f05c1dd44dec75aba956c5e9111.svg" align="middle" width="59.6409pt" height="32.9901pt"/></p>
<p align="center"><img alt="$$ S_{q} = \frac{1}{3} $$" src="svgs/d39e1469ef6b64c7985b2f523c4901b9.svg" align="middle" width="49.449015pt" height="32.9901pt"/></p>

This is a visual representation of the "magic" we performed in the first
[But why? How?](#but-why-how-round-3) section.

# The main event

But enough diversions.  We are here to figure out why / how
<img alt="$ S_{g} = \sum\limits_{n=2}^\infty \frac{n}{2^n} = \frac{1}{4} + \frac{2}{8} + \frac{3}{16} + ... = 1 $" src="svgs/651f99477584f1a8ec85d8208476c67c.svg" align="middle" width="249.786405pt" height="41.14176pt"/>

So let's draw it:

<img src="images/n-over-2^n.svg" width="512" height="512">

It's pretty.  And it seems to be filling up the box?  Well, except for that
top-right corner.  What's going on there?

The shape doesn't have any obvious complements, so we can't rely on the method
we found in [Something a teeny bit different](#something-a-teeny-bit-different).
But it is self-similar!

Just as in [Another way](#another-way), we can see say that the top-right
quarter of our box is exactly the same as the entire box, just shrunk by a
factor of 4.  And the top-left quarter looks just like
<img alt="$ \sum\limits_{n=1}^\infty \frac{1}{2^n} $" src="svgs/dd8b88355ca8c6ec10f0e38bacc69fb3.svg" align="middle" width="44.096085pt" height="41.14176pt"/>, (which we've alrady shown to equal
1) shrunk by a factor of 4.  Miracles!

The bottom-right quarter is exactly the same as the top-left, just rotated 90
degrees clockwise.

The last bottom-left quarter is shaded in completely, so its area is 1/4.

This should be enough.  Let's obfuscate!

The entire box <img alt="$ S_{g} $" src="svgs/1ca5dd82ed7a72b3b4fee71c09ac4308.svg" align="middle" width="16.9059pt" height="22.46574pt"/> is made up of 4 quarters:

<img alt="$ \mathrm{topleft} = \frac{1}{4}(\sum\limits_{n=1}^\infty \frac{1}{2^n}) $" src="svgs/2c7e6dc68dd5e7bd283ef4ed51ebcd59.svg" align="middle" width="138.30168pt" height="41.14176pt"/>
<img alt="$ \mathrm{topright} = \frac{1}{4} S_{g} $" src="svgs/352faded64d87db0fa814b9137a109db.svg" align="middle" width="107.358075pt" height="27.77577pt"/>
<img alt="$ \mathrm{bottomleft} = \frac{1}{4} $" src="svgs/6c741bb14929e7b6b48058b890eb0581.svg" align="middle" width="106.24218pt" height="27.77577pt"/>
<img alt="$ \mathrm{bottomright} = \frac{1}{4}(\sum\limits_{n=1}^\infty \frac{1}{2^n}) $" src="svgs/97c0f70dc554b1765c798bc750508835.svg" align="middle" width="178.074105pt" height="41.14176pt"/>

And they sum up to <img alt="$ S_{g} $" src="svgs/1ca5dd82ed7a72b3b4fee71c09ac4308.svg" align="middle" width="16.9059pt" height="22.46574pt"/>:

<img alt="$ S_{g} = \frac{1}{4} + \frac{1}{4}(\sum\limits_{n=1}^\infty \frac{1}{2^n}) + \frac{1}{4}(\sum\limits_{n=1}^\infty \frac{1}{2^n}) + \frac{1}{4} S_{g} $" src="svgs/1e615cb1a48b6398c150efb6f4496e3c.svg" align="middle" width="276.524655pt" height="41.14176pt"/>
<img alt="$ \frac{3}{4} S_{g} = \frac{1}{4} + \frac{1}{2}(\sum\limits_{n=1}^\infty \frac{1}{2^n}) = \frac{3}{4} $" src="svgs/6c42dd20b31959bd6570ed10813ac4e4.svg" align="middle" width="178.55343pt" height="41.14176pt"/>
<img alt="$ S_{g} = 1 $" src="svgs/0b70777b9f51077b5ac4caf1d6a5bd88.svg" align="middle" width="47.864685pt" height="22.46574pt"/>

🎉🎉🎉🎉 We did it!  We drew a picture.  And it turned out to be made of parts
that were either infinite sums whose values we'd already calculated, or itself
shrunken down.

Now I can stare at this picture and say "Well, that quarter is fully shaded, so
I know its value.  These two quarters are clearly converging to filling up each
of their quarters, and this last one is self-similar to the whole square".

<img src="images/n-over-2^n.svg" width="512" height="512">

I am still delighted by the fact that the amount of girls on-average equals the
amount of boys in that strange country that is unsuccessfully discriminating
against girls.  But now I feel like I kind of understand how it happens.


Epilogue
--------

There's a lot we didn't cover here.  Like why does the top-right corner have so
much more unshaded space than previous visualizations?  Does the answer to this
question [depend](https://mathoverflow.net/a/17963) on the population of the
country?  What about the case where families have conceived girls, but hadn't
gotten to a boy?  (I'd say that the main reason mathematicians find this
[riddle] so contentious is this detail).

But sometimes we have to be content with what is, and not dwell on what isn't.

Thanks for reading!


Thank You
---------
... to [leegao/readme2tex], because github doesn't natively support latex in
readmes.


[riddle]: https://quomodocumque.wordpress.com/2011/01/10/the-google-puzzle-and-the-perils-of-averaging-ratios/
[playbox]: https://github.com/sergeio/playbox
[leegao/readme2tex]: https://github.com/leegao/readme2tex
