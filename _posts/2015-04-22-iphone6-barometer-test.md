---
layout: post
title: iPhone6 barometer test
category: iPhone science
tags: pressure, iPhone, gas, tech
---

iPhone6(Plus) now comes with a barometer. It senses the atmosphere pressure 
and one can infer the elevation changes from the variation of the air pressure.
Apple incorporates the barometer data in their [Health Data](https://www.apple.com/ios/whats-new/health/) which includes how many flights of stairs you take
everyday. Why can't you just use the GPS data? Because the precision of the 
GPS in the vertical direction is more than 10 meters,
not enough to accurately tell if you are on the first or the second floor.
Imagine you climbed to the top of a three-story building, and your device 
said, "Meh, I am not sure if you have exercised at all.". That would be
frustrating. 

How about the barometer on the chip of a smart phone? I always thought 
the barometer cannot be very precise either. Determing a couple of meters
change in altitude might be quite difficult. But I didn't really know. So
I am doing a little calculation and test here.

I use an App called [Bar-o-Meter](https://itunes.apple.com/us/app/bar-o-meter-altimeter-barometer/id930952204?mt=8) to access the data on my iPhone6. 

<img src="{{ site.url }}/images/2015/barometer_d1.jpg" width="250px" />

It has a pressure reading at the center. The least significant digit is 
0.01 mBar, or 1 pascal (Pa), which is equal to $$1\ N/m^2$$ 
(Newton per square meter) of pressure. One Newton (a unit of force) is 
equivalent to approximately 100 grams of weight on Earth.

It also has a few altitude readings with a least significant digit at 0.01
meter, or 1 cm. Can the barometer really be sensitive to order of 1 cm change 
in altitude? I doubt it. But let's do some calculations.

The first question is, how much would the air pressure change at two different
altitude. I will just assume we move the barometer only locally (order of 
a meter) and everything scales linearly. If we know the denstity $$d$$ of the
fluid (here, air), the difference in the pressure is simply 
$$\Delta P= - d g \Delta h$$, where $$g$$ is the 
[gravitational acceleration](http://en.wikipedia.org/wiki/Gravitational_acceleration) $$g \simeq 9.8\ {\rm m}/{\rm s}^2$$, and $$\Delta h$$ is the difference in height.

To get the air density, we can use the [ideal gas law](http://en.wikipedia.org/wiki/Ideal_gas_law) $$PV = nRT$$, where $$P$$ is the pressure, $$V$$ is the
volume, $$n$$ is the amount of gas molecules (number of moles) in the volume,
$$R\simeq 8.3145\ {\rm J}\ {\rm K}^{-1} {\rm mol}^{-1}$$ is the [gas constant](http://en.wikipedia.org/wiki/Gas_constant)
 equal to the product of the 
[Boltzmann contant](http://en.wikipedia.org/wiki/Boltzmann_constant)
and the [Avogadro constant](http://en.wikipedia.org/wiki/Avogadro_constant),
and finally $$T$$ is the absolute temperature.
 
At this time, the atomesphere pressure in my room is about 1004.8 mBar
($$P = 100480\ {\rm N}/{\rm m}^2$$). 
The temperature is about 21 C ($$T= 294\ {\rm K}$$). So we have the mole
density $$n/V = P/(RT) = \frac{100480}{8.3145 \times 294} {\rm N}{\rm m}^{-2} {\rm J}^{-1}{\rm mol} = 41.1\ {\rm mol}/{\rm m^3}$$.

The air [consists of](http://eo.ucar.edu/basics/wx_1_b_1.html) 78% of 
nitrogen, 21% of oxygen, and nearly 1% of argon. Each mole of molecules of 
these three gasses weights 28 g, 32 g, and 40 g, respectively. Therefore, each 
mole of air weights very close to 29 g. Putting them together, we have the air
density $$d = 41.1\times 29\ {\rm g}/{\rm m}^3  = 1.192\ {\rm kg}/{\rm m}^3$$.

So the sensitivity of pressure to height is 
$$\Delta P/\Delta h = -d g = -11.7\ {\rm Pa}/{\rm m} $$.

First observation. If your device has a sensitivity of 1 Pa, the corresponding
sensitivity in height is about 0.1 m, not 0.01 m. So the choice of the 
least significant digit of the altitude readings does not match that of
the pressure readings. They should just show one digit below the 
decimal point.

The App can (and I assume they do) use a
[more sophisticated formula](http://www.xcmag.com/2011/07/gps-versus-barometric-altitude-the-definitive-answer/) to convert
the pressure to altitude. To compare the device's calculation and mime, I took
two readings, one on the floor, the other one in my hand raising high.

<img src="{{ site.url }}/images/2015/barometer_d1.jpg" width="250px" />
<img src="{{ site.url }}/images/2015/barometer_d2.jpg" width="250px" />

The differences between the two pressure and altitude readings are
$$-21\ {\rm Pa}$$ and 1.81 m, respectively. Their 
$$\Delta P/\Delta h = -11.6\ {\rm Pa}/{\rm m} $$, is very close to my 
calculation.


### Precision test 

The analysis above only touches upon the choice of the significant digits.
It doesn't necessarily reflect the actual precision. So I did a simple
experiment. At the bottom, there is a reset button. The "Relative Altitude"
will be set to 0.00 after the reset button is clicked. The App seems to 
refresh the reading every a couple of seconds. After setting the reading
to 0.00 while the phone was sitting on a table, I moved the iPhone up and
down a couple of time in an arm's range. I then put it back on the same table
for about 5 seconds, then read the number. Because the phone came back to the
same height, the reading should go back to 0.00. If we assume nothing else has
changed, including the atmosphere pressure, in these 15 seconds, the deviation
from zero was due to the resolution only. 

I took 75 readings. The distribution is shown below. The root mean square
(rms), representing the resolution, is 11.8 cm, much better than I would have
guessed. 

<img src="{{ site.url }}/images/2015/barometer_deltah.png" />

This result is surprising to me. Apparently I underestimated the progress
of modern technology. Obviously one can do more tests, such as long term 
stability and wider variations in altitude. And if the weather is changing
quickly, for example, a hurricane is approaching, the accuracy in altitude
 will not be this good.

