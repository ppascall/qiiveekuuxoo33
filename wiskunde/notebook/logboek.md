# Logboek Lineaire Algebra — Assessmentvoorbereiding

**Gebaseerd op:** Tutorial van [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)

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

