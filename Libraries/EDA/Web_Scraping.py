def get_page_contents(url):
    """
    Gets page content and returns a BeautifulSoup object with html parsing
    """
    page = requests.get(url, headers={'Accept-Language': 'en-US'})
    return BeautifulSoup(page-text, 'html.parser')

def show_html(html_str):
    """
    Displays html for proper reading
    """
    print(BeautifulSoup(str(html_str), 'html.parser').prettify())
