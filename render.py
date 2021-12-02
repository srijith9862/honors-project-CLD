import pickle
import ast
from jinja2 import Environment, FileSystemLoader

from genXML import tewiki, writePage


def getData(row,i):
	data = {
		'Index':row.Index.values[0],
		'Latin_name':row.Latin_name.values[0],
		'Famil':row.Famil.values[0],
		'Common_name':row.Common_name.values[0],
		'Habit':(row.Habit.values[0]),
		'Deciduous/Evergreen':row.Deciduous/Evergreen.values[0],
		'Height':row.Height.values[0],
		'Width':row.Width.values[0],
		'UK_Hardiness':row.UK_Hardiness.values[0],
		'Medicinal':row.Medicinal.values[0],
		'Range':row.Range.values[0],
		'Habitat':row.Habitat.values[0],
		'Soil':row.Soil.values[0],
		'Shade':(row.Shade.values[0]),
		'Moisture':row.Moisture.values[0],
		'Well_drained':row.Well_drained.values[0],
		'Nitrogen_fixer':row.Nitrogen_fixer.values[0],
		'pH':row.pH.values[0],
		'Acid':row.Acid.values[0],
		'Alkaline':row.Alkaline.values[0],
		'Saline': row.Saline.values[0],
		'Wind':row.Wind.values[0],
		'Growth_rate':row.Growth_rate.values[0],
		'Pollution':row.Pollution.values[0],
		'Poor_soil':row.Poor_soil.values[0],
		'Drought':row.Drought.values[0],
		'Wildlife': row.Wildlife.values[0],
		'Pollinators': row.Pollinators.values[0],
		'Self_fertile': row.Self_fertile.values[0],
		'Known_hazards':row.Known_hazards.values[0],
		'Cultivation_Details':row.Cultivation_Details.values[0],
		'Edible_uses':row.Edible_uses.values[0],
		'Uses_notes':row.Uses_notes.values[0],
		'Heavy_clay':row.Heavy_clay.values[0],
		'Propagation':row.Propagation.values[0],
		'Edibility_Rating':row.Edibility_Rating.values[0],
		'Frost_Tender':row.Frost_Tender.values[0],
		'Scented':row.Scented.values[0],
		'Medicinal_Rating':row.Medicinal_Rating.values[0]
	}



def main():
	# Load the template
	file_loader = FileSystemLoader('./Templates')
	env = Environment(loader=file_loader)
	template = env.get_template('main_template.j2')

	# Load the data (.pkl)
	plantsDF =pickle.load(open('./123.pkl', 'rb'))
	


	#remove this to generate articles for all movies
	ids = plantsDF.Index.tolist()

	# Initiate the file object
	fobj = open('movies.xml', 'w')
	fobj.write(tewiki+'\n')

	# Give the page_id from which you want to generate the articles in
	initial_page_id = 500000

	# Loop to grab all data from the .pkl and generate articles using the template
	for i, plantId in enumerate(ids):
		row = plantsDF.loc[plantsDF['Index']==plantId]
		title = row.page_heading.values[0]
		text = template.render(getData(row,i))

		writePage(initial_page_id,title,text,fobj)
		initial_page_id += 1
		print(text, '\n')

	fobj.write('</mediawiki>')
	fobj.close()

if __name__ == '__main__':
	main()