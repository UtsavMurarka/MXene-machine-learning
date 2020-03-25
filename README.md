# Machine Learning Based Classification of Non-functionalized MXenes into Metals and Non-metals 

## Introduction
This project deals with training classification models on physical properties of non-functionalized MXene molecules to classify them into metals and non-metals.
The data required was obtained from aNANt database by IISc, Bangalore.

## Data Visualization & Preprocessing
### List of Features

![Features](https://github.com/UtsavMurarka/MXene-machine-learning/blob/master/features.JPG)

### Distribution of individual features

![Features distribution](https://github.com/UtsavMurarka/MXene-machine-learning/blob/master/feature_plots.png)

### Corelation Heatmap

![corr_hmap](https://github.com/UtsavMurarka/MXene-machine-learning/blob/master/Corr_Heatmap.jpg)

## Feature Engineering

For each of the 5 atoms in the molecule we add the following properties to the molecule’s data:<br/>
1.	Neutron number
2.	Proton number
3.	Number of electrons
4.	Period
5.	Group number
6.	Atomic radius
7.	Electronegativity
8.	First Ionization Energy
9.	Density
10.	Melting point
11.	Boiling point
12.	Number of isotopes
13.	Number of shells
14.	Specific heat<br/>
So, now, in addition to the 29 features we had earlier, we now have 70 new features (14 properties x 5 atoms per molecule). Therefore, a total of 99 features.

### Distribution of individual features (NEW)
![feature_dist](https://github.com/UtsavMurarka/MXene-machine-learning/blob/master/feature_dist_99.png)
### Correlation Heatmap
![corr_hmap_new](https://github.com/UtsavMurarka/MXene-machine-learning/blob/master/corr_heatmap_new.png)

### Class Imbalance
![imb](https://github.com/UtsavMurarka/MXene-machine-learning/blob/master/imb.JPG)

## Results
Model : Random Forest

### ROC Curve
![roc](https://github.com/UtsavMurarka/MXene-machine-learning/blob/master/rf_roc1.png)

ROC-AUC = 0.931
Accuracy = 93.3%
