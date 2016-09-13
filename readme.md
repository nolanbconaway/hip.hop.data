# Analyzing Hip Hop Music using What.CD data

I got really into Memphis hip hop last week, and I had the hunch that Memphis made a lot of hip hop for its small size (small compared to LA, NYC etc). So I got info on 100k torrents from What.CD, and I compared the number of torrents tagged from each city to the 2010 census population. You can check out the Juypter notebook [here](http://nbviewer.jupyter.org/github/nolanbconaway/hip.hop.data/blob/master/analyses.ipynb). 

My hunch was close: looks like New Orleans makes the most hip hop per person, but Memphis and Atlanta are not far behind. Anyway, this data is really interesting, so here are some ideas for follow-ups.

- **frequency-by-year lines**: show top N city frequency as a function of year. possible to connect this with more population estimates.
- **Fixes for bay.area**. People use "bay.area" more than the city names in the bay area. Combine san.jose, san.francisco, oakland tags and populations into "bay.area". Keep the independent cities. 
- **Fixes for LA**. When people tag LA, they could mean any number of cities around LA proper. Combine pasadena, long.beach, costa.mesa, anaheim, riverside, torrance, inglewood into "los.angeles" population. Add los.angeles tag to any torrent tagged with those cities (if it is not already).
- **Linear regression**. Instead of simple ratios, show bar plot of each city's residual from the linear regression. Will want to aggregate some cities to higher pop first because new york is a crazy outlier.
- **plotly fixes**: get rid of the hover toolbar. get rid of grid subplot printout.