import requests
from datetime import datetime


class GKIdojarasLekero:
    def __init__(self):
        self.api_url = "https://api.open-meteo.com/v1/forecast"
        self.varosok = {
            "Budapest": {"lat": 47.4979, "lon": 19.0402},
            "Debrecen": {"lat": 47.5316, "lon": 21.6273},
            "Szeged": {"lat": 46.2530, "lon": 20.1414},
            "Pecs": {"lat": 46.0727, "lon": 18.2320},
            "Gyor": {"lat": 47.6875, "lon": 17.6504}
        }

    def gk_leker_idojaras(self, varos):
        try:
            if varos not in self.varosok:
                raise ValueError(f"Nem ismert város: {varos}")

            koordinatak = self.varosok[varos]
            params = {
                "latitude": koordinatak["lat"],
                "longitude": koordinatak["lon"],
                "current_weather": True,
                "timezone": "Europe/Budapest"
            }

            response = requests.get(self.api_url, params=params, timeout=5)
            response.raise_for_status()

            data = response.json()

            return GKIdojaras(
                varos=varos,
                homerseklet=data["current_weather"]["temperature"],
                szelsebesseg=data["current_weather"]["windspeed"],
                ido=data["current_weather"]["time"],
                weathercode=data["current_weather"]["weathercode"]
            )

        except requests.exceptions.Timeout:
            print("Hiba: Az időjárás API nem válaszolt időben!")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Hiba: Nem sikerült csatlakozni az API-hoz: {e}")
            return None
        except KeyError as e:
            print(f"Hiba: Hiányzó adat a válaszban: {e}")
            return None
        except ValueError as e:
            print(f"Hiba: {e}")
            return None

    def gk_osszes_varos_listaja(self):
        return list(self.varosok.keys())


class GKIdojaras:
    def __init__(self, varos, homerseklet, szelsebesseg, ido, weathercode):
        self.varos = varos
        self.homerseklet = homerseklet
        self.szelsebesseg = szelsebesseg
        self.ido = ido
        self.weathercode = weathercode
        self.leiras = self.gk_weathercode_leiras()

    def gk_weathercode_leiras(self):
        kodok = {
            0: "Tiszta ég",
            1: "Főleg tiszta",
            2: "Részben felhős",
            3: "Borult",
            45: "Köd",
            48: "Zúzmara",
            51: "Enyhe szitálás",
            53: "Közepes szitálás",
            55: "Erős szitálás",
            61: "Enyhe eső",
            63: "Közepes eső",
            65: "Erős eső",
            71: "Enyhe havazás",
            73: "Közepes havazás",
            75: "Erős havazás",
            77: "Hószállingózás",
            80: "Enyhe zápor",
            81: "Közepes zápor",
            82: "Erős zápor",
            85: "Enyhe hózápor",
            86: "Erős hózápor",
            95: "Zivatar",
            96: "Zivatar jégesővel",
            99: "Erős zivatar jégesővel"
        }
        return kodok.get(self.weathercode, "Ismeretlen")

    def gk_ikon_tipus(self):
        if self.weathercode == 0 or self.weathercode == 1:
            return "napsutes"
        elif self.weathercode in [2, 3]:
            return "felhos"
        elif 61 <= self.weathercode <= 82:
            return "esos"
        elif 71 <= self.weathercode <= 86:
            return "havazas"
        elif self.weathercode >= 95:
            return "zivatar"
        else:
            return "felhos"

    def __str__(self):
        return f"{self.varos}: {self.homerseklet}°C, {self.leiras}, Szél: {self.szelsebesseg} km/h"


class GKIdojarasArchivum:
    def __init__(self):
        self.lekerdezesek = []

    def hozzaad(self, idojaras):
        if idojaras:
            self.lekerdezesek.append({
                "varos": idojaras.varos,
                "homerseklet": idojaras.homerseklet,
                "leiras": idojaras.leiras,
                "ido": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    def gk_atlag_homerseklet(self):
        if not self.lekerdezesek:
            return 0
        return sum(lek["homerseklet"] for lek in self.lekerdezesek) / len(self.lekerdezesek)

    def gk_legmelegebb_varos(self):
        if not self.lekerdezesek:
            return None
        return max(self.lekerdezesek, key=lambda x: x["homerseklet"])

    def gk_leghidegebb_varos(self):
        if not self.lekerdezesek:
            return None
        return min(self.lekerdezesek, key=lambda x: x["homerseklet"])

    def __str__(self):
        if not self.lekerdezesek:
            return "Nincs lekérdezés az archívumban."

        szoveg = "IDŐJÁRÁS ARCHÍVUM:\n"
        szoveg += f"Összes lekérdezés: {len(self.lekerdezesek)}\n"
        szoveg += f"Átlag hőmérséklet: {self.gk_atlag_homerseklet():.1f}°C\n\n"

        for i, lek in enumerate(self.lekerdezesek, 1):
            szoveg += f"{i}. {lek['varos']}: {lek['homerseklet']}°C - {lek['leiras']} ({lek['ido']})\n"

        return szoveg