

"programa un reloj que se"
"actualice cada segundo"
"en python"

import time
from datetime import datetime

try:
    while True:
        ahora = datetime.now().strftime("%H:%M:%S")
        print("\rHora Actual: {}".format(ahora),end = "")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nReloj interrupt")
        
        