from django.core.mail import EmailMultiAlternatives
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site


class Command(BaseCommand):
    help = 'Send emails'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        print('Preparing')

        # (subject, message, from_email, recipient_list)
        for user in users:
            """
            Takes each user one by one and sending an email to each
            """

            reset_url = f"https://{get_current_site(request=None).domain}/password-reset/"  # current domain
            site_url = f"https://{get_current_site(request=None).domain}"  # current domain

            user_email = user.email  # user email
            frm = "bhp.se.dmc@gmail.com"  # from email
            subject = 'Time Sheet Activation Link'  # subject of the email
            message = f"""\
                Hi {user.first_name} {user.last_name},
                <br>
                <br>
                Your account for the BHP Timesheet System has been set up. The url to access the system is <a href="{site_url}" target="_blank">{site_url}</a>.
                 <br>
                 To activate your account, set the password first using the link below. 
                <br>
                <br>
                <a href="{reset_url}" target="_blank">Reset Password</a>
                <br>
                <br>     
                Good Day 😃
                """

            msg = EmailMultiAlternatives(subject, message, frm, (user_email,))
            msg.content_subtype = 'html'
            print("Sending to : ", user.email)
            msg.send()
        print("Done!!!!")
