input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    led.stopAnimation()
    if (input.compassHeading() < 45 || input.compassHeading() > 315) {
        basic.showLeds(`
            # . . . #
            # # . . #
            # . # . #
            # . . # #
            # . . . #
            `)
    } else if (input.compassHeading() < 135 && input.compassHeading() > 45) {
        basic.showLeds(`
            # # # # #
            # . . . .
            # # # # .
            # . . . .
            # # # # #
            `)
    } else if (input.compassHeading() < 225 && input.compassHeading() > 135) {
        basic.showLeds(`
            . # # # .
            # . . . .
            . # # # .
            . . . . #
            . # # # .
            `)
    } else {
        basic.showLeds(`
            # . . . #
            # . . . #
            # . # . #
            # . # . #
            . # # # .
            `)
    }
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    led.stopAnimation()
    x = input.acceleration(Dimension.Z) / 1024 * 9.8
    Show()
})
function Show () {
    y = 1
    basic.showString(convertToText(x).charAt(y))
    basic.clearScreen()
    y += 1
    if (convertToText(x).charAt(y) == ".") {
        basic.showString(".")
        basic.clearScreen()
        y += 1
        basic.showString(convertToText(x).charAt(y))
    } else {
        basic.showString(convertToText(x).charAt(y))
        y += 1
        if (convertToText(x).charAt(y) == ".") {
            basic.showString(".")
            basic.showString(convertToText(x).charAt(y))
        } else {
            basic.showString(convertToText(x).charAt(y))
            basic.showString(".")
            basic.showString(convertToText(Math.abs(x)).charAt(y))
        }
    }
    basic.clearScreen()
}
input.onButtonPressed(Button.A, function () {
    led.stopAnimation()
    x = input.acceleration(Dimension.X) / 1024 * 9.8
    Show()
})
input.onButtonPressed(Button.B, function () {
    led.stopAnimation()
    x = input.acceleration(Dimension.Y) / 1024 * 9.8
    Show()
})
let y = 0
let x = 0
bluetooth.startAccelerometerService()
bluetooth.startButtonService()
bluetooth.startLEDService()
bluetooth.startIOPinService()
bluetooth.startTemperatureService()
bluetooth.startMagnetometerService()
