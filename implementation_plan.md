# Track Report Generation Plan

create track report markdown file template

for each track in the folder 'tracks':

track: {track_name}.yaml

regenerate / create markdown file: {track_name}.md
collect slugs from the track
for each slug collect stats from according stats.json file which are presented in the each of the slug folders in 'problems' directory
past this statistic to the corresponding table in report md file
