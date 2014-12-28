#-*- coding: UTF-8 -*-

import re
import package

replacements = {"ü": "ue",
                "Ü": "Ue",
                "ä": "ae",
                "Ä": "Ae",
                "ö": "oe",
                "Ö": "Oe",
                "ß": "ss"
}

def replace(message):
  for key in replacements:
    message = message.replace(key, replacements.get(key))

  message = re.sub(r'[^\w\s!.=,?+:~_-]', '', message)
  return message

def setColours(message):
  pattern = re.compile(r'(\[([a-z]*)\])')
  for (colour, string) in re.findall(pattern, message):
    colour = package.Colours.get(string)
    message = message.replace(string, colour)
  return message
