from embeddings import gen_embeddings, save_embeddings
import os

def build_embeddings(lst: list) -> None:
    """
    call this whenever the data in files are changed.
    """
    data = gen_embeddings(lst)
    save_embeddings(data)

folder = "data"
data = []

for file in os.listdir(folder):
    if file.endswith(".txt"):
        data.append(file)

build_embeddings(data)