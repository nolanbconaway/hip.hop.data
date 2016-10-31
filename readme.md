# Analyzing Hip Hop Music using What.CD data

I recently started digging through mid-90's Memphis hip hop (there's a lot of really good stuff there, if you didn't know), and I had the hunch that Memphis made a lot of hip hop for its small size (small compared to LA, NYC etc). So I used the [What.CD API](https://github.com/WhatCD/Gazelle/wiki/JSON-API-Documentation) to obtain information on all torrents tagged "hip.hop" (75,719 releases as of October 22 2016). Users of What.CD are pretty systematic about tagging, and releases are commonly (but not always) tagged with the city they are most associated. So I can test my hunch by comparing these data to the [2010 Census](https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population).

Anyway, these data are (i think) really interesting, so this repository will contain a bunch of analyses conducted to satisfy my curiosities. 

- [ [Link](http://nbviewer.jupyter.org/github/nolanbconaway/hip.hop.data/blob/master/hiphop-per-person.ipynb) ] **Which city makes the most hip hop, relative to its population?** 
- [ [Link](http://nbviewer.jupyter.org/github/nolanbconaway/hip.hop.data/blob/master/coastal-timeline.ipynb) ] **Which coast (East, West, Third?) makes the most hip hop? What does the time-line look like?** 
- - [ [Link](http://nbviewer.jupyter.org/github/nolanbconaway/hip.hop.data/blob/master/mixtape-versus-album.ipynb) ] **When did mixtapes become so popular?** 

Some things to update:

- **Linear regression**. Instead of simple ratios, show bar plot of each city's residual from the linear regression.
- **Plotly fixes**: get rid of the hover toolbar. get rid of grid subplot printout.