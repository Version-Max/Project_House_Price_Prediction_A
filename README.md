# Price prediction of houses based on neighborhood.

## Basic Overview:

* **Goal**: Create a model that helps potential home buyers to estimate the price of homes in a particular city.

* The prices of homes can fluctuate depending on the number of bedrooms and bathrooms, the location and the histroic growth of the housing market. This project tries to take into account all the attributes that influences the home pricing and give these attributes the fair weight that they use to influence the pricing.

* We tested multiple algorithms and picked Linear Regression as the algorithm of choice to build our model.



## Why Linear Regression?

* Linear regression is one of the easiest regression algorithm to understand. However, there are other strong algorithhms that can build price prediction models. We tested such algorithms as Decision Tree & Lasso Regression.

* The data preparation effort ensured the linear regression algorithm was fed the right attributes. This preperation enabled linear regression to give the best results and accuracy.

* Linear regression algorithm also ensures a very straightforward explanation of how the housing price model works.



## Resources and code used:

* ***Python Version***: 3.8
* ***Packages***: Pandas, Matplotlib, NumPy, Pickle, Sklearn (Linear Regression, Lasso, Decision Tree, train_test_split)
* ***Data Source***: https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data



## Data Acquisition:

* Used data from kaggle (https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data).
* The reason for choosing this housing dataset is because it provides a great opportunity to practice data cleaning and feature engineering.
* Original data consists of about 13320 rows and 9 columns.



## Data Cleaning:

  ### Attribute Selection:
    
    * Using multiple combinations of attributes and domain knowledge research, 3 attributes jumped out as consequential attributes in stock placements.
    * Major attributes: Return-On-Equirty (Financial Performance/Net Income), Return-On-Investment (Indicates the efficieny of the investment) and Return-On-Assets (indicates a respective company's profitability compared to its total assets)
    
  ### Data Preperation:
    
    * We remove all the NULL values because K-Means does not deal well with NULL values or 0 values.
    * Using the domain knowledge of stocks through papers published by NYU we determine the farthest maximum values that attributes of data is expected to be under. Anything over this maximum value is automatically discarded.
    * We use the above method rid the dataset of outliers.



## Visualization:

* Plotting our newly cleaned data we notice the following visualizations:
<img src='images/plot_1.png' width='50%' height='50%'>

* We decided to use 3 standardization methods to devoid any of the attributes from distorting the clusters.
* Methods to standardize: Z-Score Standardization, Min-Max-Standardization and Inter-Quartile-Range (IQR) Standardization.
* The following are the plots of such standardizations:
<img src='images/plot_2.png' width='25%' height='25%'>
<img src='images/plot_3.png' width='25%' height='25%'>
<img src='images/plot_4.png' width='25%' height='25%'>

* Looking at the visualizations and scales it was decided to go for IQR standardized dataset

## Exploring PCA:

* PCA was explored to help model building gain speed.
* PCA was a choice to explore dimensionality reduction because of its strength to lower the weight of the data without losing any significant meaning.
* We discovered 2 components were able to give us almost 100% of variation in the data:
<img src='images/plot_5.png' width='25%' height='25%'>

## Selecting number of Ks:

* Sklearn's KMeans provides us a silhoutte function. This function ranges from (-1, 1).
* Our aim is to get a silhouette score leaning more to 1.
* n = 3 clusters gave us a score of 0.47 for IQR data and 0.48 for PCA data.

## Model Building:

* Using n = 3 we built a model for stock's standardized IQR_data.
* The standardized IQR for stocks were able to clearly cluster itself:
<img src='images/plot_6.png' width='25%' height='25%'>

* Stock's PCA dataset was also model with 3 clusters.
* The following is the distinct cluster the PCA with 2 components was able to achieve:
<img src='images/plot_7.png' width='25%' height='25%'>

## Conclusion:

* With the silhouette method and clustering analysis through visualization we have two models at hand.
* The models equally perform well but are designed to serve a comprehensive operation by using PCA and IQR standardized data.
