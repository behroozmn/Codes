#!/bin/bash
# register a function (handler) to run on script termination (CTRL+C)
# CTRL+C event handler
function on_ctrl_c() {
    echo                # Set cursor to the next line of '^C'
    tput cnorm          # show cursor. You need this if animation is used.
                        # i.e. clean-up code here
    exit 1              # Don't remove. Use a number (1-255) for error code.
}

# Put this line at the beginning of your script (after functions used by event handlers).
# Register CTRL+C event handler
trap on_ctrl_c SIGINT