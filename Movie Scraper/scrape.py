from bs4 import BeautifulSoup
import requests


def getMovieDetails(movieName):
    url = 'https://www.imdb.com'
    query = '/search/title?title='
    movieDetails = {}
    movienamequery = query+'+'.join(movieName.strip().split(' '))

    html = requests.get(url+movienamequery+'&title_type=feature')
    bs = BeautifulSoup(html.text, 'html.parser')
    result = bs.find('h3', {'class': 'lister-item-header'})

    if result is None:
        return None

    movielink = url+result.a.attrs['href']
    movieDetails['name'] = result.a.text

    html = requests.get(movielink)
    bs = BeautifulSoup(html.text, 'html.parser')
    try:
        movieDetails['year'] = bs.find('span', {'id': 'titleYear'}).a.text
    except AttributeError:
        movieDetails['year'] = 'Not available'
    subtext = bs.find('div', {'class': 'subtext'})

    movieDetails['genres'] = [
        i.text for i in subtext.findAll('a', {'title': None})]
    try:
        movieDetails['rating'] = bs.find(
            'div', {'class': 'ratingValue'}).span.text
        movieDetails['runtime'] = subtext.time.text.strip()
    except AttributeError:
        movieDetails['rating'] = 'Not yet rated'
        movieDetails['runtime'] = 'Not available'
    movieDetails['release_date'] = subtext.find(
        'a', {'title': 'See more release dates'}).text.strip()

    creditSummary = bs.findAll('div', {'class': 'credit_summary_item'})

    movieDetails['directors'] = [i.text for i in creditSummary[0].findAll('a')]
    movieDetails['writers'] = [i.text for i in creditSummary[1].findAll(
        'a') if 'name' in i.attrs['href']]
    try:
        movieDetails['cast'] = [i.text for i in creditSummary[2].findAll(
            'a') if 'name' in i.attrs['href']]

    except IndexError:
        movieDetails['cast']=movieDetails['writers']
        movieDetails['writers']='Not found'
    html = requests.get(movielink+'plotsummary')
    bs = BeautifulSoup(html.text, 'html.parser')

    movieDetails['plot'] = bs.find(
        'li', {'class': 'ipl-zebra-list__item'}).p.text.strip()

    return movieDetails


if __name__ == "__main__":
    movieName = input('Enter the movie name : \n')
    movieDetails = getMovieDetails(movieName)
    if movieDetails is None:
        print('No movie found with given name!!!!!')
        quit()
    print('\n{movie} ({year})'.format(
        movie=movieDetails['name'], year=movieDetails['year']))
    print('Rating:', movieDetails['rating'])
    print('Runtime:', movieDetails['runtime'])
    print('Release Date:', movieDetails['release_date'])
    print('Genres:', ', '.join(movieDetails['genres']))
    print('Director:', ', '.join(movieDetails['directors']))
    print('Writer:', ', '.join(movieDetails['writers']))
    print('Cast:', ', '.join(movieDetails['cast']))
    print('Plot Summary:\n', movieDetails['plot'])
