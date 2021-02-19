from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar

bhp_utility_systems = Navbar(name='bhp_utility_systems')

bhp_utility_systems.append_item(
    NavbarItem(
        name='procurement',
        label='Procurement',
        fa_icon='fa fa-list-alt',
        url_name=settings.DASHBOARD_URL_NAMES.get('procurement_url')))

bhp_utility_systems.append_item(
    NavbarItem(
        name='document',
        label='documents',
        fa_icon='fas fa-file',
        url_name=settings.DASHBOARD_URL_NAMES.get('document_url')))

bhp_utility_systems.append_item(
    NavbarItem(
        name='cms',
        label='CMS',
        fa_icon='fas fa-user',
        url_name=settings.DASHBOARD_URL_NAMES.get('cms_url')))

bhp_utility_systems.append_item(
    NavbarItem(
        name='timesheet',
        label='Timesheets',
        fa_icon='fas fa-stopwatch',
        url_name=settings.DASHBOARD_URL_NAMES.get('timesheet_home_url')))

site_navbars.register(bhp_utility_systems)
