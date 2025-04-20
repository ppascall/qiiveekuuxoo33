# Logboek Lineaire Algebra — Assessmentvoorbereiding

**Gebaseerd op:** Tutorial van [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

## Inhoudsopgave
- [1. Matrices](#1-matrices)
- [2. Inproduct van vectoren](#2-inproduct-van-vectoren)
- [3. Afstand tussen vectoren](#3-afstand-tussen-vectoren)
- [4. Reflectie](#4-reflectie)

---

## 1. Matrices

### Wat is een matrix?
Een matrix is een rechthoekige tabel van getallen, met rijen en kolommen. In lineaire algebra gebruik je matrices vooral om lineaire transformaties uit te voeren, zoals schalen, draaien en spiegelen.

### Voorbeeld: Schaling
Als we een vector vermenigvuldigen met een matrix die de vorm heeft van een diagonaal met dezelfde waarde, bijvoorbeeld:

\[ A = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}, \quad \vec{v} = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \]

Dan krijgen we:

\[ A \cdot \vec{v} = \begin{bmatrix} 2 \\ 2 \end{bmatrix} \]

Dit betekent dat de vector twee keer zo lang wordt, dus hij wordt geschaald.

### Voorbeeld: Rotatie
Een matrix kan ook een rotatie uitvoeren. De rotatiematrix over een hoek \( \theta \) in 2D is:

\[ R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \]

Bijvoorbeeld, bij een draaiing van 45 graden:

\[ R(45^°) = \begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix} \]

Als je een vector \( \begin{bmatrix} 2 \\ 0 \end{bmatrix} \) draait met deze matrix, krijg je een vector die in een hoek van 45 graden ligt met dezelfde lengte.

---

## 2. Inproduct van vectoren

### Wat is het inproduct?
Het inproduct (ook wel scalair product genoemd) van twee vectoren \( \vec{a} \) en \( \vec{b} \) is een getal dat iets zegt over hoe "gericht" de vectoren zijn ten opzichte van elkaar.

De formule is:

\[ \vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2 \]

### Voorbeeld:

\[ \vec{a} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad \vec{b} = \begin{bmatrix} 3 \\ 4 \end{bmatrix} \]

Dan is:

\[ \vec{a} \cdot \vec{b} = 1 \cdot 3 + 2 \cdot 4 = 3 + 8 = 11 \]

### Hoek tussen vectoren
Je kunt het inproduct ook gebruiken om de hoek tussen twee vectoren te berekenen:

\[ \vec{a} \cdot \vec{b} = \|\vec{a}\| \cdot \|\vec{b}\| \cdot \cos(\theta) \]

Dus:

\[ \cos(\theta) = \frac{\vec{a} \cdot \vec{b}}{\|\vec{a}\| \cdot \|\vec{b}\|} \]

En zo kun je met de inverse cosinus (arccos) de hoek \( \theta \) berekenen.

---

## 3. Afstand tussen vectoren

### Wat betekent afstand?
De afstand tussen twee vectoren in een vlak of ruimte is gewoon de lengte van het verschil tussen die vectoren.

Als \( \vec{x} \) en \( \vec{y} \) twee vectoren zijn, dan is:

\[ d(\vec{x}, \vec{y}) = \|\vec{x} - \vec{y}\| \]

Hierbij gebruiken we de Euclidische norm (ook wel de lengte of magnitude genoemd):

\[ \|\vec{v}\| = \sqrt{v_1^2 + v_2^2} \]

### Voorbeeld:

\[ \vec{x} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}, \quad \vec{y} = \begin{bmatrix} 1 \\ 4 \end{bmatrix} \]

Dan:

\[ \vec{x} - \vec{y} = \begin{bmatrix} 4 \\ -3 \end{bmatrix} \]

\[ d(\vec{x}, \vec{y}) = \sqrt{4^2 + (-3)^2} = \sqrt{16 + 9} = \sqrt{25} = 5 \]

Dus de afstand tussen \( \vec{x} \) en \( \vec{y} \) is 5 eenheden.

---

## 4. Reflectie

Wat heb ik geleerd?
- Ik begrijp nu hoe matrices gebruikt worden om transformaties uit te voeren.
- Ik zie hoe het inproduct nuttig is om richtingen en hoeken te analyseren.
- Ik kan de afstand tussen vectoren wiskundig onderbouwen en berekenen.

Wat zou ik nog verder willen doen?
- Werken met 3D vectoren en transformaties.
- Meer toepassingen in machine learning en grafische weergave onderzoeken.

Toepassingen:
- 2D/3D graphics en animaties
- Machine learning (zoals cosine similarity)
- Recommender systems en clustering
- Technische simulaties en computer vision

# Logboek Differentiëren — Assessmentvoorbereiding

Gebaseerd op:  
- 3Blue1Brown – Essence of Calculus (YouTube): https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6  
- Khan Academy uitleg over afgeleiden  
- Eigen aanvullingen en uitleg

---

## Inhoud

1. Wat is een afgeleide?
2. Helling als grafisch begrip
3. Symbolisch differentiëren (zonder code)
4. Afgeleide via limietdefinitie
5. Samenvatting eigen werk

---

## 1. Wat is een afgeleide?

Een afgeleide van een functie geeft aan hoe snel de functie verandert bij een bepaald punt.  
Bijvoorbeeld:  
Als f(x) = x², dan is f '(x) = 2x.  
Bij x = 1 is de afgeleide 2 × 1 = 2 → dit betekent dat de grafiek daar een helling van 2 heeft.

**Interpretatie:**  
- Een positieve afgeleide betekent stijging.  
- Een negatieve afgeleide betekent daling.  
- Een afgeleide van nul betekent een horizontale raaklijn.

---

## 2. Helling als grafisch begrip

In de video's van 3Blue1Brown wordt uitgelegd dat de afgeleide voortkomt uit het idee van een raaklijn aan een kromme.  
Een raaklijn is de rechte lijn die precies "meeloopt" met de grafiek op één punt.

Je kunt dit voorstellen als het nemen van de helling tussen twee punten (secant), en deze steeds dichter bij elkaar brengen totdat het één punt wordt. Dan krijg je de helling van de raaklijn: de afgeleide.

**Eigen toevoeging:**  
Ik heb zelf een schets gemaakt waarin je een kromme ziet met een raaklijn. Bij verschillende x-waarden heb ik de helling benaderd. Dit helpt visueel om het begrip beter te vatten.

**Waarom toegevoegd:**  
Niet iedereen begrijpt formules direct. Door visueel te denken wordt het idee van "helling" en "verandering" tastbaarder.

---

## 3. Symbolisch differentiëren (zonder code)

Voor standaardfuncties kun je de afgeleide berekenen met bekende regels:

- Machtregel:  
  Als f(x) = xⁿ, dan is f '(x) = n·xⁿ⁻¹  
  Voorbeeld: f(x) = x³ → f '(x) = 3x²

- Somregel:  
  De afgeleide van f(x) + g(x) is f '(x) + g '(x)

- Constantefactorregel:  
  De afgeleide van c·f(x) is c·f '(x)

- Productregel:  
  f(x)·g(x) → f '(x)·g(x) + f(x)·g '(x)

- Quotientregel:  
  f(x)/g(x) → (f '(x)·g(x) - f(x)·g '(x)) / g(x)²

- Kettingregel:  
  Als f(x) = h(g(x)), dan is f '(x) = h '(g(x))·g '(x)

**Eigen toevoeging:**  
Ik heb oefenvoorbeelden uitgewerkt met verschillende regels gecombineerd, zoals een product én kettingregel in één. Deze heb ik voorzien van uitleg bij elke stap.

**Waarom toegevoegd:**  
In het assessment wil ik laten zien dat ik de regels niet alleen ken, maar ze ook kan combineren en toepassen op complexere functies.

---

## 4. Afgeleide via limietdefinitie

De definitie van de afgeleide is gebaseerd op een limiet:

f '(x) = lim(h → 0) [(f(x + h) - f(x)) / h]

Deze formule betekent:  
De afgeleide is de grenswaarde van de gemiddelde verandering van de functie tussen twee dichtbije punten, naarmate het verschil h kleiner en kleiner wordt.

Voorbeeld met f(x) = x²:

- f(x + h) = (x + h)² = x² + 2xh + h²  
- f(x + h) - f(x) = 2xh + h²  
- (f(x + h) - f(x)) / h = 2x + h  
- lim(h → 0) = 2x

Dus: f '(x) = 2x

**Eigen toevoeging:**  
Ik heb deze stap-voor-stap uitgewerkt voor meerdere functies (zoals x³, √x en 1/x) op papier en uitgelegd wat er in elke stap gebeurt.

**Waarom toegevoegd:**  
Dit laat zien dat ik de definitie begrijp, en niet alleen regels toepas. Het helpt ook bij functies waarbij regels niet meteen toepasbaar zijn.


---

## 5. Gradient Descent

### Inhoudsopgave
- [Wat is gradient descent?](#wat-is-gradient-descent)
- [Doel](#doel)
- [Hoe werkt het?](#hoe-werkt-het)
- [Visuele intuïtie](#visuele-intuïtie)
- [Voorbeeld (1D)](#voorbeeld-1d)
- [Backpropagation](#backpropagation)
- [Toepassingen in AI](#toepassingen-in-ai)
- [Tabel](#tabel)

---


Gradient descent is een methode om een minimum (of maximum) te vinden van een functie. In machine learning wordt het vooral gebruikt om een model te trainen: het zoekt naar de waarden van de parameters (zoals gewichten in een neuraal netwerk) die de fout zo klein mogelijk maken.

Het is alsof je met een blinddoek op een berg staat en alleen voelt waar de helling naar beneden gaat — en je zet telkens kleine stappen omlaag tot je bij het dal komt.

### Wat is het doel?
Het minimaliseren van een **cost function** (ook wel: loss function). Deze functie geeft aan hoe goed of slecht je model presteert. Hoe lager de waarde, hoe beter je model.

Voorbeeld van een veelgebruikte cost function:
\[
J(\theta) = \frac{1}{2m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2
\]

Hierin:
- \( h_\theta(x) \) is de voorspelling van het model
- \( y \) is de werkelijke waarde
- \( m \) is het aantal trainingsvoorbeelden

---

### Hoe werkt het?

Bij elke stap:
1. Bereken de **gradiënt** (de richting van de stijging).
2. Neem een stap *tegenovergesteld* aan die richting.
3. Herhaal totdat je bij een minimum bent.

De updateformule:
\[
\theta := \theta - \alpha \cdot \nabla J(\theta)
\]

Waar:
- \( \theta \): parameters van je model (bijv. gewichten in een netwerk)
- \( \alpha \): learning rate (hoe groot je stap is)
- \( \nabla J(\theta) \): de gradiënt (vector van afgeleiden)

---

### Visuele intuïtie

- Een **grote learning rate** zorgt voor grote stappen — je kunt het minimum overslaan of gaan oscilleren.
- Een **kleine learning rate** geeft trage, maar stabiele stappen — het duurt langer om te convergeren.
- De **gradiënt** bepaalt de richting en helling: het is letterlijk het stijgingsgetal in meerdere richtingen tegelijk.

---

### Voorbeeld (1D)

Stel je hebt deze eenvoudige functie:
\[
f(x) = x^2
\]

De afgeleide is:
\[
f'(x) = 2x
\]

Gradient descent doet dan:
\[
x := x - \alpha \cdot 2x
\]

Als \( \alpha = 0.1 \) en je start bij \( x = 5 \), dan krijg je:

- Stap 1: \( x = 5 - 0.1 \cdot 2 \cdot 5 = 4 \)
- Stap 2: \( x = 4 - 0.1 \cdot 2 \cdot 4 = 3.2 \)
- enzovoort...

Na genoeg stappen kom je uit bij het minimum \( x = 0 \).

---

### Backpropagation (kort uitgelegd)

In neurale netwerken gebruik je **backpropagation** om de gradiënten te berekenen die nodig zijn voor gradient descent. Het is een slimme manier om de afgeleiden van de lossfunctie t.o.v. alle gewichten efficiënt uit te rekenen, door gebruik te maken van de kettingregel uit de differentiaalrekening.

1. Je berekent de **loss** na een voorspelling.
2. Je gaat **terug door het netwerk** om afgeleiden te berekenen.
3. Deze afgeleiden worden gebruikt in gradient descent om de gewichten aan te passen.

---

### Toepassingen in AI

- Training van neurale netwerken (deep learning)
- Lineaire regressie
- Logistische regressie
- Recommender systems
- Clustering en embedding-optimalisatie



---



