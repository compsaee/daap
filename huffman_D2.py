def build_huffman_tree(chars, freq):
    nodes = [{"freq": f, "symbol": s, "left": None, "right": None, "huff": ""} for f, s in zip(freq, chars)]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x["freq"])
        left = nodes[0]
        right = nodes[1]
        left["huff"] = 0
        right["huff"] = 1
        new_node = {"freq": left["freq"] + right["freq"], "symbol": left["symbol"] + right["symbol"], "left": left, "right": right, "huff": ""}
        nodes = nodes[2:]
        nodes.append(new_node)

    return nodes[0]


def print_nodes(node, val=""):
    new_val = val + str(node["huff"])
    if node["left"]:
        print_nodes(node["left"], new_val)
    if node["right"]:
        print_nodes(node["right"], new_val)
    if not node["left"] and not node["right"]:
        print(f"{node['symbol']} -> {new_val}")


def main():
    chars = ["a", "b", "c", "d", "e", "f"]
    freq = [50, 10, 30, 5, 3, 2]

    root_node = build_huffman_tree(chars, freq)

    print("Characters :", f'[{", ".join(chars)}]')
    print("Frequency  :", freq, "\n\nHuffman Encoding:")
    print_nodes(root_node)


if __name__ == "__main__":
    main()

"""
OUTPUT:

Characters : [a, b, c, d, e, f]
Frequency  : [5, 9, 12, 13, 16, 45]

Huffman Encoding:
f -> 0
c -> 100
d -> 101
a -> 1100
b -> 1101
e -> 111


"freq": f, 
"symbol": s, 
"left": None, 
"right": None, 
"huff": ""
"""
