# Logboek Lineaire Algebra — Assessmentvoorbereiding

**Gebaseerd op:** Tutorial van [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

## Inhoudsopgave
- [1. Matrices](#1-matrices)
- [2. Inproduct van vectoren](#2-inproduct-van-vectoren)
- [3. Afstand tussen vectoren](#3-afstand-tussen-vectoren)

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
---

# Logboek Differentiëren — Assessmentvoorbereiding

Gebaseerd op:  
- 3Blue1Brown – Essence of Calculus (YouTube): https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6  
- Khan Academy uitleg over afgeleiden  
- Eigen aanvullingen en uitleg

---

## Inhoud


- [1. Wat is een afgeleide?](#1-wat-is-een-afgeleide?)
- [2. Activatiefuncties](#2-activatiefuncties)
- [3. Helling bepalen](#3-helling-(afgeleide)-bepalen)
- [4. Differentiëren](#4-differentiëren)
- [5. Partieel differentiëren](#5-partieel-differentiëren)


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

## 2. Activatiefuncties


Activatiefuncties zijn een essentieel onderdeel van neurale netwerken. Ze bepalen of een neuron geactiveerd wordt, en helpen het netwerk om complexe patronen te leren. Zonder activatiefuncties zou een neuraal netwerk slechts een lineaire combinatie van zijn inputs kunnen leren.

Hieronder enkele veelgebruikte activatiefuncties:

### 1. Sigmoid Functie

De sigmoid functie zet elke input om naar een waarde tussen 0 en 1.

Formule:

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

Eigenschappen:
- Gebruikt bij binair classificatieproblemen.
- Nadeel: **vanishing gradient** probleem bij grote of kleine waarden.

### 2. Tanh Functie

De tanh (hyperbolische tangens) functie lijkt op de sigmoid, maar schaalt de output tussen -1 en 1.

Formule:

$$
\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$

Eigenschappen:
- Vaak beter dan sigmoid, omdat de output nul-gecentreerd is.
- Ook gevoelig voor het **vanishing gradient** probleem.

### 3. ReLU (Rectified Linear Unit)

ReLU is de meest gebruikte activatiefunctie in deep learning.

Formule:

$$
\text{ReLU}(x) = \max(0, x)
$$

Eigenschappen:
- Snel en eenvoudig.
- Helpt bij het oplossen van het **vanishing gradient** probleem.
- Kan leiden tot het **dode neuronen** probleem (neuronen die nooit meer activeren).

### 4. Leaky ReLU

Een variant van ReLU die een kleine negatieve helling heeft wanneer $x < 0$.

Formule:

$$
\text{LeakyReLU}(x) =
\begin{cases}
x & \text{als } x > 0 \\
\alpha x & \text{anders} \quad (\text{meestal } \alpha = 0.01)
\end{cases}
$$

Eigenschappen:
- Probeert het probleem van dode neuronen op te lossen.

### 5. Softmax Functie

Wordt vaak gebruikt in de outputlaag bij classificatieproblemen met meerdere klassen.

Formule voor de i-de klasse:

$$
\text{Softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}
$$

Eigenschappen:
- Zet outputs om in waarschijnlijkheidsdistributies (som = 1).

---

> **Samenvatting:** Activatiefuncties introduceren niet-lineariteit in het netwerk, waardoor het complexe relaties kan leren tussen invoer en uitvoer.
---

## 3. Helling (Afgeleide) Bepalen

De **helling** geeft aan hoe snel een functie verandert op een bepaald punt. In neurale netwerken gebruiken we de helling (de afgeleide) om te bepalen hoe we gewichten moeten aanpassen.

De basisideeën:

### Wat is een helling?

De helling van een functie op een punt geeft aan hoe steil de grafiek daar is.  
- Positieve helling → lijn stijgt
- Negatieve helling → lijn daalt
- Helling nul → vlak

### Helling Formule

De helling wordt wiskundig uitgedrukt als de **afgeleide**.

Formeel:

$$
\text{Helling} = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}
$$

**Betekenis:**  
De helling is de verandering van $f(x)$ gedeeld door de verandering in $x$ als $\Delta x$ heel klein wordt.

### Voorbeeld

Stel:

$$
f(x) = x^2
$$

Dan is de afgeleide:

$$
f'(x) = 2x
$$

Dus:
- Bij $x = 3$ is de helling $2 \times 3 = 6$
- De grafiek stijgt daar vrij steil omhoog.

### Gebruik van de Helling in Neurale Netwerken

In neurale netwerken wordt de helling gebruikt om:
- De **richting** van de fout (loss) te bepalen (welke kant moet het gewicht op?)
- De **snelheid** van de aanpassing te bepalen (hoe groot moet de aanpassing zijn?)

Tijdens backpropagation wordt voor elke activatiefunctie de afgeleide (helling) berekend.

---

> **Samenvatting:**  
> De helling vertelt hoe snel een functie verandert. In machine learning gebruiken we de helling om gewichten aan te passen en het netwerk te trainen.


---

## 4. Differentiëren

**Differentiëren** is het proces waarbij je de **afgeleide** van een functie bepaalt. De afgeleide vertelt ons hoe snel de functie verandert op een bepaald punt.

Differentiëren is een basisconcept in de calculus en wordt veel gebruikt in machine learning, bijvoorbeeld om de gradiënt te berekenen tijdens het trainen van neurale netwerken.

---

### Wat is differentiëren?

Differentiëren betekent het berekenen van de **helling** van een functie op elk punt.  
De uitkomst van een differentiaalbewerking is een nieuwe functie: de **afgeleide functie**.

- De afgeleide op een punt geeft de **momentane verandering** aan.
- In grafieken: de afgeleide geeft de **richtingscoëfficiënt van de raaklijn**.

---

### Formule voor differentiëren

De definitie van de afgeleide van een functie $f(x)$ is:

$$
f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}
$$

**Interpretatie:**  
- $f(x + \Delta x)$ is de functiewaarde iets verderop.
- $f(x)$ is de functiewaarde op $x$.
- De limiet zorgt ervoor dat we kijken naar een *oneindig klein stukje*.

---

### Belangrijke Differentiatieregels

Hier een paar standaard regels die je vaak nodig hebt:

- **Machtsregel**:
  $$
  \frac{d}{dx}x^n = n x^{n-1}
  $$
- **Somregel**:
  $$
  \frac{d}{dx}(f(x) + g(x)) = f'(x) + g'(x)
  $$
- **Productregel**:
  $$
  \frac{d}{dx}(f(x)g(x)) = f'(x)g(x) + f(x)g'(x)
  $$
- **Quotiëntregel**:
  $$
  \frac{d}{dx}\left(\frac{f(x)}{g(x)}\right) = \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}
  $$
- **Ketenregel**:
  $$
  \frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)
  $$

---

### Voorbeeld

Stel:

$$
f(x) = 3x^2 + 2x
$$

Differentieer:

$$
f'(x) = 6x + 2
$$

Dus:
- Bij $x = 2$ is de afgeleide $6 \times 2 + 2 = 14$.
- De helling van de grafiek bij $x = 2$ is 14 (de grafiek stijgt daar flink).

---

### Gebruik van Differentiëren in Machine Learning

- Wordt gebruikt om de **gradiënt** van de verliesfunctie (loss function) te berekenen.
- Helpt bij het bepalen **hoe de parameters (gewichten) moeten worden aangepast**.
- Centrale stap in **backpropagation**.

---

> **Samenvatting:**  
> Differentiëren is het vinden van de afgeleide van een functie. In machine learning is differentiëren cruciaal om te leren hoe het model moet verbeteren.
---

## 5. Partieël Differentieren

**Partieel differentiëren** gebruik je wanneer je een functie hebt met meerdere variabelen (bijvoorbeeld $f(x, y)$).  
Je bepaalt dan de afgeleide **met respect tot één variabele**, terwijl je de andere variabelen **constant** houdt.

Partieel differentiëren is essentieel in machine learning, bijvoorbeeld bij het optimaliseren van functies met meerdere parameters.

---

### Wat is partieel differentiëren?

Bij een functie $f(x, y)$:
- $\frac{\partial f}{\partial x}$ betekent: de afgeleide van $f$ naar $x$, waarbij $y$ constant blijft.
- $\frac{\partial f}{\partial y}$ betekent: de afgeleide van $f$ naar $y$, waarbij $x$ constant blijft.

**Belangrijk:** Alleen de variabele waar je naar differentieert verandert; de andere blijft vast!

---

### Notatie voor partieel differentiëren

De partiële afgeleide van $f(x, y)$ naar $x$ schrijf je als:

$$
\frac{\partial f}{\partial x}
$$

En naar $y$ als:

$$
\frac{\partial f}{\partial y}
$$

---

### Voorbeeld

Stel:

$$
f(x, y) = 3x^2y + 2xy^3
$$

De partiële afgeleiden zijn:

- Naar $x$:

$$
\frac{\partial f}{\partial x} = 6xy + 2y^3
$$

- Naar $y$:

$$
\frac{\partial f}{\partial y} = 3x^2 + 6xy^2
$$

**Opmerking:** Bij het differentiëren naar $x$ behandel je $y$ als een constante, en andersom.

---

### Partiёel Differentieren in Machine Learning

In machine learning (bijvoorbeeld bij gradient descent) gebruik je partieel differentiëren om:

- Voor elke parameter de richting van de fout te bepalen.
- De **gradiëntvector** te berekenen: alle partiële afgeleiden samen vormen de richting waarin de loss het snelst stijgt.

De gradiëntvector is:

$$
\nabla f(x, y) = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)
$$

---

### Ketenregel voor meerdere variabelen

Als een functie samengestelde variabelen heeft, gebruik je de **ketenregel** voor partiële afgeleiden:

Bijvoorbeeld:

$$
\frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}
$$

waar $z = f(x(t), y(t))$.

---

> **Samenvatting:**  
> Bij partieel differentiëren neem je de afgeleide naar één variabele, en behandel je de andere variabelen als constant. In machine learning wordt dit gebruikt om gradiënten te berekenen voor functies met meerdere parameters.


---
---

  # Logboek Gradient Descent

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

### Voorbeeld

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

### Backpropagation

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


---

# Logboek Wiskunde — Kostenfuncties in Machine Learning

**Onderdeel van:** Statistiek & Machine Learning

Gebaseerd op uitleg uit verschillende tutorials en samenvattingen uit de lessen.

---

## Inhoudsopgave
- [1. Mean Squared Error (MSE)](#1-mean-squared-error-mse)
- [2. Cross Entropy](#2-cross-entropy)
- [3. Softmax](#3-softmax)

---

## 1. Mean Squared Error (MSE)

### Wat is het?
De **Mean Squared Error** is een veelgebruikte kostenfunctie bij regressieproblemen. Het berekent hoe ver de voorspellingen van het model gemiddeld afwijken van de werkelijke waarden, waarbij fouten extra hard worden afgestraft doordat ze gekwadrateerd worden.

### Formule:

\[
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

waarbij:
- \( y_i \): de echte waarde
- \( \hat{y}_i \): de voorspelling van het model
- \( n \): aantal voorbeelden

### Waarom het werkt:
Het kwadrateren zorgt ervoor dat grotere fouten zwaarder meetellen. Daarom is het een gevoelige maat voor uitbijters. Hoe lager de MSE, hoe beter het model.

### Voorbeeld:

Stel we hebben deze echte waarden en voorspellingen:

\[
y = [2, 4, 6], \quad \hat{y} = [3, 5, 4]
\]

Berekening:

\[
\begin{align*}
(2 - 3)^2 &= 1 \\
(4 - 5)^2 &= 1 \\
(6 - 4)^2 &= 4 \\
\end{align*}
\]

\[
MSE = \frac{1 + 1 + 4}{3} = \frac{6}{3} = 2
\]

De gemiddelde fout (gekwadrateerd) is dus 2.

---

## 2. Cross Entropy

### Wat is het?
**Cross Entropy** wordt gebruikt bij classificatieproblemen, waarbij het model voorspellingen doet in de vorm van kansen. Deze functie vergelijkt de voorspelde kansverdeling met de werkelijke uitkomst en straft verkeerde voorspellingen sterker af als het model er erg zeker van was.

### Formule (binaire classificatie):

\[
L = - \left[ y \log(\hat{y}) + (1 - y) \log(1 - \hat{y}) \right]
\]

### Formule (multiclass classificatie):

\[
L = - \sum_{i=1}^{C} y_i \log(\hat{y}_i)
\]

waarbij:
- \( y_i \): 1 als het de juiste klasse is, anders 0
- \( \hat{y}_i \): voorspelde kans voor klasse \( i \)
- \( C \): totaal aantal klassen

###  Waarom het werkt:
Cross entropy meet hoe ver twee kansverdelingen van elkaar afliggen. Als je een verkeerde klasse met hoge zekerheid voorspelt, krijg je een hoge straf.

###  Voorbeeld (multiclass):

Stel:

\[
y = [0, 1, 0], \quad \hat{y} = [0.2, 0.7, 0.1]
\]

De juiste klasse is de tweede, dus:

\[
L = - \log(0.7) \approx 0.357
\]

Als het model had voorspeld:

\[
\hat{y} = [0.05, 0.9, 0.05]
\]

Dan zou:

\[
L = - \log(0.9) \approx 0.105
\]

**Lagere cross entropy = betere voorspelling.**

---

## 3. Softmax

### Wat is het?
De **Softmax**-functie wordt gebruikt om ruwe scores (logits) van een model om te zetten in een kansverdeling over meerdere klassen. Hierdoor kun je afleiden welke klasse het meest waarschijnlijk is.

### Formule:

\[
\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{C} e^{z_j}}
\]

waarbij:
- \( z \): vector met ruwe scores
- \( \sigma(z)_i \): kans dat input tot klasse \( i \) behoort
- \( C \): totaal aantal klassen

### Waarom het werkt:
De exponentiële functie vergroot de verschillen tussen de scores, waardoor de hoogste score dominant wordt. De output is altijd een kansverdeling die optelt tot 1.

### Voorbeeld:

Stel:

\[
z = [1, 2, 3]
\]

Bereken de exponenten:

\[
e^1 \approx 2.72,\quad e^2 \approx 7.39,\quad e^3 \approx 20.09
\]

Totaal:

\[
\sum = 2.72 + 7.39 + 20.09 = 30.2
\]

Softmax-output:

\[
\sigma(z) \approx \left[ \frac{2.72}{30.2}, \frac{7.39}{30.2}, \frac{20.09}{30.2} \right] \approx [0.09, 0.24, 0.67]
\]

De derde klasse heeft de hoogste kans → model voorspelt klasse 3.

---

# Logboek Statistiek — Assessmentvoorbereiding

**Gebaseerd op:** Eigen notities, tutorials, en praktijkvoorbeelden

## Inhoudsopgave
- [1. Data visualiseren](#1-data-visualiseren)
- [2. Scatter matrix](#2-scatter-matrix)
- [3. Normaalverdeling](#3-normaalverdeling)
- [4. Regressie-analyse](#4-regressie-analyse)
- [5. Z-scores](#5-z-scores)
- [6. Standaardafwijking](#6-standaardafwijking)
- [7. Normaliseren](#7-normaliseren)

---

## 1. Data visualiseren

### Waarom visualiseren?
Visualisaties helpen patronen, uitschieters en trends te herkennen die niet direct zichtbaar zijn in ruwe data.

### Voorbeelden van visualisaties:
- Histogram (verdeling)
- Boxplot (spreiding en outliers)
- Line chart (tijdreeksen)
- Scatter plot (relaties tussen variabelen)

Visualisaties zijn essentieel bij het verkennen van data vóórdat je modellen bouwt.

---

## 2. Scatter matrix

### Wat is een scatter matrix?
Een scatter matrix (of pair plot) laat alle combinaties van scatter plots tussen meerdere variabelen zien.

### Waarom is het handig?
- Je ziet correlaties visueel
- Je kunt patronen herkennen zoals lineaire relaties of clusters
- Het helpt bij het kiezen van relevante variabelen voor modellering

**Tooltip**: In Python kun je dit maken met `seaborn.pairplot(df)`.

---

## 3. Normaalverdeling

### Wat is het?
Een klokvormige verdeling waar de meeste waarden rond het gemiddelde liggen.

### Kenmerken:
- Symmetrisch rond het gemiddelde
- Gemiddelde = Mediaan = Modus
- Ongeveer 68% van de waarden ligt binnen 1 standaardafwijking van het gemiddelde
- Wordt vaak gebruikt als aannames voor statistische tests

### Formule:
De kansdichtheid van een normaalverdeling:

\[
f(x) = \frac{1}{\sigma \sqrt{2\pi}} \cdot e^{ -\frac{1}{2} \left( \frac{x - \mu}{\sigma} \right)^2 }
\]

Waar:
- \( \mu \): gemiddelde
- \( \sigma \): standaardafwijking

---

## 4. Regressie-analyse

### Wat is regressie?
Regressie zoekt naar een model (meestal een lijn) dat de relatie tussen een onafhankelijke en afhankelijke variabele beschrijft.

### Lineaire regressie:
Formule:

\[
y = mx + b
\]

Waar:
- \( m \): helling (slope)
- \( b \): intercept (waar de lijn de y-as kruist)

Doel: Voorspellen van \( y \) op basis van \( x \), of inzicht krijgen in hoe \( x \) en \( y \) samenhangen.

---

## 5. Z-scores

### Wat is een z-score?
Een z-score zegt hoeveel standaardafwijkingen een datapunt van het gemiddelde ligt.

### Formule:

\[
z = \frac{x - \mu}{\sigma}
\]

### Interpretatie:
- \( z = 0 \): precies gemiddeld
- \( z > 0 \): boven gemiddeld
- \( z < 0 \): onder gemiddeld
- Z-scores helpen bij het vinden van outliers en het vergelijken van scores uit verschillende datasets.

---

## 6. Standaardafwijking

### Wat meet het?
Standaardafwijking (\( \sigma \)) meet de spreiding van data rond het gemiddelde.

### Formule (populatie):

\[
\sigma = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2 }
\]

### Hoe interpreteer je het?
- Kleine \( \sigma \): data ligt dicht bij het gemiddelde
- Grote \( \sigma \): data is meer verspreid

---

## 7. Normaliseren

### Wat is normaliseren?
Normaliseren betekent dat je data herschaalt zodat het gemiddeld 0 en een standaardafwijking van 1 heeft.

### Formule:

\[
x' = \frac{x - \mu}{\sigma}
\]

Waarom?
- Maakt variabelen vergelijkbaar
- Essentieel bij algoritmen die gevoelig zijn voor schaal (zoals k-means, PCA, etc.)

---

## Reflectie

Wat heb ik geleerd?
- Statistiek is essentieel om data écht te begrijpen.
- Visualisaties zijn krachtig voor verkenning en communicatie.
- Begrippen als z-score en standaardafwijking maken abstracte data concreet.

Wat wil ik verder ontwikkelen?
- Meer oefenen met multivariate regressie
- Werken met echte datasets in Python
- Statistische inferentie en betrouwbaarheidsintervallen beter begrijpen

Toepassingen:
- Data-analyse en rapportages
- Machine learning preprocessing
- A/B testing en experimenten
- Business analytics en dashboards

---


