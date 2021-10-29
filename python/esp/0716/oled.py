import ssd1306
from machine import I2C, Pin

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("Hello", 0, 0)
oled.text("World", 0, 10)

oled.invert(False)

oled.show()