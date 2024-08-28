import pandas as pd
import plotly.express as px

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Count the number of prizes awarded each year
prizes_per_year = df['year'].value_counts().sort_index()

# Convert the Series to a DataFrame for plotting
prizes_per_year_df = prizes_per_year.reset_index()
prizes_per_year_df.columns = ['year', 'count']

# Create a bar chart
fig = px.bar(prizes_per_year_df,
             x='year',
             y='count',
             labels={'year': 'Year', 'count': 'Number of Prizes'},
             title='Number of Nobel Prizes Awarded Each Year')

# Show the figure
fig.show()
