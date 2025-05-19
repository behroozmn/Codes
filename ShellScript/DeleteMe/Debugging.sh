set -o xtrace
[or]
set -x

#EXAMPLE
# >>>>>>>>>>>>>>>>>>>>>>>> Before >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -x
a=5
echo $a
echo "bar"

# [output]
# → + a=5
# → + echo 5
# → 5
# → + echo bar
# → bar