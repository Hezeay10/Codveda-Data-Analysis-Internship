# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load cleaned dataset
df = pd.read_csv("cleaned_sentiment_dataset.csv")
# display first few rows and column names
print(df.head())
print(df.columns)
# Bar Plot: Sentiment Distribution

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="Sentiment"
)

plt.title("Distribution of Sentiments")
plt.xlabel("Sentiment")
plt.ylabel("Number of Posts")

plt.tight_layout()

plt.savefig("plots/sentiment_bar_plot.png")

plt.show()
# Line Chart: Average Likes by Hour

hourly_likes = df.groupby("Hour")["Likes"].mean()


plt.figure(figsize=(8,5))

plt.plot(
    hourly_likes.index,
    hourly_likes.values,
    marker="o"
)


plt.title("Average Likes by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Likes")

plt.legend(["Average Likes"])

plt.tight_layout()

plt.savefig("plots/hourly_likes_line_chart.png")

plt.show()
# Scatter Plot: Likes vs Retweets

plt.figure(figsize=(8,5))


sns.scatterplot(
    data=df,
    x="Likes",
    y="Retweets"
)


plt.title("Relationship Between Likes and Retweets")
plt.xlabel("Likes")
plt.ylabel("Retweets")


plt.tight_layout()

plt.savefig("plots/likes_retweets_scatter.png")


plt.show()