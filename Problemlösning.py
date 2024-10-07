


tables = [ "ettans", "Tvåans" , "treans", "fyrans" , "femmans" , "sexans" , "sjuans" , "åttans" , "nians" , "tians" , "elvans" , "tolvans" ]

for table in range(1,13):
    print(f"{tables[table-1].upper()} GÅNGERTABELL")
    for factor in range(1,11):
        print(f"{table} * {factor} = {table * factor}")











