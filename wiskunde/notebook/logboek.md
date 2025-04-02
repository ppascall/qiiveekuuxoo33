# Wiskunde Portfolio

## Inhoudsopgave
1. **Matrixrekening**
   - Basisbewerkingen met matrices
   - Determinanten en inverse
   - Toepassingen in AI en data science

2. **Lijnalgebra**
   - Vectoren en lineaire transformaties
   - Eigenwaarden en eigenvectoren
   - Toepassingen in machine learning

3. **Kansrekening en Statistiek**
   - Kansverdelingen en verwachtingswaarden
   - Centrale limietstelling
   - Hypothesetesten en regressieanalyse

4. **Calculus**
   - Differentiëren en integreren
   - Toepassingen in optimalisatie
   - Gradiënten en Jacobiaanse matrices

---

## 1. Matrixrekening

### Basisbewerkingen
Een matrix is een rechthoekige opstelling van getallen, bijvoorbeeld:

\[
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
\]

Operaties zoals optellen, aftrekken en matrixvermenigvuldiging worden als volgt gedefinieerd:
- **Optellen**: \( A + B = (a_{ij} + b_{ij}) \)
- **Matrixvermenigvuldiging**: \( AB = C \), waarbij \( c_{ij} = \sum_{k} a_{ik} b_{kj} \)

### Determinanten en inverse
De determinant van een \(2 \times 2\) matrix is:
\[
\det(A) = a_{11}a_{22} - a_{12}a_{21}
\]
Een matrix is inverteerbaar als \( \det(A) \neq 0 \), en de inverse wordt berekend met:
\[
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix}
\]

### Toepassing: AI en Data Science
- Inverses en determinanten worden gebruikt in lineaire regressie en optimalisatieproblemen.
- Singular Value Decomposition (SVD) wordt toegepast in beeldcompressie en aanbevelingssystemen.

---

## 2. Lijnalgebra

### Vectoren en lineaire transformaties
Een vector is een rij of kolom getallen:
\[
\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}
\]
De norm van een vector wordt gegeven door:
\[
||\mathbf{v}|| = \sqrt{x^2 + y^2}
\]

Lineaire transformaties worden voorgesteld door matrixvermenigvuldiging:
\[
T(\mathbf{v}) = A \mathbf{v}
\]

### Eigenwaarden en eigenvectoren
De eigenwaardevergelijking luidt:
\[
A\mathbf{v} = \lambda \mathbf{v}
\]
waarbij \( \lambda \) de eigenwaarde is en \( \mathbf{v} \) de eigenvector.

### Toepassing: Machine Learning
- PCA (Principale Componenten Analyse) gebruikt eigenvectoren om dimensies te reduceren in datasets.
- Google’s PageRank-algoritme is gebaseerd op eigenvectorberekeningen.

---

## 3. Kansrekening en Statistiek

### Kansverdelingen en verwachtingswaarden
Een kansverdeling geeft de waarschijnlijkheid aan van verschillende uitkomsten. De verwachtingswaarde is:
\[
E[X] = \sum x P(x)
\]

Voor continue verdelingen:
\[
E[X] = \int x f(x) dx
\]

### Centrale limietstelling
De som van onafhankelijke willekeurige variabelen nadert een normale verdeling naarmate het aantal waarnemingen toeneemt.

### Hypothesetesten en regressieanalyse
- T-testen en p-waarden worden gebruikt om statistische significantie te bepalen.
- Lineaire regressie wordt gebruikt om verbanden tussen variabelen te modelleren:
\[
y = \beta_0 + \beta_1 x + \varepsilon
\]

---

## 4. Calculus

### Differentiëren en integreren
De afgeleide van een functie \( f(x) \) geeft de verandering weer:
\[
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
\]

Integratie is de inverse bewerking:
\[
\int f(x) dx
\]

### Toepassingen in optimalisatie
- Gradiënten worden gebruikt in machine learning om kostenfuncties te minimaliseren.
- Newton’s methode wordt gebruikt voor snelle optimalisatie.

### Gradiënten en Jacobiaanse matrices
Voor een functie \( f: \mathbb{R}^n \to \mathbb{R}^m \) wordt de Jacobiaan gegeven door:
\[
J_f = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \dots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \dots & \frac{\partial f_m}{\partial x_n} \end{bmatrix}
\]

---

## Conclusie
Deze wiskundige concepten zijn cruciaal voor AI, data-analyse en optimalisatieproblemen. Begrip van matrixrekening, lijnalgebra, statistiek en calculus vormt de basis voor geavanceerde methoden zoals neurale netwerken en deep learning.

