#!/bin/bash
# Short commit helper - 3-4 words maximum
if [ $# -eq 0 ]; then
    echo "Usage: ./sc.sh \"commit message\""
    exit 1
fi

# Get the message and limit to 4 words
message="$1"
short_message=$(echo "$message" | cut -d' ' -f1-4)

git add .
git commit -m "$short_message"
