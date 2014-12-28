import random

list = {"red": "B",
        "green": "C",
        "orange": "G",
        "yellow": "F",
        "striped": "J" }


def get(colour):
  if colour ==  "multi":
    return ''

  if colour == "auto":
    result = random.choice(list.values())
    print result
  else:
    result = list.itervalues().next()
    if(colour is not None and colour in list):
      result = list.get(colour)

  return "~FD" + result
