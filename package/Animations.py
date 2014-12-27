list = {"auto": "A",
        "hold": "C",
        "interlock": "D",
        "rolldown": "E",
        "rollup": "F",
        "rollin": "G",
        "rollout": "H",
        "rollleft": "I",
        "rollright": "J",
        "rotate": "K",
        "slide": "L",
        "snow": "M",
        "sparkle": "N",
        "spray": "O",
        "starburst": "P",
        "switch": "Q",
        "twinkle": "R",
        "wipedown": "S",
        "wipeup": "T",
        "wipein": "U",
        "wipeout": "V",
        "wipeleft": "W",
        "wiperight": "X",
        "cyclecolour": "Y",
        "clock": "Z",
        "hold-roll": "[",
        "roll-hold": "\""
 }


def get(animation):
  result = list.itervalues().next()
  if(animation is not None and animation in list):
    result = list.get(animation)  
 
  return result
