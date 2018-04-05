from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#we will be scraping for mixed drink recipes
my_url = 'https://www.liquor.com/recipes/page/1'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#turn recipe into soup
page_soup = soup(page_html, "html.parser")

for h3 in page_soup.find_all('h3'):
	#Follows the link to the recipe
	recipe_url = uReq(h3.a.get('href'))
	recipe_html = recipe_url.read()
	recipe_url.close()
	#turn recipe page into soup
	recipe_soup = soup(recipe_html, "html.parser")

	print("\n")

	#name of the drink
	print(h3.get_text())

	# ingreditents and amounts
	print("INGREDIENTS:")
	shopping_list = recipe_soup.find_all("div", class_ = "row x-recipe-unit")
	for line in shopping_list:
		ingredient = line.find("div", class_ = "col-xs-8 x-recipe-ingredient").get_text().strip()
		amount = line.find("div", class_ = "ml-value").get_text().strip()
		print('{:12}'.format(amount) + "	" + ingredient)

	#recipe
	print("RECIPE:")
	recipe = recipe_soup.find("div", class_ = "row x-recipe-prep")
	steps = recipe.find_all('p')
	for text in steps:
		print(text.get_text())

