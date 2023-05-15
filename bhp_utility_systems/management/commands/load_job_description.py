import json
from django.core.management.base import BaseCommand
from bhp_personnel.models import JobDescription
from bhp_personnel.models import Department


class Command(BaseCommand):
    help = 'Load JobDescription data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        job_descriptions_data = self.load_data_from_json(json_file)
        self.process_data(job_descriptions_data)

    def load_data_from_json(self, json_file):
        with open(json_file, 'r') as file:
            return json.load(file)

    def process_data(self, job_descriptions_data):
        count = 0
        for data in job_descriptions_data:
            job_description_fields = data['fields']
            job_description_fields['id'] = data['pk']
            job_description_fields.pop('site', None)

            if job_description_fields['department']:
                hod = job_description_fields['department'][0]
                dept_name = job_description_fields['department'][1]
                try:
                    department = Department.objects.get(dept_name=dept_name, hod=hod)
                    job_description_fields['department'] = department
                except Department.DoesNotExist:
                    self.stderr.write(self.style.WARNING(
                        'Department with these details {} not found. Skipping row {}.'.format(job_description_fields["department"], job_description_fields["id"])))
                    continue

            try:
                job_description = JobDescription.objects.get(id=job_description_fields['id'])
            except JobDescription.DoesNotExist:
                job_description = JobDescription.objects.create(**job_description_fields)
                count += 1
            else:
                self.stderr.write(self.style.WARNING("JobDescription with id {} already exists. Skipping row.".format(job_description_fields["id"])))
                continue

        self.stdout.write(
            self.style.SUCCESS('Successfully loaded {} JobDescription records'.format(count)))
