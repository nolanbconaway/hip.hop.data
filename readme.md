# Analyzing Hip Hop Music using What.CD data

##`data.db` contains:

1. Data from 2000 pages of torrents tagged "hip.hop" on What.CD (almost 100,000 releases). I scraped the information on the evening of September 8 2016. The resulting tables in the database (`torrents`, `tags`) contain the artist, album, release type, year, tags, and # snatches of each release.
2. 2010 census data for the [largest US cities](https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population) from wikipedia. The table `cities` contains the city, state, and 2010 population of the top 304.


##To-do:

- **Ratio bar plot**: show the tag frequency / city population ratio for the top N cities.
- **Ratio-by-year scatter**: show city popularity as a function of year.
- **Possible missed location-based tags**. This is a data cleaning problem. For example, "bay.area" is a very popular tag, but is not in the list of cities.
- **Decade-tags vs release years**. I noticed that "2010s" is the most popular tag, and "1980s" is also one of the most popular tags. How do these tags relate to the actual number of releases in each year?
- **plotly fixes**: get rid of the hover toolbar.