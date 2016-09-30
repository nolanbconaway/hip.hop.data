# ---- WHAT IS THIS SCRIPT?
# (1) The biggest US cities (NYC, LA, SF) are in the census actually recorded  
# 	under many sub-cities (e.g., SF and Oakland are separated), but people tag 
# 	cities using the greater urban area.
# (2) Specific to SF, people more commonly use the 'bay.area' tag, which is not 
# 	in the census records.
# 
# This script solves these two problems by aggregating populations / torrents for 
# each of the major cities.
# -----

import sqlite3
import pandas as pd

def uniqify(seq, idfun=None): 
    """return unique items in a list. Thanks to:
    https://www.peterbe.com/plog/uniqifiers-benchmark """
    if idfun is None:
        def idfun(x): return x
    seen, result = {}, []
    for item in seq:
        marker = idfun(item)
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result


con = sqlite3.Connection('data.db')
tags = pd.read_sql_query('SELECT * from tags;', con)
cities = pd.read_sql_query('SELECT * from cities;', con)

# define subareas in large cities
big_cities = dict()
big_cities['bay.area'] = ['antioch', 'berkeley', 'concord', 'daly.city', 'fairfield', 'fremont', 'oakland', 'san.francisco', 'san.jose', 'san.mateo', 'santa.clara', 'santa.rosa', 'sunnyvale', 'vallejo']
big_cities['new.york'] = ['bronx', 'brooklyn', 'manhattan', 'newark', 'new.york', 'queens', 'staten.island']
big_cities['los.angeles'] = ['burbank', 'compton', 'downey', 'el.monte', 'glendale', 'inglewood', 'lancaster', 'long.beach', 'los.angeles', 'norwalk', 'palmdale', 'pasadena', 'pomona', 'santa.clarita', 'torrance', 'west.covina']

# define states for the big cities
states = {	'bay.area': 	'california',
			'new.york': 	'new.york',
			'los.angeles': 	'california'}

# make combined cities entries
print ('Computing city populations...')
for k in big_cities.keys():

	# compute population
	citypop = 0
	for v in big_cities[k]:
		if not any(cities.city==v): continue
		citypop += list(cities.population[cities.city==v])[0]

	print '\t' + k + ': ' + str(citypop)

	# add data to table
	if k in list(cities.city):
		cities.loc[cities.city==k, 'population'] = citypop
	else:
		cities = cities.append(dict(
			city = k, state = states[k],population = citypop
			), ignore_index=True)

# make combined torrents tags entries
print ('\nFinding torrents that need to be tagged...')
for k in big_cities.keys():

	# get list of torrent IDs associated with the area
	ids = list(tags.id[tags.tag.str.contains(k)])
	for v in big_cities[k]:
		ids += tags.id[tags.tag.str.contains(v)].tolist()
	ids = uniqify(ids)
	
	# add area tag if not already present
	for i in ids:
		if any(tags.tag[tags.id==i].str.contains(k)): continue
		tags = tags.append( dict(id = i, tag = k), ignore_index=True)

# insert new rows into sqlite
print ('\nWriting data to sqlite...')
tags.to_sql('tags', con, if_exists = 'replace', 
	dtype = dict(id = 'INTEGER', tag = 'TEXT'))
cities.to_sql('cities', con, if_exists = 'replace',
	dtype = dict(city = 'TEXT', state = 'TEXT', population = 'INTEGER'))
con.close()



