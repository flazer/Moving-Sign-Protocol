Moving-Sign-Protocol
====================

A pythonclient for sending commands to a "Led-Moving-Sign"

Written by flazer, with the great help of phia at c31c3 - 2014

HowTo:

- Checkout project
- Open led.py
- Change device-specific-things

- cli:
led.py "message you want to display" 

Optional params:
-a: Animation
-c: Colour
-f: Font
-s: Speed

You are also able to use multiple colors in a message.
For this use "multi" as colourparameter and add the color in brackets directly into the message.
example:
[red]This is [green]just a [orange]test.

