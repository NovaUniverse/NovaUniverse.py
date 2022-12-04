from pathlib import Path
import pdoc

GITHUB_RAW = "https://raw.githubusercontent.com/NovaUniverse/NovaUniverse.py/v2"

pdoc.render.configure(logo=f"{GITHUB_RAW}/assets/logo.png", logo_link="https://novauniversepy.devgoldy.me/", footer_text="Copyright (C) 2022 - Dev Goldy", 
template_directory=Path("./docs_template"))

pdoc.pdoc("./novauniverse", output_directory=Path("./docs/"))