from django.core.management.base import BaseCommand
import json
from main.models import City

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def handle(self, *args, **kwargs):
        json_file = 'main/static/tn.json'
        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data:
                instance = City(
                    gov=item['city'],
                    state=item['state'],
                )
                instance.save()