import sqlite3
con = sqlite3.connect(':memory:')
con.enable_load_extension(True)
a = con.execute("pragma compile_options;")
for i in a: print(i); #check for ENABLE_JSON1

