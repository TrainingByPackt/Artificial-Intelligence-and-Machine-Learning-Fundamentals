# Data preprocessing for classification

Load csv data on 2017-2018 January kickstarter projects from Kaggle.com, and apply preprocessing steps on the loaded data. 

​URL: https://www.kaggle.com/kemical/kickstarter-projects

Notice this repository does not contain the Kickstarter file. Please download it to make the code work.

Exercises:

1. Import the data frame using Pandas
2. Replace NA and N/A values with an outlier
3. Drop the ID column
4. Perform binarization on the `'backers'` column
5. Perform label encoding on the currency column. Possible labels are: `['AUD', 'CAD', 'CHF', 'DKK', 'EUR', 'GBP', 'HKD', 'JPY', 'MXN', 'NOK', 'NZD', 'SEK', 'SGD', 'USD']`
6. Perform min-max scaling on the `'goal'` column

Solution: `kickstarter.py`