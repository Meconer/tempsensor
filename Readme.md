## Rapportering av temperatur och luftfuktighet till blynk

På en nyinstallerad Raspberry Pi Os:

blynkToken.py finns för att slippa lägga upp token på github

Kopiera in tempsensor.py och blynkToken.py med sftp user@host. T.ex:

>sftp mats@zeroalpha

>put tempsensor.py

>put blynkToken.py


Testa att köra tempsensor.py från pajen med :

>python tempsensor.py


Lägg in en rad i crontab med 
>crontab -e

med innehållet

>*/10 * * * * python ~/tempsensor.py

som gör att scriptet tempsensor.py i hemkatalogen körs var tionde minut