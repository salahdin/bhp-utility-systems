from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


bhp_utility_systems = Navbar(name='bhp_utility_systems')

bhp_utility_systems.append_item()

site_navbars.register(bhp_utility_systems)
