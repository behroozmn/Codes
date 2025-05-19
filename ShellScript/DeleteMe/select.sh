#!/bin/bash
echo "choose one of them"
select x in one two three; do
    if [ -n "$x" ]; then
        echo "Have you selected :$x"
        break
    else
        echo 'invalid choice'
    fi
done
