#!/data/data/com.termux/files/usr/bin/bash

echo "Extrayendo texto limpio..."

rm -rf tmp_text
mkdir tmp_text

for f in *.html; do
  sed 's/<[^>]*>//g' "$f" | tr -s ' ' | tr '[:upper:]' '[:lower:]' > "tmp_text/$f.txt"
done

echo "Calculando similitud..."

cd tmp_text

for f in *.txt; do
  for g in *.txt; do
    if [ "$f" != "$g" ]; then
      
      # Intersección de palabras
      comunes=$(comm -12 <(tr ' ' '\n' < "$f" | sort | uniq) \
                         <(tr ' ' '\n' < "$g" | sort | uniq) | wc -l)

      # Total palabras únicas promedio
      total_f=$(tr ' ' '\n' < "$f" | sort | uniq | wc -l)
      total_g=$(tr ' ' '\n' < "$g" | sort | uniq | wc -l)

      avg=$(( (total_f + total_g) / 2 ))

      if [ "$avg" -gt 0 ]; then
        sim=$(( comunes * 100 / avg ))

        if [ "$sim" -gt 70 ]; then
          echo "SIMILARIDAD ALTA ($sim%): $f == $g"
        fi
      fi

    fi
  done
done

echo "Listo."
