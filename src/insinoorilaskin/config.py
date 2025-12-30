import os
from importlib import resources as pkg_resources
from pathlib import Path

from dotenv import load_dotenv

import insinoorilaskin

load_dotenv()

PACKAGE_NAME = "insinoorilaskin"

with pkg_resources.as_file(pkg_resources.files(insinoorilaskin)) as package_dir:
    DEFAULT_CONFIG_FILE_PATH = package_dir / "logger_config.toml"

LOGGER_CONFIG_FILE = Path(os.environ.get("insinoorilaskin_LOGGER_CONFIG_FILE", DEFAULT_CONFIG_FILE_PATH))
