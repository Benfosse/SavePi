import milight
controller = milight.MiLight({'host': '192.168.1.37', 'port': 8899}, wait_duration=0) #Create a controller with 0 wait between commands
light = milight.LightBulb(['rgbw']) #Can specify which types of bulbs to use
controller.send(light.all_on()) # Turn on all lights, equivalent to light.on(0)
