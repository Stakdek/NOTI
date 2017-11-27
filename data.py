# -*- coding: utf-8 -*-
data = ['''Man is the best computer we can put aboard a spacecraft… and the only one that can be mass produced with unskilled labor. (Wernher von Braun) (Der Mensch ist der beste Computer, den wir in ein Raumschiff stecken können ... und der einzige der sich in Massenproduktion durch ungelernte Arbeit herstellen lässt.''',

        '''Es gibt Beweise, die auf die alten Griechen zurückgehen, und heutzutage immer noch gültig sind. Andrew J. Wiles, Mathematiker ''',

        '''Um eine Einkommensteuererklärung abgeben zu können, muß man ein Philosoph sein. Für einen Mathematiker ist es zu schwierig. Albert Einstein ''',

        '''Ich sei, gewähret mir die Bitte, in eurem Netzwerk der Dritte.''',

        '''Die technische Entwicklung der Kernwaffen seit den 1940er Jahren hat eine große Vielfalt unterschiedlicher Varianten hervorgebracht. Unterschieden werden grundsätzlich Atombomben nach dem Kernspaltungs- oder Fissionsprinzip („klassische“ Atombombe) und nach dem Kernfusionsprinzip (Wasserstoff- oder H-Bombe).''',

        '''Erst wenn der letzte FTP Server kostenpflichtig, der letzte GNU-Sourcecode verkauft, der letzte Algorithmus patentiert, der letzte Netzknoten verkommerzialisert ist, werdet Ihr merken, dass Geld nicht von alleine programmiert.''',

        '''Man kann nicht sagen, welcher Programmteil den Hauptteil der Leistung fressen wird. Da Engpässe oft an überraschenden Stellen auftauchen, soll man nichts zur Erhöhung der Geschwindigkeit einbauen, bevor man gezeigt hat, wo der Engpass sitzt.''',

        '''Miss die Programmlaufzeit. Feile erst an der Geschwindigkeit, wenn du sie gemessen hast, und selbst dann erst, wenn der betrachtete Teil einen dominierenden Anteil der Rechenzeit frisst.''',

        '''Klein ist schön.''',

        '''Bevorzuge Portierbarkeit vor Effizienz.''',

        '''Schlechter ist besser.''',

        '''Regel der Transparenz: Entwirf mit dem Ziel der Durchschaubarkeit, um die Fehlersuche zu vereinfachen.''',

        '''Man is the best computer we can put aboard a spacecraft...''',

        '''Es gibt Beweise, die auf die alten Griechen zurückgehen''',

        '''Um eine Einkommensteuererklärung abgeben zu können, muß man ein Philosoph sein.''',

        '''Ich sei, gewähret mir die Bitte in eurem Netzwerk der Dritte.''',

        '''Die technische Entwicklung der Kernwaffen seit den 1940er Jahren hat eine große Vielfalt unterschiedlicher Varianten hervorgebracht.''',

        '''Erst wenn der letzte FTP Server kostenpflichtig, der letzte GNU-Sourcecode verkauft, der letzte Algorithmus patentiert, der letzte Netzknoten verkommerzialisert ist werdet Ihr merken, dass Geld nicht von alleine programmiert.''',

        '''Regel der Transparenz: Entwirf mit dem Ziel der Durchschaubarkeit, um die Fehlersuche zu vereinfachen.''',

        '''Regel der Trennung: Trenne den Grundgedanken von der Umsetzung, trenne die Schnittstellen von der Verarbeitungslogik.''',

        '''Regel der Klarheit: Klarheit ist besser als Gerissenheit.''',

        '''Unix wurde nicht entwickelt, um seine Benutzer daran zu hindern, dumme Dinge zu tun, denn das würde diese auch davon abhalten, schlaue Dinge zu tun.''',

        '''Regel 1: Man kann nicht sagen, welcher Programmteil den Hauptteil der Leistung fressen wird. Da Engpässe oft an überraschenden Stellen auftauchen, soll man nichts zur Erhöhung der Geschwindigkeit einbauen, bevor man gezeigt hat, wo der Engpass sitzt.''',

        '''Regel 2: Miss die Programmlaufzeit. Feile erst an der Geschwindigkeit, wenn du sie gemessen hast, und selbst dann erst, wenn der betrachtete Teil einen dominierenden Anteil der Rechenzeit frisst.''',

        '''Regel 3: Hochgezüchtete Algorithmen sind langsam, wenn die Eingabedatenmenge n klein ist, und das ist der Normalfall. Hochgezüchtete Algorithmen haben große Fixkosten. Solange man nicht weiß, dass n häufig große Werte annehmen wird, soll man auf hochgezüchtete Algorithmen verzichten. (Und selbst wenn n groß wird, gilt zuerst Regel 2.)''',

        '''Regel 4: Hochgezüchtete Algorithmen sind fehleranfälliger als einfache, und sie sind viel schwieriger zu implementieren. Benutze sowohl einfache Algorithmen als auch einfache Datenstrukturen.''',

        '''Regel 5: Daten sind wichtiger. Wenn du die richtigen Datenstrukturen gewählt hast und alles gut gestaltet ist, werden sich die Algorithmen fast immer von alleine ergeben. Datenstrukturen sind das zentrale Thema des Programmierens, nicht Algorithmen.''',

        '''Regel 6: Es gibt keine Regel 6.''',

        '''Klein ist schön.''',

        '''Gestalte jedes Programm so, dass es eine Aufgabe gut erledigt.''',

        '''Erzeuge so bald wie möglich einen funktionierenden Prototyp.''',

        '''Bevorzuge Portierbarkeit vor Effizienz.''',

        '''Speichere Daten in einfachen Textdateien.''',

        '''Verwende die Hebelwirkung der Software zu deinem Vorteil.''',

        '''Verwende Shell-Skripte, um die Hebelwirkung und die Portierbarkeit zu verbessern.''',

        '''Vermeide Benutzeroberflächen, die den Benutzer fesseln.''',

        '''Mache jedes Programm zu einem Filter.''',

        '''Lass den Benutzer die Umgebung nach seinen Bedürfnissen festlegen.''',

        '''Mache Betriebssystemkerne klein und leichtgewichtig.''',

        '''Benutze Kleinschreibung und halte Befehlsnamen kurz.''',

        '''Verschwende keine Bäume.''',

        '''Schweigen ist Gold.''',

        '''Denke parallel.''',

        '''Die Summe der Teile ist mehr als das Ganze.''',

        '''Suche die 90/10-Lösung.''',

        '''Schlechter ist besser.''',

        '''Denke hierarchisch.''',

        '''Regel der Modularität: Schreibe einfache Bestandteile, die durch saubere Schnittstellen verbunden werden.''',

        '''Regel der Klarheit: Klarheit ist besser als Gerissenheit.''',

        '''Regel des Zusammenbaus: Entwirf Programme so, dass sie mit anderen Programmen verknüpft werden können.''',

        '''Regel der Trennung: Trenne den Grundgedanken von der Umsetzung, trenne die Schnittstellen von der Verarbeitungslogik.''',

        '''Regel der Einfachheit: Entwirf mit dem Ziel der Einfachheit; füge Komplexität nur hinzu, wenn es unbedingt sein muss.''',

        '''Regel der Sparsamkeit: Schreibe nur dann ein großes Programm, wenn sich klar zeigen lässt, dass es anders nicht geht.''',

        '''Regel der Transparenz: Entwirf mit dem Ziel der Durchschaubarkeit, um die Fehlersuche zu vereinfachen.''',

        '''Regel der Robustheit: Robustheit ist das Kind von Transparenz und Einfachheit.''',

        '''Regel der Darstellung: Stecke das Wissen in die Datenstrukturen, so dass die Programmlogik dumm und robust sein kann.''',

        '''Regel der geringsten Überraschung: Mache beim Entwurf der Schnittstellen immer das Nächstliegende, welches für die wenigsten Überraschungen beim Benutzer sorgt.''',

        '''Regel der Stille: Wenn ein Programm nichts Überraschendes zu sagen hat, soll es schweigen.''',

        '''Regel des Reparierens: Wenn das Programm scheitert, soll es das lautstark und so früh wie möglich tun.''',

        '''Regel der Wirtschaftlichkeit: Die Arbeitszeit von Programmierern ist teuer; spare sie auf Kosten der Rechenzeit.''',

        '''Regel der Code-Generierung: Vermeide Handarbeit; schreibe Programme, die Programme schreiben, falls möglich.''',

        '''Regel der Optimierung: Erstelle Prototypen, bevor du dich an den Feinschliff machst. Mache es lauffähig, bevor du es optimierst.''',

        '''Regel der Vielseitigkeit: Misstraue allen Ansprüchen auf „den einzig wahren Weg“.''',

        '''Regel der Erweiterbarkeit: Entwirf für die Zukunft, denn sie wird schneller kommen als du denkst.''',

        '''Der Zugriff sowohl auf lokale Laufwerke wie auch Netzlaufwerke erfolgt über dieselbe Verzeichnisstruktur; es gibt nicht verschiedene Laufwerke, sondern alles sind Verzeichnisse und Dateien in derselben Baumstruktur.''',

        '''Virtuelle Laufwerke können ebenfalls problemlos realisiert werden, denn sie erscheinen ebenfalls nur als Verzeichnis. Jede Image-Datei an jedem Ort kann durch mounten in den Verzeichnisbaum an jeder Stelle eingebunden werden.''',

        '''Auch der Zugriff auf Geräte erfolgt über das Dateisystem. Einem Gerätetreiber wird eine Gerätedatei im Verzeichnis /dev zugeordnet; durch Lesen und Schreiben dieser Datei kann ein Programm mit dem Gerätetreiber kommunizieren.''',

        '''Auf Kernel-Daten kann ebenfalls über die Verzeichnisstruktur zugegriffen werden, und zwar über das Verzeichnis /proc.''',

        '''„Unix ist einfach. Es erfordert lediglich ein Genie, um seine Einfachheit zu verstehen.“ (Dennis Ritchie)''',

        '''„Unix wurde nicht entwickelt, um seine Benutzer daran zu hindern, dumme Dinge zu tun, denn das würde diese auch davon abhalten, schlaue Dinge zu tun.“ (Doug Gwyn)''',

        '''„Unix sagt niemals ›bitte‹.“ (Rob Pike)''',
	'''Die erste Regel des Fight-Clubs ist: Man redet nicht über den Fight-Club.''',
    ]
