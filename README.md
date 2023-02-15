
# Predict Future Sales

This repository contains code and data for the Kaggle competition "Predict Future Sales". The goal of the competition is to predict monthly sales for a set of products and shops, based on historical sales data.

## Getting started

### Requirements

To run the code in this repository, you will need:
* Python 3
* Jupyter Notebook or another Python development environment

### Installation
1. Clone this repository to your local machine:
    ```
    git clone https://github.com/arnavandraskar/Predict-future-sales.git
    ```

2. Install the required Python packages:

```
pip install -r requirements.txt
```
### Data
The data for this competition can be downloaded from the Kaggle website here.The data consists of the following files:

* `sales_train.csv`: Monthly sales data for each shop and product (from January 2013 to October 2015).
* `test.csv`: Test set. You need to forecast the sales for these shops and products for November 2015.
* `items.csv`: Supplementary information about the items/products.
* `item_categories.csv`: Supplementary information about the item categories.
* `shops.csv`: Supplementary information about the shops.

### Notebooks
This repository contains several Jupyter Notebooks that demonstrate different approaches to solving the problem. These notebooks are located in the notebooks directory:

* `01-exploratory-data-analysis.ipynb`: Exploratory data analysis of the sales data.
* `02-feature-engineering.ipynb`: Feature engineering and creation of a baseline model.
* `03-time-series-forecasting.ipynb`: Time series forecasting using ARIMA and Facebook Prophet.
* `04-machine-learning.ipynb`: Machine learning approaches to predicting future sales.
