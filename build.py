import jinja2
import os
from bs4 import BeautifulSoup
from markdown import markdown

whereami = os.path.dirname(os.path.realpath(__file__))
templates = whereami + '/template'
book_location = whereami + '/book'
web_location = whereami + '/html'

chapters = [
	'introduction.md'
]

def build_chapters():
	for p in chapters:
		fq = os.path.join(book_location, p)
		basefilename = os.path.splitext(os.path.basename(p))[0]
		filename = basefilename + '.html'
		filename = os.path.join(web_location, filename)
		with open(fq, 'r') as myfile:
    			md=myfile.read()
		html = markdown(md)
		soup = BeautifulSoup(html, 'html.parser')
		text = soup.prettify()
		html = render_page('chapter.html', content=text)
		with open(filename,"w+") as f:
			f.write(html)

def render_page(file_name, **data):
	environment = jinja2.Environment(loader=jinja2.FileSystemLoader(templates))
	return environment.get_template(file_name).render(data)

if not os.path.exists(web_location):
	os.mkdir(web_location)

build_chapters()