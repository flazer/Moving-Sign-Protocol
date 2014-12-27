list = {"small": "@",
        "five-row-normal": "A",
        "five-row-bold": "B",
        "five-row-wide": "C",
        "five-row-wide-shade": "D",
        "seven-row-normal": "E",
        "seven-row-bold": "F",
        "seven-row-wide":"G",
        "seven-row-wide-shade":"H",
        "seven-row-colour-shade":"I",
        "seven-row-fancy-normal":"J",
        "seven-row-fancy-bold":"K",
        "seven-row-fancy-wide":"L",
        "seven-row-fancy-wide-shade":"M",
        "seven-row-fancy-colour-shade":"N",
        "ten-row-normal":"O",
        "ten-row-bold":"P",
        "ten-row-wide":"Q",
        "ten-row-wide-shade":"R",
        "15-16-normal":"S",
        "15-16-bold":"T",
        "15-16-wide":"U",
        "15-16-wide-shade":"V",
        "24-row":"W",
        "32-row":"X"
}


def get(font):
  result = list.itervalues().next()
  if(font is not None and font in list):
    result = list.get(font)

  return result

