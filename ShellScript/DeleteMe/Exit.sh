
################################################################################ Command.Exit.WhenFailed.EvenPipeline
set -o pipefail

#EXAMPLE
# >>>>>>>>>>>>>>>>>>>>>>>> Before >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -e
foo | echo "a"
echo "bar"

# [output]
# →
# → a
# → line 5: foo: command not found
# → bar


# >>>>>>>>>>>>>>>>>>>>>>>> After >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -eo pipefail
foo | echo "a"
echo "bar"

# [output]
# → a
# → line 5: foo: command not found
##################################################################################################################################


######################################################################################### Command.Exit.WhenFailed
set -o errexit
[or]
set -e


#EXAMPLE
# >>>>>>>>>>>>>>>>>>>>>>>> Before >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
foo
echo "bar"

#[output]
# → line 4: foo: command not found
# → bar

# >>>>>>>>>>>>>>>>>>>>>>>> After >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -e
foo
echo "bar"

#[output]
# → line 5: foo: command not found

# >>>>>>>>>>>>>>>>>>>>>>>> PreventImmediateExit >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -e
foo || true
echo "bar"

#[output]
# → line 5: foo: command not found
# → bar




########################################################################################################################



############################################################### Exit.WhenUseUndeclaredVariables
set -o nounset
[or]
set -u

#EXAMPLE
# >>>>>>>>>>>>>>>>>>>>>>>> Before >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -e
echo $a
echo "bar"

# [output]
# →
# → bar


# >>>>>>>>>>>>>>>>>>>>>>>> After >>>>>>>>>>>>>>>>>>>>>>>>
#!/bin/bash
set -eu
echo $a
echo "bar"

# [output]
# → line 5: a: unbound variable
##################################################################################################3

