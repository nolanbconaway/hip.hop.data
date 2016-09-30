# Analyzing Hip Hop Music using What.CD data

I got really into Memphis hip hop last week, and I had the hunch that Memphis made a lot of hip hop for its small size (small compared to LA, NYC etc). So I got info on 100k torrents from What.CD, and I compared the number of torrents tagged from each city to the 2010 census population. You can check out the Juypter notebook [here](http://nbviewer.jupyter.org/github/nolanbconaway/hip.hop.data/blob/master/analyses.ipynb). 

My hunch was close: looks like New Orleans makes the most hip hop per person, but Memphis and Atlanta are not far behind. Anyway, this data is really interesting, so here are some ideas for follow-ups.

- **Frequency-by-year lines**: show top N city frequency as a function of year. possible to connect this with more population estimates.
- **Linear regression**. Instead of simple ratios, show bar plot of each city's residual from the linear regression.
- **Plotly fixes**: get rid of the hover toolbar. get rid of grid subplot printout.
- **Artist share**: pie charts of the top artists in the big cities.
- **Tag frequency on a map**. Put the frequency of tags (or population ratio) on a US map.