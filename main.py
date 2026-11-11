import threading
import requests
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Window.clearcolor = (0.13, 0.13, 0.15, 1)
GOLD = (0.85, 0.68, 0.25, 1)


class WeatherApp(App):
    def build(self):
        self.title = "Weather App"
        root = BoxLayout(orientation="vertical", padding=24, spacing=14)

        root.add_widget(Label(text="WEATHER", font_size="30sp",
                              color=GOLD, size_hint_y=None, height=70))

        self.city_input = TextInput(hint_text="Enter city", multiline=False,
                                    font_size="20sp", size_hint_y=None,
                                    height=60)
        self.city_input.bind(on_text_validate=self.search)
        root.add_widget(self.city_input)

        root.add_widget(Button(text="Search", font_size="20sp",
                               size_hint_y=None, height=60,
                               background_normal="",
                               background_color=GOLD, color=(0, 0, 0, 1),
                               on_release=self.search))

        self.result = Label(text="", font_size="20sp", halign="center",
                            valign="top")
        self.result.bind(size=lambda w, s: setattr(w, "text_size", s))
        root.add_widget(self.result)
        return root

    def search(self, *args):
        city = self.city_input.text.strip()
        if not city:
            return
        self.result.text = "Loading..."
        threading.Thread(target=self.fetch, args=(city,), daemon=True).start()

    def fetch(self, city):
        try:
            url = f"https://wttr.in/{city}?format=j1"
            data = requests.get(url, timeout=10).json()
            c = data["current_condition"][0]
            text = (f"City: {city}\n\n"
                    f"Temperature: {c['temp_C']} C\n"
                    f"Humidity: {c['humidity']} %\n"
                    f"Condition: {c['weatherDesc'][0]['value']}")
        except Exception:
            text = "City not found or internet unavailable."
        Clock.schedule_once(lambda dt: setattr(self.result, "text", text))


WeatherApp().run()
