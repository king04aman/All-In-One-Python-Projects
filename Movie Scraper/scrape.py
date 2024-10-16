from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def requestUrl_and_bs4(url:str):
    # All request and parser goes through here
    agents = UserAgent().random
    user_agent={"User-Agent": agents}

    # Fixed the requests (changed status code from 403 to 200) 
    html = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(html.text, 'html.parser')

    return soup


def getMovieDetails(movieName:str):
    url = 'https://www.imdb.com'
    query = '/search/title?title='
    movieDetails = {}
    movienamequery = query+'+'.join(movieName.strip().split(' '))
    website_url = url+movienamequery+'&title_type=feature'

    bs = requestUrl_and_bs4(website_url)

    result = bs.find('a', {'class': 'ipc-title-link-wrapper'})
    if result is None:
        return None

    movielink = url+result.attrs['href']

    bs = requestUrl_and_bs4(movielink)

    # Fix the movie name
    movieDetails['name'] = bs.find('h1', {'data-testid': 'hero__pageTitle'}).text

    # Fix year, runtime
    box_one = bs.find('div', {'class': 'sc-b7c53eda-0 dUpRPQ'}).ul
    box = box_one.find_all('li')
    try:
        movieDetails['year'] = box[0].text
    except AttributeError:
        movieDetails['year'] = 'Not available'

    # Fix genres
    box_two = bs.find('div', {'data-testid': "genres"})
    movieDetails['genres'] = [
       i.text for i in box_two.select('div.ipc-chip-list__scroller>a>span')]
    
    # Fix ratings
    try:
        movieDetails['rating'] = f"{bs.find(
            'div', {'data-testid': 'hero-rating-bar__aggregate-rating__score'}).span.text}/10 ({bs.find('div', {'class': 'sc-bde20123-3 gPVQxL'}).text})"
        movieDetails['runtime'] = box[2].text.strip()
    except AttributeError:
        movieDetails['rating'] = 'Not yet rated'
        movieDetails['runtime'] = 'Not available'

    # To get movie release date
    movie_release_dates_url= f"{url}{box[0].a.attrs['href']}" 
    soup = requestUrl_and_bs4(movie_release_dates_url)

    movieDetails['release_date'] = soup.select_one('#rel_1 > div > ul > li > span.ipc-metadata-list-item__list-content-item').text

    creditSummary = bs.select('div.ipc-metadata-list-item__content-container > ul')

    movieDetails['directors'] = [i.text for i in creditSummary[0].select('li>a')]
    
    try:
        movieDetails['cast'] = [i.text for i in creditSummary[2].select('li>a')]
        movieDetails['writers'] = [i.text for i in creditSummary[1].select('li>a')]

    except IndexError:
        movieDetails['cast']=movieDetails['writers']
        movieDetails['writers']='Not found'

    movieDetails['plot'] = bs.find('span', {'data-testid': 'plot-l'}).text.strip()
   
    return movieDetails

def main():
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

if __name__ == "__main__":
    main()
