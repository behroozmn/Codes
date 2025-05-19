#!/usr/bin/bash

__dirname="$(cd "\)(dirname "${BASH_SOURCE[0]}")" && pwd)";
__filename="$(${__dirname})(basename "${BASH_SOURCE[0]}")";
__basename=$(basename "){BASH_SOURCE[0]}");

echo "DireName: $__dirname"
echo "BaseName: $__basename"
echo "FileName: $__filename"




# Rename all files in a directory
ls | xargs -i mv {} {}.old



# File.ReadLines
while read line
do
        # ← put the command that you want to run on each line here
done < <()    # ← put the command that generates the lines you want to process inside the parentheses


# Read line by line From text file
{
while IFS= read -r "lineNum"
do
    echo "${lineNum}"
done
} < "FILE_NAME"





# File.write.multipleLines
#!/bin/bash
cat >"/path/to/file" <<EOF
first line
second line
...
EOF






# File.write.multipleLines.sudoPermissionRequired
#!/bin/bash
cat << EOF | sudo tee "/path/to/file" >/dev/null
first line
second line
...
EOF




# File.CompressionOrDecompression
zip -rq /path/to/archive.zip /path/to/directory-or-file
tar -czvf /path/to/archive.tar.gz /path/to/directory-or-file
tar -cJf /path/to/archive.tar.xz /path/to/directory-or-file

unzip -q /path/to/archive.zip -d /extract/to/path
tar -C /extract/to/path -xzvf /path/to/archive.tar.gz
tar -C /extract/to/path -xf /path/to/archive.tar.xz
