from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window


class ConvertMilesKm(App):
    message = StringProperty()
    input = StringProperty()

    def build(self):
        self.title = 'Convert Miles to KM'
        self.root = Builder.load_file('convert_miles_km_.kv')
        self.input = '0'
        return self.root

    def handle_convert(self, value):
        result = float(value) * 1.60934
        self.message = str(result)

    def handle_increments(self, value):
        result = float(self.input) + value
        self.input = str(result)


ConvertMilesKm().run()
