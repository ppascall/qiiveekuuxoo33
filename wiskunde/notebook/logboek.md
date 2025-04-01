# Wiskunde Portfolio - Uitgebreid

## Lineaire Algebra

Lineaire algebra is een essentieel onderdeel van de wiskunde dat zich richt op de studie van vectoren, vectorruimten en lineaire transformaties. Het is cruciaal voor AI omdat het een fundamenteel raamwerk biedt voor het representeren en manipuleren van data.

### Belangrijke Concepten

**Vectoren:**

* Een vector is een object met zowel een richting als een grootte.
* Vectoren kunnen worden gebruikt om punten in de ruimte weer te geven, evenals fysieke grootheden zoals kracht en snelheid.
* **Voorbeeld:** In een 2D-coördinatensysteem kan een vector worden weergegeven als <span class="math-inline">\\begin\{pmatrix\} 3 \\\\ 4 \\end\{pmatrix\}</span>, wat een verplaatsing van 3 eenheden in de x-richting en 4 eenheden in de y-richting betekent.

**Matrices:**

* Een matrix is een rechthoekig schema van getallen, gerangschikt in rijen en kolommen.
* Matrices worden gebruikt om lineaire transformaties weer te geven, stelsels van vergelijkingen op te lossen en data op te slaan.
* **Voorbeeld:** Een 3x3 matrix kan er als volgt uitzien: <span class="math-inline">\\begin\{pmatrix\} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \\end\{pmatrix\}</span>

**Matrix Operaties:**

* **Optellen:** Matrices kunnen worden opgeteld als ze dezelfde afmetingen hebben. De overeenkomstige elementen worden bij elkaar opgeteld.
    * **Voorbeeld:** <span class="math-inline">\\begin\{pmatrix\} 1 & 2 \\\\ 3 & 4 \\end\{pmatrix\} \+ \\begin\{pmatrix\} 5 & 6 \\\\ 7 & 8 \\end\{pmatrix\} \= \\begin\{pmatrix\} 6 & 8 \\\\ 10 & 12 \\end\{pmatrix\}</span>
* **Vermenigvuldigen:** Matrixvermenigvuldiging is een complexere bewerking waarbij rijen van de eerste matrix worden gecombineerd met kolommen van de tweede matrix.
    * **Voorbeeld:** <span class="math-inline">\\begin\{pmatrix\} 1 & 2 \\\\ 3 & 4 \\end\{pmatrix\} \\times \\begin\{pmatrix\} 5 & 6 \\\\ 7 & 8 \\end\{pmatrix\} \= \\begin\{pmatrix\} 19 & 22 \\\\ 43 & 50 \\end\{pmatrix\}</span>

**Afstanden:**

* **Euclidische Afstand:** De kortste afstand tussen twee punten, berekend met de stelling van Pythagoras.
    * **Formule:** <span class="math-inline">d\_E\(a, b\) \= \\sqrt\{\\sum\_\{i\=1\}^\{n\}\(a\_i \- b\_i\)^2\}</span>
    * **Voorbeeld:** De Euclidische afstand tussen de punten (1, 2) en (4, 6) is <span class="math-inline">\\sqrt\{\(4\-1\)^2 \+ \(6\-2\)^2\} \= 5</span>
* **Manhattan Afstand:** De som van de absolute verschillen van de coördinaten van twee punten.
    * **Formule:** <span class="math-inline">d\_M\(a, b\) \= \\sum\_\{i\=1\}^\{n\}\|a\_i \- b\_i\|</span>
    * **Voorbeeld:** De Manhattan afstand tussen de punten (1, 2) en (4, 6) is |4-1| + |6-2| = 7

**Speciale Matrices:**

* **Getransponeerde Matrix:** Een matrix waarbij de rijen en kolommen zijn verwisseld.
    * **Voorbeeld:** De getransponeerde van <span class="math-inline">\\begin\{pmatrix\} 1 & 2 \\\\ 3 & 4 \\end\{pmatrix\}</span> is <span class="math-inline">\\begin\{pmatrix\} 1 & 3 \\\\ 2 & 4 \\end\{pmatrix\}</span>
* **Inverse Matrix:** Een matrix die, wanneer vermenigvuldigd met de originele matrix, de identiteitsmatrix oplevert.
    * **Voorbeeld:** Als <span class="math-inline">A \= \\begin\{pmatrix\} 2 & 0 \\\\ 1 & 1 \\end\{pmatrix\}</span>, dan is <span class="math-inline">A^\{\-1\} \= \\begin\{pmatrix\} 1/2 & 0 \\\\ \-1/2 & 1 \\end\{pmatrix\}</span> en <span class="math-inline">A \\times A^\{\-1\} \= \\begin\{pmatrix\} 1 & 0 \\\\ 0 & 1 \\end\{pmatrix\}</span> (de identiteitsmatrix)
* **Determinant:** Een scalaire waarde die kan worden berekend uit de elementen van een vierkante matrix. De determinant geeft informatie over de eigenschappen van de matrix, zoals of deze inverteerbaar is.
    * **Voorbeeld:** De determinant van <span class="math-inline">\\begin\{pmatrix\} 2 & 1 \\\\ 3 & 4 \\end\{pmatrix\}</span> is <span class="math-inline">\(2 \\times 4\) \- \(1 \\times 3\) \= 5</span>

### Toepassingen in AI

* **Data Representatie:** Datasets worden vaak weergegeven als matrices, waarbij rijen individuele datapunten zijn en kolommen kenmerken.
* **Beeldverwerking:** Afbeeldingen kunnen worden gezien als matrices van pixels.
* **Tekstverwerking:** Matrices kunnen worden gebruikt om woordfrequenties weer te geven (zie "one-hot encoding").
* **One-hot Encoding:** Categorische data (zoals kleuren) kunnen worden omgezet in binaire vectoren.
    * **Voorbeeld:** De kleuren rood, groen en blauw kunnen worden weergegeven als: rood = (1, 0, 0), groen = (0, 1, 0), blauw = (0, 0, 1).
* **Lineaire Regressie:** Het modelleren van lineaire relaties tussen variabelen.
* **Regularisatie:** Technieken om overfitting in modellen te verminderen.
* **Dimensionaliteitsreductie:** Technieken zoals Principal Component Analysis (PCA) gebruiken lineaire algebra om de complexiteit van data te verminderen.
* **Deep Learning:** Lineaire algebra is de basis van neurale netwerken, waar matrices worden gebruikt om gewichten en activaties weer te geven.

## Differentiëren

Differentiëren is een fundamentele techniek uit de calculus die de helling (of veranderingssnelheid) van een functie berekent. In AI wordt het veel gebruikt voor het optimaliseren van modellen.

### Belangrijke Concepten

* **Afgeleide:** De afgeleide van een functie f(x) geeft de helling van de raaklijn aan de grafiek van de functie in een bepaald punt.
    * **Notatie:** f'(x) of <span class="math-inline">\\frac\{dy\}\{dx\}</span>
    * **Voorbeeld:** Als f(x) = x^2, dan is f'(x) = 2x. Dit betekent dat de helling van de functie f(x) = x^2 op elk punt x gelijk is aan 2x. Dus, op x = 3 is de helling 2 * 3 = 6.
* **Richtingcoëfficiënt:** De helling van een rechte lijn.
    * **Voorbeeld:** Voor de lijn y = 2x + 3 is de richtingcoëfficiënt 2.
* **Productregel:** Wordt gebruikt om de afgeleide te vinden van een functie die het product is van twee andere functies.
    * **Formule:** (uv)' = u'v + uv'
    * **Voorbeeld:** Als f(x) = x^2 \sin(x), dan is f'(x) = 2x \sin(x) + x^2 \cos(x)
* **Quotiëntregel:** Wordt gebruikt om de afgeleide te vinden van een functie die het quotiënt is van twee andere functies.
    * **Formule:** <span class="math-inline">\(\\frac\{u\}\{v\}\)' \= \\frac\{u'v \- uv'\}\{v^2\}</span>
    * **Voorbeeld:** Als f(x) = <span class="math-inline">\\frac\{x^2\}\{x\+1\}</span>, dan is f'(x) = <span class="math-inline">\\frac\{2x\(x\+1\) \- x^2\}\{\(x\+1\)^2\}</span>
* **Kettingregel:** Wordt gebruikt om de afgeleide te vinden van een samengestelde functie.
    * **Formule:** (f(g(x)))' = f'(g(x)) \cdot g'(x)
    * **Voorbeeld:** Als f(x) = (x^2 + 1)^3, dan is f'(x) = 3(x^2 + 1)^2 \cdot 2x
* **Partiële Afgeleide:** De afgeleide van een functie met meerdere variabelen, genomen met betrekking tot één van die variabelen, terwijl de andere constant worden gehouden.
    * **Voorbeeld:** Als f(x, y) = x^2y + 3y^2, dan is <span class="math-inline">\\frac\{\\partial f\}\{\\partial x\} \= 2xy</span> en <span class="math-inline">\\frac\{\\partial f\}\{\\partial y\} \= x^2 \+ 6y</span>

### Toepassingen in AI

* **Gradient Descent:** Een optimalisatiealgoritme dat afgeleiden gebruikt om het minimum van een functie te vinden.
* **Kostenfuncties:** Functies die de fout van een model meten. Differentiëren helpt bij het vinden van de parameters die deze fout minimaliseren.
* **Activatiefuncties:** Functies die bepalen of een neuron "vuurt" in een neuraal netwerk. De afgeleide van activatiefuncties is nodig voor het trainen van neurale netwerken.

## Gradient Descent

Gradient descent is een iteratief optimalisatiealgoritme dat wordt gebruikt om de parameters van een model te vinden die de kostenfunctie minimaliseren. Het maakt gebruik van afgeleiden om de richting van de steilste afdaling te bepalen.

### Stappen van Gradient Descent

1.  **Initialisatie:** Start met willekeurige waarden voor de parameters van het model.
2.  **Bereken de Gradiënt:** Bereken de afgeleide van de kostenfunctie met betrekking tot elke parameter. De gradiënt is een vector van partiële afgeleiden.
3.  **Update Parameters:** Update de parameters in de richting van de negatieve gradiënt. De grootte van de update wordt bepaald door de "learning rate".
    * **Formule:** <span class="math-inline">\\theta \= \\theta \- \\alpha \\nabla J\(\\theta\)</span>, waarbij <span class="math-inline">\\theta</span> de parameters zijn, <span class="math-inline">\\alpha</span> de learning rate en <span class="math-inline">\\nabla J\(\\theta\)</span> de gradiënt van de kostenfunctie.
4.  **Herhaal:** Herhaal stap 2 en 3 totdat de kostenfunctie is geminimaliseerd of een stopcriterium is bereikt (bijv. een maximaal aantal iteraties).

### Voorbeeld

Stel dat we een lineair regressiemodel hebben <span class="math-inline">h\_\\theta\(x\) \= \\theta\_0 \+ \\theta\_1x</span> en de kostenfunctie is de Mean Squared Error (MSE): <span class="math-inline">J\(\\theta\_0, \\theta\_1\) \= \\frac\{1\}\{m\} \\sum\_\{i\=1\}^\{m\} \(h\_\\theta\(x^\{\(i\)\}\) \- y^\{\(i\)\}\)^2</span>

1.  We beginnen met willekeurige waarden voor <span class="math-inline">\\theta\_0</span> en <span class="math-inline">\\theta\_1</span>.
2.  We berekenen de partiële afgeleiden van J met betrekking tot <span class="math-inline">\\theta\_0</span> en <span class="math-inline">\\theta\_1</span>.
3.  We updaten <span class="math-inline">\\theta\_0</span> en <span class="math-inline">\\theta\_1</span> met de formules:
    * <span class="math-inline">\\theta\_0 \= \\theta\_0 \- \\alpha \\frac\{\\partial J\}\{\\partial \\theta\_0\}</span>
    * <span class="math-inline">\\theta\_1 \= \\theta\_1 \- \\alpha \\frac\{\\partial J\}\{\\partial \\theta\_1\}</span>
4.  We herhalen dit proces totdat de MSE zo laag mogelijk is.

## Kostenfuncties

Kostenfuncties (ook wel verliesfuncties genoemd) meten hoe goed een model presteert door de fout tussen de voorspelde en werkelijke waarden te kwantificeren. Het doel van het trainen van een model is om deze functie te minimaliseren.

### Veelvoorkomende Kostenfuncties

* **Mean Squared Error (MSE):** Berekent het gemiddelde van de gekwadrateerde verschillen tussen de voorspelde en werkelijke waarden.
    * **Formule:** <span class="math-inline">MSE \= \\frac\{1\}\{n\} \\sum\_\{i\=1\}^\{n\} \(y\_i \- \\hat\{y\}\_i\)^2</span>, waarbij <span class="math-inline">y\_i</span> de werkelijke waarde is en <span class="math-inline">\\hat\{y\}\_i</span> de voorspelde waarde.
    * **Gebruik:** Regressieproblemen.
* **Cross Entropy:** Meet de prestaties van een classificatiemodel. Het kwantificeert het verschil tussen twee kansverdelingen.
    * **Formule:** <span class="math-inline">CE \= \- \\sum\_\{i\=1\}^\{C\} y\_i \\log\(\\hat\{y\}\_i\)</span>, waarbij C het aantal klassen is, <span class="math-inline">y\_i</span> de werkelijke kans is (0 of 1 voor binaire classificatie) en <span class="math-inline">\\hat\{y\}\_i</span> de voorspelde kans.
    * **Gebruik:** Classificatieproblemen.
* **Softmax:** Wordt vaak gebruikt in combinatie met Cross Entropy voor multi-klasse classificatieproblemen. Het zet een vector van getallen om in een kansverdeling.
    * **Formule:** <span class="math-inline">\\text\{Softmax\}\(x\)\_i \= \\frac\{e^\{x\_i\}\}\{\\sum\_\{j\=1\}^\{K\} e^\{x\_j\}\}</span>, waarbij x de invoervector is en K het aantal klassen.

## Kansen berekenen met dobbelstenen

* **Kans op een specifieke som:** Bereken de kans dat de som van twee dobbelstenen gelijk is aan een bepaald getal.
    * **Voorbeeld:** De kans dat de som 7 is, is 6/36 of 1/6.
        * Gunstige uitkomsten: (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)
        * Totale uitkomsten: 36
        * P(som=7) = 6/36 = 1/6
    * **Voorbeeld:** De kans dat de som 3 is, is 2/36 of 1/18.
        * Gunstige uitkomsten: (1, 2), (2, 1)
        * P(som=3) = 2/36 = 1/18
    * **Voorbeeld:** De kans dat de som 4 is, is 3/36 of 1/12.
        * Gunstige uitkomsten: (1, 3), (2, 2), (3, 1)
        * P(som=4) = 3/36 = 1/12
    * **Voorbeeld:** De kans dat de som 11 is, is 2/36 of 1/18.
        * Gunstige uitkomsten: (5, 6), (6, 5)
        * P(som=11) = 2/36 = 1/18
* **Kans op een som kleiner dan een getal:** Bereken de kans dat de som van twee dobbelstenen kleiner is dan een bepaald getal.
    * **Voorbeeld:** De kans dat de som kleiner is dan 5 is 6/36 of 1/6.
        * Gunstige uitkomsten: (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 1)
        * P(som<5) = 6/36 = 1/6

## Combinatoriek

* **Teams samenstellen:** Bereken het aantal manieren om een team samen te stellen uit een groep mensen.
    * **Voorbeeld:** Een team van 2 mannen en 2 vrouwen uit een groep van 6 mannen en 5 vrouwen kan op 150 manieren worden samengesteld.
        * Aantal manieren om 2 mannen uit 6 te kiezen: <span class="math-inline">\\binom\{6\}\{2\} \= 15</span>
        * Aantal manieren om 2 vrouwen uit 5 te kiezen: <span class="math-inline">\\binom\{5\}\{2\} \= 10</span>
        * Totaal aantal manieren: 15 * 10 = 150

## Verwachtingswaarde

* **Verwachtingswaarde berekenen:** Bereken de gemiddelde uitkomst van een kansproces.
    * **Voorbeeld:** Bereken de verwachte winst van een bedrijf dat fietsen verhuurt.
        * Gegeven: Prijs per fiets = 17 euro, Gemiddelde kosten per dag = 15 euro.
        * Verwacht aantal verhuurde fietsen: E(k) = 2.63 (berekend met kansentabel)
        * Verwachte winst = (17 * 2.63) - 15 = 29.71 euro

## Poisson verdeling

* **Kans op een bepaald aantal gebeurtenissen:** Bereken de kans op een bepaald aantal gebeurtenissen in een bepaald interval, gegeven het gemiddelde aantal gebeurtenissen.
    * **Voorbeeld:** Bereken de kans dat een bedrijf hoogstens 3 telefoontjes per uur krijgt, gegeven dat het gemiddeld 7 telefoontjes per uur ontvangt.
        * Formule: <span class="math-inline">P\(X\=k\) \= \\frac\{e^\{\-\\lambda\} \\lambda^k\}\{k\!\}</span>
        * P(X ≤ 3) = P(X=0) + P(X=1) + P(X=2) + P(X=3) ≈ 0.0817

## Normale verdeling

* **Kans berekenen met normale verdeling:** Bereken de kans dat een waarde binnen een bepaald bereik valt in een normale verdeling.
    * **Voorbeeld:** Bereken de kans dat een denneboom kleiner is dan 2.8 meter, gegeven dat de gemiddelde hoogte 3.2 meter is met een standaardafwijking van 0.17 meter.
        * Z-score: Z = (2.8 - 3.2) / 0.17 ≈ -2.35
        * P(X < 2.8) = P(Z < -2.35) ≈ 0.0094
    * **Voorbeeld:** Bereken de kans dat een denneboom groter is dan 2.9 meter, gegeven dat de gemiddelde hoogte 3.3 meter is met een standaardafwijking van 0.12 meter.
        * Z-score: Z = (2.9 - 3.3) / 0.12 ≈ -3.33
        * P(X > 2.9) = P(Z > -3.33) ≈ 0.9996

## Kansen benaderen

* **Kansen benaderen met de z-tabel:** Gebruik de z-tabel om kansen te benaderen voor een normale verdeling.
    * **Voorbeeld:** Bereken de kans dat een telefoongesprek tussen de 7 en 15 minuten duurt, gegeven het gemiddelde van 11 minuten en een standaardafwijking van 4 minuten.
        * Z-scores: Z1 = (7 - 11) / 4 = -1, Z2 = (15 - 11) / 4 = 1
        * P(-1 < Z < 1) = P(Z < 1) - P(Z < -1) ≈ 0.6826
    * **Voorbeeld:** Bereken de kans dat een telefoongesprek tussen de 9 en 15 minuten duurt, gegeven het gemiddelde van 15 minuten en een standaardafwijking van 3 minuten.
        * Z-scores: Z1 = (9 - 15) / 3 = -2, Z2 = (15 - 15) / 3 = 0
        * P(-2 < Z < 0) = P(Z < 0) - P(Z < -2) ≈ 0.4772
    * **Voorbeeld:** Bereken de kans dat een telefoongesprek langer duurt dan 20 minuten, gegeven het gemiddelde van 18 minuten en een standaardafwijking van 1 minuut.
        * Z-score: Z = (20 - 18) / 1 = 2
        * P(Z > 2) = 1 - P(Z < 2) ≈ 0.0228
    * **Voorbeeld:** Bereken de kans dat een telefoongesprek tussen de 9 en 12 minuten duurt, gegeven het gemiddelde van 15 minuten en een standaardafwijking van 3 minuten.
        * Z-scores: Z1 = (9 - 15) / 3 = -2, Z2 = (12 - 15) / 3 = -1
        * P(-2 < Z < -1) = P(Z < -1) - P(Z < -2) ≈ 0.1359

## Belangrijke Punten voor het Assessment

* **Lineaire Algebra:**
    * Begrijp de basisconcepten zoals vectoren, matrices en matrixoperaties.
    * Weet hoe lineaire algebra wordt gebruikt in AI (bijv. data representatie, one-hot encoding).
    * Ken de definities en berekeningen van Euclidische en Manhattan afstand.
    * **Voorbeeldvraag:** Leg uit hoe je twee matrices vermenigvuldigt en geef een voorbeeld.
* **Differentiëren:**
    * Leg uit wat een afgeleide is en hoe je deze kunt gebruiken om de helling van een functie te bepalen.
    * Ken de differentieerregels (productregel, quotiëntregel, kettingregel) en pas ze toe.
    * Begrijp het concept van partiële afgeleiden.
    * **Voorbeeldvraag:** Bereken de afgeleide van de functie f(x) = x^3 \cdot \cos(x).
* **Gradient Descent:**
    * Beschrijf het doel en de stappen van het gradient descent algoritme.
    * Leg uit waarom afgeleiden nodig zijn voor gradient descent.
    * **Voorbeeldvraag:** Leg uit hoe gradient descent werkt en wat de rol is van de learning rate.
* **Kostenfuncties:**
    * Definieer wat een kostenfunctie is en waarom we deze gebruiken.
    * Leg het verschil uit tussen MSE en Cross Entropy en wanneer je ze gebruikt.
    * Ken de Softmax functie en de toepassing ervan.
    * **Voorbeeldvraag:** Wat is het verschil tussen Mean Squared Error en Cross Entropy, en wanneer gebruik je welke?
* **Kansberekening:**
    * Begrijp de basisprincipes van kansberekening, inclusief het berekenen van kansen met dobbelstenen en andere scenario's.
    * Ken de Poisson verdeling en de normale verdeling en weet hoe je deze kunt gebruiken om kansen te berekenen.
    * Weet hoe je de z-tabel kunt gebruiken om kansen te benaderen.
    * **Voorbeeldvraag:** Bereken de kans dat de som van twee dobbelstenen 8 is.