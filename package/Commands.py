def build(package, args):
  colour = package.Colours.get(args.colour)
  font = package.Fonts.get(args.font)
  animation = package.Animations.get(args.animation)
  speed = package.Speeds.get(args.speed)
  message = package.Message.setColours(args.message)
  message = package.Message.replace(message)

  command = "~00~00~00~00~00"
  command += "~01"
  command += "FF00"
  command += "~02"
  command += "A0"
  command += animation
  command += speed
  command += "27F200701022008010200002300~FF~FF11~FE"
  command += font
  command += colour
  command += message
  command += "~030023~04"
  
  return command
