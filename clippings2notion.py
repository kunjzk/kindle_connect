from notion.client import NotionClient
from notion.block import *
import re
import argparse

def setup(token_v2_in, page_url):
	#access private account using the token_v2 value
	client = NotionClient(token_v2=token_v2_in)

	#access the page you want
	page = client.get_block(page_url)

	print("The title is:", page.title)
	
	if len(page.children) is 0 or page.children[0]._type is not "header": page.children.add_new(HeaderBlock, title="Kindle Highlights")


def get_quotes(filename):
	with open(filename, "r") as f:
		all_content = f.read()
		all_content = all_content.replace(u'\xa0', u' ')
		raw_clippings = re.split('\n\n\.\. [a-zA-Z0-9]{8} ; Your ;  ;.{20}\n\n', all_content)
		del raw_clippings[0]
		return raw_clippings		

def write_quotes(token_v2_in, page_url, quotes):	
	#access private account using the token_v2 value
	client = NotionClient(token_v2=token_v2_in)

	#access the page you want
	page = client.get_block(page_url)
	
	for quote in quotes:
		page.children.add_new(TextBlock, title=quote)
		page.children.add_new(DividerBlock)
	
def main():

	parser = argparse.ArgumentParser(description="clippings to notion")
	parser.add_argument('token_v2', type=str, help="(str) V2 token. Open notion.so and login. Developer tools -> Application -> cookies -> token_v2")
	parser.add_argument('page_url', type=str, help="(str) URL of page for book")
	parser.add_argument('rst_file_path', type=str, help="(str) path to RST file")
	
	args = parser.parse_args()
	token_v2_in = args.token_v2
	page_url = args.page_url
	rst_path = args.rst_file_path

	setup(token_v2_in,page_url)
	quotes = get_quotes(rst_path)
	write_quotes(token_v2_in, page_url, quotes)	


if __name__ == "__main__":
	main()

