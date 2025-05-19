#!/bin/bash

cat test.json
#{"title":"Person","type":"object","properties":{"firstName":{"type":"string"},"lastName":{"type":"string"},"age":{"description":"Age in years","type":"integer","minimum":0}},"required":["firstName","lastName"]}

cat test.json | python -m json.tool
cat test.json | jq
