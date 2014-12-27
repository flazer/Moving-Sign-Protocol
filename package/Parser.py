import argparse

def parse():
  parser=argparse.ArgumentParser(
      description="""MSCP-Client (Moving Sign Communication Protocol - Client) Written by flazer with help from phia at C31C3.""",
      epilog="""You can use this code, for whatever you want, except earning money! For more information please write a message to info@flazer.net""")

  parser.add_argument('message', default=' ', help='Message to display')
  parser.add_argument('-c', '--colour', default='red', help="Color to be used on ledbar")
  parser.add_argument('-a', '--animation', default='auto', help="Animation to be used on ledbar")
  parser.add_argument('-s', '--speed', default='slow', help="Speed to be used on ledbar")
  parser.add_argument('-f', '--font', default='five-row-normal', help="Font to be used on ledbar")
  return parser
