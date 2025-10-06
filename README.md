# 🍴 Zomato Restaurant Data Analysis (EDA with Streamlit)

This project performs **Exploratory Data Analysis (EDA)** on the **Zomato Restaurant Dataset** using Python and Streamlit.  
It provides insights into restaurant ratings, cuisines, costs, and customer behavior across different countries.  

---

## 📊 Project Overview

The food industry is a rapidly growing sector, and understanding customer preferences is crucial.  
This project helps answer key questions such as:

- Which countries have the most restaurants listed on Zomato?  
- What are the most popular cuisines worldwide?  
- How are restaurant ratings distributed?  
- What is the relationship between **cost for two** and **ratings**?  
- How do price ranges vary across restaurants?  
- Which cuisines and countries are the most expensive?  

The project also includes **visual dashboards** for better storytelling.

---

## 🗂️ Dataset Information

We used the following files from the [Zomato Kaggle Dataset](https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data):

- `zomato.csv` → Main dataset containing restaurant details  
- `Country-Code.xlsx` → Mapping of `Country Code` to `Country Name`  

The dataset includes:  
- Restaurant name, location, and cuisines  
- Aggregate ratings & votes  
- Average cost for two  
- Price range categories  

---

## 🔎 Key Features in the Analysis

✅ **Top 10 Countries** with the most restaurants  
✅ **Top 10 Cuisines** globally  
✅ **Distribution of Ratings** (histogram with KDE)  
✅ **Price Range Analysis** (pie chart)  
✅ **Cost vs Rating Scatterplot** (bubble chart with votes & price range)  
✅ **Correlation Heatmap** (cost, votes, ratings, price range)  
✅ **Votes Distribution**  
✅ **Average Cost by Country**  
✅ **Cuisine vs Average Rating**  

All analyses are presented with **interactive Streamlit dashboards**.

---

## 🛠️ Tech Stack

- **Python 3.9+**  
- **Pandas** – Data manipulation  
- **Matplotlib / Seaborn** – Visualization  
- **Streamlit** – Interactive dashboard  
- **OpenPyXL** – For Excel file reading  

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/zomato-restaurant-analysis.git
cd zomato-restaurant-analysis
