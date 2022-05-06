# Predict-future-sales
All industries aim to manufacture just the right number of products at the right time, but for retailers this issue is particularly critical as they also need to manage perishable inventory efficiently.

Too many items and too few items are both scenarios that are bad for business. (Estimates suggest that poor inventory management costs US retailers close to two billion dollars per year.)

## Business Problem
Demand forecasting is the process of predicting what the demand for certain products will be in the future. This helps manufacturers to decide what they should produce and guides retailers toward what they should stock.

## Demand forecasting is aimed at improving the following processes:
Supplier relationship management

Customer relationship management

Order fulfillment and logistics

Marketing campaigns

Manufacturing flow management

## Use of Machine Learning
Machine learning techniques allows for predicting the amount of products/services to be purchased during a defined future period. In this case, a software system can learn from data for improved analysis. Compared to traditional demand forecasting methods, a machine learning approach allows you to:

Accelerate data processing speed

Provide a more accurate forecast

Automate forecast updates based on the recent data

Analyze more data

Identify hidden patterns in data

Create a robust system

Increase adaptability to changes

## Data Gathering
Dataset is taken from kaggle competition and can be downloaded from here.

## Data Description:
You are provided with daily historical sales data. The task is to forecast the total amount of products sold in every shop for the test set. Note that the list of shops and products slightly changes every month. Creating a robust model that can handle such situations is part of the challenge.

## File descriptions
sales_train.csv — the training set. Daily historical data from January 2013 to October 2015.\
test.csv — the test set. You need to forecast the sales for these shops and products for November 2015.\
sample_submission.csv — a sample submission file in the correct format.\
items.csv — supplemental information about the items/products.\
item_categories.csv — supplemental information about the items categories.\
shops.csv- supplemental information about the shops.

## Data fields
ID — an Id that represents a (Shop, Item) tuple within the test set\
shop_id — unique identifier of a shop\
item_id — unique identifier of a product\
item_category_id — unique identifier of item category\
item_cnt_day — number of products sold. You are predicting a monthly amount of this measure\
item_price — current price of an item\
date — date in format dd/mm/yyyy\
date_block_num — a consecutive month number, used for convenience. January 2013 is 0, February 2013 is 1,…, October 2015 is 33\
item_name — name of item\
shop_name — name of shop\
item_category_name — name of item category

## Existing Approaches
Source: https://www.analyticsvidhya.com/blog/2021/06/predict-future-sales-using-xgbregressor/#h2_1

This is a blog on analytics vidhya by De-Yu Chao where they had approach it as a machine learning problem. They used XGBoost regressor model to predict future sales and scored 0.8865 (root mean squared error).

Do check out above link to know more about their solution, they have explained it in very detailed with code.

## My Improvements
I did experiment with various ML models, used some features from De-Yu Chao’s solution , tried playing with some quarter based features (can also look it as a moving averages feature). Best model among all (LightGBM) scored 0.8607(root mean squared error) which is slight an improvement form De-Yu Chao’s solution (0.8865 rmse).

All industries aim to manufacture just the right number of products at the right time, but for retailers this issue is particularly critical as they also need to manage perishable inventory efficiently.

Too many items and too few items are both scenarios that are bad for business. (Estimates suggest that poor inventory management costs US retailers close to two billion dollars per year.)

## Business Problem
Demand forecasting is the process of predicting what the demand for certain products will be in the future. This helps manufacturers to decide what they should produce and guides retailers toward what they should stock.

## Demand forecasting is aimed at improving the following processes:
Supplier relationship management

Customer relationship management

Order fulfillment and logistics

Marketing campaigns

Manufacturing flow management

## Use of Machine Learning
Machine learning techniques allows for predicting the amount of products/services to be purchased during a defined future period. In this case, a software system can learn from data for improved analysis. Compared to traditional demand forecasting methods, a machine learning approach allows you to:

Accelerate data processing speed

Provide a more accurate forecast

Automate forecast updates based on the recent data

Analyze more data

Identify hidden patterns in data

Create a robust system

Increase adaptability to changes

reference: If you want to learn above topics in more detail, here’s a blog by Liudmyla Taranenko from where it is abstracted.

## Data Gathering
Dataset is taken from kaggle competition and can be downloaded from here.

## Data Description:
You are provided with daily historical sales data. The task is to forecast the total amount of products sold in every shop for the test set. Note that the list of shops and products slightly changes every month. Creating a robust model that can handle such situations is part of the challenge.

## File descriptions
sales_train.csv — the training set. Daily historical data from January 2013 to October 2015.

test.csv — the test set. You need to forecast the sales for these shops and products for November 2015.

sample_submission.csv — a sample submission file in the correct format.

items.csv — supplemental information about the items/products.

item_categories.csv — supplemental information about the items categories.

shops.csv- supplemental information about the shops.

## Data fields
ID — an Id that represents a (Shop, Item) tuple within the test set

shop_id — unique identifier of a shop

item_id — unique identifier of a product

item_category_id — unique identifier of item category

item_cnt_day — number of products sold. You are predicting a monthly amount of this measure

item_price — current price of an item

date — date in format dd/mm/yyyy

date_block_num — a consecutive month number, used for convenience. January 2013 is 0, February 2013 is 1,…, October 2015 is 33

item_name — name of item

shop_name — name of shop

item_category_name — name of item category

## Existing Approaches
Source: https://www.analyticsvidhya.com/blog/2021/06/predict-future-sales-using-xgbregressor/#h2_1

This is a blog on analytics vidhya by De-Yu Chao where they had approach it as a machine learning problem. They used XGBoost regressor model to predict future sales and scored 0.8865 (root mean squared error).

Do check out above link to know more about their solution, they have explained it in very detailed with code.

## My Improvements
I did experiment with various ML models, used some features from De-Yu Chao’s solution , tried playing with some quarter based features (can also look it as a moving averages feature). Best model among all (LightGBM) scored 0.8607(root mean squared error) which is slight an improvement form De-Yu Chao’s solution (0.8865 rmse).

