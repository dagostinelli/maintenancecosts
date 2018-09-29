import jinja2
import os
import pathlib
from bs4 import BeautifulSoup
from markdown import markdown
from shutil import copyfile

whereami = os.path.dirname(os.path.realpath(__file__))
templates_location = whereami + '/templates'
input_location = whereami + '/../book'
output_location = whereami + '/../docs/book'
output_location_root = whereami + '/../docs'

chapters = [
	'toc.md',
	'introduction.md',
	'audience.md',
	'curate-your-code.md'
]

def build_chapters():
	for p in chapters:
		md = read_file_into_string(os.path.join(input_location, p))
		html = markdown_to_html(md)
		render_page_to_destination('chapter.html', os.path.join(output_location, change_file_extension(p, '.html')), content=html)

def markdown_to_html(md):
	html = markdown(md)
	soup = BeautifulSoup(html, 'html.parser')
	text = soup.prettify()
	return text

def read_file_into_string(f):
	with open(f, 'r') as myfile:
		return myfile.read()

def change_file_extension(p, ext):
	basefilename = os.path.splitext(os.path.basename(p))[0]
	filename = basefilename + ext
	return filename

def render_page_to_destination(template, destination, **data):
	html = render_page(template, **data)
	with open(destination, "w+") as f:
		f.write(html)

def render_page(template, **data):
	environment = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_location))
	return environment.get_template(template).render(data)

def main():
	pathlib.Path(output_location).mkdir(parents=True, exist_ok=True)

	render_page_to_destination('index.html', os.path.join(output_location_root, 'index.html'))
	build_chapters()	

if __name__ == "__main__":
	main()
