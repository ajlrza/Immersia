#!/usr/bin/env python3

# Make the test files executable
chmod +x * ./engine/tests/*.py

# Loop through them and execute one by one

errors=()

for file in /src/*.py; do

    $file > "output.txt"
    output=$(cat "output.txt")

     if [[ $output =~ ^FAILED$ ]]; then
        errors+=("${output}")
     fi

done

errors_length=${#errors[@]}
