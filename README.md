# minimalnotworkingexample
manage dbconnection and appstatus and dbtables


### main: mc-desktop.py
hier werden Objekte von DbConnection und ApplicationStatus erzeugt  
um im weiteren immer darauf zuzugreifen und properties zu manipulieren.

*wichtig ist, dass ich jeweils exakt einmal ein objekt davon erzeuge, damit alle immer die gleichen Informationen haben*

### appstatus
class ApplicationStatus  
enthält bspw CurrentDate als property und hat funktionen um die Properties zu ändern

*hier ist Zugriff auf ein DbConnection Objekt nötig und die DbTables*

### dbconnection
class DbConnection  
ein Objekt dieser Klasse hält eine Datenbankverbindung inne.  
Die Datenbankverbindung wird fast überall in der App benötigt

### dbtables
BESONDERS PROBLEMATISCH  
enthält Klassendefinitionen zu tables aus der Datenbank.  
Die Klassendefinitionen müssen so sein wie sie sind: sie benötigen Base (und engine) von DbConnection  
aber von vornherein, also man kann ihnen Base nicht im Konstruktor übergeben. 

*keinen blassen Schimmer, was man hier tun könnte*
