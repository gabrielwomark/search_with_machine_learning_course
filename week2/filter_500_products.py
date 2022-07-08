from collections import defaultdict


def filter_categories(data_path, output_path, min_num_products=500):
    cat_to_products = defaultdict(list)
    with open(data_path, "r") as fin:
        for line in fin:
            line = line.strip()
            cat, product = line.split(" ", 1)
            cat_to_products[cat].append(product)
    
    with open(output_path, "w") as fout:
        for cat, products in cat_to_products.items():
            if len(products) < min_num_products:
                continue
            for product in products:
                fout.write(" ".join([cat, product]) + "\n")

if __name__ == "__main__":
    import sys
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    min_num_products = 500
    if len(sys.argv) == 4:
        min_num_products = sys.argv[3]
    filter_categories(input_path, output_path)