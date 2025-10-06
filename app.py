import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# Load Data
# -----------------------
@st.cache_data
def load_data():
    zomato = pd.read_csv("zomato.csv", encoding="latin-1")
    country = pd.read_excel("Country-Code.xlsx")
    zomato = pd.merge(zomato, country, on="Country Code", how="left")
    zomato.drop_duplicates(inplace=True)
    zomato = zomato.dropna(subset=['Cuisines', 'Aggregate rating'])
    return zomato

zomato = load_data()

# -----------------------
# Streamlit UI
# -----------------------
st.set_page_config(page_title="Zomato Restaurant Data Analysis", layout="wide")

st.title("🍴 Zomato Restaurant Data Analysis")
st.markdown("An interactive **Exploratory Data Analysis (EDA)** of Zomato Restaurants across different countries.")

# Sidebar
st.sidebar.header("🔎 Navigation")
menu = st.sidebar.radio(
    "Choose a section:",
    [
        "Top 10 Countries",
        "Top 10 Cuisines",
        "Rating Distribution",
        "Price Range Distribution",
        "Cost vs Rating",
        "Correlation Heatmap",
        "Votes Distribution",
        "Average Cost by Country",
        "Cuisine vs Rating"
    ]
)

# -----------------------
# 1. Top 10 Countries
# -----------------------
if menu == "Top 10 Countries":
    st.subheader("🌍 Top 10 Countries with Most Restaurants")
    country_counts = zomato['Country'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=country_counts.values, y=country_counts.index, palette="viridis", ax=ax)
    ax.set_title("Top 10 Countries with Most Restaurants")
    st.pyplot(fig)

# -----------------------
# 2. Top 10 Cuisines
# -----------------------
elif menu == "Top 10 Cuisines":
    st.subheader("🍲 Top 10 Cuisines Worldwide")
    cuisine_counts = zomato['Cuisines'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=cuisine_counts.values, y=cuisine_counts.index, palette="magma", ax=ax)
    ax.set_title("Top 10 Cuisines")
    st.pyplot(fig)

# -----------------------
# 3. Rating Distribution
# -----------------------
elif menu == "Rating Distribution":
    st.subheader("⭐ Distribution of Restaurant Ratings")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(zomato['Aggregate rating'], bins=20, kde=True, color='purple', ax=ax)
    ax.set_title("Distribution of Ratings")
    st.pyplot(fig)

# -----------------------
# 4. Price Range Distribution
# -----------------------
elif menu == "Price Range Distribution":
    st.subheader("💰 Price Range Distribution")
    price_range = zomato['Price range'].value_counts()
    fig, ax = plt.subplots(figsize=(7,7))
    price_range.plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=140,
        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'],
        ax=ax
    )
    ax.set_ylabel("")
    ax.set_title("Distribution of Price Ranges (1=Cheap, 4=Luxury)")
    st.pyplot(fig)

# -----------------------
# 5. Cost vs Rating Scatter
# -----------------------
elif menu == "Cost vs Rating":
    st.subheader("💵 Cost for Two vs ⭐ Rating")
    fig, ax = plt.subplots(figsize=(10,6))
    sns.scatterplot(
        x=zomato['Average Cost for two'],
        y=zomato['Aggregate rating'],
        size=zomato['Votes'],
        hue=zomato['Price range'],
        alpha=0.6,
        palette="coolwarm",
        ax=ax
    )
    ax.set_xlabel("Average Cost for Two")
    ax.set_ylabel("Aggregate Rating")
    ax.set_title("Cost vs Rating (Bubble size = Votes)")
    st.pyplot(fig)

# -----------------------
# 6. Correlation Heatmap
# -----------------------
elif menu == "Correlation Heatmap":
    st.subheader("📊 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(8,6))
    corr = zomato[['Average Cost for two','Price range','Votes','Aggregate rating']].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
    st.pyplot(fig)

# -----------------------
# 7. Votes Distribution
# -----------------------
elif menu == "Votes Distribution":
    st.subheader("🗳️ Distribution of Votes")
    fig, ax = plt.subplots(figsize=(10,6))
    sns.histplot(zomato['Votes'], bins=50, kde=False, color="teal", ax=ax)
    ax.set_xlim(0, 2000)  # limit extreme outliers
    ax.set_title("Votes Distribution (limited to 2000 for clarity)")
    st.pyplot(fig)

# -----------------------
# 8. Average Cost by Country
# -----------------------
elif menu == "Average Cost by Country":
    st.subheader("🌎 Average Cost for Two by Country")
    avg_cost_country = zomato.groupby("Country")["Average Cost for two"].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=avg_cost_country.values, y=avg_cost_country.index, palette="cubehelix", ax=ax)
    ax.set_title("Top 10 Countries by Average Cost for Two")
    st.pyplot(fig)

# -----------------------
# 9. Cuisine vs Rating
# -----------------------
elif menu == "Cuisine vs Rating":
    st.subheader("🍛 Top Cuisines vs Average Rating")
    cuisine_rating = zomato.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=cuisine_rating.values, y=cuisine_rating.index, palette="plasma", ax=ax)
    ax.set_title("Top 10 Cuisines by Average Rating")
    st.pyplot(fig)
