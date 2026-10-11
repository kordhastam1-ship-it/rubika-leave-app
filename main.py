import asyncio
import threading
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class RubikaApp(App):
    def build(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        self.layout.add_widget(
            Label(
                text="ترک کانال‌های روبیکا",
                font_size=24
            )
        )

        self.phone = TextInput(
            hint_text="شماره حساب روبیکا",
            multiline=False
        )
        self.layout.add_widget(self.phone)

        self.status = Label(
            text="آماده شروع",
            font_size=18
        )
        self.layout.add_widget(self.status)

        self.button = Button(
            text="شروع ترک کانال‌ها",
            font_size=22,
            size_hint=(1, 0.25)
        )
        self.button.bind(on_press=self.start_task)
        self.layout.add_widget(self.button)

        return self.layout

    def start_task(self, instance):
        phone = self.phone.text.strip()

        if not phone:
            self.status.text = "ابتدا شماره حساب را وارد کن"
            return

        self.status.text = (
            "رابط برنامه آماده است؛ "
            "اتصال امن روبیکا هنوز تنظیم نشده."
        )
        self.button.disabled = True

    def on_stop(self):
        pass

RubikaApp().run()
