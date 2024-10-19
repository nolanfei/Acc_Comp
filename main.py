def on_button_pressed_a():
    global x
    led.stop_animation()
    x = input.acceleration(Dimension.X) / 1024 * 9.8
    Show()
input.on_button_pressed(Button.A, on_button_pressed_a)

def Show():
    global y
    y = 1
    basic.show_string(convert_to_text(x).char_at(y))
    basic.clear_screen()
    y += 1
    if convert_to_text(x).char_at(y) == ".":
        basic.show_string(".")
        basic.clear_screen()
        y += 1
        basic.show_string(convert_to_text(x).char_at(y))
    else:
        basic.show_string(convert_to_text(x).char_at(y))
        y += 1
        if convert_to_text(x).char_at(y) == ".":
            basic.show_string(".")
            basic.show_string(convert_to_text(x).char_at(y))
        else:
            basic.show_string(convert_to_text(x).char_at(y))
            basic.show_string(".")
            basic.show_string(convert_to_text(abs(x)).char_at(y))
    basic.clear_screen()

def on_button_pressed_ab():
    global x
    led.stop_animation()
    x = input.acceleration(Dimension.Z) / 1024 * 9.8
    Show()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global x
    led.stop_animation()
    x = input.acceleration(Dimension.Y) / 1024 * 9.8
    Show()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    led.stop_animation()
    if input.compass_heading() < 45 or input.compass_heading() > 315:
        basic.show_leds("""
            # . . . #
            # # . . #
            # . # . #
            # . . # #
            # . . . #
            """)
    elif input.compass_heading() < 135 and input.compass_heading() > 45:
        basic.show_leds("""
            # # # # #
            # . . . .
            # # # # .
            # . . . .
            # # # # #
            """)
    elif input.compass_heading() < 225 and input.compass_heading() > 135:
        basic.show_leds("""
            . # # # .
            # . . . .
            . # # # .
            . . . . #
            . # # # .
            """)
    else:
        basic.show_leds("""
            # . . . #
            # . . . #
            # . # . #
            # . # . #
            . # # # .
            """)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

y = 0
x = 0
bluetooth.start_accelerometer_service()
bluetooth.start_button_service()
bluetooth.start_led_service()
bluetooth.start_io_pin_service()
bluetooth.start_temperature_service()
bluetooth.start_magnetometer_service()