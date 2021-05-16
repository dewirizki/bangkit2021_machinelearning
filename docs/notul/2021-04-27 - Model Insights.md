# CAPSTONE PROJECT - FINDINGS

> Note: using this in proposal will probably result in violation of academic integrity as I paraphrased the findings without referring to the exact works.

## Recommender System from Hungary

### Summary
This article mentioned the use of Expert Systems. The data is available as a graph of comparisons between organic matter and relative yield.

The fertiliser comes in different forms and shapes, though they prefer to use NPK (Nitrogen, Phosphorus, and Potassium) as a fertilizer:
- Sand,
- Sandy loam,
- Loam,
- Clay loam, and
- Clay.

Therefore, we need these things as a dataset:
- Data of fertiliser and relative yield

### Math

NPK fertilizer recommender is by this formula:

$$x = Y * SNC_y * F_{SNS} ± C$$

where:
- $Y$ = planned yield level
- $SNC_Y$ = specific nutrient content at the planned yield level
- $F_{SNS}$ = factor depending on the nutrient status of the soil
- $C$ = correction factor

## Brazilian fertilisation recommendation system (for Melon) based on nutritional balance

### Summary

Another research that gives out fertilisation recommendation system is also made. Since this research is based on improvisation from the existing recommendation tables, this works like it. In other words, this system works as a rule-based model.

## Detection of nutrition deficiency in plants using proximal images and Machine Learning

> [Source](https://doi.org/10.1016/j.compag.2019.04.035) is over on ScienceDirect. Personally I used my UGM subscription, but if you guys are interested you guys might wanna ask me for the article or head over to Sci-hub :P

### Summary
This article sums up the state of research on image-based nutrional deficiency with Machine Learning.

Here are the image types being used for the model input:
- Multispectral - that is, an image of something within a specific wavelength ranges across the electromagnetic spectrum;
- Hyperspectral - that is, an image of something with each 'pixels' containing information on the specific location from across the spectrum;
- Normal RGB — that is, an image of something within the colour spectrum.
> Verdict: we will be using input from a camera device — that is, an image taken from end-users' camera — therefore making such other options unreachable for us.

In terms of the detection method being used:
- Artificial Neural Network
- Support Vector Machines (SVM)
- Discriminant Analysis (DA)
- k-Nearest Neighbours (kNN)
- Fuzzy logic
- Statistical classifier
- Genetic algorithms
- Random Forest

In terms of the detection method being used, here are several tried classifiers with its accuracy ratings explained:

#### Artificial Neural Networks
In one research, a single multi-layered perceptron is used to classify oil palm images into one of these categories: healthy, nitrogen, magnesium, or potassium deficient, with 67% accuracy.

One research uses Radial Basis Function neural network with different function — their model performed significantly better, with poorer extrapolation capabilities. This one is not usually used in more complex image classification tasks because they only provide one hidden layer. However, the said research compared RBF to other classifiers and found that, in a setting with 6,000 spectral images of three varieties of 12-week old tobacco plants and other photos of leaves with ranging ages and labeled with its respective nutricient deficiencies, RBFs were comparable to SVMs and ranging around 80% accuracy compared to Supervised Relevance Neural Gas (SRNG) and Generalised Relevance Learning Vector Quantisation (GRLVQ) with below 70% accuracy.

In another research, SVM kernel method (SVMKM) is compared to other methods: Extreme Learning Machines (ELM), Fisher's Linear Discriminant Algorithm (LDA), Random decision forests (RF) and k-Nearest Neighbours (kNN), with SVM-KM getting 96.9% accuracy while being topped only by Random decision forests (97.2%). The original intent of this comparison was to see how ELM compares to others, turned out this finding states that ELM is better used for regression analysis rather than classification purposes.

SVMs were used in two research in which said researchers extract features from images before being forwarded to the model:
- In one research, 14 colours and morphological features are extracted from images, of which only a select few are forwarded to the model;
- 288 RGB images of the detached leaves were captured by a flat-bed scanner with a resolution of 300 DPI;

Accuracy analysis showed that these models have an accuracy of around 87% to 100%. Extreme learning were also used, with the results slightly below SVM in terms of accuracy.

#### Deep Neural Networks
Deep learning is becoming the standard. Since 2015, almost all works in this respect utilises DNN. Four pre-trained Convolutional Neural Networks have been used on 384 images comprising the 16 nitrogen treatments: accuracy varies in the growth stage, but classification using CNN and RGB images were more accurate (61.8% percentage) compared to using traditional texture methods (50-60% in average). One other research uses a relatively simple CNN to classify soybean leaf images into one of nine classes that comprised of five diseases, two nutritional deficiencies (potassium and ferrum), herbicide injury and healthy leaves. Although the data are collected manually, they managed to gather 25,000 images with an 18-mega pixel camera: the model results in 94% accuracy.

#### Discriminant Analysis
A method used to find a combination of features that suitably characterised or separates two or more classes of objects, it only performed well in specific circumstances: for NPK deficiency classifier, top-three leaves for 10 rice plants with 13 nutrition levels were collected and scanned using a 300-dpi CCD sensor, totalling 150 images: classification accuracy varied from 83% to 91% depending on the leaf growth stage.

#### k-Nearest Neighbour
k-NN is simple. That is the reason why it performed terribly when compared to others. **However**, in a setup where the deficiency is known *a priori*, kNN with RGB performed better.

### Data
Things that researchers need to watch out for in terms of data:
- Disorders with similar symptoms
- Simultaneous disorders
- Illumination conditions

## Crop Recommendation System to Maximize Crop Yield using ML in India

### Preface
India is a vast country, but a lot of the citizens find themselves needing to do agriculture. 55% of the whole Indian population finds themselves working there, compared to 5% in the United States of America, due to heavy mechanisation.

In short, lots of farmers but very low yield.

### Summary

bla

### Dataset

Secondary, from Polytest Laboratories soil testing lab in Pune, Maharashtra, India. Here are the attributes:
- Depth
- Texture
- pH
- Soil colour
- Permeability
- Drainage
- Water holding
- Erosion

Here are the crops:
- Groundnut
- Pulses
- Cotton
- Vegetables
- Banana
- Paddy
- Sorghum
- Sugarcane
- Coriander

### Model
The model is a combination of other models. Termed as 'ensemble' or 'model combiners', it strives to attain better prediction and efficiency than any of its models could achieve alone.

They use Majority Voting technique.

For the individual models, they use SVM, Naïve-bayes, MLP, Random forest, and Lambda function containing rules from logic.

In terms of the rule being used in the Lambda function:
- IF ph is mild alkaline
- AND depth is above 90
- AND water holding capacity is LOW
- AND drainage is moderate
- AND erosion is LOW
- THEN PADDY

## Maize yield and nitrate loss prediction with Machine Learning
> Location: seven locations in the US midwest

### Data input
Simulated with the Agricultural Production Systems Simulator (APSIM) with observations of maize yield and nitrate loss in drainage over 5-7 years, resulting in 3 million simulated data points of maize yields and N loss.

In detail:
- Weather years
- Locations
- Water table: average, deep, shallow
- Surface residue: amount of C:N
- Initial soil N in the profile: average, high, low
- Sowing time: if temperature is more than 15 °C, 10 days after, 20 days after
- Residue removal: percentage
- Cover crop: none, after winter, just before sowing
- Nitrate strategy: fall (100% ammonium on 25 November), spring (100% of urea-ammonium nitrate at sowing), split
- Nitrate rate: MRTN (maximum return to N value at each site), 0.7 * the MRTN, 1.3 * the MRTN
- Cultivar: typical (calibrated per location), high YP (increased radiation-use efficiency by 10%), high NUE (decrease N concentration in grains from 1.2% to 1%)