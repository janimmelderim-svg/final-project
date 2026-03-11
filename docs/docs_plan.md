***A. Programmas apraksts***



 		**komandrinda** ir bez izskaistinājumiem bez smukām ikonām un sagatavotas vides. tās ikonas ko spiežu uz datora ir tikai vizuāls atvieglinājums. komandrinda ir termināli rakstāms teksts, ko izpilda dators. piemēram lai atvērtu failu vai folderi, es parasti izpildu dubultklikšķi. šajā gadījumā es ar tekstu rakstu terminālī un dators to izpilda.

 		**izdevumu izsekotājs** ir tēriņu apkopotājs. Šis rīks ļauj ievadīt, apskatīt un veidot kopsavilkumu iepriekš ievadītiem datiem par maniem izdevumiem.

 		**komandrindas uzdevumu izsekotājs** ir maza programma, kas izpilda darbības tikai ar tekstu, kas rakstīts termināli. Tas spēs apkopot ievadītos izdevumus un sakārtot izdevumus pa kategorijām un mēnešiem.

 

 	**Funkcionalitāte**

 			*Nebaidīties sapņot un pieļaut kļūdas. iespējams pilnu funkcionalitāti sapratīšu tikai rakstot kodu.*



 		1. *pievienot uzdevumu*

a) datums

datums ir YYYY-MM-DD formātā

b) summa

summa ir 11.00 divi cipari aiz komata

c) kategorija

kategorijas ir no iepriekš sagatavota saraksta, ko var pielāgot individuāli

d) apraksts

teksts, ko ievada, lai paskaidrotu izdevumu. var atkārtoties, var neatkārtoties

 	programma saglabā šo 4 konkrēto lietu virkni atmiņā

 		2. *parādīt izdevumus*

programma sakārto visus datus tabulā.

 		3. *filtrēt pēc mēneša*

visus ierakstus filtrē pēc mēneša un rāda kopsummu

 		4. *kopsumma pa kategorijām*

visus ierakstus filtrē pēc kategorijas un rāda kopsummu

 		5. *filtrēt pēc mēneša un kategorijas*

filtrs, kas atfiltrē mēnesi un kategoriju (**papildus funkcionalitāte, optional**)

 		6. *dzēst izdevumus*

dzēst izdevumus var pēc nr. sarakstā, nevis visus izdevumus uzreiz.

 		7. *CSV eksports*

CSV eksports ir datu iznese īpašā .csv failā, kur pēc tam var atvērt excel vai google sheet

 		8. *Datu persistance*

šis ir json fails. tas saglabā manus ievadītos datus uz diska, lai tie nepazustu. ja man nav šis json fails, tad katra ievade man neparādītos. tā ir kā vēsture, kas saglabājas.



***B. Datu struktūra***



Man ir jāievada 4 datu veidi -

a) datums

b) summa

c) kategorija

d) apraksts



1. Atveram failu (py programma.py)

2\. No izvēlnes izvēlamies "pievienot izdevumu" ar atbilstošo ciparu no izvēlnes (visticamāk tā būs 1. izvēle)

3\. ievadam summu (rakstam ciparu piem. 1.50)

4\. ievadam kategoriju. kategoriju izvēlas no jau iepriekš izveidota saraksta. (izvēlamies ciparu no 1. līdz ...)

5\. ievadam aprakstu. teksts ar ko paskaidrojam izdevumu (piem. pusdienas vai pārtika vai santehnika )



 	Vēl īsti nesaprotu, kā atvērt failu, lai tas paliek atvērts, jo idejiski iepriekšējā nedēļā lai ievadītu izdevumu katrs reizi bija jāraksta py. programma.py izdevums summa, bet iepriekšējās nedēļās guess.py minēšanas spēlē bija tikai jāpalaiž programma terminālī un tad varēja viņu izspēlēt līdz galam, nerakstot katru reizi pirms tam "py guess.py". Droši vien šoreiz jāsaliek abi divi kopā.

 	Šāda struktūra jau atkārtojas no iepriekšējiem mājasdarbiem un izskatās, ka tā būtu drošakā izvēle, lai arī nezinātājs sekojot līdzi soļiem varētu izpildīt prasīto un veiksmīgi ierakstīt izdevumus nesalaužot programmu. Liekas, tomēr, ka būs jānodrošina validācijas, kā piemēram datums jāraksta YYYY-MM-DD un summa nevar būt teksts, lai izpilde būtu muļķu droša.



***C. Moduļu plāns***



1. app.py
   	Galvenais fails. Caur šo notiks visa darbība komandrindā. Tas ļaus ievadīt un komandu un atgriezīs datus izmantojot pārējos failus. Šajā failā būs izveidota galvenā izvēlne, datu ievade un rādīs tabulu ar ievadītajiem tēriņiem.
   a. *display\_menu()*: parāda iespējamās darbības
   b. *get\_user\_input()*: izmanto input() komandu, lai iegūtu izdevumu, summu, kategoriju un aprakstu
   c. *show\_expenses\_table(expenses)*: ievadītos datus parāda tabulas veidā
   d. *main()*: galvenais cikls, kas neļauj programmai aizvērties, kamēr neizvēlas to aizvērt
2. storage.py
   	Šī būs programmas atmiņa. Tas ierakstīs un nolasīs datus no .json faila. Šis fails ļaus saglabāt jaunus izdevumus .json failā, atvēr .json failu, nolasīs tur esošo informāciju un atgriezīs sarakstā, ko saprot python, kā arī atradīs pēc nr. ierakstu un spēs to dzēst
   a. *load\_expenses()*: atver expenses.json failu un nolasīs visus datus
   b. *save\_expenses(expenses)*: paņem ievadītos datus un saglabā tos .json failā
   c. *add\_expenses(expenses)*: pievieno ievadītos datus .json failam un izsauc save\_expenses(expenses) 
   d. *delete\_expenses(index)*: atrod un izdzēš pievienoto datu rindu pēc nr.
3. logic.py
   	loģiskās darbības. Šeit notiks visi aprēķini un datu šķirošana. Šajā failā būs filtrs pa mēnešiem, kas atgriezīs datus pa mēnešiem. Aprēķinās kopsummu izdevumiem un izveidos kopsavilkumu pa kategorijām.
   a. *filter\_by\_month(expenses, month)*: saņem visus izdevumus un atgriež tikai tos kas ir prasītajā mēnesī
   b. *calculate\_total(expenses)*: saskaita visu izdevumu summu eur
   c. *calculate\_category(expenses)*: sagrupē izdevumus pa kategorijām un atgriež attiecīgās kategorijas summu
   d. *validate\_date(date\_string)*: pārbauda vai datums ievadīts YYYY-MM-DD formātā
4. export.py
   	Šis fails būs atbildīgs par to, lai datus varētu eksportēt uz .csv failu un excel vai google sheets to varēs nolasīt. Kā arī šo .csv failu saglabās
   a. *export\_to\_csv(expenses, filename)*: paņem izdevumu sarakstu un pārvērš to par .csv failu 
5. expenses.json
   	Šī ir datu ierakstīšana atmiņā, lai katru reizi nav visi dati pa jaunu jāievada. praktiski sanāk, kā datu noliktava strādā.



***D. Lietotāja scenāriji***



1. Lietotājs pievieno izdevuma datumu aprakstot vārdos. programma parāda kļūdas paziņojumu un ļauj mēģināt ievadīt datumu pareizajā formātā
2. Lietotājs vēlas dzēst izdevumu nr. 5, toties kļūdas ievadē un ieraksta "25", kas neeksistē. programma parāda kļūdas paziņojumu un ļauj mēģināt vēlreiz.
3. Lietotājs vēlas redzēt kopsavilkumu pa kategorijām. viņš no galvenās izvēles izvēlas ciparu, kas atbilst "kopsavilkums pa kategorijām" un pēc tam no nākošās izvēlnes izvēlas kuru kategoriju vēlas redzēt.



***E. Robežgadījumi***



1. *Kas notiek ja expenses.json neeksistē?*
   	Programma atgriezīs tukšu sarakstsu
2. *Kas notiek, ja lietotājs ievada negatīvu summu? Tukšu aprakstu? Nepareizu datumu?*
   	ja leitotājs ievadīs negatīvu summu, tad nostrādās validācija un neļaus saglabāt negatīvu skaitli. tas pats ar tukšu aprakstu un nepareizu datumu. visiem šiem gadījummiem būs validācijas, kas atgriezīs teksta veidā paziņojumu, ka jāievada pareizi izdevums.
3. Kas notiek, ja saraksts ir tukšs un lietotājs izvēlas "Parādīt"?

&nbsp;	arī šim gadījumam nostrādās validācija un atgriezīs tekstu ar to, ka pašlaik ierakstu nav. 



