#!/bin/bash
cd images
for img in $(ls); do
    name=$(echo $img | sed 's/\.svg//');
    echo $name
    rsvg-convert -f png $name.svg > $name.png
done
