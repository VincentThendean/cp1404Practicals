from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

CONVERSION_VALUE = 1.60934


class ConvertMilesKm(App):
    message = StringProperty()
    input = StringProperty()

    def build(self):
        self.title = 'Convert Miles to KM'
        self.root = Builder.load_file('convert_miles_km_.kv')
        self.input = '0'
        return self.root

    def handle_convert(self, value):
        try:
            result = float(value) * CONVERSION_VALUE
            self.message = str(result)
        except ValueError:
            self.message = '0'

    def handle_increments(self, saved_number, value):
        try:
            result = float(saved_number) + value
            self.input = str(result)
        except ValueError:
            self.input = '0'
            result = float(0) + value
            self.input = str(result)


ConvertMilesKm().run()
