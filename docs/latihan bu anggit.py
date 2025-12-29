# LIBRARY #
import math
from collections import Counter

# FUNGSI DAN PROSEDUR #

# Entropy
def entropy(data) :
    n = len( data)
    nGrup = Counter(data)
    ent = 0.0
    for c in nGrup. Values():
        p = c / n
        ent -= p * math. log2(p)
        return ent
    
# Gain
def gain(data_input, data_output, fitur):
    base_ent = entropy(data_output)
    base_n = len(data_output)

    # kelompok berdasarkan nilai atribut
    subsets = {}
    for x, label in zip(data_input, data_output):
        key = x[fitur]
        subsets.setdefault(key, []).append(label)

    subsets_ent = 0.0
    for labels in subsets.values():
        subsets_ent +=  (len(labels) / base_n) * entropy(labels)

    return base_ent - subsets_ent

# Tree
def buat_tree(data_input, data_output, feature_indices):
    # semua output (label) sama -> leaf
    if len(set(data_output)) == 1:
        return data_output[0]

    # fitur kosong -> habis
    if not feature_indices:
        return Counter(data_output).most_common(1)[0][0]

    # Pilih fitur terbaik berdasarkan gain
    gains = [(gain(data_input, data_output, idx), idx) for idx in feature_indices]
    gains.sort(reverse=True)
    best_gain, best_fitur = gains[0]

    # jika gain = 0 -> tidak ada peningkatan
    if best_gain == 0:
        return Counter(data_output).most_common(1)[0][0]

    tree = {best_fitur: {}}

    # Nilai-nilai unik fitur pada data saat ini
    values = set(x[best_fitur] for x in data_input)
    for val in values:
        # buat subset data untuk nilai fitur = val
        sub_input = [x for x, label in zip(data_input, data_output) if x[best_fitur] == val]
        sub_output = [label for x, label in zip(data_input, data_output) if x[best_fitur] == val]

        # jika subset kosong
        if not sub_input:
            tree[best_fitur][val] = Counter(data_output).most_common(1)[0][0]
        else:
            sisa_fitur = [i for i in feature_indices if i != best_fitur]
            tree[best_fitur][val] = buat_tree(sub_input, sub_output, sisa_fitur)

    return tree

# INILISIASI #

#
            
