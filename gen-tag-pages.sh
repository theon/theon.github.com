#!/usr/bin/env bash

# Dirty script to generate a page per tag with all the posts for that tag
tags=$(
    for post_file in `ls  _posts/`; do
        grep -oP "(?<=tags:).*" _posts/$post_file | tr -d ":[] " | tr "," "\n" | sort -u
    done
)

for tag in $tags; do
    file=tag/${tag}.html

    echo "---" > $file
    echo "layout: base" >> $file
    echo "---" >> $file
    echo "" >> $file
    echo "{% assign tag_name = '$tag' %}" >> $file
    echo "{% assign tag_pages = site.tags.${tag} %}" >> $file
    echo "{% include tag_page.html %}" >> $file
done