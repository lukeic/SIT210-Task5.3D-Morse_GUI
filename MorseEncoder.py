import time
import RPi.GPIO as GPIO


class MorseEncoder:

    LED = 11

    MAPPING = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ">": "-.--.-",
        "<": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
        "DLT": "........",
    }

    def __init__(self, parent=None):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.LED, GPIO.OUT)

    def __char_array(self, str):
        return list(str)

    def __send_dot(self):
        GPIO.output(self.LED, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(self.LED, GPIO.LOW)
        time.sleep(0.25)

    def __send_dash(self):
        GPIO.output(self.LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.LED, GPIO.LOW)
        time.sleep(0.25)

    def __send_signal(self, signal):
        if signal == ".":
            self.__send_dot()
        elif signal == "-":
            self.__send_dash()

    def encode(self, message):
        _message = message.upper()
        print("Sending: {}".format(_message))
        if _message == "DLT":
            for signal in self.__char_array(self.MAPPING.get("DLT")):
                self.__send_signal(signal)
            return
        for char in self.__char_array(_message):
            encoding = self.MAPPING.get(char)
            if encoding is None:
                return
            for signal in self.__char_array(encoding):
                self.__send_signal(signal)
            time.sleep(0.25)

    def dispose(self):
        GPIO.output(self.LED, GPIO.LOW)
        GPIO.cleanup()
