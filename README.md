Dataset Content

The dataset is sourced from Kaggle. 

I have created a fictional user story. However, the predictive analytics done, could be applied in a real project within the workplace.

The dataset that I have found on Kaggle is under the Code institute account, therefore, I have decided to trust this dataset and use it within my project. This document has almost 1.500 rows and represents housing records from a city called Ames located within the region of Iowa, US.

This dataset contains house profiles, such as: floor areas, basement, garage, kitchen, lot, porch, wood deck, year built, etc, for houses built between 1972 and 2010, and their respectively sale price.  

For the house profile provided by this dataset I have created the table from below which is was built up with a variable, meaning of each individual variable and units use to measure these variables.

In any part of the project that you are on, and you don’t understand one of the categories that the analysis has been done, please refer to the below table. 

Variable	Meaning	Units
1stFlrSF	First floor square feet	334 – 4692
2ndFlrSF	Second floor square feet	0-2065
BedroomAbvGr	Bedrooms above grade (this doesn’t NOT include basement bedrooms) 	0-8
BsmtExposure	Refers to walkout of garden level walls	Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No exposure; None: no basement
BsmtFinType1	Rating of basement finished area.	GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinished; None: No Basement
BsmtFinSF1	Type 1 finished square feet	0 - 5644
BsmtUnfSF	Unfinished square feet of basement area	0 - 2336
TotalBsmtSF	Total square feet of basement area	0 - 6110
GarageArea	Size of garage in square feet	0 - 1418
GarageFinish	Year garage was built	Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage
GarageYrBlt	Interior finish of the garage	1900 - 2010
GrLivArea	Above grade (ground) living area square feet	334 - 5642
KitchenQual	Kitchen quality	Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor
LotArea	Lot size in square feet	1300 - 215245
LotFrontage	Linear feet of street connected to property	21 - 313
MasVnrArea	Masonry veneer area in square feet	0 - 1600
EnclosedPorch	Enclosed porch area in square feet	0 - 286
OpenPorchSF	Open porch area in square feet	0 - 547
OverallCond	Rates the overall condition of the house	10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor
OverallQual	Rates the overall material and finish of the house	10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor
WoodDeckSF	Wood deck area in square feet	0 - 736
YearBuilt	Original construction date	1872 - 2010
YearRemodAdd	Remodel date (same as construction date if no remodelling or additions)	1950 - 2010
SalePrice	Sale Price	34900 - 755000

Business Requirements.

I am studying a Full Stack Developer course with Code Institute. I just learnt how to use Machine Learning as part of my last project and how to predict future trends which I will be using in my career as a Data Scientist. 

My niece who lives in America started a little real estate business, and part of her vision was to buy 6 houses in a small town from Iowa, called Ames. As Ames is known for its robust, stable economy and flourishing cultural environment with a population over 89,540 people, my niece believes that this will be a very good investment. Buying some old houses, refurbish them and after selling them at a higher price. 

Overall, my niece has a good understanding of the average prices for the houses in this region. However, because this investment will be very important for her business, she reached out to her uncle who will be able to use the power of machine learning to predict the prices for these homes, without risking an inaccurate appraisal. 

My niece has conducted research, and she found a public dataset for the houses that have been sold over the years. She will be able to share this data with me in order to create an accurate prediction for each of the houses that she plans to sell after refurbishment. 

Hypothesis and how to validate?

Hypothesis for the sale prices after refurbishment.

-	An evaluation must be conducted on the dataset that has been received from my niece in order to visualise the other houses that have been sold in that area. Following this evaluation, we will be able to see what is the criteria that influences the pricing of each house that has been sold, and what are the similar attributes to the 6 houses that my niece would like to sell.

-	The analysis shows that the important factors to determine a house price is highly influenced by the size of each room. Starting with the ground floor, leaving room, the first floor and if the house has a basement or a garage. As part of the factors that influence the house prices, we have to include the year of construction, the quality of the used materials and the last refurbishments.

Rationale to map the business requirements to the Data Visualizations and ML tasks

List the business requirements and rationale to map them to the data visualizations and ML tasks.

Business requirement 1 – Data Visualization and Correlation study.

-	As a data analyst I will need to visualize the data related to the house records, so that I can discover how the price will be influenced by each attribute of each house presented in the dataset.

-	As a data analyst I will need to conduct a correlation study (Pearson and Spearman) so I can better understand how the variables are correlated to sale price. So that I can discover how the house attributes correlate with the sale price of the houses.

	Correlation and/or PPS studies may be performed to investigate the most relevant variables correlated to the sale price.

-	As a data analyst I would like to plot the main variables against the sale price so that I can visualise insights that can discover how the house attributes correlate with the sale price.

Visualize these variables against the sale price and summarise the insights.

Business requirement 2 

-	As a data analyst I would need to be able to predict the sale price of these houses.

Build an ML Model, so that I can predict the house prices, when my niece decides to sell the 6 houses, that she will be refurbishing. At the same time, as the dataset its accurate to this area, she could come back to this project and use it again for future houses that she might want to sell or buy.

-	Deliver an ML system that is capable of reliably predicting the summed sale price of the 6 newly refurbished houses. 

-	Use either conventional ML or Neural Networks to map the relationships between the features and the target. 

-	Consider changing the ML Task from regression and classification if you find a valid rationale for that.

-	If conventional ML is used for modelling, with packages like scikit-learn for example, conduct and extensive hyperparameter optimization for a given algorithm. 

Refer to the Scikit-learn lesson, Unit notebook 6: Cross-Validation Search Part 2.

At the end of the notebook, is a list of hyperparameter options and values to start with for the family of algorithms covered in the course. 


ML Business Case

Business Case Assessment

1.	What are the business requirements?

	Business requirement 1:

o	My niece would like to discover how the house attributes correlate with the sale price.

o	Therefore, she would expect to be able to visualize the correlation variables against the sale price. (This will be discussed in the business requirement 2).

o	My niece would be interested in predicted the price of the newly refurbished houses, and any other new houses that she would buy in the future.

2.	Can the above business requirements be answered with conventional data analysis?

o	Technically yes, we can use the conventional data analysis to investigate how the house attributes are correlated with the sale prices. 

3.	Does my niece require a dashboard or an API endpoint?

o	As I would like to offer my best help to my niece by building this project, I would like her to be able to come back to this in case she would like to use it again in the future.

4.	What would make my niece consider this project a successful outcome?

o	For my niece to consider this a successful outcome, she would need to see a study showing the most relevant variables corelated to the sale price.

o	Also, if she would like to predict other house prices from this region and of course the price of the 6 houses that she newly refurbished. 

5.	As a data analyst I would like to be able to break down the project into epics and user stories. 

o	 Information gathered from a public point and data collection in: (DataCollection.ipynb).

o	Data visualization, cleaning, and preparation in: (SalePriceStudy.ipynb).

o	Model training, optimization, and validation in: (FeatureEngineering.ipynb).

o	Dashboard planning, designing and development.

o	Dashboard deployment and release. 

6.	Ethical or Privacy concerns?

o	As this dataset has been found from a public source, my niece doesn’t need to concern of any. 

7.	Does the data suggest a particular model?

o	The data suggests a regressor model where the target is the sale price.

8.	What are the model inputs and intended outputs? 

o	The sale price can be influenced by the house attribute information provided above, and the outputs is the predicted sale price.

9.	What are the criteria for the performance goal of the predictions?

o	I have agreed with my niece that an R2 score of at least 0.75 on the train set as well as on the test set would be perfect.

10.	How would my niece benefit from this?

o	My niece would be able to maximize the sale price for the newly refurbished houses as well as for future on sale houses that her small real estate agency might occur. 

Dashboard Design

Dashboard Expectations

The dashboard should contain:

o	A project summary page, showing the project dataset summary and my niece’s requirements for this project.

o	A page listing the findings related to which features that have the strongest correlation to the house sale price.

o	A page displaying the 6 houses attributes and their respective predicted sale price.

	It should display a message informing the summed predicted price for all the 6 houses newly refurbished.

	Add interactive input and widgets that allow a user to provide real-time house data to predict the sale price.

o	A page indicating my project hypothesis(es) and how I would validate it across the project. 

o	A technical page displaying my model performance, and if I would deploy a ML pipeline to have displayed my pipeline steps. 

Page 1: Quick project summary

Quick project summary: 

	Describe project dataset.

	State business requirements.

	Dataset Content Guidelines.

Page 2: House Sale Price Study

	In the inception point of the project, I wanted this page to answer business requirement 1, but I couldn’t know in advance which plots would need to be displayed. 

	After we analysed the data, I aggreged with my niece that the page will:

o	State business requirement 1.

o	Checkbox: data inspection on housing sale dataset.

o	Display the number of rows and columns in the data and display the first ten rows of the data.

o	Display the variables that bear the strongest correlation to sale price and the conclusions.

o	Checkbox: Individual plots showing how the sale price correlates to each variable. 

Page 3: Price Predictor

	State business requirement 2

	List the details of the inherited houses and their respective price predictions.

	Display the total sum of all the predicted house sales price.

	A set of widgets inputs, which relate to house sales dataset.

o	The best features, discovered during feature engineering notebook are available to my nice in order to capture the attribute of each house that she asked for a price prediction.

	“Run predictive analysis”, this button serves to house data, provided by my niece, to the ML pipelines, and predicts the sale price for the house and displays the result to her (Therefore, she would be able to calculate the price as well for these 6 houses, and in future for the other houses that she might buy or sell). 

Page 4: Project Hypothesis and Validation

	 Before the analysis, I knew that this page would describe each project hypothesis, the conclusion, and how I will validate each one of them. 

	After the data analysis, we can report that:

o	1. An evaluation of sales price of other houses from this area are based on similar attributes with the 6 houses that my niece would like to sell, therefore, this project should provide an accurate prediction of sales price for each house. 

o	2. The correlation analysis shows that the sizes of the ground floor living area, the first floor, the basement, and the garage, play a key role in determining the house price. In addition, the year of the house when was built and the last refurbishment, the quality of the used materials also plays a significant role in determining a house price. 

Page 5: ML: House Sale Price Prediction

	Considerations and conclusions after the pipeline will be trained.

	Present the ML Pipeline steps.

	Feature importance: List the features and plot the best features.

	Pipeline performance evaluation: Show model evaluation and plots.

Unfixed Bugs

	As the project is still in inception, I do not know if there are any bugs yet. This will be updated once the project 
will be almost finished. 

Deployment

Heroku

•	The App live link is: TBC 

•	The project was deployed to Heroku using the following steps.

1.	Log in to Heroku and create an App

2.	At the Deploy tab, select GitHub as the deployment method.

3.	Select your repository name and click Search. Once it is found, click Connect.

4.	Select the branch you want to deploy, then click Deploy Branch.

5.	The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

Credits

Content

TBC

References

tbc

Acknowledgements

tbc
