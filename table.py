import pandas

data = [10, 9, 7, 8, 10]

siswa = ['Ahmad', 'Riski', 'Budi', 'Sucipto', 'Farhan']

nilai = pandas.DataFrame({
  "Name": siswa,
  "Score": data
})

print(nilai)
