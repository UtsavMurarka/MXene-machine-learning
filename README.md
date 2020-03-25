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

For each of the 5 atoms in the molecule we add the following properties to the molecule’s data:<\br>
1.	Neutron number<\br>
2.	Proton number<\br>
3.	Number of electrons<\br>
4.	Period<\br>
5.	Group number<\br>
6.	Atomic radius<\br>
7.	Electronegativity<\br>
8.	First Ionization Energy<\br>
9.	Density<\br>
10.	Melting point<\br>
11.	Boiling point<\br>
12.	Number of isotopes<\br>
13.	Number of shells<\br>
14.	Specific heat<\br>
So, now, in addition to the 29 features we had earlier, we now have 70 new features (14 properties x 5 atoms per molecule). Therefore, a total of 99 features.

