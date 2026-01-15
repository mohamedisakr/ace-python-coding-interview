from re import findall
page = """
<a href="https://subscription.manning.com" target="_blank" class="nav-manning-online-button clickable"></a>
<a href="/" id="home-link" class="nav-home-button"></a>
<a href="/catalog/programming-languages-and-styles/python"><span>Python</span></a>
"""
# method 1: do it yourself
keyword = 'href="'
n = len(keyword)
start_quote = page.find(keyword) + n
# Find the first quote AFTER the start_quote
end_quote = page.find('"', start_quote)

url = page[start_quote:end_quote]
print(url)

# # Method 2: Using Regular Expressions (Regex)
# # Matches everything inside the href="..." quotes
links = findall(r'href=["\'](.*?)["\']', page)
print("-" * 50)
print(*links, sep='\n')
# print('\n'.join(links))
