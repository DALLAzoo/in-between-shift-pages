from pathlib import Path
import re
P=Path(__file__).with_name('in_between_shift_site_v13_source_toc.html')
s=P.read_text(encoding='utf-8')
# Update the generated source-level table of contents. Run after edits.
entries=[]
for m in re.finditer(r'<!-- SECTION: ([^|]+) \| ([^\n]+?) -->',s):
    entries.append((m.group(1).strip(),m.group(2).strip(),s.count('\n',0,m.start())+1))
lines=['<!-- AUTO-GENERATED SOURCE INDEX: run python build_tarot_toc.py after editing -->']
lines += [f'<!-- L{line:04d} | {name} | {desc} -->' for name,desc,line in entries]
lines.append('<!-- END SOURCE INDEX -->')
index='\n'.join(lines)
s=re.sub(r'<!-- AUTO-GENERATED SOURCE INDEX:.*?<!-- END SOURCE INDEX -->',index,s,flags=re.S)
# Recalculate once more because the index itself may change line count.
entries=[]
for m in re.finditer(r'<!-- SECTION: ([^|]+) \| ([^\n]+?) -->',s):
    entries.append((m.group(1).strip(),m.group(2).strip(),s.count('\n',0,m.start())+1))
lines=['<!-- AUTO-GENERATED SOURCE INDEX: run python build_tarot_toc.py after editing -->']
lines += [f'<!-- L{line:04d} | {name} | {desc} -->' for name,desc,line in entries]
lines.append('<!-- END SOURCE INDEX -->')
s=re.sub(r'<!-- AUTO-GENERATED SOURCE INDEX:.*?<!-- END SOURCE INDEX -->','\n'.join(lines),s,flags=re.S)
P.write_text(s,encoding='utf-8')
print('\n'.join(lines))
