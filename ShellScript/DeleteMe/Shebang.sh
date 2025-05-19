#!/usr/bin/bash
# -*- coding: utf-8 -*-

# Or

#!/usr/bin/bash
# -*- coding: ascii -*-

# Or

#!/usr/bin/bash
# -*- coding: latin-1 -*-



#!/usr/bin/env
#!/bin/bash

#Notice
#1-[/usr/bin/env] bash is more portable than [/bin/bash]

#2-Avoid using #!/usr/bin/env bash -e (vs set -e),
#  because when someone runs your script as bash ./script.sh,
#  the exit on error will be ignored.


