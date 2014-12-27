list = {"fastest": "1",
        "faster": "2",
        "normal": "3",
        "slow": "4",
        "slower": "5",
}


def get(speed):
  result = list.itervalues().next()
  if(speed is not None and speed in list):
    result = list.get(speed)

  return result
