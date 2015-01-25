---
layout: post
title: Golden Ratio and Fibonacci Numbers
category: math
tags: golden_ratio, Fibonacci, series
---

Pretty much everybody heard about the golden ratio, and if you are a little
math-inclined or still remember something from school, you may have heard 
the Fibonacci numbers too. That is, 0, 1, 1, 2, 3, 5, 8, 13, 21, etc, where
each number in the sequence is the sum of the previous two numbers,
$$f_n = f_{n-1} + f_{n-2}$$. The golden ratio and the Fibonacci numbers
are related. As the sequence goes on, the ratio of the adjacent numbers
approaches the golden ratio, i.e., 
$$
\lim_{n\to \infty} (f_n/f_{n+1}) = \phi = 0.61803398875 \dots
$$

Many people think that the golden ratio is the most beautiful ratio
and can be found everywhere in art, architecture, and even in nature.
But some people argue that most of those perceptions are 
[just myths](http://www.lhup.edu/~dsimanek/pseudo/fibonacc.htm).
People often strech the observations to fit their theories and cherry-pick
evidence. But, I am not going to talk about this here.

On wikipedia or Google you can find a lot of mathematics on the golden ratio
and Fibonacci numbers. Here I want to share a simple way I understand 
(and remember) them.

## Golden Ratio and Paper Cutting


The simplest way (for me, at least) to remember the golden ratio is the 
following. Take a rectangular piece of paper; cut away the largest square
(the side equal to the short side of the original rectangle); if the
remaining rectangle is *similar* to the original, then ratio of the 
two sides of the rectangle (short to long) is the golden ratio.

![Rectangle division]({{ site.url }}/images/2015/golden-ratio-1.png)

As shown in the picture above, the equality of the two ratios can be
expressed in an equation:

$$
\frac{1-x}{x} = \frac{x}{1}.
$$

Multiply both side by $$x$$ and move things around a little bit, you get

$$
x^2 + x -1 =0.
$$

It's a simple quadratic equation and can be solved easily,
$$ x = \frac{1}{2}(-1 \pm \sqrt{5}) $$. Taking the positive solution,
we get $$ x = \phi= \frac{1}{2}(-1 + \sqrt{5}) = 0.61803398875 \dots $$.
The other solution is exactly $$-1/\phi = -1-\phi = -1.61803398875 \dots $$.

Fibonacci Numbers and Convergence of Ratios
-------------------------------------------

The ratio of adjacent numbers in Fibonacci sequence converges to
the golden ratio. 

Let's prove the ratio will converge. For a sequence $$\{a_n\}$$ where
$$a_n = a_{n-1}+a_{n-2}$$, let's take the difference of the two ratios

$$
\begin{eqnarray}
\delta_n &=& \frac{a_{n+1}}{a_{n+2}} - \frac{a_{n}}{a_{n+1}} \\
&=& \frac{a_{n+1}^2 - a_{n}a_{n+2}}{a_{n+1} a_{n+2}}
\end{eqnarray}
$$

The numerator can be written as 

$$
\begin{eqnarray}
N_n &\equiv& a^2_{n+1} - a_n a_{n+2} \\
&=& a^2_{n+1} - a_n (a_n + a_{n+1})\\
&=& -a_n^2 + a_{n+1}(a_{n+1} - a_n) \\
&=& -a_n^2 + a_{n+1}a_{n-1},
\end{eqnarray}
$$

which is exactly $$-N_{n-1}$$, that is, the numerator of $$\delta_{n-1}$$
with a negative sign. You can go all the way down to $$\delta_0$$; each 
time you go one step down, you flip the sign but keep the magnitude constant.
The denominator $$a_{n+1}a_{n+2}$$, on the other hand, is a fast
growing number. So $$\delta_n$$ will approach zero very quickly. Therefore,
we can conclude that the ratio $$a_n/a_{n+1}$$ converges (as long as 
$$\delta_n$$ approaches zero faster than $$1/n$$, which is true in this case).

Note that, it does not matter what the starting values $$a_1$$ and $$a_2$$ are.
As long as $$a_n = a_{n-1}+a_{n-2}$$ relation holds, the ratio converges as 
$$n\to \infty$$. So it can be regular Fibonacci numbers 
$$\{1, 1, 2, 3, 5\dots\}$$, or so-called Lucas numbers
$$\{2, 1, 3, 4, 7\dots\}$$, or whatever $$a_1$$, $$a_2$$ you choose,
even negative numbers. The ratio converges very quickly.

![Sequence ratio convergence]({{ site.url }}/images/2015/fibonacci-ratio-converge.png)


Paper cutting again
---------------------------

In the first figure, we cut a square out of a rectangular paper, and
we let the remaining smaller rectangle be similar to the original, and
then we conclude the ratio of the two sides is the golden ratio.
Clearly if we start with the golden ratio, we can repeat this operation
and cut the paper (mathematically) forever.

What if the ratio is not the golden ratio to start with?

First we define the situation that we say we cannot cut the paper in
way anymore. That is, when the ratio of the two side $$x \ge 2$$, because
when this happens, the long side will still be a long side after a
square is removed, or it will become a square and you don't know how to
cut it anymore.

It can be shown that to cut this rectangular forever, the only ratio
you can start with is the golden ratio. If you start with a ratio of two
adjacent Fibonacci numbers (can be very close to the golden ratio but not
exactly), you will end up with [a square (or two)](http://www.mathsisfun.com/numbers/images/fibonacci-spiral.gif),
that is, the ratio of the sides is $$a_2/a_1$$.

