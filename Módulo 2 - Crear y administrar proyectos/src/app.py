# Lanzar el entorno virtual
# cd env\Scripts>
# activate

from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)


# deactivate    --Para desactivar el entorno virtual