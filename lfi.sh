while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  curl 'adress...key='"$p"
done < /path to the directory with the dictionary of interesting files (LFI)
