print("--main.py")
import machine
import ili9341


def color565(r, g=0, b=0):
    """Convert red, green and blue values (0-255) into a 16-bit 565 encoding.  As
    a convenience this is also available in the parent adafruit_rgb_display
    package namespace."""
    try:
        r, g, b = r  # see if the first var is a tuple/list
    except TypeError:
        pass
    return (r & 0xF8) << 8 | (g & 0xFC) << 3 | b >> 3


spi = machine.SPI(1, baudrate=32000000)
display = ili9341.ILI9341(spi, cs=machine.Pin(0), dc=machine.Pin(15))

display.fill(color565(255, 0, 0))
