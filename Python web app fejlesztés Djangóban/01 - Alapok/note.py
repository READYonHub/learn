# 1.
import django

# 2.
# Django verzió kiiratás
#print(django.get_version())

# 3. 
# terminalba -> django-admin

# 4.
# terminalna -> django-admin startproject mysite . 
# létrehoz az aktuális mapában (a ponttal) egy új django projektet ami a startproject névre hallgat

# létrejön a manage.py és a mysite mapppa
# létrejön egy manage.py fájl, ami a django projekthez tartozo management command line eszköz készlet lesz
# a mysite mappában a projethez tartozó konfigurációs fájllaink lesznek
# a settings.py-ban vannak ténylegesen a beállítások, amiket majd a projekt hasznára tudunk majd használni 
# az urls.py-ban vannak azok az elérésiutvonalak amiket majd kiakarunk szolgálni , ha vlk pl böngészőböl megnézi az oldalt
# az asgi és wsgi akkor lesznek relevánsak, ha majd kiakarjuk publikálni az alkalmazásunkat és majd elkell döntenünk, hogy milyen futtatókörnyezetben van a projektünk futtatva

# 5.
# van lehetőségünk futtatni egy develoopment servert a manage.py fájl jóvoltából
# teminálba ->  python.exe .\manage.py runserver  
# ez elindit egy helyi developbent servert 
# [24/Apr/2024 15:18:14] "GET / HTTP/1.1" 200 10629
# latjuk a datumot, http kérés, indexe, http kod meret

# 6. 
# az app - az a projekten belül a saját környezetében teljes applikáció, gyakorlatilag a django projektek úgy vannak kitalálva, hogy jól elválasztható komponensekből vannak fölépítve ezek a projektek, hogy egyszerre több ember is tudjon rajta dolgozni
# 
# terminalba -> python.exe .\manage.py startapp example 
# ez létrehozott egy example mappát
# a benne lévő fájlok majd befognak csatlakoznia  projektbe a saját magunk írt kóddal együtt

# 7.
# az example-ban van egy view.py
# ezek gyakorlatilag azok a nézetek, azok a tartalmak, amiket elérhetővé akarunk tenni
# létre tudunk itt hozni a view-kban függvényeket, amiket elnevezünk valahogy és azok valamilyen tartalmaz szolgáltatnak a böngészőnek
# def index(request):   -> paraméterként a request-et adtam meg, ez a böngésző által iintézett kérés és a hozzá tartozó meta adatok
# return HttpResponse() -> vissza adunk valamilyen tartalmat, ez most még nem létezik, hozzuk létre vagy alt+enter és segít nekünk ezt beimportálni
# from django.http import HttpResponse -> ezt láthatjuk felül a gyorbillentyűzettel ha létrehoztuk
# paraméternek azt a tartalmat kell megadni amit vissza akarunk kapni
# a view az maga nem csinál semmit csak vissza add egy tartalmat, viszont ezt jelezni kell valahogy, hogy honnan és mikor 
# ezt az urls.py fájlban kell megadni 
# itt már van egy admin url, de ezt ki kell törölni és létrehozom a 
# path('', views.index, name="index"),
# a path() bejegyzésben megadok egy üres stringet ami a '',
# a views.index -> a views-ból szeretném az index függvényt, ehhez be kell importálnom alt+enter és importálás
# from example import views fog megjelenni felül
# még megadjuk, hogy melyik függvényt szeretném innen (name="index")
# ha ez kész inditsuk el a dev szervert
# terminal -> python.exe .\manage.py runserver
# ujratölti az alkalmazást, eltunt a default oldal és a mi view-nk jelenik meg
# ha a kódunkban báármilyen változás történt, mentés után a server automatikusan fríssiti,
# de sajnos nem böngésző szinten ezért frissitenünk kell azt is külön



