import pandas as pd
import plotly.express as px

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Count the number of prizes awarded each year
prizes_per_year = df['year'].value_counts().sort_index()

# Calculate the 5-year rolling average
rolling_avg = prizes_per_year.rolling(window=5).mean()

# Convert the Series to a DataFrame for plotting
rolling_avg_df = rolling_avg.reset_index()
rolling_avg_df.columns = ['year', 'rolling_avg']

# Create a line chart of the rolling average
fig = px.line(rolling_avg_df,
              x='year',
              y='rolling_avg',
              labels={'year': 'Year', 'rolling_avg': '5-Year Rolling Average of Prizes'},
              title='5-Year Rolling Average of Nobel Prizes Awarded Each Year')

# Show the figure
fig.show()
