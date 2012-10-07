pyMorsek8055
============

An example usage of the pyk8055 library. To run, install the pyk8055 from http://libk8055.sourceforge.net

This program connects to a velleman K8055(N) on adress 0 (both adress jumpers are set)

What it does
------------

It listens for a sequence of short/long button presses and match them to a dict. Every pause of a second, it'll see if the inputted sequence match any dict key. it it matches, it outputs his correponding value, in this case the matching letter/number acording to the morse squence entered by the button(s).
