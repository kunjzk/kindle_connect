from notion.client import NotionClient


parser = argparse.ArgumentParser(description="clear the page")
parser.add_argument('token_v2', type=str, help="(str) V2 token. Open notion.so and login. Developer tools -> Application -> cookies -> token_v2")
parser.add_argument('page_url', type=str, help="(str) URL of page for book")

args = parser.parse_args()
token_v2_in = args.token_v2
page_url = args.page_url

#access private account using the token_v2 value
client = NotionClient(token_v2=token_v2_in)

#access the page you want
page = client.get_block(page_url)
	
for child in page.children:
	child.remove(True)
