# Analyzing Hip Hop Music using What.CD data

This all started because I went really deep into the [Hypnotize Minds](https://en.wikipedia.org/wiki/Hypnotize_Minds) catalog, and I noticed that Memphis seemed to turn out a whole lot of hip hop music given its small size (small compared to NYC, LA, etc). I'm convinced DJ Paul is one of the hardest working artists out there. 

Anyway, I basically wanted some analysis of the amount of hip hop music produced in each city, relative to the city population. So I used the [What.CD API](https://github.com/WhatCD/Gazelle/wiki/JSON-API-Documentation) to obtain information on all torrents tagged "hip.hop" (75,719 releases as of October 22 2016), and I compared those data to the [2010 Census](https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population).

Anyway, these data are (i think) really interesting, so this repository will contain a bunch of analyses conducted to satisfy my curiosities. 

- [ [Link](http://nbviewer.jupyter.org/github/nolanbconaway/hip.hop.data/blob/master/hiphop-per-person.ipynb) ] **Which city makes the most hip hop, relative to its population?** 
- [ [Link](http://nbviewer.jupyter.org/github/nolanbconaway/hip.hop.data/blob/master/coastal-timeline.ipynb) ] **Which coast (East, West, Third?) makes the most hip hop? What does the time-line look like?** 
- [ [Link](http://nbviewer.jupyter.org/github/nolanbconaway/hip.hop.data/blob/master/mixtape-versus-album.ipynb) ] **When did mixtapes become so popular?** 
- [ [Link](most-prolific-artists.ipynb) ] **Who is the most prolific artist in hip hop?** 


Some things to update:

- **Linear regression**. Instead of simple ratios, show bar plot of each city's residual from the linear regression.
- **Plotly fixes**: get rid of the hover toolbar. get rid of grid subplot printout.
