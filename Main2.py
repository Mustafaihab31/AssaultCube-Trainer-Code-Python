# Import Packs
import PyQt5.QtWidgets as Q
import PyQt5.QtGui as G
from pymem import *
from pymem.process import *
import time

# Get The Game Name And Module Name

Game = Pymem("ac_client.exe")
module = pymem.process.module_from_name(Game.process_handle, "ac_client.exe").lpBaseOfDll
# Assign Variables With Offsets
rifle_offsets = [0x8, 0xE38, 0x64, 0x34, 0x98, 0xBDC]
health_offsets = [0xEC]
bomb_offset = [0x144]
sniper_offset = [0x13C]
pistol_offset = [0x12C]
sub_machine_offset = [0x8, 0x1AC, 0x454]
shotgun_offset = [0x134]
carbine_offset = [0x130]
armmor_offset = [0xF0]
dual_pistol_offset = [0x148]


time.sleep(1)

# Define Window And Tabs
class window(Q.QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Assault Cube Trainer V 1.2")
        self.setGeometry(500,500,400,300)

        tabwidget = Q.QTabWidget()
        tabwidget.addTab(Tab1(), "Values Changer")
        tabwidget.addTab(tab2(), "?")

        vbox = Q.QVBoxLayout()
        vbox.addWidget(tabwidget)

        self.setLayout(vbox)


# Define Tab1
class Tab1(Q.QWidget):
    def __init__(self):
        super().__init__()



        self.setLayout(Q.QVBoxLayout())




        chose_gun_lablel = Q.QLabel("Chose A Gun To Refill Default Is Rifle")
        chose_gun_lablel.setFont(G.QFont("Arial", 16))
        self.layout().addWidget(chose_gun_lablel)

        weapon_selector = Q.QComboBox()

        weapon_selector.addItem("Rifle")
        weapon_selector.addItem("Sniper")
        weapon_selector.addItem("Pistol")
        weapon_selector.addItem("Carbine")
        weapon_selector.addItem("Submachine Gun")
        weapon_selector.addItem("Shotgun")
        weapon_selector.addItem("Dual Pistol")

        self.layout().addWidget(weapon_selector)


        ammo_Text =Q.QLabel("Set Ammo")
        ammo_Text.setFont(G.QFont("Arial", 24))
        self.layout().addWidget(ammo_Text)

        ammo_button = Q.QPushButton("Refill", clicked = lambda: excuteammorefill())
        self.layout().addWidget(ammo_button)

        health_text = Q.QLabel("Set Health")
        health_text.setFont(G.QFont("Arial", 24))
        self.layout().addWidget(health_text)

        health_button = Q.QPushButton("Set", clicked = lambda: excutehealthset())
        self.layout().addWidget(health_button)



        bomb_text = Q.QLabel("Set Bomb")
        bomb_text.setFont(G.QFont("Arial", 24))
        self.layout().addWidget(bomb_text)

        bomb_button = Q.QPushButton("Set", clicked = lambda: excutebombset())
        self.layout().addWidget(bomb_button)

        Armour_text = Q.QLabel("Set Armour")
        Armour_text.setFont(G.QFont("Arial", 24))
        self.layout().addWidget(Armour_text)

        Armour_button = Q.QPushButton("Set", clicked = lambda: excuteArmourset())
        self.layout().addWidget(Armour_button)






        def excutehealthset():
                Game.write_int(getPointerAddr(module + 0x0018AC00, health_offsets), 300000)


        def excuteammorefill():
                selector_text = weapon_selector.currentText()

                if selector_text == "Rifle":
                    Game.write_int(getPointerAddr(module + 0x00183828, rifle_offsets), 300000)
                if selector_text == "Sniper":
                    Game.write_int(getPointerAddr(module + 0x0017E0A8, sniper_offset), 300000)
                if selector_text == "Pistol":
                    Game.write_int(getPointerAddr(module + 0x0018AC00, pistol_offset), 300000)
                if selector_text == "Submachine Gun":
                    Game.write_int(getPointerAddr(module + 0x00183828, sub_machine_offset), 300000)
                if selector_text == "Shotgun":
                    Game.write_int(getPointerAddr(module + 0x0018AC00, shotgun_offset), 300000)
                if selector_text == "Carbine":
                    Game.write_int(getPointerAddr(module + 0x0017E0A8, carbine_offset), 300000)
                if selector_text == "Dual Pistol":
                    Game.write_int(getPointerAddr(module + 0x0018AC00, dual_pistol_offset), 300000)



        def excutebombset():
                Game.write_int(getPointerAddr(module + 0x0018AC00, bomb_offset), 300)
        def excuteArmourset():
                Game.write_int(getPointerAddr(module + 0x0017E0A8, armmor_offset), 300000)

        def getPointerAddr(base, offsets):
                addr = Game.read_int(base)
                for offset in offsets:
                    if offset != offsets[-1]:
                        addr = Game.read_int(addr + offset)

                addr = addr + offsets[-1]
                return addr



# hahaha


class tab2(Q.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(Q.QVBoxLayout())

        coming_text = Q.QLabel("Coming Soon")
        coming_text.setFont(G.QFont("Arial", 50))
        self.layout().addWidget(coming_text)










app = Q.QApplication([])
Window = window()
Window.show()
app.exec_()

