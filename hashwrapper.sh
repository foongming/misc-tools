for f in *.csv; do
  python hash.py -i "$f" -o "hashed-${f%.csv}.csv"
done
