![For Sale](/static/images/frsale.png "Price Predictor")
<img align="right" width="225" height="100" src="https://learningpeople.imgix.net/https%3A%2F%2Fadmin.learningpeople.com%2Fwp-content%2Fuploads%2F2019%2F01%2Fcode-institute.png?ixlib=gatsbyFP&fit=crop&auto=compress%2Cformat&w=320&h=141&s=3becdd2d48871285d91458e006867cb4" alt="code institute logo">

---

# House Pricing (PP5)

This project has been made as part of the 5 milestone projects within the Full Stack Developer course provided by Code Institute. 
This project will be the last one within this course, and represents the Predictive Analytics path that i have chosen. Therefore, the initial idea for this project was 'working with data'.

In this project you will be taken step by step withing everything that is happening from data cleaning to feature engineering, as the content has been personalised in a specific way, making you feeling welcomed, and helping by offering a great understanding of each individual step and what I did and how I did. 

At any point, if you get confused, please refer back to the readme file as you will find a lot of important information that has been used within the project.

![Mockup](/static/images/mockupp.png)


**The live application can be found [here.](https://house-price-predictor-pp5.herokuapp.com/)**

## Dataset Content

- The dataset is sourced from [Kaggle.](https://www.kaggle.com/)

***What is Kaggle?***

- *Kaggle is an online community platform for data scientists and machine learning enthusiasts.* 
- *Kaggle allows users to collaborate with other users, find and publish datasets, use GPU integrated notebooks, and compete with other data scientists to solve data science challenges.*

Within this project, I have created a fictional user story. 
However, the predictive analytics done, could be applied in a real project within the workplace or if you live in Ames.

- As mentioned above, the dataset I found on Kaggle, is under the Code institute account. 
Therefore, I have decided to trust this dataset and use it within my project. 

This document contains 1.460 *(1.461 including the name of each variable)* rows and represents housing records from a city called Ames located within the region of Iowa, US.

- This dataset contains house profiles, such as: 
	- floor areas, 
	- basement,
	- garage,
	- kitchen,
	- lot,
	- porch,
	- wood deck,
	- year built etc.
	
	For houses built between 1872 and 2010, and their respectively sale price.  

For the house profile provided in this dataset, I have created the table located below which has been built up with the variables provided by the dataset, and each individual meaning and units use to measure these variables.

In any part of the project that you are on, and you don’t understand one of the categories that the analysis has been done, please refer to the below table. 

---

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692 - (Min - Max > Sq. ft.)|
|2ndFlrSF|Second floor square feet|0 - 2065 - (Min - Max > Sq. ft.)|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8 - (Min - Max > Bedrooms)|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinished; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644 - (Min - Max > Sq. ft.)|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336 - (Min - Max > Sq. ft.)|
|TotalBsmtSF|Total square feet of basement area|0 - 6110 - (Min - Max > Sq. ft.)|
|GarageArea|Size of garage in square feet|0 - 1418 - (Min - Max > Sq. ft.)|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010 - (Min - Max > Year Built)|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642 - (Min - Max > Sq. ft.)|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245 - (Min - Max > Sq. ft.)|
|LotFrontage| Linear feet of street connected to property|21 - 313 - (Min - Max > Lin. ft.)|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600 - (Min - Max > Sq. ft.)|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286 - (Min - Max > Sq. ft.)|
|OpenPorchSF|Open porch area in square feet|0 - 547 - (Min - Max > Sq. ft.)|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736 - (Min - Max > Sq. ft.)|
|YearBuilt|Original construction date|1872 - 2010 - (Min - Max > Year Built)|
|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010 - (Min - Max > Remodel Year)|
|SalePrice|Sale Price|34.900 - 755.000 - (Min - Max > Sale price in $)|


--- 
## Scrum Master - Development

- In the beginning of the project i decided to create a project, where to input 'issues', the idea was to help me in following a direction while building this project. 
- The Table Project can be found [here.](https://github.com/users/Vasi012/projects/4)


![table](/static/images/pp5.png)

## Business Requirements.

I am studying a Full Stack Developer course with Code Institute. I just learnt how to use Machine Learning as part of my last project and how to predict future trends which I will be using in my career as a Data Scientist. 

My niece who lives in America started a little real estate business, and part of her vision was to buy 6 houses in a small town from Iowa, called Ames. As Ames is known for its robust, stable economy and flourishing cultural environment with a population over 89,540 people, my niece believes that this will be a very good investment. Buying some old houses, refurbish them and after selling them at a higher price. 

Overall, my niece has a good understanding of the average prices for the houses in this region. However, because this investment will be very important for her business, she reached out to her uncle who will be able to use the power of machine learning to predict the prices for these homes, without risking an inaccurate appraisal. 

My niece has conducted research, and she found a public dataset for the houses that have been sold over the years. She will be able to share this data with me in order to create an accurate prediction for each of the houses that she plans to sell after refurbishment. 

---

## Hypothesis and how to validate?

1. Hypothesis one.

- We consider the price of houses to be higher if the house has had a larger surface measured in sq. ft.
	- A correlation study can help in investigating if this is true.

2. Hypothesis Two.

- We consider that the houses with the same util surface measured in sq. ft. but built more recently has had a higher price then a older built home.
	- A correlation study can help in investigating if this is true.

3. Hypothesis Three.

- We consider that the houses with the same util surface measured in sq. ft. built in a recent year but remodeled recently has had a higher price then a house built in the same year but not remodeled. 
	- A correlation study can help in investigating if this is true.

4. Hypothesis Four.

- We consider that a house with similar sq. ft., but with a higher quality of materials and condition scores might have had a higher sales price.
	- A correlation study can help in investigating if this is true.

---

## Rationale to map the business requirements to the Data Visualizations and ML tasks

List the business requirements and rationale to map them to the data visualizations and ML tasks.

---

### Business requirement 1 – Data Visualization and Correlation study.

-	As a data analyst I will need to visualize the data related to the house records, so that I can discover how the price will be influenced by each attribute of each house presented in the dataset.

-	As a data analyst I will need to conduct a correlation study (Pearson and Spearman) so I can better understand how the variables are correlated to sale price. So that I can discover how the house attributes correlate with the sale price of the houses.
	- Correlation and/or PPS studies may be performed to investigate the most relevant variables correlated to the sale price.

-	As a data analyst I would like to plot the main variables against the sale price so that I can visualize insights that can discover how the house attributes correlate with the sale price.

- Visualize these variables against the sale price and summaries the insights.


## Outcome after predicting pricing.

- After conducting our study, we realised that the features that impact the price are:

![FeaturesImactingPrice](/static/images/importancefeat.png)

- We can take a closer look at each:
- GrLivArea (Above grade (ground) living area square feet)

![GrLivArea](/static/images/GrLivArea.png)

- GarageArea (Size of garage in square feet)

![GarageArea](/static/images/garageArea.png)

- YearBuilt (Original construction date)

![YearBuilt](/static/images/YearBuilt.png)

- 1stFlrSF (First Floor square feet)

![1stFlrSF](/static/images/train.png)

- OverallQual (Rates the overall material and finish of the house)

![OverallQual](/static/images/OverallQual.png)

- TotalBsmtSF (Total square feet of basement area)

![TotalBsmtSF](/static/images/TotalBsmtSF.png)

- More details could be found in the live app, the link has been posted in the top of the read me / deployment. 

---

### Business requirement 2 

-	As a data analyst I would need to be able to predict the sale price of these houses.

-	Build an ML Model, so that I can predict the house prices, when my niece decides to sell the 6 houses, that she will be refurbishing. At the same time, as the dataset its accurate to this area, she could come back to this project and use it again for future houses that she might want to sell or buy.

-	Deliver an ML system that is capable of reliably predicting the summed sale price of the 6 newly refurbished houses. 

-	Use either conventional ML or Neural Networks to map the relationships between the features and the target. 

-	Consider changing the ML Task from regression and classification if you find a valid rationale for that.

-	If conventional ML is used for modelling, with packages like scikit-learn for example, conduct and extensive hyperparameter optimization for a given algorithm. 

*Refer to the Scikit-learn lesson, Unit notebook 6: Cross-Validation Search Part 2.*

*At the end of the notebook, is a list of hyperparameter options and values to start with for the family of algorithms covered in the course.*


## Outcome after price prediction.

- My niece wanted to find out what are the prices for the 6 houses. 

![6predictions](/static/images/nieceprediction.png)

- In the feature she could use the added tool to be able to predict pricing for houses by imputing her own inputs.This can be located on the deployed site.

![ownimputs](/static/images/trypredict.png)


---

## ML Business Case

### Business Case Assessment

1.	What are the business requirements?

### Business requirement 1:

- My niece would like to discover how the house attributes correlate with the sale price.
- Therefore, she would expect to be able to visualize the correlation variables against the sale price. (This will be discussed in the business requirement 2).
- My niece would be interested in predicted the price of the newly refurbished houses, and any other new houses that she would buy in the future.

2.	Can the above business requirements be answered with conventional data analysis?

- Technically yes, we can use the conventional data analysis to investigate how the house attributes are correlated with the sale prices. 

3.	Does my niece require a dashboard or an API endpoint?

- As I would like to offer my best help to my niece by building this project, I would like her to be able to come back to this in case she would like to use it again in the future.

4.	What would make my niece consider this project a successful outcome?

- For my niece to consider this a successful outcome, she would need to see a study showing the most relevant variables correlated to the sale price.
- Also, if she would like to predict other house prices from this region and of course the price of the 6 houses that she newly refurbished. 

5.	As a data analyst I would like to be able to break down the project into epics and user stories. 

- Information gathered from a public point and data collection in: (DataCollection.ipynb).
- Data visualization, cleaning, and preparation in: (SalePriceStudy.ipynb).
- Model training, optimization, and validation in: (FeatureEngineering.ipynb).
- Dashboard planning, designing and development.
- Dashboard deployment and release. 

6.	Ethical or Privacy concerns?

- As this dataset has been found from a public source, my niece doesn’t need to concern of any. 

7.	Does the data suggest a particular model?

- The data suggests a regressor model where the target is the sale price.

8.	What are the model inputs and intended outputs? 

- The sale price can be influenced by the house attribute information provided above, and the outputs is the predicted sale price.

9.	What are the criteria for the performance goal of the predictions?

- I have agreed with my niece that an R2 score of at least 0.75 on the train set as well as on the test set would be perfect.

10.	How would my niece benefit from this?

- My niece would be able to maximize the sale price for the newly refurbished houses as well as for future on sale houses that her small real estate agency might occur. 


### Outcome after price prediction:

- After the finalisation of this project, we could see that the R2 that i aggreed with my niece has been meet. She initialy requested an R2 score above 0.75. 

![r2score](/static/images/scoretrainandtest.png)

- And we can see how the train sets and test sets have been conducted so they can be almost similar.

![testandtrain](/static/images/graftraintest.png)


---

## Dashboard Design

### Dashboard Expectations

The dashboard should contain:

- A project summary page, showing the project dataset summary and my niece’s requirements for this project.
- A page listing the findings related to which features that have the strongest correlation to the house sale price.
- A page displaying the 6 houses attributes and their respective predicted sale price.
- It should display a message informing the summed predicted price for all the 6 houses newly refurbished.
- Add interactive input and widgets that allow a user to provide real-time house data to predict the sale price.
- A page indicating my project hypothesis(es) and how I would validate it across the project. 
- A technical page displaying my model performance, and if I would deploy a ML pipeline to have displayed my pipeline steps. 

### Page 1: Quick project summary

Quick project summary: 

- Describe project dataset.
- State business requirements.
- Dataset Content Guidelines.

### Page 2: House Sale Price Study

- In the inception point of the project, I wanted this page to answer business requirement 1, but I couldn’t know in advance which plots would need to be displayed. 
- After we analysed the data, I aggreged with my niece that the page will:
- State business requirement 1.
- Checkbox: data inspection on housing sale dataset.
- Display the number of rows and columns in the data and display the first ten rows of the data.
- Display the variables that bear the strongest correlation to sale price and the conclusions.
- Checkbox: Individual plots showing how the sale price correlates to each variable. 

### Page 3: Price Predictor

- State business requirement 2
- List the details of my nieces' houses and their respective price predictions.
- Display the total sum of all the predicted house sales price.
- A set of widgets inputs, which relate to house sales dataset.
- The best features, discovered during feature engineering notebook are available to my nice in order to capture the attribute of each house that she asked for a price prediction.
- “Run predictive analysis”, this button serves to house data, provided by my niece, to the ML pipelines, and predicts the sale price for the house and displays the result to her (Therefore, she would be able to calculate the price as well for these 6 houses, and in future for the other houses that she might buy or sell). 

### Page 4: Project Hypothesis and Validation

- Before the analysis, I knew that this page would describe each project hypothesis, the conclusion, and how I will validate each one of them. 

- After the data analysis, we can report that:

1. An evaluation of sales price of other houses from this area are based on similar attributes with the 6 houses that my niece would like to sell, therefore, this project should provide an accurate prediction of sales price for each house. 

2. The correlation analysis shows that the sizes of the ground floor living area, the first floor, the basement, and the garage, play a key role in determining the house price. In addition, the year of the house when was built and the last refurbishment, the quality of the used materials also plays a significant role in determining a house price. 

### Page 5: ML: House Sale Price Prediction

- Considerations and conclusions after the pipeline will be trained.
- Present the ML Pipeline steps.
- Feature importance: List the features and plot the best features.
- Pipeline performance evaluation: Show model evaluation and plots.

---

## Unfixed Bugs

- After conducting a set of tests, I haven found any bugs.
- However, there are some warning as the pandas packages are updating, and some variables might not work accordingly. The project has been checked before submission on the 2nd of February, and everything works as expected.   

---

## Deployment

The master branch of this repository has been used for the deployed version of this application.

## Using Github & Gitpod

To deploy my Data application, I had to use the [Code Institute Full Template](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues).

- Click the Use This Template button.
- Add a repository name and brief description.
- Click the Create Repository from Template to create your repository.
- To create a Gitpod workspace you then need to click Gitpod, this can take a few minutes.
- When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than creating a new one. You should pin the workspace so that it isn't deleted.
- Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
	- git add .: adds all modified files to a staging area
	- git commit -m "A message explaining your commit": commits all changes to a local repository.
	- git push: pushes all your committed changes to your Github repository.

## Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](link)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open command line interface on your computer
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.

$ git clone [ADD Project link](https://house-price-predictor-pp5.herokuapp.com/)

7. Press Enter. Your local clone will be created.

## Deployment To Heroku

- The App live link is: [HERE!](https://house-price-predictor-pp5.herokuapp.com/)
- The project was deployed to Heroku using the following steps.
1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

---

## Credits & Content used.

- The content of this project, represent the understanding provided by walk-through projects provided by Code Institute.
- There might be some similarities as some contents have been copied and modified directly from the walk-through project 2 'Churnometer'. 
- Some bugs and issues appeared withing the project have been fixed using [Stack Overflow](https://stackoverflow.com/).
- I have explored in more details different terms used withing deep machine learning from [YouTube.](https://www.youtube.com/)
- Some issues that I encountered during this project have resolved withing the Slack Community, many thanks to Niel_ci. 
- The readme file has been built using the Code Institute template.
- Some elements present in the readme file have been inspired from [Van-essa.](https://github.com/van-essa/heritage-housing-issues#readme) 
- My mentor Marcel who guided me thru the project making sure the best practices are used.


## Acknowledgements

Thank you Code Institute for this awesome course, I really enjoyed being taken from believing that coding is a gibberish language to actually understanding it and working with.
- Many thanks to my both mentors who guided me throughout this course, Daisy and Marcel. 
- And huge thanks to Jordan White, who introduced me to this course, and pushed me to don't stop, not mattering how hard it was at the time.  

---