import base64, gzip, json

# Read and compress
data = open('Rwanda-2023-full-data.csv', 'rb').read()
compressed = gzip.compress(data, 9)
encoded = base64.b64encode(compressed).decode('ascii')

# Split into lines of 100 chars for readability
lines = [encoded[i:i+100] for i in range(0, len(encoded), 100)]
joined = '"\n"'.join(lines)

# Write the cell code
cell_code = f'''# --- Embedded CSV data (gzip + base64) ---
import base64, gzip
from pathlib import Path

_b64 = (
"{joined}"
)

_csv_bytes = gzip.decompress(base64.b64decode(_b64))
CSV_PATH = Path("/content/data/Rwanda-2023-full-data.csv")
CSV_PATH.parent.mkdir(exist_ok=True)
CSV_PATH.write_bytes(_csv_bytes)
print(f"Wrote {{len(_csv_bytes):,}} bytes to {{CSV_PATH}}")
'''

with open('_embed_cell.py', 'w') as f:
    f.write(cell_code)

print(f'Generated _embed_cell.py ({len(cell_code):,} chars)')
