import turtle
from GK_idojaras_lib import GKIdojarasLekero, GKIdojarasArchivum


class app:
    def __init__(self):
        self.ablak = turtle.Screen()
        self.ablak.title("Időjárás Információs Rendszer")
        self.ablak.setup(width=1000, height=700)
        self.ablak.bgcolor("lightblue")

        self.lekero = GKIdojarasLekero()
        self.archivum = GKIdojarasArchivum()
        self.varosok = self.lekero.gk_osszes_varos_listaja()
        self.aktualis_varos_index = 0
        self.aktualis_idojaras = None

        self.rajz_teknos = turtle.Turtle()
        self.rajz_teknos.hideturtle()
        self.szoveg_teknos = turtle.Turtle()
        self.szoveg_teknos.hideturtle()
        self.szoveg_teknos.speed(0)

        self.ablak.listen()
        self.ablak.onkey(self.idojaras_lekerdez, "space")
        self.ablak.onkey(self.kovetkezo_varos, "Right")
        self.ablak.onkey(self.elozo_varos, "Left")
        self.ablak.onkey(self.archivum_megjelenites, "a")
        self.ablak.onkey(self.utasitasok_megjelenites, "h")
        self.ablak.onkey(self.ablak.bye, "Escape")

        self.utasitasok_megjelenites()

        self.ablak.mainloop()

    def idojaras_lekerdez(self):
        self.rajz_teknos.clear()
        self.szoveg_teknos.clear()

        varos = self.varosok[self.aktualis_varos_index]

        self.szoveg_teknos.penup()
        self.szoveg_teknos.goto(0, 250)
        self.szoveg_teknos.write("Időjárás lekérdezése...", align="center", font=("Arial", 14, "normal"))

        self.aktualis_idojaras = self.lekero.gk_leker_idojaras(varos)

        if self.aktualis_idojaras:
            self.archivum.hozzaad(self.aktualis_idojaras)
            self.idojaras_megjelenites()
        else:
            self.szoveg_teknos.clear()
            self.szoveg_teknos.goto(0, 0)
            self.szoveg_teknos.write("Hiba: Nem sikerült lekérdezni az időjárást!", align="center",
                                     font=("Arial", 16, "bold"))

    def idojaras_megjelenites(self):
        self.rajz_teknos.clear()
        self.szoveg_teknos.clear()

        if not self.aktualis_idojaras:
            return

        self.szoveg_teknos.penup()
        self.szoveg_teknos.goto(0, 280)
        self.szoveg_teknos.write(f"IDŐJÁRÁS - {self.aktualis_idojaras.varos}", align="center",
                                 font=("Arial", 18, "bold"))

        self.szoveg_teknos.goto(0, 240)
        self.szoveg_teknos.write(f"{self.aktualis_idojaras.homerseklet}°C", align="center", font=("Arial", 36, "bold"))

        self.szoveg_teknos.goto(0, 190)
        self.szoveg_teknos.write(f"{self.aktualis_idojaras.leiras}", align="center", font=("Arial", 14, "normal"))

        self.szoveg_teknos.goto(0, 160)
        self.szoveg_teknos.write(f"Szélsebesség: {self.aktualis_idojaras.szelsebesseg} km/h", align="center",
                                 font=("Arial", 12, "normal"))

        ikon_tipus = self.aktualis_idojaras.gk_ikon_tipus()
        self.rajzol_ikon(ikon_tipus)

        self.szoveg_teknos.goto(-400, -300)
        self.szoveg_teknos.write(f"Város {self.aktualis_varos_index + 1}/{len(self.varosok)}",
                                 font=("Arial", 10, "normal"))

    def rajzol_ikon(self, tipus):
        self.rajz_teknos.speed(0)
        self.rajz_teknos.penup()

        if tipus == "napsutes":
            self.rajzol_nap()
        elif tipus == "felhos":
            self.rajzol_felh()
        elif tipus == "esos":
            self.rajzol_eso()
        elif tipus == "havazas":
            self.rajzol_ho()
        elif tipus == "zivatar":
            self.rajzol_villam()

    def rajzol_nap(self):
        self.rajz_teknos.goto(0, -50)
        self.rajz_teknos.pendown()
        self.rajz_teknos.pencolor("orange")
        self.rajz_teknos.fillcolor("yellow")
        self.rajz_teknos.begin_fill()
        self.rajz_teknos.circle(50)
        self.rajz_teknos.end_fill()

        self.rajz_teknos.penup()
        for _ in range(8):
            self.rajz_teknos.goto(0, 0)
            self.rajz_teknos.pendown()
            self.rajz_teknos.forward(80)
            self.rajz_teknos.penup()
            self.rajz_teknos.goto(0, 0)
            self.rajz_teknos.right(45)

    def rajzol_felh(self):
        self.rajz_teknos.goto(-60, 20)
        self.rajz_teknos.pendown()
        self.rajz_teknos.pencolor("gray")
        self.rajz_teknos.fillcolor("lightgray")
        self.rajz_teknos.begin_fill()
        self.rajz_teknos.circle(30)
        self.rajz_teknos.goto(0, 20)
        self.rajz_teknos.circle(40)
        self.rajz_teknos.goto(40, 20)
        self.rajz_teknos.circle(30)
        self.rajz_teknos.end_fill()

    def rajzol_eso(self):
        self.rajzol_felh()

        self.rajz_teknos.penup()
        self.rajz_teknos.pencolor("blue")
        self.rajz_teknos.pensize(2)

        for x in range(-40, 50, 20):
            self.rajz_teknos.goto(x, -20)
            self.rajz_teknos.pendown()
            self.rajz_teknos.goto(x - 10, -60)
            self.rajz_teknos.penup()

    def rajzol_ho(self):
        self.rajzol_felh()

        self.rajz_teknos.pencolor("white")
        self.rajz_teknos.fillcolor("white")

        for x in range(-40, 50, 20):
            self.rajz_teknos.penup()
            self.rajz_teknos.goto(x, -30)
            self.rajz_teknos.pendown()
            self.rajz_teknos.dot(10)
            self.rajz_teknos.goto(x - 5, -50)
            self.rajz_teknos.dot(8)

    def rajzol_villam(self):
        self.rajzol_felh()

        self.rajz_teknos.penup()
        self.rajz_teknos.goto(0, -20)
        self.rajz_teknos.pendown()
        self.rajz_teknos.pencolor("yellow")
        self.rajz_teknos.pensize(4)
        self.rajz_teknos.goto(-10, -40)
        self.rajz_teknos.goto(5, -40)
        self.rajz_teknos.goto(-5, -70)

    def kovetkezo_varos(self):
        self.aktualis_varos_index = (self.aktualis_varos_index + 1) % len(self.varosok)
        if self.aktualis_idojaras:
            self.idojaras_lekerdez()

    def elozo_varos(self):
        self.aktualis_varos_index = (self.aktualis_varos_index - 1) % len(self.varosok)
        if self.aktualis_idojaras:
            self.idojaras_lekerdez()

    def archivum_megjelenites(self):
        self.rajz_teknos.clear()
        self.szoveg_teknos.clear()

        self.szoveg_teknos.penup()
        self.szoveg_teknos.goto(0, 300)
        self.szoveg_teknos.write("IDŐJÁRÁS ARCHÍVUM", align="center", font=("Arial", 18, "bold"))

        if not self.archivum.lekerdezesek:
            self.szoveg_teknos.goto(0, 0)
            self.szoveg_teknos.write("Nincs lekérdezés az archívumban!", align="center", font=("Arial", 14, "normal"))
            return

        y_pos = 250
        self.szoveg_teknos.goto(0, y_pos)
        self.szoveg_teknos.write(f"Összes lekérdezés: {len(self.archivum.lekerdezesek)}", align="center",
                                 font=("Arial", 12, "normal"))

        y_pos -= 30
        self.szoveg_teknos.goto(0, y_pos)
        self.szoveg_teknos.write(f"Átlag hőmérséklet: {self.archivum.gk_atlag_homerseklet():.1f}°C", align="center",
                                 font=("Arial", 12, "normal"))

        legmelegebb = self.archivum.gk_legmelegebb_varos()
        y_pos -= 30
        self.szoveg_teknos.goto(0, y_pos)
        self.szoveg_teknos.write(f"Legmelegebb: {legmelegebb['varos']} ({legmelegebb['homerseklet']}°C)",
                                 align="center", font=("Arial", 12, "normal"))

        leghidegebb = self.archivum.gk_leghidegebb_varos()
        y_pos -= 30
        self.szoveg_teknos.goto(0, y_pos)
        self.szoveg_teknos.write(f"Leghidegebb: {leghidegebb['varos']} ({leghidegebb['homerseklet']}°C)",
                                 align="center", font=("Arial", 12, "normal"))

        y_pos -= 50
        self.szoveg_teknos.goto(-400, y_pos)
        self.szoveg_teknos.write("Lekérdezések:", font=("Arial", 12, "bold"))

        y_pos -= 30
        for lek in self.archivum.lekerdezesek[-10:]:
            self.szoveg_teknos.goto(-400, y_pos)
            self.szoveg_teknos.write(f"{lek['varos']}: {lek['homerseklet']}°C - {lek['leiras']}",
                                     font=("Arial", 10, "normal"))
            y_pos -= 25

    def utasitasok_megjelenites(self):
        self.szoveg_teknos.clear()
        self.rajz_teknos.clear()

        self.szoveg_teknos.penup()
        self.szoveg_teknos.goto(0, 300)
        self.szoveg_teknos.write("IDŐJÁRÁS INFORMÁCIÓS RENDSZER", align="center", font=("Arial", 18, "bold"))

        utasitasok = [
            "IRÁNYÍTÁS:",
            "SPACE - Időjárás lekérdezése",
            "RIGHT ARROW (→) - Következő város",
            "LEFT ARROW (←) - Előző város",
            "A - Archívum megtekintése",
            "H - Utasítások megjelenítése",
            "ESCAPE - Kilépés",
            "",
            "ELÉRHETŐ VÁROSOK:",
            "Budapest, Debrecen, Szeged, Pécs, Győr"
        ]

        y_pos = 220
        for utasitas in utasitasok:
            self.szoveg_teknos.goto(-350, y_pos)
            if "IRÁNYÍTÁS:" in utasitas or "ELÉRHETŐ VÁROSOK:" in utasitas:
                self.szoveg_teknos.write(utasitas, font=("Arial", 12, "bold"))
            else:
                self.szoveg_teknos.write(utasitas, font=("Arial", 11, "normal"))
            y_pos -= 30


if __name__ == "__main__":
    app()