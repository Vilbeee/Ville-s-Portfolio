# S&P 500 ESG Project:

### Introduction:

It has become quite apparent that sustainability has taken its place as an essential evaluation metric amongst investors. Investors increasingly base their investments using Environmental, Social and Governance (ESG) scores as one of the criteria. Companies that do well related to ESG metrics are often seen as less risky, great for long-term and at good tackling uncertainty. Investing in companies that have proven to make sustainable choices, can also work as a channel for investors to make a positive difference. To make the ESG investing phenomenon a more straightforward process, companies have been given ESG risk ratings based on their environmental, social and governance practices.

This project focuses on companies in the S&P 500 index. The analysis is done in each of the three main categories of ESG as well as using the total ESG rating of each company. The data will be analysed by each sector as well as by individual companies. The objective is to create a good overview of sustainability amongst the largest companies in the United States. The dataset used in this project was sourced from Kaggle. The data will be prepared and the analysis will be done using Power BI.

I will be dividing this project brief into three parts. The first part will consist of the steps taken in the preparation of the data. In the second part I will be explaining some of the steps taken in the creation of the dashboard. In addition I will be showcasing all of the notable features I added in it. The third and final official part will consist of analyzing the data using the visuals in the dashboard I created. Finally I will finish by giving my overall thoughts about the project and discussing its limitations as well as possible areas of improvement. 

#### The parameters in the dataset:

- Environment Risk Score: A score indicating the company's environmental sustainability and impact.

- Governance Risk Score: A score reflecting the quality of the company's governance structure.

- Social Risk Score: A score assessing the company's societal and employee-related practices.

- Controversy Level: The level of controversies associated with the company's ESG practices.

- Controversy Score: A numerical representation of the extent of ESG-related controversies.

- ESG Risk Percentile: The company's rank in terms of ESG risk compared to others.

- ESG Risk Level: A categorical indication of the company's ESG risk level.

## Part 1. Data Preparation

While the data was mostly clean and ready to be analyzed, there were some small annoyances that had to be handled before I was able to start creating my Power BI dashboard.

First I had to deal with the common problem with .CVS files where the headers are not recognized automatically. Thankfully there is an easy fix for this.

![Use first row as headers](https://github.com/user-attachments/assets/7201d8ba-4c55-429e-a79d-2dfbf801e5b9)

After this I began dealing with blank data cells. This meant Replacing blank cells with "null". As well as checking whether the dataset had any other null equivalents. This data set had some cells with the text N/A or None Controversy Level, which were both equal to null. 

![Replace blanks with null](https://github.com/user-attachments/assets/b4b63aab-a89d-40bc-8c1b-6a9570109aad)

![Check for null equivalents and replace them](https://github.com/user-attachments/assets/c56a71de-c10f-4eee-8556-ee161b55a228)

There were some rows with nulls on all of the ESG metrics, which meant that these companies were unfortunately impossible to add into the analysis. This is why I unchecked nulls on one of the ESG score columns and hid those companies.

![Uncheck null](https://github.com/user-attachments/assets/bf4138a3-3eeb-4ab8-9ce0-054d2843fe2f)

I realized that the ESG Risk percentile column values were written as "31st percentile". This meant that the datatype would be recognized as text instead of a numerical value. This is why I created a new column by using the "Column From Examples" tool.

![Creating a new percentile column with numbers](https://github.com/user-attachments/assets/f29bb47c-ac30-4231-8eff-52a2bcd60733)

Before being able to detect the right data types for all columns I had to deal with some commas and dots. The dataset was using commas as a thousand separator, which made the system recognize the values as decimals. The dataset was also using dots instead of commas for decimals, which made the system recognize those values as text. In the Finnish language commas are used with decimal numbers.

![Replace comma with blank for proper data type detection](https://github.com/user-attachments/assets/a784d6e6-c50f-4208-a3b6-80cad5c40e9e)

![Replace dot with comma for proper datatype detection](https://github.com/user-attachments/assets/0aeb4b0a-e192-4b99-a27d-817eb12aa029)

![Detect datatype](https://github.com/user-attachments/assets/9ca9d222-997f-465f-810d-e0a8ca46da10)

Now that I was finally able to detect the right datatypes, I decided to make some final tidying such as shortening some columns' values for nicer visuals when creating the dashboard. The Controversy column as an example below.

![Create improved columns](https://github.com/user-attachments/assets/1260b449-d5f2-4559-864a-487e53fe1f72)

During the dashboard creation I realized a need for a state column, which ended up requiring quite a lot of manual work as the "Column From Examples" tool was not able to recognize the similarities between the format in the Address column.

![State Column](https://github.com/user-attachments/assets/3f965b54-c5e6-4f05-b543-1fd2a22ec334)


## Part 2. Dashboard Creation

I began my dashboard creation by creating a colour scheme, which would fit the theme ESG. As one of the main things people think of when they hear the word sustainability is the environment as well as climate issues, I decided to move forward with a light background tone and green visuals reminiscent of nature.

For functionality, I wanted to keep the layout simple, but have it contain as much information as possible. I aimed for a final product where one can get all of the important information at a glance and then proceed to further investigate different sectors or metrics in detail. 

As the home page, I chose a layout which showcases the total ESG risk score figures. The graphs will be analysed more in the analysis part of this brief.

![Layout](https://github.com/user-attachments/assets/7121fbb0-3433-47c6-ba2f-5ef8cde8e2e1)

I divided the dashboard into 5 main sections. First section is the one in the picture above containing the total ESG scores. The second, third and fourth sections contain the exact same figures except total ESG score is replaced with the environmental, social and governance scores in that order. The fifth section contains controvery score data. The Fifth section can be seen below.

![controversy layout](https://github.com/user-attachments/assets/dfc368e7-dbb6-4afd-8443-504ad195561d)

While It has some some differences to the previous layouts, I wanted to keep it as similar as possible, while still making the best use of the data set. For the controversy layout, I had to create a risk percentile grouping using DAX.

```DAX
Risk Percentile Groups = 
SWITCH(
    TRUE(),
    'S&P500 ESG Risk Ratings Data'[ESG Risk Percentile] <= 20, "1-20",
    'S&P500 ESG Risk Ratings Data'[ESG Risk Percentile] <= 40, "21-40",
    'S&P500 ESG Risk Ratings Data'[ESG Risk Percentile] <= 60, "41-60",
    'S&P500 ESG Risk Ratings Data'[ESG Risk Percentile] <= 80, "61-80",
    'S&P500 ESG Risk Ratings Data'[ESG Risk Percentile] <= 100, "81-100",
    "Uncategorized"
)
```
The final layout I added was a Map layout. As most of the S&P 500 companies' addresses were located in the United States, It was interesting to add a map feature to showcase the states with the best and worst ESG risk scores on average.

![map](https://github.com/user-attachments/assets/386a09f3-690e-45dd-a18d-c4a80daab5f2)

I used conditionally formatted colours for the map to get an idea of each state's average total ESG risk score at a glance. Conditional formatting was also used in all of the graphs to either highlight good and bad values or to highlight large/small values. This makes it much faster to get a grasp of the visuals and how the metrics should be read.

I added quick filtering options on all of the graphs as well as using the sector dropdown menu located at the top right corner. This allows for fast comparison between different sectors or risk levels.

The dashboard can be navigated using the buttons on the panel on the left side. The buttons are assigned from top to bottom in the order as I described the layout. 

The dashboard can be found and accessed using the .p file found at:



The entire dashboard can also be seen as a .pdf file at:



## Part 3. Analysis

### Total ESG

The analysis will be done in the same order as the dashboard was described. I will be starting with the total ESG scores as this will give us a good overall view into the dataset and sectors. 

Firstly we can see that the overall average ESG risk score is 21,53 and the median is 21,05. These two figures give us a good benchmark moving forward. As we see in the figure below, there are five sector that have an average above the total average and six sectors below it. The clear highest average score out of all the sector is in the energy sector. While the outstanding lowest average is in the real estate sector. For a potential ESG-investor this would mean that the energy sector at a glance seems like an area to avoid, while real estate could potentially be a great option.

![total average sector](https://github.com/user-attachments/assets/590fd38a-d828-42ce-b663-2139f67ad39a)

While the sector average is much higher than the overall average, we can see that there are still some potentially good companies even by ESG metrics, if we sort the dashboard by the energy sector. Both Kinder Morganm Inc. and Schlumberger Limited are under the overall average score and place in the low category and the low end of the medium category based on risk level. Based on purely ESG metrics, these two companies could be potentially good investment options as they outperform their sector.

![ESG total energy](https://github.com/user-attachments/assets/dc5936b0-45c1-45fb-9661-450dafccc7d7)

When looking at the bottom 10 scores sorting by company, we can see that almost half of the companies come from the technology sector, a third come from the real estate sector and the rest come from consumer cyclical and communication services sectors. The technology and real estate sectors stand out as the two major outperformers when it comes to ESG scores and should be quite safe bets to an ESG-investor.

### Environmenta, Social and Governance

While the total ESG risk score gives a good overview of the sectors and the companies, It doesn't necessarily tell the full story. If a company is doing great on two of the three categories of ESG, but perform much worse than average on the last criteria, It should raise some concern in the investors. 

As could most likely be expected by many, the energy sector is clearly the worst performer when it comes to the environmental risk score. 

![environmental risk](https://github.com/user-attachments/assets/dbf619de-6912-4ec0-aa2e-19b15b106c05)

But while the energy sector performs badly in the environment scoring, it performs better than average in both social and governance scores based on average scores. The overall average in the social score by sector is 9,07 and in the governance sector 6,73. 

![social risk](https://github.com/user-attachments/assets/68d8bb0f-2b68-453b-bb05-ba48517af02f)

![governance risk](https://github.com/user-attachments/assets/5b840f68-b070-4488-bf49-564d1dfe0146)

It is also important to note that there can be cases like financial sector, in which their total average score is better than average, but two of the subcategories are worse than average. In this case financial sector's total average is being dragged down by their very good environmental score. Despite this it is good to consider their outstandingly bad governance score. This can be the case for individual companies as well, which is why it is important to research in more detail before locking in one's purchase.

### Controversy

When considering the average controversy score by sector, we can once again see the energy sector outperforming most of the sectors despite their worst average total ESG risk score. As technology and real estate sectors stand as the top two best performing sectors by this criteria as well, an investor should be quite convinced that for an ESG-investment, these two sectors should be considered. 

Looking at the average controversy score by risk percentile, we can observe quite expected results as the average controversy score rises quite linearly as the risk percentage goes up. This is atleast until the last percentile group, during which the controversy score rises around double the amount compared to the changes between the other percentile groups. While these two metrics may seem to move quite closely together, it is good to note that this is not always the case. For example Hasbro had the lowest individual total ESG score out of all of the companies, yet places in the moderate category by controversy level.

![controversy by risk percentile](https://github.com/user-attachments/assets/c31e7471-0d8d-49a0-b677-52c4db4f870f)

The amount of companies per controversy level graph indicates that if an investor was to invest in S&P 500, on average the investment would be considered a moderate controversy level investment. 

![amount of companies per controversy level](https://github.com/user-attachments/assets/a827e5d9-e774-4259-ab6b-9932e72d92f4)

And finally looking at the map visual of average total ESG risk score by State, we can clearly see that a large portion of the bad performing companies are located around Texas. Comparing Texas and New York, which both have 41 companies in them, Texas has an average of 25,56 which is quite a bit higher than the overall average where as New York has an average of 19,53, a little bit lower than the overall average. A good chunk of this difference can be explained by the differences in the sectors that the companies in these areas operate in. Texas has 13 companies from the energy sector, where as New York only has one. California has 60 companies yet only an 18,25 average. A large portion of this can be explained by the 25 technology companies and 6 real estate companies that reside there.

![map](https://github.com/user-attachments/assets/c229053f-f2b4-4a41-a67e-51abd19acc13)

### Conclusion

Based on this dataset S&P 500 is on average quite ESG-investor friendly, but as we could see, there are major differences between sectors and companies. It also became apparent that sectors can often perform well on some criteria and much worse on others. This is why looking at the total ESG risk might not be the wisest way of ESG-investing. Depending on one's investing philosophies and what they deem important, it is important to look at the finer details before making the final decision. It is also good to understand that while ESG-metrics may give one a good glimpse on how a company performs it doesn't always tell the full story. For example a company selling a polluting factory to another company might upgrade their environmental risk score, but it doesn't necessarily decrease pollution as the other company will continue using the factory. This is why it is good to additionaly study the ESG-actions of the companies you may want to invest in.

### Final thoughts

My aim on this project was to create a simple yet functional dashboard, which can be used to easily analyse and compare sectors and companies based on their ESG metrics. The dashboard focuses more on finding the promising companies rather than showcasing the bad performers. I believe this was the correct path, as it would have more real life function for an investor looking for their next target.

I believe that the dashboard fulfills its job extremely well as it is easy to use and contains all of the information needed for the comparison based on this data. I also find the dashboard visually pleasing and fitting for the theme. 

Overall I was able to showcase my skills in using Power BI as well as analysing and reading into ESG data. Hopefully this project also shows my personal interest in the subject matter as well as the art of data analysis.

### Limitations & Possible improvements

While the data set was nicely prepared and has nearly 400 companies worth of data for the ESG metrics, it is still missing a good chunk of companies from the S&P 500. As a lot of the ESG related data is behind a paywall, I was not able to get access to it. I would gladly add yearly data into this analysis and use it for trend analysis. For a constantly evolving area such as sustainability, trend analysis would be important to see which companies are improving and which are lacking behind. This could make a major difference in an investors decision. While I believe my analysis was worthy of the current data and the graphs I was using, some more scientific analysis could aslo be implemented in the future.

I am satisified with the sorting possibilities of my dashboard, but to make it perfect, I believe a better system for sorting by companies could be created. Currently it takes some time to scroll through the dropdown menu or the list in the map layout.