import json

# ~ import pygal
import pygal_maps_world.maps as pwm
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code

#load data to list
filename = 'data/population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
	
#create a dict including world population
	cc_populations = {}
	for pop_dict in pop_data:
		if pop_dict['Year'] == 2010:
			country = pop_dict['Country Name']
			population = int(float(pop_dict['Value']))
			print(country + ":" + str(population))
			code = get_country_code(country)
			if code:
				cc_populations[code] = population
				print(code + ":" + str(population))
			else:
				print("ERROR -" + country)
				cc_populations[code] = population
	
	#divide countries into 3 group according to their population
	cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
	for cc, pop in cc_populations.items():
		if pop < 1000000:
			cc_pops_1[cc] = pop
		elif pop < 1000000000:
			cc_pops_2[cc] = pop
		else:
			cc_pops_3[cc] = pop
			
	#how many countries in every group
	print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3)) 
	
# ~ wm = pwm.World()
wm_style = RS('#336699',base_style=LCS)
wm = pwm.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
# ~ wm.add('2010',cc_populations)
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_population.svg')
