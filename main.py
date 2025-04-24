def generate():
    print("generating tables...")
    tables = ""
    for i in range (1,21):
        tables = ""
        for j in range (1,21):
            # print(f"{i} X {j} = {i*j} \n ")
            tables+= f"{i} X {j} = {i*j} \n"
        print(f"done generating tables for {i} \n")
        
        with open(f"tables/table_{i}.csv", "w") as f:
            f.write(tables)

generate()