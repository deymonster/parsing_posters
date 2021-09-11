from django.core.management.base import BaseCommand
from posters.models import *
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
        
        for item in data['results']:
            response_event = requests.get(f"{url_ticket}{item['uuid']}")
            sleep(0.15)
            event_data = response_event.json()
            event = Event(
                title=event_data['title'], 
                description=event_data['description'])
            event_url = event_data['poster']
            response = requests.get(event_url, stream=True)
            file_name = event_url.split('/')[-1]
            lf = tempfile.NamedTemporaryFile()
            for block in response.iter_content(1024 * 8):
                if not block:
                    break
                lf.write(block)
			
            event.image.save(file_name, files.File(lf))
            event.save()

            session = Session(
                start_at=event_data['start_at'],
                finish_at=event_data['finish_at'],
                title_address=event_data['venue']['title'],
                address = event_data['venue']['address']

            )  
            session.save()  


            for price in event_data['price_categories']:
                ticket = Ticket(
                    title=price['title'],
                    price=price['price'],
                    event=event,
                    session=session

                )

            scheme_url = event_data['scheme']
            if scheme_url:
                response = requests.get(scheme_url, stream=True)
                file_name = scheme_url.split('/')[-1]
                lf = tempfile.NamedTemporaryFile()
                for block in response.iter_content(1024 * 8):
                    if not block:
                        break
                    lf.write(block)
                ticket.scheme.save(file_name, files.File(lf))
            else:
                continue
            ticket.save()
        
        self.stdout.write(self.style.SUCCESS('Added all posters!'))