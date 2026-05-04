from wifi import spusti_wifi
from motory import vypni_motory
from ledky import vypni_ledky
from server import spusti_server

vypni_motory()
vypni_ledky()

spusti_wifi()
spusti_server()