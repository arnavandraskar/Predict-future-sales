{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "EDA_future_sales.ipynb",
      "provenance": [],
      "collapsed_sections": [
        "9oDvQonWLF7S",
        "vsZRD5b9Vy9z",
        "wefS1WvIVWqZ",
        "702wqd7kVjhm",
        "-Bt7Wfv4WpVD",
        "isZU-6d-XF1T",
        "echiuOntcObo",
        "tgXYW56NcKtp",
        "uLwSvSFocHGP",
        "x1onXjgDcFyD"
      ]
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Requirement gathering\n",
        "\n"
      ],
      "metadata": {
        "id": "XNNwdSMwdoOM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ],
      "metadata": {
        "id": "MULY2RByLUzj"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nKq-R8_LKh8W",
        "outputId": "72009286-8ded-4649-f3ff-a92a555a133f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2022-02-20 17:17:55--  https://storage.googleapis.com/kaggle-competitions-data/kaggle-v2/8587/868304/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1645553228&Signature=i13kABmhOt19aL2FrDI%2FwL%2BkHWSneIK1xI6X5lFtXbMM58ML6b5ZVTNRJj%2FwRHx2SPg4lPGNYB9HroQn%2FGMS8%2FP6H%2B6smau%2BFNaoHFcOf%2BDOR4zh0%2F1My0C84XxO9z24xtb56UtruRBPxQZrHfjsjVn7TE2naIbQ2d6JHb1wjH4WDRsvv7DkHmtMo%2BhPoM2ndJUw55ipViVXn2t9qTL5dVEbZhhommVqKzAk9HnpGlVuwHkGCVIED5vT3lFg6xZvEheyL1I821yZrwJ60qmMe6UMR468lm2uuh43mFpOn%2FyA8Ti34mR2%2FqXV9bByhJN%2FvD3GzQuWV2gQ70VET%2FiP9Q%3D%3D&response-content-disposition=attachment%3B+filename%3Dcompetitive-data-science-predict-future-sales.zip\n",
            "Resolving storage.googleapis.com (storage.googleapis.com)... 108.177.125.128, 142.250.157.128, 142.251.8.128, ...\n",
            "Connecting to storage.googleapis.com (storage.googleapis.com)|108.177.125.128|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 15845085 (15M) [application/zip]\n",
            "Saving to: ‘competitive-data-science-predict-future-sales.zip’\n",
            "\n",
            "competitive-data-sc 100%[===================>]  15.11M  9.84MB/s    in 1.5s    \n",
            "\n",
            "2022-02-20 17:17:57 (9.84 MB/s) - ‘competitive-data-science-predict-future-sales.zip’ saved [15845085/15845085]\n",
            "\n"
          ]
        }
      ],
      "source": [
        "!wget --header=\"Host: storage.googleapis.com\" --header=\"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36\" --header=\"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\" --header=\"Accept-Language: en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,mr;q=0.5\" --header=\"Referer: https://www.kaggle.com/\" \"https://storage.googleapis.com/kaggle-competitions-data/kaggle-v2/8587/868304/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1645553228&Signature=i13kABmhOt19aL2FrDI%2FwL%2BkHWSneIK1xI6X5lFtXbMM58ML6b5ZVTNRJj%2FwRHx2SPg4lPGNYB9HroQn%2FGMS8%2FP6H%2B6smau%2BFNaoHFcOf%2BDOR4zh0%2F1My0C84XxO9z24xtb56UtruRBPxQZrHfjsjVn7TE2naIbQ2d6JHb1wjH4WDRsvv7DkHmtMo%2BhPoM2ndJUw55ipViVXn2t9qTL5dVEbZhhommVqKzAk9HnpGlVuwHkGCVIED5vT3lFg6xZvEheyL1I821yZrwJ60qmMe6UMR468lm2uuh43mFpOn%2FyA8Ti34mR2%2FqXV9bByhJN%2FvD3GzQuWV2gQ70VET%2FiP9Q%3D%3D&response-content-disposition=attachment%3B+filename%3Dcompetitive-data-science-predict-future-sales.zip\" -c -O 'competitive-data-science-predict-future-sales.zip'"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!unzip 'competitive-data-science-predict-future-sales.zip'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3gsA_OSMKwna",
        "outputId": "b4b521d5-4fc4-4b64-b248-e8580b451947"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archive:  competitive-data-science-predict-future-sales.zip\n",
            "  inflating: item_categories.csv     \n",
            "  inflating: items.csv               \n",
            "  inflating: sales_train.csv         \n",
            "  inflating: sample_submission.csv   \n",
            "  inflating: shops.csv               \n",
            "  inflating: test.csv                \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# EDA"
      ],
      "metadata": {
        "id": "9oDvQonWLF7S"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df_train = pd.read_csv(\"sales_train.csv\") \n",
        "df_items = pd.read_csv(\"items.csv\")\n",
        "df_item_cat = pd.read_csv(\"item_categories.csv\")\n",
        "df_shops = pd.read_csv(\"shops.csv\")\n",
        "df_test = pd.read_csv(\"test.csv\")"
      ],
      "metadata": {
        "id": "16wL0wrnKwkA"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_train.shape #shape of data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3c56ZguBKwWc",
        "outputId": "ffc056a1-2352-4d8a-e2a9-7dd40f40ddee"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2935849, 6)"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_train.head() #reading top 5 rows"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "B-0K0Y3ZMcVE",
        "outputId": "4e7cc9e3-00ae-496c-f370-b567ee4d2253"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-9587fdc8-1f3e-480a-b1bd-fe7b807bca05\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>date</th>\n",
              "      <th>date_block_num</th>\n",
              "      <th>shop_id</th>\n",
              "      <th>item_id</th>\n",
              "      <th>item_price</th>\n",
              "      <th>item_cnt_day</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>02.01.2013</td>\n",
              "      <td>0</td>\n",
              "      <td>59</td>\n",
              "      <td>22154</td>\n",
              "      <td>999.00</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>03.01.2013</td>\n",
              "      <td>0</td>\n",
              "      <td>25</td>\n",
              "      <td>2552</td>\n",
              "      <td>899.00</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>05.01.2013</td>\n",
              "      <td>0</td>\n",
              "      <td>25</td>\n",
              "      <td>2552</td>\n",
              "      <td>899.00</td>\n",
              "      <td>-1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>06.01.2013</td>\n",
              "      <td>0</td>\n",
              "      <td>25</td>\n",
              "      <td>2554</td>\n",
              "      <td>1709.05</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>15.01.2013</td>\n",
              "      <td>0</td>\n",
              "      <td>25</td>\n",
              "      <td>2555</td>\n",
              "      <td>1099.00</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9587fdc8-1f3e-480a-b1bd-fe7b807bca05')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-9587fdc8-1f3e-480a-b1bd-fe7b807bca05 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-9587fdc8-1f3e-480a-b1bd-fe7b807bca05');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "         date  date_block_num  shop_id  item_id  item_price  item_cnt_day\n",
              "0  02.01.2013               0       59    22154      999.00           1.0\n",
              "1  03.01.2013               0       25     2552      899.00           1.0\n",
              "2  05.01.2013               0       25     2552      899.00          -1.0\n",
              "3  06.01.2013               0       25     2554     1709.05           1.0\n",
              "4  15.01.2013               0       25     2555     1099.00           1.0"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_train.info() #Data types and other info"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fp1TuQAfKwhv",
        "outputId": "6913e504-07aa-405c-aff8-dc28d8056abf"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 2935849 entries, 0 to 2935848\n",
            "Data columns (total 6 columns):\n",
            " #   Column          Dtype  \n",
            "---  ------          -----  \n",
            " 0   date            object \n",
            " 1   date_block_num  int64  \n",
            " 2   shop_id         int64  \n",
            " 3   item_id         int64  \n",
            " 4   item_price      float64\n",
            " 5   item_cnt_day    float64\n",
            "dtypes: float64(2), int64(3), object(1)\n",
            "memory usage: 134.4+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_train.describe() #statistical info"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "OygBnYyLKwfX",
        "outputId": "6191de0c-f3f0-4240-eeb3-0fde9070676f"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-69e47e1a-3e01-4273-827a-88b1ca46e0d0\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>date_block_num</th>\n",
              "      <th>shop_id</th>\n",
              "      <th>item_id</th>\n",
              "      <th>item_price</th>\n",
              "      <th>item_cnt_day</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>2.935849e+06</td>\n",
              "      <td>2.935849e+06</td>\n",
              "      <td>2.935849e+06</td>\n",
              "      <td>2.935849e+06</td>\n",
              "      <td>2.935849e+06</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>1.456991e+01</td>\n",
              "      <td>3.300173e+01</td>\n",
              "      <td>1.019723e+04</td>\n",
              "      <td>8.908532e+02</td>\n",
              "      <td>1.242641e+00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>9.422988e+00</td>\n",
              "      <td>1.622697e+01</td>\n",
              "      <td>6.324297e+03</td>\n",
              "      <td>1.729800e+03</td>\n",
              "      <td>2.618834e+00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000e+00</td>\n",
              "      <td>0.000000e+00</td>\n",
              "      <td>0.000000e+00</td>\n",
              "      <td>-1.000000e+00</td>\n",
              "      <td>-2.200000e+01</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>7.000000e+00</td>\n",
              "      <td>2.200000e+01</td>\n",
              "      <td>4.476000e+03</td>\n",
              "      <td>2.490000e+02</td>\n",
              "      <td>1.000000e+00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>1.400000e+01</td>\n",
              "      <td>3.100000e+01</td>\n",
              "      <td>9.343000e+03</td>\n",
              "      <td>3.990000e+02</td>\n",
              "      <td>1.000000e+00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>2.300000e+01</td>\n",
              "      <td>4.700000e+01</td>\n",
              "      <td>1.568400e+04</td>\n",
              "      <td>9.990000e+02</td>\n",
              "      <td>1.000000e+00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>3.300000e+01</td>\n",
              "      <td>5.900000e+01</td>\n",
              "      <td>2.216900e+04</td>\n",
              "      <td>3.079800e+05</td>\n",
              "      <td>2.169000e+03</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-69e47e1a-3e01-4273-827a-88b1ca46e0d0')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-69e47e1a-3e01-4273-827a-88b1ca46e0d0 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-69e47e1a-3e01-4273-827a-88b1ca46e0d0');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "       date_block_num       shop_id       item_id    item_price  item_cnt_day\n",
              "count    2.935849e+06  2.935849e+06  2.935849e+06  2.935849e+06  2.935849e+06\n",
              "mean     1.456991e+01  3.300173e+01  1.019723e+04  8.908532e+02  1.242641e+00\n",
              "std      9.422988e+00  1.622697e+01  6.324297e+03  1.729800e+03  2.618834e+00\n",
              "min      0.000000e+00  0.000000e+00  0.000000e+00 -1.000000e+00 -2.200000e+01\n",
              "25%      7.000000e+00  2.200000e+01  4.476000e+03  2.490000e+02  1.000000e+00\n",
              "50%      1.400000e+01  3.100000e+01  9.343000e+03  3.990000e+02  1.000000e+00\n",
              "75%      2.300000e+01  4.700000e+01  1.568400e+04  9.990000e+02  1.000000e+00\n",
              "max      3.300000e+01  5.900000e+01  2.216900e+04  3.079800e+05  2.169000e+03"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_train.isnull().sum() #checking missing value"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dLY6m_jvKwdA",
        "outputId": "1ee02fd9-098b-41fd-e4b5-1e66f0e0629b"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "date              0\n",
              "date_block_num    0\n",
              "shop_id           0\n",
              "item_id           0\n",
              "item_price        0\n",
              "item_cnt_day      0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Number of Duplicates\" ,len(df_train[df_train.duplicated()]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lRkQfM9gKwYk",
        "outputId": "c6459065-44ba-4109-8f37-0f76d7ef85ed"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of Duplicates 6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_train[\"date\"]= pd.to_datetime(df_train[\"date\"], format='%d.%m.%Y')\n",
        "df_train.sort_values(by=\"date\", inplace=True)\n",
        "df_train.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "2JAfjZ19KwR1",
        "outputId": "5715229f-84ba-43c5-fb32-0ad91869e82f"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-b61d9187-7534-4703-a954-22f6d8585438\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>date</th>\n",
              "      <th>date_block_num</th>\n",
              "      <th>shop_id</th>\n",
              "      <th>item_id</th>\n",
              "      <th>item_price</th>\n",
              "      <th>item_cnt_day</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>49800</th>\n",
              "      <td>2013-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>18</td>\n",
              "      <td>5823</td>\n",
              "      <td>2500.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29784</th>\n",
              "      <td>2013-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>27</td>\n",
              "      <td>5573</td>\n",
              "      <td>849.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>35476</th>\n",
              "      <td>2013-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>7</td>\n",
              "      <td>1006</td>\n",
              "      <td>399.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8330</th>\n",
              "      <td>2013-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>19</td>\n",
              "      <td>17707</td>\n",
              "      <td>899.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>57384</th>\n",
              "      <td>2013-01-01</td>\n",
              "      <td>0</td>\n",
              "      <td>14</td>\n",
              "      <td>19548</td>\n",
              "      <td>149.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b61d9187-7534-4703-a954-22f6d8585438')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b61d9187-7534-4703-a954-22f6d8585438 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b61d9187-7534-4703-a954-22f6d8585438');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "            date  date_block_num  shop_id  item_id  item_price  item_cnt_day\n",
              "49800 2013-01-01               0       18     5823      2500.0           1.0\n",
              "29784 2013-01-01               0       27     5573       849.0           1.0\n",
              "35476 2013-01-01               0        7     1006       399.0           1.0\n",
              "8330  2013-01-01               0       19    17707       899.0           1.0\n",
              "57384 2013-01-01               0       14    19548       149.0           1.0"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"We have records from date {} to {}\".format(df_train.date.min().date(),df_train.date.max().date()))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nPTD_i3pzVb8",
        "outputId": "04c76346-5200-426c-d4e4-ccdb79c01cd4"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "We have records from date 2013-01-01 to 2015-10-31\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_train_2 = df_train.merge(df_items, on='item_id', how='left' )\n",
        "print(\"shop ids in train data:\", len(df_train.shop_id.unique()), \" Out of:\", len(df_shops.shop_id.unique()))\n",
        "print(\"item ids in train data:\", len(df_train.item_id.unique()), \" Out of:\", len(df_items.item_id.unique()))\n",
        "print(\"item cataegory ids in train data:\", len(df_train_2.item_category_id.unique()), \" Out of:\", len(df_items.item_category_id.unique()))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nqbz6s33KwPa",
        "outputId": "9029bd3d-f880-487b-bfb5-ae96964a1ed8"
      },
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "shop ids in train data: 60  Out of: 60\n",
            "item ids in train data: 21807  Out of: 22170\n",
            "item cataegory ids in train data: 84  Out of: 84\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_test_2 = df_test.merge(df_items, on='item_id', how='left' )\n",
        "print(\"shop ids in test data:\", len(df_test.shop_id.unique()), \" Out of:\", len(df_shops.shop_id.unique()))\n",
        "print(\"item ids in test data:\", len(df_test.item_id.unique()), \" Out of:\", len(df_items.item_id.unique()))\n",
        "print(\"item cataegory ids in test data:\", len(df_test_2.item_category_id.unique()), \" Out of:\", len(df_items.item_category_id.unique()))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v4Gz8p36KvAn",
        "outputId": "1380a785-3105-4b8b-cf0e-d4b866d0c166"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "shop ids in test data: 42  Out of: 60\n",
            "item ids in test data: 5100  Out of: 22170\n",
            "item cataegory ids in test data: 62  Out of: 84\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Analysing Outliers"
      ],
      "metadata": {
        "id": "vsZRD5b9Vy9z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10,4))\n",
        "sns.boxplot(x=df_train.item_cnt_day)\n",
        "for i in range(90,101):\n",
        "  print(\"{}th percenile value of item count: {}\".format(i,np.percentile(df_train.item_cnt_day.values,i)))\n",
        "outlier_item_cnt = np.percentile(df_train.item_cnt_day.values,100) "
      ],
      "metadata": {
        "id": "FkLZzshXKu9N",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 471
        },
        "outputId": "b42b0ad0-3872-46d9-f6ea-d5c2c5cbd0fd"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "90th percenile value of item count: 2.0\n",
            "91th percenile value of item count: 2.0\n",
            "92th percenile value of item count: 2.0\n",
            "93th percenile value of item count: 2.0\n",
            "94th percenile value of item count: 2.0\n",
            "95th percenile value of item count: 2.0\n",
            "96th percenile value of item count: 2.0\n",
            "97th percenile value of item count: 3.0\n",
            "98th percenile value of item count: 3.0\n",
            "99th percenile value of item count: 5.0\n",
            "100th percenile value of item count: 2169.0\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAj8AAAEHCAYAAABBbSdqAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAARnElEQVR4nO3df6yd910f8PcntgM4qbriRB3z6G5HE7BR1JKGirKBsqotdrqpY2MTHVpcwA1DEAfSSe2S69QuXtcxtUiJJrIAGYnGhvC2CLTWptVCoLWhxCmp0180pjgiUZr6RwpJs7rO9Xd/3HOvjq/vte/1j5zj+329pKP7nO95nu/zOd+vz+O3nufc+1RrLQAAvbhk1AUAALyUhB8AoCvCDwDQFeEHAOiK8AMAdGXlUla+4oor2sTExAUqBQDg/HnkkUcOt9aunNu+pPAzMTGRffv2nb+qAAAukKp6Yr52l70AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArYx9+7rrrrtx1112jLgMAWCbGPvzs3r07u3fvHnUZAMAyMfbhBwDgfBJ+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICurBx1AWfywgsvjLoEAGAZGfvw01obdQkAwDLishcA0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK6sHHUBw44cOZLJyclUVW699dZs3rx59rXrr79+dIXN49JLL02SfPOb30xV5Y477sjOnTvTWsvmzZuzdevWrF27Nu94xzuyY8eObN26NQ888EC2bNmSD33oQ5mamsqKFSuyefPm3HHHHdm+fXvuvffetNby7ne/O3feeWfe9773Zc2aNbP7PHLkSLZv354tW7bkwx/+cFpr2bFjR5599tnccsst2b59e+6///6TtpvZZm5fp3PgwIFs2bIla9euzXve8555a1mM+fb94IMP5v3vf3/Wrl2byy67LCtWrMiOHTtOqnfr1q2z722p+zxTHUkWHI+zGaveGTNgqcbhuLFi27Zti175nnvu2XbTTTddsGLuvvvu7NmzJ4cOHcr+/fvzta997YLt61xNTU1lampq9vmePXvyzDPP5PDhw9m7d2++/vWv5+jRo9mzZ0+mpqayZ8+efOUrX8n+/ftz4MCBHDly5KR19+7dm6eeeiqHDx/O/v3786UvfSnf+MY38sY3vnF2H3fffXc+8YlPZP/+/Xn88cdz+PDhHDt2LDt37syhQ4eyd+/ePPnkkydtN7PN3L5O59Zbb82hQ4dy9OjRBWtZjPn2/a53vSsnTpzIc889NzsGx44dO6neT37yk6e0n4vhOh599NEFx+Nsxqp3xgxYqpfyuLF9+/ant23bds/c9rG57HXkyJHs2rVr9vnBgwdHV8xZePHFF2eXn3/++VPaX3zxxbTWTnlfM+sOb3Pw4MG01rJ79+4cOXIkyfT47N69+5Q+PvKRj8w+f/7550/abnib4b5O58CBAyf1P18tizHfvh988MGTxmnGrl27Tqp3bvu5GK5j165dC47H2YxV74wZsFTjctwYm/Bz3333zfsfY8+mpqZy//33J5kenxMnTpyyznxjNrPd8DbDfZ3Ojh07zljLYsy37w984APzrnv8+PHZeo8fP35K+7kYruP48eOz/c99P2czVr0zZsBSjctxo1prp1+h6qYkNyXJq171qtc/8cQTF6SQG264IS+88MIF6ftitnr16nz0ox9d8visXr06SU7aZqav0zndd6sWs/2MufWuXr36tPXPV+9S97mYOhbqe756z2W/PTBmwFK91MeNqnqktXbd3PYznvlprd3TWruutXbdlVdeeWGqS/LmN785VXXB+r8YrVy5Mm95y1uS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\n",
            "text/plain": [
              "<Figure size 720x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "99% of training records has less 5 or less item count\n",
        "\n",
        "Only 1% of training records has more than 5 item count"
      ],
      "metadata": {
        "id": "UKtK5NbvrLIi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10,4))\n",
        "sns.boxplot(x=df_train.item_price)\n",
        "for i in range(90,101):\n",
        "  print(\"{}th percenile value of item price: {}\".format(i,np.percentile(df_train.item_price.values,i)))\n",
        "outlier_item_price = np.percentile(df_train.item_price.values,100) "
      ],
      "metadata": {
        "id": "XI7AbR58Kuzo",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 471
        },
        "outputId": "f3f393e2-c51f-4f2d-d820-cd4144a9b190"
      },
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "90th percenile value of item price: 1999.0\n",
            "91th percenile value of item price: 2090.0\n",
            "92th percenile value of item price: 2299.0\n",
            "93th percenile value of item price: 2499.0\n",
            "94th percenile value of item price: 2599.0\n",
            "95th percenile value of item price: 2690.0\n",
            "96th percenile value of item price: 2999.0\n",
            "97th percenile value of item price: 3190.0\n",
            "98th percenile value of item price: 3590.0\n",
            "99th percenile value of item price: 5999.0\n",
            "100th percenile value of item price: 307980.0\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAj8AAAEHCAYAAABBbSdqAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAQQ0lEQVR4nO3df6xedX0H8PeHXkQC/ig/YhyaVa1GnEgHndHEKWygRU1wQTOzJdRtSZ3bqi7xDxaaVRJI3M8M6jKCzlgWMn+xRbMEsChhyRbF1hUKI0phuNk4qQVFkKkt3/3xnNZL6b3tg0/vfXq/r1fy5J7zPec85/t8+n3u8+4557mnWmsBAOjFcYvdAQCAhST8AABdEX4AgK4IPwBAV4QfAKArM+OsfNppp7UVK1Ycpa4AAEzOtm3bvtdaO/3g9rHCz4oVK7J169bJ9QoA4Cipqm8dqt1pLwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6MrMYndgtk2bNuX2229PkrzpTW/K+vXrF7lHAMBSM1XhZ+fOndn9vT0HpgEAJm2qwk+SZNn0dQkAWDpc8wMAdEX4AQC6IvwAAF0RfgCArgg/AEBXhB8AoCvCDwDQFeEHAOiK8AMAdEX4AQC6IvwAAF0RfgCArgg/AEBXhB8AoCvCDwDQFeEHAOiK8AMAdEX4AQC6IvwAAF0RfgCArgg/AEBXhB8AoCvCDwDQFeEHAOiK8AMAdEX4AQC6IvwAAF0RfgCArgg/AEBXhB8AoCvCDwDQFeEHAOiK8AMAdEX4AQC6IvwAAF0RfgCArgg/AEBXhB8AoCvCDwDQFeEHAOiK8AMAdGWqws+uXbuSJ/cdmN+0aVM2bdq0iD0CAJaamcXuwGxPPPFE0tqB+Z07dy5ibwCApWiqjvwAABxtwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdEX4AgK4IPwBAV4QfAKArwg8A0BXhBwDoivADAHRF+AEAuiL8AABdmVnsDsznzjvvTJKcd955i9uRCVq+fHkeffTR7Nu3L0myatWqbN++PevWrcsNN9yQq6++OitXrsyePXuyYcOGPProo9m1a1cuueSS3Hjjjdm4cWPOP//8efexZ8+eXHHFFXn/+9+fa665Jhs3bsypp556xH3cv/242wHA4UzDZ4wjPwvskUceORB8kmT79u1Jkuuuuy6PP/54rrzyyiTJ5s2bc++992bXrl1JkhtvvDFJctVVVx12H5s3b86OHTty5ZVXZseOHbn++uvH6uP+7cfdDgAOZxo+Y6Y2/Ow/6tObBx98MNu2bctNN910yOV79+7NbbfdNuf2e/bsyc0335zWWh588MG01nLzzTdnz549R7T/2duPsx0AHM60fMZMZ/h5ct/h11nCNm7cmL179865fL6jP5s3b86TTz75lLZ9+/YdccKevf042wHA4UzLZ8xhw09VrauqrVW1dffu3QvRp+499thjaa3NuXy+YHTrrbc+bfnevXuzZcuWI9r37O3H2Q4ADmdaPmMOG35aa9e11la31laffvrpC9Gn5LhlC7OfKXXyySenquZcPjMz93XqF1xwwdOWz8zM5MILLzyifc/efpztAOBwpuUzZjpPe3XuiiuumDfgXH755XMuW7t2bY477qn/rMuWLcull156RPuevf042wHA4UzLZ8zUhp+zzz57sbuwKFasWJFzzz03F1100SGXz8zMzPtV91NPPTVr1qxJVWXFihWpqqxZs+aIv044e/txtgOAw5mWz5ipDT9L1fLly7Ns2c9O661atSpJsm7dupx00knZsGFDklE6PvPMM3PGGWckSS655JIk8x/12W/t2rU566yzsmHDhpx11lljJ+v92zvqA8CkTcNnTM13Ye3BVq9e3bZu3XrUOvO2t70tjz3+o2TZTFa9+lUH2q+++uqjtk8AYGmqqm2ttdUHtzvyAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCg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\n",
            "text/plain": [
              "<Figure size 720x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "99% of traning records has 5999 or less item price\n",
        "\n",
        "Only 1% of training records has more than 5999 item price"
      ],
      "metadata": {
        "id": "aGmLhqXBssm9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "###Shop wise selling"
      ],
      "metadata": {
        "id": "wefS1WvIVWqZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df_train_3 = df_train.groupby(['shop_id'], as_index=False)['item_cnt_day'].sum()\n",
        "plt.figure(figsize=(20,4))\n",
        "sns.barplot(x=\"shop_id\",y=\"item_cnt_day\", data=df_train_3)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 280
        },
        "id": "0yksyI_9talv",
        "outputId": "28743ad9-913d-4ad2-b23c-0e14d7823c7a"
      },
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1440x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Item category wise selling"
      ],
      "metadata": {
        "id": "702wqd7kVjhm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df_train_3 = df_train_2.groupby(['item_category_id'], as_index=False)['item_cnt_day'].sum()\n",
        "plt.figure(figsize=(23,4))\n",
        "sns.barplot(x=\"item_category_id\",y=\"item_cnt_day\", data = df_train_3)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 280
        },
        "id": "s0EDMYiRtajk",
        "outputId": "79cacd4d-12d7-4a05-f254-f5d62c5c646f"
      },
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1656x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Month wise selling"
      ],
      "metadata": {
        "id": "-Bt7Wfv4WpVD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df_train_3 = df_train.groupby(['date_block_num'], as_index=False)['item_cnt_day'].sum()\n",
        "plt.figure(figsize=(15,3))\n",
        "sns.barplot(x=\"date_block_num\",y=\"item_cnt_day\", data = df_train_3)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 226
        },
        "id": "boZOmNrGtahe",
        "outputId": "dbd0e0a1-5cc8-438a-edb4-7c176fb9965d"
      },
      "execution_count": 83,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1080x216 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# EDA on shop_id and item_id exist in test data"
      ],
      "metadata": {
        "id": "isZU-6d-XF1T"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "test_shop = df_test['shop_id'].unique()\n",
        "test_item = df_test['item_id'].unique()\n",
        "# Only shops that exist in test data\n",
        "_train = df_train[df_train['shop_id'].isin(test_shop)]\n",
        "# Only items that exist in test data\n",
        "_train = _train[_train['item_id'].isin(test_item)]"
      ],
      "metadata": {
        "id": "U_2lbhxRtafT"
      },
      "execution_count": 85,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"shape after exluding unwanted shop and item ids \",_train.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TVFxHk-8tac9",
        "outputId": "286a99a8-25a7-4837-f134-6b10094b64b7"
      },
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "shape after exluding unwanted shop and item ids  (1224439, 6)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Number of Duplicates\" ,len(_train[_train.duplicated()]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5BQO4gNBZwBv",
        "outputId": "f957858e-9357-4bda-bccb-ce634950ba0b"
      },
      "execution_count": 91,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of Duplicates 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Outlier Analysing"
      ],
      "metadata": {
        "id": "echiuOntcObo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10,4))\n",
        "sns.boxplot(x=_train.item_cnt_day)\n",
        "for i in range(90,101):\n",
        "  print(\"{}th percenile value of item count: {}\".format(i,np.percentile(_train.item_cnt_day.values,i)))\n",
        "outlier_item_cnt = np.percentile(_train.item_cnt_day.values,100) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 471
        },
        "id": "QWbQqc1iaBgz",
        "outputId": "6e542917-0397-47bd-d00e-1d0380bfcdb2"
      },
      "execution_count": 93,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "90th percenile value of item count: 2.0\n",
            "91th percenile value of item count: 2.0\n",
            "92th percenile value of item count: 2.0\n",
            "93th percenile value of item count: 2.0\n",
            "94th percenile value of item count: 2.0\n",
            "95th percenile value of item count: 2.0\n",
            "96th percenile value of item count: 3.0\n",
            "97th percenile value of item count: 3.0\n",
            "98th percenile value of item count: 4.0\n",
            "99th percenile value of item count: 7.0\n",
            "100th percenile value of item count: 2169.0\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAj8AAAEHCAYAAABBbSdqAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAQfklEQVR4nO3dfYxldX3H8c93H1xUjEWWUEulA0Yqa4wKq1FbDW0UF9OG2qdYTMFWu9YH1qoNtYXIbk1bqwETSCPFhwqprdG2RNOWVWxEqbTKrOICPi0qphIQWAEhKDq7v/4xd3Yvw87szjrDvTu/1yuZzJ1zzj3nN+eXe/ede+7srdZaAAB6sWLUAwAAeCSJHwCgK+IHAOiK+AEAuiJ+AICurFrIxmvXrm0TExNLNBQAgMWzbdu2u1prR81evqD4mZiYyOTk5OKNCgBgiVTVd/a13GUvAKAr4gcA6Ir4AQC6In4AgK6IHwCgK+IHAOiK+AEAuiJ+AICuiB8AoCviBwDoivgBALoifgCArogfAKAr4gcA6Ir4AQC6In4AgK6IHwCgK+IHAOiK+AEAujLW8XPxxRfn4osvHvUwAIBlZKzjZ+vWrdm6deuohwEALCNjHT8AAItN/AAAXRE/AEBXxA8A0BXxAwB0RfwAAF0RPwBAV8QPANAV8QMAdEX8AABdET8AQFfEDwDQFfEDAHRF/AAAXRE/AEBXxA8A0BXxAwB0RfwAAF0RPwBAV8QPANAV8QMAdEX8AABdET8AQFfEDwDQFfEDAHRF/AAAXRE/AEBXxA8A0BXxAwB0RfwAAF0RPwBAV8QPANAV8QMAdEX8AABdET8AQFfEDwDQFfEDAHRF/AAAXRE/AEBXxA8A0BXxAwB0RfwAAF1ZNeoBzOeBBx4Y9RAAgGVmrOOntTbqIQAAy4zLXgBAV8QPANAV8QMAdEX8AABdET8AQFfEDwDQFfEDAHRF/AAAXRE/AEBXxA8A0BXxAwB0RfwAAF0RPwBAV8QPANAV8QMAdEX8AABdET8AQFfEDwDQFfEDAHRF/AAAXRE/AEBXxA8A0BXxAwB0RfwAAF0RPwBAV8QPANAV8QMAdEX8AABdET8AQFfEDwDQFfEDAHRF/AAAXRE/AEBXxA8A0BXxAwB0RfwAAF0RPwBAV8QPANCVVaMewLCdO3dmy5Yt2bRpU1796lfvWX7KKac8IsdfvXp1VqxYkaOPPjp33HFHWmtZu3Ztbr311iRJVeW4447L6173upx77rn58Y9/nLe97W254oorsmnTplx00UXZtGlTLrzwwjzwwAO5/fbbc+yxx+acc87JBRdckKrKm9/85lx00UU5//zzk2TP73vhhRemtZa3vOUte9YfeeSR+zw3+1o/28z2+9tuse873z4mJydzzjnn5F3veldOPvnkJTv2Uu6PvZxb4GCMw3PHys2bNx/wxpdeeunmjRs3LtlgLrnkklxzzTXZvn177rnnniU7zlx2796dXbt25d57783U1FR27dqV++677yHb3H333bn22mvzwx/+MEnyuc99Lrfffnu2b9+eb3zjG9m+fXt27NiRe+65J1NTU9m5c2e2b9+em2++OXfeeeee7X70ox/l+uuv3/P77tixI3fddddD1j/vec/bc9zhc7Ov9bPNbL+/7Rb7vvPtY+PGjXnwwQdz7bXX5owzzliyYy/l/tjLuQUOxiP53LFly5bbNm/efOns5WNz2Wvnzp3ZunVrWmu55ZZbRj2ced1///17bk9NTe0Z81xjH142s92VV16ZK6+88mH3mVm/devW7Ny5M8nDz83s9bMNbz/fdot93/n2MTk5uee83X///dm2bduSHHsp98dezi1wMMbluWNs4ueyyy7L7t27Rz2MR8xPfvKTTE1Nzbl+165dufzyy5Ps+9wMr59tePv5tlvs+863j9mvMM5c9lvsYy/l/tjLuQUOxrg8d+w3fqpqY1VNVtXknXfeuWQD+dSnPjVvDCw3rbW01uZcPzU1lauuuirJvs/N8PrZhrefb7vFvu98+xh+tSzJw35erGMv5f7Yy7kFDsa4PHfsN35aa5e21ta31tYfddRRSzaQF73oRVm1aqzef72kqipVNef6VatW5cUvfnGSfZ+b4fWzDW8/33aLfd/59nH44Yc/ZJvZPy/WsZdyf+zl3AIHY1yeO8bmstdZZ52VFSvGZjhLbvXq1fPG3sqVK3PmmWcm2fe5GV4/2/D282232Pedbx+zL3tt2bJlSY69lPtjL+cWOBjj8twxNrVx5JFHZsOGDamqTExMjHo48xp+1WLVqlV7xjzX2IeXzWx32mmn5bTTTnvYfWbWb9iwYc+fAM4+N7PXzza8/XzbLfZ959vH+vXr95y3ww8/fJ9/6r4Y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\n",
            "text/plain": [
              "<Figure size 720x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "99%  dataset has 7 or less sellings\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "AZWXkBGgcuTy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10,4))\n",
        "sns.boxplot(x=_train.item_price)\n",
        "for i in range(90,101):\n",
        "  print(\"{}th percenile value of item price: {}\".format(i,np.percentile(_train.item_price.values,i)))\n",
        "outlier_item_price = np.percentile(_train.item_price.values,100) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 471
        },
        "id": "wDf0h_XraBdj",
        "outputId": "184dcdec-925f-4b58-80a8-0f721ae84d60"
      },
      "execution_count": 94,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "90th percenile value of item price: 2499.0\n",
            "91th percenile value of item price: 2599.0\n",
            "92th percenile value of item price: 2599.0\n",
            "93th percenile value of item price: 2599.0\n",
            "94th percenile value of item price: 2799.0\n",
            "95th percenile value of item price: 2999.0\n",
            "96th percenile value of item price: 3190.0\n",
            "97th percenile value of item price: 3490.0\n",
            "98th percenile value of item price: 3790.0\n",
            "99th percenile value of item price: 4990.0\n",
            "100th percenile value of item price: 59200.0\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAj8AAAEHCAYAAABBbSdqAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAUMklEQVR4nO3df7BmdX0f8PdndxEtqygL41jI9EI2KFulRmhGacqAQQO6QMaRqdPIrrVomurOKjiOgR0XmKmTFgezgBPHYkujbU1iafkhYCCw7UyZqLsJqyj+uOKmkcG4WZrEjRZd+PaP59zr3bu/7u69l3t3v6/XzJ17zvec55zv89nnnH0/33Oe+1RrLQAAvViy0B0AAHguCT8AQFeEHwCgK8IPANAV4QcA6MqyQ1n5xBNPbGNjY/PUFQCAubN169a/aq2dNL39kMLP2NhYtmzZMne9AgCYJ1X15/tqd9kLAOiK8AMAdEX4AQC6IvwAAF0RfgCArgg/AEBXhB8AoCvCDwDQFeEHAOiK8AMAdEX4AQC6IvwAAF0RfgCArgg/AEBXhB8AoCvCDwDQFeEHAOiK8AMAdEX4AQC6smyhO7A/N998c8bHx/PEE08kSU4++eQ9lq9cuTLr1q1biK4BAEewRRt+xsfH88ijjyVpSZLvP/2zri790VML1CsA4Ei3aMNPkjzz906YnP7xK940Of2Cb9yzEN0BAI4C7vkBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALqyqMLPzTffnJtvvvmI2S4AcORZttAdmGp8fPyI2i4AcORZVCM/AADzTfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8IPANAV4QcA6IrwAwB0RfgBALoi/AAAXRF+AICuCD8AQFeEHwCgK8sWugPPhW3btiVJzjvvvIXtyCwdc8wx+elPfzqrbdx666254oorJufPOOOMPPbYY3uss3Tp0jzzzDOT8+ecc04efvjhJMmaNWvyzne+M+Pj43tsZ6ozzzwzGzduzHvf+948+eSTWbp0aV7+8pfn61//+n77dfrpp+eVr3xlbr/99sN+bvuqT1XliiuuyKc+9anccMMNOf744/fb7/256qqrcsstt+Tpp59Oklx++eX59Kc/fcDHnHrqqfnud797aE/gCLFkyZJs2LAh119//WTb9NfRscceO1mvJFm1alV27NiRHTt25PLLL8+2bduycePGbNu2Lddff302btyY888/f49jdPPmzbnjjjvysY99LBdddFHuvffebNy4Mdddd93kOmNjY7ntttuyc+fObNiwIVWVH/3oR9m+ffvk63jFihXZuXNnrrrqqlx88cVJstd+brrpptx+++257LLL8p73vGdGdbj66qvz8MMP59xzz92jFhN27tyZ6667Lhs3bsyKFStmtM19GR8fz/r167Np06asXLnysLdzIDPp65YtW/LBD34wN9xwQ84666y9lj/44IN7/FvC/szVsTEb1Vqb8cpnn31227Jly7x1Zv369UmSTZs2Zf369dn6+F9OLvvxK940Of2Cb9yTs057aTZt2jSj7R7poWcujY2NZfv27bPaxubNm/OOd7xjv9upqlxyySW54447ZrWfubZ8+fKceOKJh/z8qyqHcpz0YNmyZdm9e/dhP37iNfL5z38+u3fvzrJly/LAAw/sFUrOP//8PWq/r/1u3rw5N954Y+68886D7vOhhx5Ksnf4mT4/Ewd7zI033pi77rorl1xySd7//vfPaJv7MnGsTQS9+TCTvq5evTq7du3K8uXLc/fdd++1/IILLtjj3xL2Z66OjZmoqq2ttbOntx/1l70Enz3NNvgkyUc/+tEDbqe1tuiCT5Ls2rXrsJ6/4LO32QSfZFTTu+++e3I7u3fv3utYPe+88/aq/b72+/a3vz333nvvjPZ511137XM/U3384x8/6LauvvrqPeY//OEP7zG/c+fO3HfffWmt5b777svOnTsPus19GR8fn3zNbt++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\n",
            "text/plain": [
              "<Figure size 720x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "99%  dataset has 4990 or less item price\n"
      ],
      "metadata": {
        "id": "VbVRzbdedHqC"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Shop wise selling"
      ],
      "metadata": {
        "id": "tgXYW56NcKtp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df_train_3 = _train.groupby(['shop_id'], as_index=False)['item_cnt_day'].sum()\n",
        "plt.figure(figsize=(20,4))\n",
        "sns.barplot(x=\"shop_id\",y=\"item_cnt_day\", data=df_train_3)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 280
        },
        "id": "ch78uisfaBbR",
        "outputId": "860e8f79-824b-4c47-82ec-a6801c913e62"
      },
      "execution_count": 95,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1440x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### catogery wise selling"
      ],
      "metadata": {
        "id": "uLwSvSFocHGP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "_train_2 = _train.merge(df_items, on='item_id', how='left' )\n",
        "df_train_3 = _train_2.groupby(['item_category_id'], as_index=False)['item_cnt_day'].sum()\n",
        "plt.figure(figsize=(23,4))\n",
        "sns.barplot(x=\"item_category_id\",y=\"item_cnt_day\", data = df_train_3)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 280
        },
        "id": "b3lpfbZ4aBY0",
        "outputId": "dedbff47-f904-4884-8e26-db51887d87ca"
      },
      "execution_count": 96,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1656x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Month wise selling"
      ],
      "metadata": {
        "id": "x1onXjgDcFyD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df_train_3 = _train.groupby(['date_block_num'], as_index=False)['item_cnt_day'].sum()\n",
        "plt.figure(figsize=(15,3))\n",
        "sns.barplot(x=\"date_block_num\",y=\"item_cnt_day\", data = df_train_3)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 226
        },
        "id": "zR4ycErfb3BY",
        "outputId": "5b102dae-335d-4bb9-9c92-bdb91882f59b"
      },
      "execution_count": 97,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1080x216 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "zvq6A2hbb291"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "jj2n9VW_b249"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}