# Úkol 9 - Okáč

import random

pole = ["červená", "modrá", "zelená", "žlutá", "černá"]

nahodna_volba = random.choice(pole)
index_volby = nahodna_volba.index

print(f"Náhodná volba je {nahodna_volba} a leží na indexu {index_volby}")