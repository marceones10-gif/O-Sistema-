# main.py (parte 1A/5)

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.list import MDList
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from datetime import date
import random

KV = """
<RecruitmentScreen>:
    name: 'recruitment_screen'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)
        Widget:
        MDLabel:
            text: "Você foi convocado para ser um jogador!"
            halign: "center"
            font_style: "H4"
            size_hint_y: None
            height: self.texture_size[1]
            markup: True
            color: app.theme_cls.primary_color
        MDLabel:
            text: "Você aceita?"
            halign: "center"
            font_style: "H4"
            size_hint_y: None
            height: self.texture_size[1]
            markup: True
            color: (0, 1, 1, 1)
        BoxLayout:
            orientation: "horizontal"
            spacing: dp(20)
            size_hint_x: None
            width: self.minimum_width
            size_hint_y: None
            height: dp(48)
            pos_hint: {"center_x": 0.5}
            MDRectangleFlatButton:
                text: "SIM"
                font_style: "Button"
                on_release: app.root.current = 'home_screen'
                md_bg_color: app.theme_cls.primary_color
                text_color: app.theme_cls.text_color
                line_color: app.theme_cls.primary_color
                size_hint_x: None
                width: dp(100)
            MDRectangleFlatButton:
                text: "NÃO"
                font_style: "Button"
                on_release: app.show_exit_dialog()
                md_bg_color: 0, 0, 0, 0
                text_color: app.theme_cls.primary_color
                line_color: app.theme_cls.primary_color
                size_hint_x: None
                width: dp(100)
        Widget:
<HomeScreen>:
    name: 'home_screen'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)
        MDLabel:
            id: player_class_label
            text: "RANKING: [b]CARREGANDO...[/b]"
            halign: "center"
            font_style: "H5"
            size_hint_y: None
            height: dp(48)
            markup: True
            color: app.theme_cls.primary_color
        MDLabel:
            id: current_class_label
            text: "CLASSE: [b]CARREGANDO...[/b]"
            halign: "center"
            font_style: "H5"
            size_hint_y: None
            height: dp(48)
            markup: True
            color: (0, 1, 1, 1)
        MDLabel:
            id: player_level_label
            text: "[b]NÍVEL:[/b] 0"
            halign: "center"
            font_style: "H4"
            size_hint_y: None
            height: dp(48)
            markup: True
            color: app.theme_cls.accent_color
        MDLabel:
            id: xp_label
            text: "XP: 0/0"
            halign: "left"
            font_style: "Subtitle1"
            size_hint_y: None
            height: dp(24)
            color: app.theme_cls.text_color
        MDProgressBar:
            id: xp_bar
            value: 0
            max: 1
            color: (0, 1, 0, 1)
            size_hint_y: None
            height: dp(10)
        MDLabel:
            id: stamina_label
            text: "Stamina: 0/0"
            halign: "left"
            font_style: "Subtitle1"
            size_hint_y: None
            height: dp(24)
            color: app.theme_cls.text_color
        MDProgressBar:
            id: stamina_bar
            value: 0
            max: 1
            color: (0, 0, 1, 1)
            size_hint_y: None
            height: dp(10)
        MDLabel:
            id: coins_label
            text: "[b]Moedas:[/b] 0"
            halign: "left"
            font_style: "Subtitle1"
            size_hint_y: None
            height: dp(24)
            markup: True
            color: app.theme_cls.text_color
        Widget:
            size_hint_y: None
            height: dp(20)
        MDLabel:
            text: "[b]Atributos[/b]"
            halign: "center"
            font_style: "H6"
            size_hint_y: None
            height: dp(30)
            markup: True
            color: app.theme_cls.primary_color
        MDLabel:
            id: attr_strength
            text: "[b]Força:[/b] 0"
            halign: "left"
            font_style: "H6"
            size_hint_y: None
            height: dp(28)
            markup: True
            color: app.theme_cls.text_color
        MDLabel:
            id: attr_agility
            text: "[b]Agilidade:[/b] 0"
            halign: "left"
            font_style: "H6"
            size_hint_y: None
            height: dp(28)
            markup: True
            color: app.theme_cls.text_color
        MDLabel:
            id: attr_intelligence
            text: "[b]Inteligência:[/b] 0"
            halign: "left"
            font_style: "H6"
            size_hint_y: None
            height: dp(28)
            markup: True
            color: app.theme_cls.text_color
        MDLabel:
            id: attr_vitality
            text: "[b]Vitalidade:[/b] 0"
            halign: "left"
            font_style: "H6"
            size_hint_y: None
            height: dp(28)
            markup: True
            color: app.theme_cls.text_color
        MDLabel:
            id: attr_perception
            text: "[b]Percepção:[/b] 0"
            halign: "left"
            font_style: "H6"
            size_hint_y: None
            height: dp(28)
            markup: True
            color: app.theme_cls.text_color
        Widget:
            size_hint_y: None
            height: dp(5)
        MDRectangleFlatButton:
            text: "Missão Diária"
            on_release: root.show_mission_popup()
            pos_hint: {"center_x": 0.5}
            md_bg_color: app.theme_cls.primary_color
            text_color: app.theme_cls.text_color
            line_color: app.theme_cls.primary_color
            size_hint_y: None
            height: dp(48)
        MDRectangleFlatButton:
            text: "Loja"
            on_release: app.root.current = 'store_screen'
            pos_hint: {"center_x": 0.5}
            md_bg_color: app.theme_cls.primary_color
            text_color: app.theme_cls.text_color
            line_color: app.theme_cls.primary_color
            size_hint_y: None
            height: dp(48)
        MDRectangleFlatButton:
            text: "Atributos"
            on_release: app.root.current = 'attributes_screen'
            pos_hint: {"center_x": 0.5}
            md_bg_color: app.theme_cls.accent_color
            text_color: app.theme_cls.text_color
            size_hint_y: None
            height: dp(48)
        MDRectangleFlatButton:
            text: "Sala de Classes"
            on_release: app.root.current = 'classroom_screen'
            pos_hint: {"center_x": 0.5}
            md_bg_color: app.theme_cls.primary_color
            text_color: app.theme_cls.text_color
            line_color: app.theme_cls.primary_color
            size_hint_y: None
            height: dp(48)
        Widget:

<ExercisesScreen>:
    name: 'exercises_screen'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(12)
        MDLabel:
            text: "LISTA DE MISSÕES (EXERCÍCIOS)"
            halign: "center"
            font_style: "H5"
            size_hint_y: None
            height: dp(50)
            color: app.theme_cls.primary_color
        ScrollView:
            do_scroll_x: False
            MDList:
                id: exercise_list
                padding: dp(4)
                spacing: dp(8)
        MDRectangleFlatButton:
            text: "Voltar"
            on_release: app.root.current = 'home_screen'
            pos_hint: {"center_x": 0.5}
            size_hint_y: None
            height: dp(48)
            md_bg_color: app.theme_cls.accent_color
            text_color: app.theme_cls.text_color

<StoreScreen>:
    name: 'store_screen'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(8)
        spacing: dp(6)
        MDLabel:
            text: "Loja do Sistema"
            halign: "center"
            font_style: "Subtitle1"
            size_hint_y: None
            height: dp(28)
            color: app.theme_cls.primary_color
        MDLabel:
            id: coins_label
            text: "Moedas: 0"
            halign: "center"
            font_style: "Body2"
            size_hint_y: None
            height: dp(22)
        ScrollView:
            do_scroll_x: False
            MDList:
                id: store_list
                padding: dp(4)
                spacing: dp(8)
        BoxLayout:
            size_hint_y: None
            height: dp(40)
            spacing: dp(8)
            MDRectangleFlatButton:
                id: refresh_btn
                text: "Atualizar"
                font_size: "12sp"
                on_release: root.populate_store()
                md_bg_color: app.theme_cls.primary_color
                text_color: app.theme_cls.text_color
            MDRectangleFlatButton:
                text: "Voltar"
                font_size: "12sp"
                on_release: app.root.current = 'home_screen'
                md_bg_color: app.theme_cls.accent_color
                text_color: app.theme_cls.text_color

<AttributesScreen>:
    name: 'attributes_screen'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(12)
        spacing: dp(8)
        MDLabel:
            text: "DISTRIBUIR PONTOS"
            halign: "center"
            font_style: "H5"
            size_hint_y: None
            height: dp(36)
            color: app.theme_cls.primary_color
        MDLabel:
            id: points_label
            text: "PONTOS DISPONÍVEIS: 0"
            halign: "center"
            font_style: "Body1"
            size_hint_y: None
            height: dp(24)
            color: app.theme_cls.text_color
            markup: True
        ScrollView:
            do_scroll_x: False
            MDList:
                id: attrs_list
                padding: dp(4)
        BoxLayout:
            size_hint_y: None
            height: dp(44)
            spacing: dp(8)
            MDRectangleFlatButton:
                text: "CONFIRMAR"
                on_release: root.confirm()
                md_bg_color: app.theme_cls.primary_color
                text_color: app.theme_cls.text_color
            MDRectangleFlatButton:
                text: "RESETAR"
                on_release: root.reset_temp()
                md_bg_color: app.theme_cls.accent_color
                text_color: app.theme_cls.text_color
            MDRectangleFlatButton:
                text: "VOLTAR"
                on_release: app.root.current = 'home_screen'
                md_bg_color: (0,0,0,0)
                text_color: app.theme_cls.primary_color
                line_color: app.theme_cls.primary_color

<ClassroomScreen>:
    name: 'classroom_screen'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(12)
        MDLabel:
            text: "CLASSES DO MUNDO DE SOLO LEVELING"
            halign: "center"
            font_style: "H5"
            size_hint_y: None
            height: dp(50)
            color: app.theme_cls.primary_color
        ScrollView:
            do_scroll_x: False
            MDList:
                id: class_list
                padding: dp(4)
                spacing: dp(8)
        MDRectangleFlatButton:
            text: "Voltar para Home"
            on_release: app.root.current = 'home_screen'
            pos_hint: {"center_x": 0.5}
            size_hint_y: None
            height: dp(48)
            md_bg_color: app.theme_cls.accent_color
            text_color: app.theme_cls.text_color
"""

class BaseScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.1, 0, 0.2, 1)
            self.bg = Rectangle(size=self.size, pos=self.pos)
            Color(0, 0, 0.3, 1)
            self.bg2 = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos
        self.bg2.size = (self.width, self.height * 0.6)
        self.bg2.pos = (self.x, self.y)

class RecruitmentScreen(BaseScreen):
    pass

class HomeScreen(BaseScreen):
    mission_dialog = None

    def on_pre_enter(self, *args):
        app = MDApp.get_running_app()
        self.ids.player_class_label.text = f"RANKING: [b]{app.get_player_ranking().upper()}[/b]"
        self.ids.current_class_label.text = f"CLASSE: [b]{app.get_player_class().upper()}[/b]"
        self.ids.player_level_label.text = f"[b]NÍVEL:[/b] {app.player_level}"
        self.ids.xp_label.text = f"XP: {app.player_xp}/{app.player_xp_max}"
        self.ids.xp_bar.max = app.player_xp_max
        self.ids.xp_bar.value = app.player_xp
        self.ids.stamina_label.text = f"Stamina: {app.player_stamina}/{app.player_stamina_max}"
        self.ids.stamina_bar.max = app.player_stamina_max
        self.ids.stamina_bar.value = app.player_stamina
        self.ids.coins_label.text = f"[b]Moedas:[/b] {app.player_coins}"
        self.ids.attr_strength.text = f"[b]Força:[/b] {app.player_strength}"
        self.ids.attr_agility.text = f"[b]Agilidade:[/b] {app.player_agility}"
        self.ids.attr_intelligence.text = f"[b]Inteligência:[/b] {app.player_intelligence}"
        self.ids.attr_vitality.text = f"[b]Vitalidade:[/b] {app.player_vitality}"
        self.ids.attr_perception.text = f"[b]Percepção:[/b] {app.player_perception}"

    def show_mission_popup(self):
        if not self.mission_dialog:
            app = MDApp.get_running_app()
            exercises = app.get_daily_exercises()
            exercise_text = "\n".join([f"• {ex}" for ex in exercises[:5]])

            content = BoxLayout(orientation='vertical', spacing=dp(15), padding=dp(10), size_hint_y=None)
            content.height = dp(250)

            content.add_widget(MDLabel(
                text="MISSÃO DIÁRIA",
                halign="center",
                font_style="H4",
                theme_text_color="Custom",
                text_color=(0, 1, 1, 1)
            ))
            content.add_widget(MDLabel(
                text=exercise_text,
                halign="center",
                font_style="H6"
            ))

            self.mission_dialog = MDDialog(
                type="custom",
                content_cls=content,
                md_bg_color=(0.1, 0.1, 0.3, 0.98),
                radius=[25, 25, 25, 25],
                buttons=[
                    MDRectangleFlatButton(
                        text="VER TODOS",
                        md_bg_color=(0.5, 0, 1, 1),
                        text_color=(1, 1, 1, 1),
                        on_release=lambda x: self.go_to_exercises()
                    ),
                    MDRectangleFlatButton(
                        text="VOLTAR",
                        md_bg_color=(0, 0.5, 1, 1),
                        text_color=(1, 1, 1, 1),
                        on_release=lambda x: self.mission_dialog.dismiss()
                    )
                ]
            )
        self.mission_dialog.open()

    def go_to_exercises(self):
        self.mission_dialog.dismiss()
        MDApp.get_running_app().root.current = 'exercises_screen'

class ExercisesScreen(BaseScreen):
    _exercise_list_populated = False
    exercise_detail_dialog = None

    def on_enter(self, *args):
        self.add_exercises()# main.py (parte 1B/4) - Continuação ExercisesScreen

    def add_exercises(self):
        if hasattr(self.ids, 'exercise_list'):
            exercise_list_widget = self.ids.exercise_list
            exercise_list_widget.clear_widgets()
        else:
            print("Atenção: exercise_list não encontrada por ID.")
            return

        app = MDApp.get_running_app()
        exercises = app.get_daily_exercises()

        palette = [
            (0.00, 0.80, 1.00, 0.18),
            (0.65, 0.00, 1.00, 0.18),
            (0.40, 0.85, 1.00, 0.18),
            (1.00, 0.60, 0.00, 0.18),
            (0.00, 1.00, 0.50, 0.18),
        ]

        for idx, exercise in enumerate(exercises):
            ex_data = app.exercises_data.get(exercise, {})
            tipo = ex_data.get("tipo", "repeticao")
            valor = ex_data.get("valor", 10)

            if tipo == "tempo":
                valor_text = f"{valor//60:02d}:{valor%60:02d}"
            else:
                valor_text = f"x{valor}"

            card = MDCard(
                orientation="horizontal",
                padding=dp(12),
                spacing=dp(12),
                size_hint_y=None,
                height=dp(80),
                radius=[12],
                elevation=2,
                md_bg_color=palette[idx % len(palette)],
                on_release=lambda x, ex=exercise: self.show_exercise_detail(ex)
            )

            info_box = BoxLayout(orientation="vertical", size_hint_x=0.7)
            label = MDLabel(
                text=f"[b]{exercise.upper()}[/b]",
                markup=True,
                halign="left",
                valign="middle",
                font_style="H6",
                size_hint_y=None,
                height=dp(30)
            )
            label.bind(size=label.setter("text_size"))

            valor_label = MDLabel(
                text=valor_text,
                halign="left",
                valign="middle",
                font_style="Body1",
                size_hint_y=None,
                height=dp(20),
                theme_text_color="Secondary"
            )

            info_box.add_widget(label)
            info_box.add_widget(valor_label)

            card.add_widget(info_box)
            exercise_list_widget.add_widget(card)

    def show_exercise_detail(self, exercise_name):
        app = MDApp.get_running_app()
        ex_data = app.exercises_data.get(exercise_name, {})

        if not ex_data:
            app.show_info_dialog(exercise_name, "Instruções não disponíveis ainda.")
            return

        content = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10), size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        content.add_widget(MDLabel(
            text=f"[b]{exercise_name.upper()}[/b]",
            markup=True,
            halign="center",
            font_style="H5",
            size_hint_y=None,
            height=dp(40)
        ))

        tipo = ex_data.get("tipo", "repeticao")
        valor = ex_data.get("valor", 10)
        if tipo == "tempo":
            content.add_widget(MDLabel(
                text=f"DURAÇÃO: {valor//60:02d}:{valor%60:02d}",
                halign="center",
                font_style="H6",
                size_hint_y=None,
                height=dp(30),
                theme_text_color="Primary"
            ))
        else:
            content.add_widget(MDLabel(
                text=f"REPETIÇÕES: x{valor}",
                halign="center",
                font_style="H6",
                size_hint_y=None,
                height=dp(30),
                theme_text_color="Primary"
            ))

        content.add_widget(MDLabel(
            text="[b]INSTRUÇÕES[/b]",
            markup=True,
            halign="left",
            font_style="H6",
            size_hint_y=None,
            height=dp(30)
        ))

        instr = MDLabel(
            text=ex_data.get("instrucoes", ""),
            halign="left",
            valign="top",
            font_style="Body1",
            size_hint_y=None
        )
        instr.bind(texture_size=instr.setter('size'))
        content.add_widget(instr)

        content.add_widget(MDLabel(
            text="[b]ÁREA DE FOCO[/b]",
            markup=True,
            halign="left",
            font_style="H6",
            size_hint_y=None,
            height=dp(30)
        ))

        musculos_text = " • ".join(ex_data.get("musculos", []))
        content.add_widget(MDLabel(
            text=musculos_text,
            halign="left",
            font_style="Body2",
            size_hint_y=None,
            height=dp(30),
            theme_text_color="Secondary"
        ))

        self.exercise_detail_dialog = MDDialog(
            type="custom",
            content_cls=content,
            md_bg_color=(0.1, 0.1, 0.3, 0.98),
            radius=[20, 20, 20, 20],
            buttons=[
                MDRectangleFlatButton(
                    text="CONCLUIR (+15 XP)",
                    md_bg_color=(0, 0.8, 0, 1),
                    text_color=(1, 1, 1, 1),
                    on_release=lambda x: self.complete_exercise(exercise_name)
                ),
                MDRectangleFlatButton(
                    text="FECHAR",
                    md_bg_color=(0, 0.5, 1, 1),
                    text_color=(1, 1, 1, 1),
                    on_release=lambda x: self.exercise_detail_dialog.dismiss()
                )
            ]
        )
        self.exercise_detail_dialog.open()

    def complete_exercise(self, exercise_name):
        app = MDApp.get_running_app()
        if app.player_stamina < 10:
            app.show_info_dialog("Sem Stamina", "Você precisa de pelo menos 10 de Stamina para completar o exercício.")
            return
        app.player_stamina -= 10
        app.player_xp += 15
        app.player_coins += 50
        self.exercise_detail_dialog.dismiss()
        app.show_info_dialog("Missão Concluída!", f"{exercise_name} completo!\n+15 XP | +50 Moedas | -10 Stamina")

# --- FIM DA PARTE 1 ---# main.py (parte 2) - Código Python CORRIGIDO e OTIMIZADO (COMPACTO)

class StoreScreen(BaseScreen):
    current_offers = ListProperty([])

    def on_enter(self, *args): self.refresh_if_needed()

    def refresh_if_needed(self):
        app = MDApp.get_running_app()
        today = date.today().isoformat()
        if app.store_last_refresh!= today or not app.store_current_offers:
            app.store_current_offers = random.sample(app.store_pool, k=min(3, len(app.store_pool)))
            app.store_last_refresh = today
        self.current_offers = app.store_current_offers
        self.render()

    def render(self):
        app = MDApp.get_running_app()
        self.ids.coins_label.text = f"Moedas: {app.player_coins}"
        self.ids.store_list.clear_widgets()
        desc_map = {
            "heal": "Restaura +40 de Stamina (até o máximo) e dá +10 XP.", "strength": "Aumenta Força em +1 permanentemente.",
            "agility": "Aumenta Agilidade em +1 permanentemente.", "intelligence": "Aumenta Inteligência em +1 permanentemente.",
            "vitality": "Aumenta Vitalidade em +1 permanentemente.", "perception": "Aumenta Percepção em +1 permanentemente.",
            "reset": "Reseta atributos para os valores base e devolve os pontos gastos.",
            "teleport": "Item especial (placeholder): concede +100 moedas por enquanto.",
            "dungeon": "Item especial (placeholder): concede +25 XP por enquanto.",
            "random": "Caixa Misteriosa: revela e aplica um efeito aleatório da loja.",
        }
        palette = [(0.00, 0.80, 1.00, 0.18), (0.65, 0.00, 1.00, 0.18), (0.40, 0.85, 1.00, 0.18),]
        for idx, item in enumerate(self.current_offers):
            card = MDCard(
                orientation="vertical", padding=dp(12), spacing=dp(6),
                size_hint_y=None, height=dp(150), radius=[12], elevation=2,
                md_bg_color=palette[idx % len(palette)],
            )
            title = MDLabel(
                text=f"[b]{item['name']}[/b]", markup=True, halign="left",
                valign="middle", font_style="H6", size_hint_y=None, height=dp(26),
            )
            title.bind(size=title.setter("text_size"))
            price = MDLabel(
                text=f"Preço: {item['price']} moedas", halign="left", valign="middle",
                font_style="Body1", size_hint_y=None, height=dp(22), theme_text_color="Secondary",
            )
            price.bind(size=price.setter("text_size"))
            desc = MDLabel(
                text=desc_map.get(item.get("effect"), "Item especial."), halign="left",
                valign="top", font_style="Body2", size_hint_y=None, height=dp(44),
                theme_text_color="Hint",
            )
            desc.bind(size=desc.setter("text_size"))
            btn_row = BoxLayout(size_hint_y=None, height=dp(36), spacing=dp(8))
            btn = MDRectangleFlatButton(
                text="Comprar", size_hint=(1, 1), height=dp(32), width=dp(110),
                font_size="13sp", md_bg_color=app.theme_cls.primary_color,
                text_color=app.theme_cls.text_color,
            )
            if app.player_coins < item['price']: btn.disabled = True
            btn.bind(on_release=lambda inst, it=item: self.buy_item(it))
            btn_row.add_widget(Widget())
            btn_row.add_widget(btn)
            card.add_widget(title)
            card.add_widget(price)
            card.add_widget(desc)
            card.add_widget(btn_row)
            self.ids.store_list.add_widget(card)

    def buy_item(self, item):
        app = MDApp.get_running_app()
        if app.player_coins < item['price']:
            app.show_info_dialog("Moedas insuficientes", "Você não tem moedas suficientes.")
            return
        app.player_coins -= item['price']
        msg = app.apply_item_effect(item)
        self.render()
        app.show_info_dialog("Compra realizada", msg)
        if app.root and app.root.current == 'home_screen':
            app.root.get_screen('home_screen').on_pre_enter()

    def populate_store(self):
        app = MDApp.get_running_app()
        today = date.today().isoformat()
        if app.store_last_refresh!= today: self.refresh_if_needed()
        else: app.show_info_dialog("Loja", "Novas ofertas só amanhã.")

class AttributesScreen(BaseScreen):
    temp = {}

    def on_pre_enter(self, *args):
        app = MDApp.get_running_app()
        self.temp = {
            "strength": app.player_strength, "agility": app.player_agility,
            "intelligence": app.player_intelligence, "vitality": app.player_vitality,
            "perception": app.player_perception, "points": app.player_attribute_points,
        }
        self.render()

    def render(self):
        app = MDApp.get_running_app()
        self.ids.points_label.text = f"PONTOS DISPONÍVEIS: [b]{self.temp['points']}[/b]"
        lst = self.ids.attrs_list
        lst.clear_widgets()
        mapping = [("strength", "FORÇA"), ("agility", "AGILIDADE"), ("intelligence", "INTELIGÊNCIA"), ("vitality", "VITALIDADE"), ("perception", "PERCEPÇÃO"),]
        palette_attrs = [
            (0.80, 0.20, 0.20, 0.18), (0.20, 0.80, 0.20, 0.18),
            (0.20, 0.20, 0.80, 0.18), (0.80, 0.80, 0.20, 0.18), (0.80, 0.20, 0.80, 0.18),
        ]
        for idx, (key, label) in enumerate(mapping):
            card = MDCard(
                orientation="horizontal", padding=dp(8), spacing=dp(8),
                size_hint_y=None, height=dp(60), radius=[12], elevation=2,
                md_bg_color=palette_attrs[idx % len(palette_attrs)],
            )
            name = MDLabel(
                text=f"[b]{label}: {self.temp[key]}[/b]", markup=True,
                halign="left", valign="center", font_style="H6", size_hint_x=0.6,
            )
            name.bind(size=name.setter('text_size'))
            button_layout = BoxLayout(size_hint_x=0.4, spacing=dp(4))
            minus = MDRectangleFlatButton(
                text="-", size_hint=(1, 1), font_size="20sp",
                md_bg_color=app.theme_cls.accent_color, text_color=app.theme_cls.text_color
            )
            plus = MDRectangleFlatButton(
                text="+", size_hint=(1, 1), font_size="20sp",
                md_bg_color=app.theme_cls.primary_color, text_color=app.theme_cls.text_color
            )
            base_val = getattr(app, f"player_{key}")
            minus.disabled = self.temp[key] <= base_val
            plus.disabled = self.temp["points"] <= 0
            minus.bind(on_release=lambda inst, k=key: self.change(k, -1))
            plus.bind(on_release=lambda inst, k=key: self.change(k, +1))
            button_layout.add_widget(minus)
            button_layout.add_widget(plus)
            card.add_widget(name)
            card.add_widget(button_layout)
            lst.add_widget(card)

    def change(self, attr, delta):
        # CORREÇÃO: era self.temp += 1 (errado), agora é self.temp[attr]
        if delta > 0 and self.temp["points"] > 0:
            self.temp[attr] += 1
            self.temp["points"] -= 1
        elif delta < 0:
            app = MDApp.get_running_app()
            base_val = getattr(app, f"player_{attr}")
            if self.temp[attr] > base_val:
                self.temp[attr] -= 1
                self.temp["points"] += 1
        self.render()

    def reset_temp(self):
        app = MDApp.get_running_app()
        self.temp = {
            "strength": app.player_strength, "agility": app.player_agility,
            "intelligence": app.player_intelligence, "vitality": app.player_vitality,
            "perception": app.player_perception, "points": app.player_attribute_points,
        }
        self.render()

    def confirm(self):
        app = MDApp.get_running_app()
        app._set_player_strength(self.temp["strength"])
        app._set_player_agility(self.temp["agility"])
        app._set_player_intelligence(self.temp["intelligence"])
        app._set_player_vitality(self.temp["vitality"])
        app._set_player_perception(self.temp["perception"])
        app.player_attribute_points = self.temp["points"]
        app.show_info_dialog("Atributos", "Distribuição confirmada.")
        app.root.current = 'home_screen'# main.py (parte 3A/5)

class ClassroomScreen(BaseScreen):
    classes_info = [
        {"nome": "Monarca das Sombras", "descricao": "Classe única e lendária de Sung Jin-Woo. Permite extrair e comandar um exército de soldados das sombras."},
        {"nome": "Necromante", "descricao": "Classe inicial focada em ressuscitar e controlar mortos-vivos. Evolui para Monarca das Sombras no caso de Jin-Woo."},
        {"nome": "Lutador", "descricao": "Caçadores especializados em combate corpo a corpo, com alta força e resistência física."},
        {"nome": "Mago", "descricao": "Caçadores que utilizam magia para ataque, defesa, cura ou suporte estratégico."},
        {"nome": "Arqueiro", "descricao": "Focados em ataques de longo alcance com arcos, bestas ou outras armas de projétil."},
        {"nome": "Assassino", "descricao": "Caçadores ágeis e furtivos, mestres em ataques surpresa e danos rápidos a alvos únicos."},
        {"nome": "Curandeiro", "descricao": "Habilidades de suporte essenciais para grupos, restaurando saúde e aplicando buffs em aliados."}
    ]

    def on_enter(self, *args): self.populate_classes()

    def populate_classes(self):
        list_widget = self.ids.class_list
        list_widget.clear_widgets()
        palette = [
            (0.1, 0.1, 0.3, 0.8), (0.3, 0.1, 0.1, 0.8), (0.1, 0.3, 0.1, 0.8),
            (0.3, 0.3, 0.1, 0.8), (0.1, 0.3, 0.3, 0.8), (0.3, 0.1, 0.3, 0.8),
            (0.2, 0.2, 0.2, 0.8),
        ]
        app = MDApp.get_running_app()
        class_points_map = {
            "Lutador": app.class_strength_points,
            "Mago": app.class_intelligence_points,
            "Assassino": app.class_agility_points,
            "Curandeiro": app.class_vitality_points,
            "Arqueiro": app.class_perception_points,
        }

        for idx, cls in enumerate(self.classes_info):
            card = MDCard(
                orientation="vertical", padding=dp(12), spacing=dp(6),
                size_hint_y=None, height=dp(160),
                radius=[12], elevation=3,
                md_bg_color=palette[idx % len(palette)],
            )
            title = MDLabel(
                text=f"[b]{cls['nome'].upper()}[/b]", markup=True, halign="center",
                valign="middle", font_style="H6", size_hint_y=None, height=dp(30),
                color=(1,1,1,1)
            )
            title.bind(size=title.setter("text_size"))

            class_name_for_points = cls['nome']
            current_class_points = class_points_map.get(class_name_for_points, 0)
            points_label = MDLabel(
                text=f"Pontos: {current_class_points}",
                halign="center",
                valign="middle",
                font_style="Subtitle1",
                size_hint_y=None,
                height=dp(20),
                color=(0.8, 0.8, 0.8, 1)
            )
            points_label.bind(size=points_label.setter("text_size"))

            description = MDLabel(
                text=cls['descricao'], halign="center", valign="top",
                font_style="Body2", size_hint_y=None, height=dp(90),
                color=(0.8,0.8,0.8,1)
            )
            description.bind(size=description.setter("text_size"))

            card.add_widget(title)
            if class_name_for_points not in ["Monarca das Sombras", "Necromante"]:
                card.add_widget(points_label)
            card.add_widget(description)
            list_widget.add_widget(card)

class LelexApp(MDApp):
    BASE_STATS = {"strength": 10, "agility": 8, "intelligence": 7, "vitality": 12, "perception": 9}

    player_name = StringProperty("Lelex")
    player_xp = NumericProperty(50)
    player_xp_max = NumericProperty(100)
    player_stamina = NumericProperty(75)
    player_stamina_max = NumericProperty(100)
    player_coins = NumericProperty(1000000)
    player_strength = NumericProperty(10)
    player_agility = NumericProperty(8)
    player_intelligence = NumericProperty(7)
    player_vitality = NumericProperty(12)
    player_perception = NumericProperty(9)
    player_attribute_points = NumericProperty(5)
    player_level = NumericProperty(1)
    player_level_max = NumericProperty(100)

    class_strength_points = NumericProperty(10 // 5)
    class_agility_points = NumericProperty(8 // 5)
    class_intelligence_points = NumericProperty(7 // 5)
    class_vitality_points = NumericProperty(12 // 5)
    class_perception_points = NumericProperty(9 // 5)

    exercises_data = {
        "Agachamento Livre (Bodyweight Squats)": {
            "tipo": "repeticao",
            "valor": 15,
            "instrucoes": "Fique em pé com os pés na largura dos ombros.\n\nFlexione os joelhos e desça o quadril como se fosse sentar em uma cadeira, mantendo as costas retas.\n\nDesça até as coxas ficarem paralelas ao chão.\n\nRetorne à posição inicial empurrando os calcanhares contra o chão.",
            "musculos": ["Quadríceps", "Glúteos", "Panturrilhas"]
        },
        "Flexão de Joelhos (Knee Push-ups)": {
            "tipo": "repeticao",
            "valor": 10,
            "instrucoes": "Apoie as mãos no chão na largura dos ombros e os joelhos no chão.\n\nMantenha o corpo reto dos joelhos até a cabeça.\n\nFlexione os cotovelos e desça o peito em direção ao chão.\n\nEmpurre de volta à posição inicial.",
            "musculos": ["Peito", "Tríceps", "Ombros"]
        },
        "Prancha (Plank)": {
            "tipo": "tempo",
            "valor": 30,
            "instrucoes": "Apoie os antebraços no chão com os cotovelos alinhados aos ombros.\n\nEstenda as pernas para trás, apoiando as pontas dos pés.\n\nMantenha o corpo reto da cabeça aos calcanhares.\n\nContraia o abdômen e segure a posição.",
            "musculos": ["Abdômen", "Lombar", "Ombros"]
        },
        "Elevação de Panturrilha (Calf Raises)": {
            "tipo": "repeticao",
            "valor": 20,
            "instrucoes": "Fique em pé com os pés na largura dos ombros.\n\nEleve os calcanhares do chão, ficando na ponta dos pés.\n\nSegure por 1 segundo no topo.\n\nDesça lentamente até os calcanhares tocarem o chão.",
            "musculos": ["Panturrilhas"]
        },
        "Afundo (Lunges)": {
            "tipo": "repeticao",
            "valor": 12,
            "instrucoes": "Fique em pé com os pés juntos.\n\nDê um passo à frente com uma perna.\n\nFlexione ambos os joelhos até 90 graus.\n\nEmpurre o pé da frente para voltar à posição inicial.\n\nAlterne as pernas.",
            "musculos": ["Quadríceps", "Glúteos", "Posteriores"]
        },
        "Flexão Padrão (Push-ups)": {
            "tipo": "repeticao",
            "valor": 10,
            "instrucoes": "Apoie as mãos no chão na largura dos ombros e as pontas dos pés.\n\nMantenha o corpo reto da cabeça aos calcanhares.\n\nFlexione os cotovelos e desça o peito em direção ao chão.\n\nEmpurre de volta à posição inicial.",
            "musculos": ["Peito", "Tríceps", "Ombros", "Core"]
        }
    }

    easy_exercises_pool = [
        "Agachamento Livre (Bodyweight Squats)", "Flexão de Joelhos (Knee Push-ups)",
        "Prancha (Plank)", "Elevação de Panturrilha (Calf Raises)", "Afundo (Lunges)",
        "Ponte (Glute Bridge)", "Abdominal Crunch", "Superman",
        "Tríceps no Banco (Dips - adaptado)", "Remada Invertida (Bodyweight Rows - adaptado)"
    ]
    advanced_exercises_pool = [
        "Flexão Padrão (Push-ups)", "Agachamento Búlgaro (Bulgarian Split Squats)",
        "Pistol Squats (Agachamento Unilateral)", "Flexão Diamante (Diamond Push-ups)",
        "Prancha Lateral (Side Plank)", "Burpees", "Mountain Climbers",
        "Leg Raises (Elevação de Pernas)", "Flexão Declinada (Deline Push-ups)",
        "Chin-ups/Pull-ups Invertidos (Inverted Chin-ups/Pull-ups)"
    ]

    store_pool = [
        {"id": "elixir_cura", "name": "Elixir de Cura", "price": 500, "effect": "heal"},
        {"id": "cristal_forca", "name": "Cristal de Força", "price": 800, "effect": "strength"},
        {"id": "adaga_serpente", "name": "Adaga da Serpente", "price": 700, "effect": "agility"},
        {"id": "tomo_sabedoria", "name": "Tomo da Sabedoria", "price": 900, "effect": "intelligence"},
        {"id": "amuleto_vital", "name": "Amuleto Vital", "price": 950, "effect": "vitality"},
        {"id": "lente_aguia", "name": "Lente da Águia", "price": 850, "effect": "perception"},
        {"id": "pedra_teleporte", "name": "Pedra de Teleporte", "price": 1500, "effect": "teleport"},
        {"id": "chave_reset", "name": "Chave de Reset de Atributos", "price": 2000, "effect": "reset"},
        {"id": "chave_dungeon", "name": "Chave de Dungeon", "price": 1800, "effect": "dungeon"},
        {"id": "caixa_misteriosa", "name": "Caixa Misteriosa", "price": 1200, "effect": "random"},
    ]
    store_current_offers = []
    store_last_refresh = ""

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        self.store = JsonStore('save.json')
        self.load_game()
        Builder.load_string(KV)
        screen_manager = MDScreenManager()
        screen_manager.add_widget(RecruitmentScreen())
        screen_manager.add_widget(HomeScreen())
        screen_manager.add_widget(ExercisesScreen())
        screen_manager.add_widget(StoreScreen())
        screen_manager.add_widget(AttributesScreen())
        screen_manager.add_widget(ClassroomScreen())
        Clock.schedule_interval(self.regen_stamina, 60)
        return screen_manager# main.py (parte 3B/5)

    def on_stop(self):
        self.save_game()

    def save_game(self):
        self.store.put('player',
            name=self.player_name, xp=self.player_xp, xp_max=self.player_xp_max,
            stamina=self.player_stamina, stamina_max=self.player_stamina_max, coins=self.player_coins,
            strength=self.player_strength, agility=self.player_agility, intelligence=self.player_intelligence,
            vitality=self.player_vitality, perception=self.player_perception,
            attribute_points=self.player_attribute_points, level=self.player_level,
            class_str=self.class_strength_points, class_agi=self.class_agility_points,
            class_int=self.class_intelligence_points, class_vit=self.class_vitality_points,
            class_per=self.class_perception_points,
            store_offers=self.store_current_offers, store_refresh=self.store_last_refresh
        )

    def load_game(self):
        if self.store.exists('player'):
            p = self.store.get('player')
            self.player_name = p.get('name', 'Lelex')
            self.player_xp = p.get('xp', 50)
            self.player_xp_max = p.get('xp_max', 100)
            self.player_stamina = p.get('stamina', 75)
            self.player_stamina_max = p.get('stamina_max', 100)
            self.player_coins = p.get('coins', 1000000)
            self.player_strength = p.get('strength', self.BASE_STATS["strength"])
            self.player_agility = p.get('agility', self.BASE_STATS["agility"])
            self.player_intelligence = p.get('intelligence', self.BASE_STATS["intelligence"])
            self.player_vitality = p.get('vitality', self.BASE_STATS["vitality"])
            self.player_perception = p.get('perception', self.BASE_STATS["perception"])
            self.player_attribute_points = p.get('attribute_points', 5)
            self.player_level = p.get('level', 1)
            self.class_strength_points = p.get('class_str', self.BASE_STATS["strength"] // 5)
            self.class_agility_points = p.get('class_agi', self.BASE_STATS["agility"] // 5)
            self.class_intelligence_points = p.get('class_int', self.BASE_STATS["intelligence"] // 5)
            self.class_vitality_points = p.get('class_vit', self.BASE_STATS["vitality"] // 5)
            self.class_perception_points = p.get('class_per', self.BASE_STATS["perception"] // 5)
            self.store_current_offers = p.get('store_offers', [])
            self.store_last_refresh = p.get('store_refresh', '')

    def regen_stamina(self, dt):
        if self.player_stamina < self.player_stamina_max:
            self.player_stamina = min(self.player_stamina + 1, self.player_stamina_max)
            if self.root and self.root.current == 'home_screen':
                self.update_home_screen()

    def update_home_screen(self):
        if self.root and self.root.current == 'home_screen':
            self.root.get_screen('home_screen').on_pre_enter()

    def on_player_xp(self, instance, value):
        self.check_level_up()
        self.update_home_screen()

    def on_player_level(self, instance, value):
        self.player_xp_max = 100 + (self.player_level * 10)
        self.update_home_screen()

    def check_level_up(self):
        levels_gained = 0
        while self.player_xp >= self.player_xp_max:
            self.player_xp -= self.player_xp_max
            self.player_level += 1
            self.player_attribute_points += 1
            levels_gained += 1
        if levels_gained > 0:
            self.show_info_dialog("Level Up!", f"Você subiu {levels_gained} nível(is)!\nAgora é Nível {self.player_level}\nRanking: {self.get_player_ranking()}\nClasse: {self.get_player_class()}")

    def get_player_ranking(self):
        level = self.player_level
        if 1 <= level <= 5: return "Jogador mais fraco"
        elif 6 <= level <= 10: return "Ranking E"
        elif 11 <= level <= 20: return "Ranking D"
        elif 21 <= level <= 35: return "Ranking C"
        elif 36 <= level <= 50: return "Ranking B"
        elif 51 <= level <= 65: return "Ranking A"
        elif 66 <= level <= 75: return "Rei dos mortos"
        elif 76 <= level <= 85: return "Caçador das sombras"
        elif 86 <= level <= 95: return "Soberano das sombras"
        elif 96 <= level <= self.player_level_max: return "Monarca das sombras"
        else: return "Lenda Suprema"

    def get_player_class(self):
        all_class_points = [
            self.class_strength_points, self.class_intelligence_points,
            self.class_agility_points, self.class_vitality_points,
            self.class_perception_points
        ]
        if all(p >= 20 for p in all_class_points):
            return "Monarca das Sombras"
        elif all(p >= 10 for p in all_class_points):
            return "Necromante"

        classes = {
            "Lutador": self.class_strength_points,
            "Mago": self.class_intelligence_points,
            "Assassino": self.class_agility_points,
            "Curandeiro": self.class_vitality_points,
            "Arqueiro": self.class_perception_points
        }
        max_class = max(classes, key=classes.get)
        if classes[max_class] == 0:
            return "Nenhuma Classe"
        return max_class

    def update_class_points(self, attr_name, old_value, new_value):
        if new_value > old_value:
            gained_blocks = (new_value // 5) - (old_value // 5)
            if gained_blocks > 0:
                if attr_name == "strength":
                    self.class_strength_points += gained_blocks
                elif attr_name == "intelligence":
                    self.class_intelligence_points += gained_blocks
                elif attr_name == "agility":
                    self.class_agility_points += gained_blocks
                elif attr_name == "vitality":
                    self.class_vitality_points += gained_blocks
                elif attr_name == "perception":
                    self.class_perception_points += gained_blocks

                self.update_home_screen()
                if self.root and self.root.current == 'classroom_screen':
                    self.root.get_screen('classroom_screen').populate_classes()

    def _set_player_strength(self, value):
        old_value = self.player_strength
        self.player_strength = value
        self.update_class_points("strength", old_value, value)

    def _set_player_agility(self, value):
        old_value = self.player_agility
        self.player_agility = value
        self.update_class_points("agility", old_value, value)

    def _set_player_intelligence(self, value):
        old_value = self.player_intelligence
        self.player_intelligence = value
        self.update_class_points("intelligence", old_value, value)

    def _set_player_vitality(self, value):
        old_value = self.player_vitality
        self.player_vitality = value
        self.update_class_points("vitality", old_value, value)

    def _set_player_perception(self, value):
        old_value = self.player_perception
        self.player_perception = value
        self.update_class_points("perception", old_value, value)

    def get_daily_exercises(self):
        # EXERCÍCIOS FIXOS E PROGRESSIVOS (não aleatórios)
        exercises = [
            "Agachamento Livre (Bodyweight Squats)",
            "Flexão de Joelhos (Knee Push-ups)",
            "Prancha (Plank)"
        ]

        # Desbloqueia exercícios fixos conforme evolui
        if self.player_level >= 5:
            exercises.append("Afundo (Lunges)")
        if self.player_level >= 10:
            exercises.append("Elevação de Panturrilha (Calf Raises)")
        if self.player_level >= 15:
            # No nível 15, troca flexão de joelhos por flexão padrão
            exercises.remove("Flexão de Joelhos (Knee Push-ups)")
            exercises.append("Flexão Padrão (Push-ups)")

        return exercises

    def apply_item_effect(self, item):
        eff = item.get("effect")
        msg = "Item adquirido."

        if eff == "heal":
            before = self.player_stamina
            self.player_stamina = min(self.player_stamina + 40, self.player_stamina_max)
            gained = self.player_stamina - before
            self.player_xp += 10
            msg = f"Elixir usado: +{gained} de Stamina e +10 XP."
        elif eff == "strength": self._set_player_strength(self.player_strength + 1); msg = "Força +1 permanente."
        elif eff == "agility": self._set_player_agility(self.player_agility + 1); msg = "Agilidade +1 permanente."
        elif eff == "intelligence": self._set_player_intelligence(self.player_intelligence + 1); msg = "Inteligência +1 permanente."
        elif eff == "vitality": self._set_player_vitality(self.player_vitality + 1); msg = "Vitalidade +1 permanente."
        elif eff == "perception": self._set_player_perception(self.player_perception + 1); msg = "Percepção +1 permanente."
        elif eff == "reset":
            base = self.BASE_STATS
            total_spent = (self.player_strength - base["strength"] +
                          self.player_agility - base["agility"] +
                          self.player_intelligence - base["intelligence"] +
                          self.player_vitality - base["vitality"] +
                          self.player_perception - base["perception"])

            self._set_player_strength(base["strength"])
            self._set_player_agility(base["agility"])
            self._set_player_intelligence(base["intelligence"])
            self._set_player_vitality(base["vitality"])
            self._set_player_perception(base["perception"])

            self.class_strength_points = base["strength"] // 5
            self.class_agility_points = base["agility"] // 5
            self.class_intelligence_points = base["intelligence"] // 5
            self.class_vitality_points = base["vitality"] // 5
            self.class_perception_points = base["perception"] // 5

            self.player_attribute_points += total_spent
            msg = f"Atributos resetados. Você recebeu {total_spent} ponto(s) para redistribuir."
        elif eff == "teleport": self.player_coins += 100; msg = "Pedra de Teleporte ativada: +100 moedas."
        elif eff == "dungeon": self.player_xp += 25; msg = "Chave de Dungeon usada: +25 XP."
        elif eff == "random":
            base_items = [i for i in self.store_pool if i["id"]!= "caixa_misteriosa"]
            chosen = random.choice(base_items)
            sub_msg = self.apply_item_effect(chosen)
            msg = f"Caixa Misteriosa revelou: {chosen['name']}. {sub_msg}"
        if eff in ["heal", "dungeon"]: self.check_level_up()
        return msg

    def show_exit_dialog(self):
        self.dialog = MDDialog(
            title="[color=#ADD8E6]Notificação[/color]",
            text="Seu coração vai Parar em 0,2 Segundos! Deseja se tornar um jogador?",
            buttons=[
                MDRectangleFlatButton(
                    text="SIM", on_release=self.accept_recruitment,
                    md_bg_color=self.theme_cls.primary_color, text_color=self.theme_cls.text_color,
                ),
                MDRectangleFlatButton(
                    text="NÃO", on_release=self.exit_app,
                    md_bg_color=(1, 0, 0, 1), text_color=(1, 1, 1, 1),
                ),
            ],
        )
        self.dialog.open()

    def accept_recruitment(self, obj): self.dialog.dismiss(); self.root.current = 'home_screen'
    def close_dialog(self, obj): self.dialog.dismiss()
    def exit_app(self, obj): self.stop()

    def show_info_dialog(self, title, text):
        self.info_dialog = MDDialog(
            title=title, text=text,
            buttons=[MDFlatButton(text="OK", on_release=lambda x: self.info_dialog.dismiss())],
        )
        self.info_dialog.open()

if __name__ == "__main__":
    LelexApp().run()
