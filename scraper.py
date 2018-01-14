from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#we will be scraping for mixed drink recipes
my_url = 'https://www.liquor.com/recipes/page/1'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#turn recipe 
page_soup = soup(page_html, "html.parser")

for h3 in page_soup.find_all('h3'):
	#Follows the link to the recipe
	recipe_url = uReq(h3.a.get('href'))
	recipe_html = recipe_url.read()
	recipe_url.close()
	#turn recipe page into soup
	recipe_soup = soup(recipe_html, "html.parser")

	print("\n")

	amounts = recipe_soup.find("div", class_ = "ml-value")
	ingredients = recipe_soup.find("div", class_ = "col-xs-8 x-recipe-ingredient")

	#name of the drink
	print(h3.get_text())
	print("INGREDIENTS:")
	print("RECIPE:")
	recipe = recipe_soup.find("div", class_ = "row x-recipe-prep")
	steps = recipe.find_all('p')
	for text in steps:
		print(text.get_text())

