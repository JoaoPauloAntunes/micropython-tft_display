print("--main.py")
from machine import SPI, Pin
from rgb import color565
import ili9341


spi = SPI(1, baudrate=32000000)
display = ili9341.ILI9341(spi, cs=Pin(0), dc=Pin(15))

# display.fill(color565(255, 0, 0))
