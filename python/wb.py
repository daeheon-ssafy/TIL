import webbrowser

heros = ['iron man','batman','wonder woman']

url='https://www.google.com/search?q='

for hero in heros:
    webbrowser.open(f'{url}{hero}')