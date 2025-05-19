#!/usr/bin/bash
mysql -u root -p123456  -h localhost -e "USE sadrsds;SELECT * FROM raiddisk;"
mysql -u root -p123456 "sadrsds" -h localhost -e "SELECT * FROM raiddisk;"

