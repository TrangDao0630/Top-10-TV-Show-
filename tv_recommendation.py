import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
tv_show_data = pd.read_csv('TV_show_data.csv')

# Clean and prepare the data
tv_show_data['Genres'] = tv_show_data['Genres'].apply(lambda x: eval(x) if isinstance(x, str) else [])
tv_show_data['Premiere Date'] = pd.to_datetime(tv_show_data['Premiere Date'], errors='coerce')
tv_show_data['End Date'] = pd.to_datetime(tv_show_data['End Date'], errors='coerce')

# Get the top 10 TV shows by rating
top_10_shows = tv_show_data.nlargest(10, 'Rating')

# Extract relevant information
top_10_names = top_10_shows['Name']
top_10_genres = [genre for sublist in top_10_shows['Genres'] for genre in sublist]
top_10_types = top_10_shows['Type']
top_10_languages = top_10_shows['Language']
top_10_networks = top_10_shows['Network']

# Plot the top 10 TV show names
plt.figure(figsize=(10, 6))
plt.barh(top_10_names, top_10_shows['Rating'], color='skyblue')
plt.xlabel('Rating')
plt.title('Top 10 TV Shows by Rating')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Plot the genres of the top 10 TV shows
genre_counts = pd.Series(top_10_genres).value_counts()
plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar', color='lightgreen')
plt.title('Genres of Top 10 TV Shows')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot the types of the top 10 TV shows
type_counts = top_10_types.value_counts()
plt.figure(figsize=(10, 6))
type_counts.plot(kind='bar', color='lightcoral')
plt.title('Types of Top 10 TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot the languages of the top 10 TV shows
language_counts = top_10_languages.value_counts()
plt.figure(figsize=(10, 6))
language_counts.plot(kind='bar', color='lightblue')
plt.title('Languages of Top 10 TV Shows')
plt.xlabel('Language')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot the networks of the top 10 TV shows
network_counts = top_10_networks.value_counts()
plt.figure(figsize=(10, 6))
network_counts.plot(kind='bar', color='lightpink')
plt.title('Networks of Top 10 TV Shows')
plt.xlabel('Network')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()