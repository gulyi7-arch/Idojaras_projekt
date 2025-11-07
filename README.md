Időjárás Információs Rendszer

Gulyás Kornél RBXQ1O

Feladat Leírása:
Ez az alkalmazás egy időjárás információs rendszer, amely valós időjárási adatokat kérdez le az internetről és jeleníti meg grafikusan. 
A program:
- Valós időjárási adatokat kérdez le webes API-ról (Open-Meteo)
- Megjeleníti az aktuális hőmérsékletet, időjárást és szélsebességet
- Turtle graphics ikonokat rajzol az időjárás típusa szerint
- Magyar városok időjárását tudja lekérdezni (Budapest, Debrecen, Szeged, Pécs, Győr)
- Archívumot vezet a lekérdezésekről
- Statisztikákat készít (legmelegebb, leghidegebb)

Modulok és Függvények

Turtle:
-turtle.Turtle
-turtle.Screen
-turtle.penup, pendown
-turtle.goto
-turtle.circle
-turtle.dot
-turtle.pencolor, fillcolor
-turtle.begin_fill, end_fill
-turtle.forward, right, left
-turtle.listen, onkey
-turtle.hideturtle, clear
-turtle.write
-datetime.now, .strftime
- requests.get
- response.json
- response.raise_for_status
- requests.exceptions.Timeout
- requests.exceptions.RequestException
- json.load

Osztályok

-GK_IdojarasLekero
-GK_Idojaras
-GK_IdojarasArchivum
-app

