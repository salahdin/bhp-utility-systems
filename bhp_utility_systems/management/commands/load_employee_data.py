from dateutil import parser

from django.core.management.base import BaseCommand

from bhp_personnel.models import Employee, Supervisor, Department


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Data fine path, csv file')

    def handle(self, *args, **kwargs):
        already_exists = 0
        created = 0
        file_path = kwargs['file_path']
        data = self.data(file_path=file_path)
        count = 0
        phone_count = 10
        phone_count1 = 10
        for data_item in data:

            options = {}
            for field_name in self.all_model_fields:
                if field_name == 'supervisor':
                    s_details = data_item.get(field_name).split("|")
                    if len(s_details) == 1:
                        s_details = data_item.get(field_name).split(" ")
                    if len(s_details) == 4:
                        supervisor, created = Supervisor.objects.get_or_create(
                            first_name=s_details[0],
                            last_name=s_details[1],
                            cell=s_details[2],
                            email=s_details[3])
                    else:
                        try:
                            supervisor = Supervisor.objects.get(
                                first_name=s_details[0],
                                last_name=s_details[1])
                        except Supervisor.DoesNotExist:
                            cell = '712111'+ str(phone_count)
                            self.stdout.write(
                                self.style.WARNING(f'Cell {cell}'))
                            supervisor, created = Supervisor.objects.get_or_create(
                                first_name=s_details[0],
                                last_name=s_details[1],
                                cell=cell,
                                email=(s_details[0][0]+s_details[1]+'@bhp.org.bw').lower())
                            phone_count += 1
                    options[field_name] = supervisor

                elif field_name == 'department':
                    d_details = data_item.get(field_name).split("|")
                    if len(d_details) > 1:
                        dept, created = Department.objects.get_or_create(
                            hod=d_details[0],
                            dept_name=d_details[1])
                    else:
                        dept, created = Department.objects.get_or_create(
                            hod=d_details[0],
                            dept_name='Admin')
                    options[field_name] = dept
                else:
                    options[field_name] = data_item.get(field_name)
            
            # Convert date to date objects
            try:
                hired_date = parser.parse(options.get('hired_date')).date()
            except parser.ParserError:
                options.update(hired_date=None)
            else:
                options.update(hired_date=hired_date)

            try:
                Employee.objects.get(
                    employee_code=int(data_item.get('employee_code')))
            except Employee.DoesNotExist:
                if options.get('cell') == '':
                    options['cell'] = '712111'+ str(phone_count1)
                    phone_count1 += 1
                Employee.objects.create(**options)
                created += 1
            else:
                already_exists += 1
            count += 1
            self.stdout.write(
                self.style.SUCCESS(f'Count {count}'))
        self.stdout.write(
            self.style.SUCCESS(f'A total of {created} have been created'))
        self.stdout.write(
            self.style.WARNING(f'Total items {already_exists} already exist'))

    def data(self, file_path=None):
        data = []
        f = open(file_path, 'r')
        lines = f.readlines()
        header = lines[0]
        lines.pop(0)
        header = header.strip()
        header = header.split(',')
        self.stdout.write(self.style.WARNING(f'Total items {len(lines)}'))
        for line in lines:
            line = line.strip()
            line = line.split(',')
            data_item = dict(zip(header, line))
            data.append(data_item)
        return data

    @property
    def all_model_fields(self):
        """Returns a list of employee model fields.
        """
        exclude_fields = [
            'created',
            'modified',
            'user_created',
            'user_modified',
            'hostname_created',
            'hostname_modified',
            'revision',
            'device_created',
            'device_modified',
            'id',
            'site',
            'slug',
            'studies',
            'subject_identifier', ]
        fields = []
        for field in Employee._meta.get_fields():
            if field.name not in exclude_fields:
                fields.append(field.name)
        return fields
