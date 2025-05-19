# -*- coding: utf-8 -*-
# Or
# -*- coding: ascii -*-
# Or
# -*- coding: latin-1 -*-

# Encod.Hash
hash=\((echo -n "\)variableToHash" | md5sum | cut -f1 -d ' ')

# Encode.base64
base64Encoded=$(echo -n "String" | base64)

#  Decode.base64
base64Encoded=$(echo -n "String" | base64)
base64Decoded=$(echo -n "<Hash>" | base64 -d)

Decode_CodeToString() {
    Code=$1
    local msg=\((base64 -d <<<"\)Code")
}