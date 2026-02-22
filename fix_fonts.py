lines = open('index.html', encoding='utf-8').readlines()
result = []
i = 0
while i < len(lines):
    line = lines[i]
    if 'Kaisei+Tokumin' in line or (i > 0 and 'Kaisei+Tokumin' in lines[i-1] and 'rel="stylesheet"' in line):
        i += 1
        continue
    if 'M+PLUS+1p' in line:
        i += 1
        continue
    if 'New+Tegomin' in line:
        # replace entire line with new fonts
        result.append('    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Share+Tech+Mono&family=Noto+Serif+TC:wght@400;600;700&display=swap" rel="stylesheet">\n')
        i += 1
        continue
    result.append(line)
    i += 1

open('index.html', 'w', encoding='utf-8').writelines(result)
print(f'Done. {len(result)} lines')
# Verify
for j, l in enumerate(result[:16], 1):
    print(f'{j}: {l.rstrip()[:100]}')
