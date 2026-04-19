import base64, gzip

data = open('Rwanda-2023-full-data.csv', 'rb').read()
compressed = gzip.compress(data, 9)
encoded = base64.b64encode(compressed).decode('ascii')

with open('_csv_payload.txt', 'w') as f:
    f.write(encoded)

print(f'Written _csv_payload.txt ({len(encoded)} chars)')
