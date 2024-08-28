import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Count the number of prizes awarded each year
prizes_per_year = df['year'].value_counts().sort_index()

# Calculate the 5-year rolling average
rolling_avg = prizes_per_year.rolling(window=5).mean()

# Create the scatter plot of the number of prizes awarded each year
plt.figure(figsize=(10, 6))
plt.scatter(prizes_per_year.index, prizes_per_year.values, color='blue', label='Number of Prizes')

# Superimpose the 5-year rolling average line
plt.plot(rolling_avg.index, rolling_avg.values, color='red', label='5-Year Rolling Average', linewidth=2)

# Add titles and labels
plt.title('Nobel Prizes Awarded Each Year with 5-Year Rolling Average')
plt.xlabel('Year')
plt.ylabel('Number of Prizes')
plt.legend()

# Save the plot as an image file
plt.savefig('nobel_prizes_plot.png')
