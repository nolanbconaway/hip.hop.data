# Analyzing Hip Hop Music using What.CD data

Need to decide on a report format! Options:

- **Jupyter**. Pros: great integration with Github. Cons: plotting is terrible.
- **Shiny R**. Pros: great, interactive plotting. Cons: no Github integration, Shiny R servers are super slow, wacky programming paradigm.
- **Rmarkdown**. Pros: OK Github integration (saves an HTML file), great plotting. Cons: unclear if these are easy to make in sublime.

##`data.db` contains:

1. Data from 2000 pages of torrents tagged "hip.hop" on What.CD (almost 100,000 releases). I scraped the information on the evening of September 8 2016. The resulting tables in the database (`torrents`, `tags`) contain the artist, album, release type, year, tags, and # snatches of each release.
2. 2010 census data for the [largest US cities](https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population) from wikipedia. The table `cities` contains the city, state, and 2010 population of the top 304.


