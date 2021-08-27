from django.core.management.base import BaseCommand
from posters.models import Posters
import requests
from time import sleep
from django.core.files import File


import tempfile
from django.core import files



url = 'https://api.showdiver.com/events/?page=1&page_size=58&search=&period_start=&period_end='
url_ticket = 'https://api.showdiver.com/events/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}  

class Command(BaseCommand):
    help = 'Parsing from showdiver.com'


    def handle(self, *args, **options):
        r = requests.get(url, headers=HEADERS, timeout=50)
        data = r.json()
        #count = data['count']
        for item in data['results']:
            response_event = requests.get(f"{url_ticket}{item['uuid']}")
            sleep(0.15)
            poster_data = response_event.json()
            poster = Posters(
                title=poster_data['title'], 
                description=poster_data['description'],
                start_at=poster_data['start_at'],
                finish_at=poster_data['finish_at'],
                title_address=poster_data['venue']['title'],
                address = poster_data['venue']['address'],
                for price in poster_data['price_categories'][]
                )
            poster_url = poster_data['poster']
            response = requests.get(poster_url, stream=True)
            file_name = poster_url.split('/')[-1]
            lf = tempfile.NamedTemporaryFile()
            for block in response.iter_content(1024 * 8):
                if not block:
                    break
                lf.write(block)
			            
            poster.image.save(file_name, files.File(lf))
            poster.save()
        self.stdout.write(self.style.SUCCESS('Added all posters!'))