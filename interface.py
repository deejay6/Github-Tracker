def copy_csv():
    with open("output.csv") as f2:
        lines = f2.readlines()
        lines = [l for l in lines if "ROW" in l]
        with open("comparator.csv", "w") as f1:
            f1.writelines(lines)


copy_csv()