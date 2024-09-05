from packages.toraja.settings.app_config import NgrokAppConfig
from os.path import dirname, basename
from packages.toraja.conversion.conversion import humanize_string


class Config(NgrokAppConfig):
    name = basename(dirname(__file__))
    verbose_name = humanize_string(name)
