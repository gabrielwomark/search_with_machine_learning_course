import csv
import fasttext

SIMILARITY_THRESH = 0.75
model = fasttext.load_model("/workspace/datasets/fasttext/title_model.bin")


with open("/workspace/datasets/fasttext/top_words.txt") as fin:
    with open("/workspace/datasets/fasttext/synonyms.csv", "w") as fout:
        writer = csv.writer(fout)
        for line in fin:
            word = line.strip()
            neighbors = model.get_nearest_neighbors(word, k=20)
            
            # threshold neighbors to improve precision of synonyms
            neighbors = [word for sim_score, word in neighbors if sim_score > SIMILARITY_THRESH]

            writer.writerow([word] + neighbors)