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
        label='document',
        fa_icon='fas fa-file',
        url_name=settings.DASHBOARD_URL_NAMES.get('document_url')))

bhp_utility_systems.append_item(
    NavbarItem(
        name='CMS',
        label='CMS',
        fa_icon='',
        url_name=settings.DASHBOARD_URL_NAMES.get('cms_url')))

site_navbars.register(bhp_utility_systems)
