from pathlib import Path

root = Path('files')
fpaths = root.glob("**/*") 

for path in fpaths:
  if path.is_file():
    par1 = path.parts[-3]
    par2 = path.parts[-2]
    newfname = par1 + '-' + par2 + '-' + path.name
    newfpath = path.with_name(newfname)
    path.rename(newfpath)