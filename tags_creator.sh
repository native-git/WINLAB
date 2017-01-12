#!/usr/bin/env bash

#edit the range to print different numbers

for i in $(seq 0 25)

do

chilitags-creator $i 40
mv $i.png ./Grid_Tags/Size_40_Tags

done