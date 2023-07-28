# Mood Travel Spain
##### Final Project Data Analytics bootcamp, by Ainara Guerra


![image](https://github.com/ainaraguerraf/final-project-ironhack-data/assets/115892160/23e9362b-5bb0-4b94-be7e-45a8e91cb129)


In this project you will find these folders, which are ordered chronologically following the steps in the project:

1. [Gathered data from datos.gob.es](https://github.com/ainaraguerraf/final-project-ironhack-data/tree/main/1.%20Gathered%20data%20from%20datos.gob.es)
2. [Creating and cleaning the dataset](https://github.com/ainaraguerraf/final-project-ironhack-data/tree/main/2.%20Creating%20the%20dataset)
3. [EDA](https://github.com/ainaraguerraf/final-project-ironhack-data/tree/main/3.%20EDA)
4. [SQL](https://github.com/ainaraguerraf/final-project-ironhack-data/tree/main/4.%20SQL)
5. [Tableau](https://github.com/ainaraguerraf/final-project-ironhack-data/tree/main/5.%20Tableau)
6. [Model](https://github.com/ainaraguerraf/final-project-ironhack-data/tree/main/6.%20Model)
7. [Recommender](https://github.com/ainaraguerraf/final-project-ironhack-data/tree/main/7.%20Recommender)
8. [Recommender examples](https://github.com/ainaraguerraf/final-project-ironhack-data/tree/main/8.%20Recommender%20examples%20(video))
9. Presentation


# 📃 Case study

The government of Spain wants to build a public online platform for their citizens to discover the country and promote national tourism. Although international tourists are the main source of income for this country, they want to change the paradigm and create more sustainable tourism with its citizens.

This public online platform will contain a personalized recommender that the user can use to discover sites for their next travel, according to their age, how are they traveling, and how she or he is feeling about this trip.


As a junior data analyst, the government wants me to create an MVP or this site recommender. This first MVP will be for new users and it will be based on the average preferences of other users for each site. The government has already started a focus group to recollect information about places, and they will give me the average data for each site. This data is about places in different cities and regions: Madrid, Vigo, Barcelona, Euskadi (as a region) and La Palma (as a region).


---
# 🔍 How was the dataset created

In reality, the data gathering was much more complex than the case study. It was the most difficult part of this project. We can divide the dataset into three main groups:

![image](https://github.com/ainaraguerraf/final-project-ironhack-data/assets/115892160/df4689f1-39a8-49d0-a328-e9d6af029a32)

### Data retrieved from datos.gob.es
Since the case study is with the Spanish government, I decided to get the basic data of each site from datos.gob.es. Data was fragmented and very different from region to region. I have to unify the categories of each site, then I reduced after that to improve this feature for the model. This resulted in 5000 rows of different sites.

It was at this moment also when I conceived the column "average sentiment". Based on my expertise regarding cultural site management and my passion for travel, I reviewed each site to create this column divided into history freak, adventurous, curious, artsy and relax.

### Data retrieve using Google API
I used the Google API and the free budget that this company gives initially to retrieve latitude, longitude, address and rating. At this point, the information I retrieved from Google API was a filter to only keep the sites that have longitude, latitude and rating, which resulted in 3.500 rows.

### Synthetic data
The third part of building the dataset is where the magic happens but with responsible usage of data and ethics always in mind.

The main difference between this project and other travel recommendation systems is that it is personalized. Webs such as Tripadvisor give random rankings of sites and "one size fits all" results.

So, to make it personalized, we needed features that could relate that place to users. I decided to go for the "average age" of the people that go to that place and the "average way of travel", it these people are going mostly in groups, alone, in couples or in family. 

When creating these columns, I encountered three situations:
- Fill it with random values, which was useless for the model.
- Heavily imbalanced data. For example, young people are average in most of the parks and lookout sites. This serves the model very well, giving 0.95 accuracy or more. _But_ this situation is not closer to reality, and I didn't find that ethical to work with.
- Clustered and slightly imbalanced data. Creating the datasets both with giving random values and clustering some categories. This gives between 0.78 and 0.81 accuracy and I found very decent taking into consideration I created all of this from scratch. Also, I find it more ethical because it is closer to reality.


  


---
# 🤖 The model
For the recommender, I chose a multiclass machine learning model. I tried different ones and I chose at the end random forest, with 0.78 accuracy. Some other ML gave me a higher accuracy score, but I know better how Random Forest works, so I preferred to stay safer at this point.

The target of the model (x) is the category most suitable to the inputs (y). So, the user inputs age, way of travel, mood for this trip and destination. The model gives him or her the category most suitable for his or her characteristics. It works in all the dataset with all the regions, because I don't have enough data to train the model for each region. 

Moreover, after giving the category, I created a query to retrieve the top sites of that category in that destination, based on Google ratings. 

In Streamlit, this function also retrieves a map, to make it more user-friendly.



---
# 🖼️ The brand: Mood Travel Spain
Everything on this project was wrapped up in the brand "Mood Travel Spain". 


![image](https://github.com/ainaraguerraf/final-project-ironhack-data/assets/115892160/93b33387-ad53-4a91-a545-b88fe0cd6a6f)



---

# 🪄 Recommender usage examples

Here you have a video of how this recommender works:

<a href="https://youtu.be/51KsRWyh7mE"><img src="http://img.youtube.com/vi/51KsRWyh7mE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>


