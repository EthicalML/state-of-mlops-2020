ONE_HOT_SIZE = 5
HIDDEN_LAYER_SIZE = 5
NUM_HIDDEN_LAYERS = 3

SEQUENCE_LENGTH = 30
UNROLLED = False

g = PGM([9, 10], origin=[0, 0])

input_char = g.add_node(Node('input_char', '$x$', 1.25, 2))
input_one_hot = helpers.layer(
    g,
    [f'$xo_{i}$' for i in range(ONE_HOT_SIZE)],
    2.25, 3.5, spacing=0.75)
helpers.fully_connect(g, [input_char], input_one_hot)

hidden_layers = [
    helpers.layer(
        g,
        [f'$h_{{{i,j}}}$' for j in range(HIDDEN_LAYER_SIZE)],
        3.5 + i,
        3.5,
        spacing=0.75,
        observed=True)
    for i in range(NUM_HIDDEN_LAYERS)
]
helpers.fully_connect(g, input_one_hot, hidden_layers[0])
for i in range(1, NUM_HIDDEN_LAYERS):
    helpers.fully_connect(
        g, hidden_layers[i - 1], hidden_layers[i])

if UNROLLED:
    pass

output_one_hot = helpers.layer(
    g,
    ['$yo_{i}$' for i in range(ONE_HOT_SIZE)],
    6.75, 3.5, spacing=0.75)
output_char = g.add_node(Node('output_char', '$y$', 7.75, 2))

helpers.fully_connect(g, hidden_layers[-1], output_one_hot)
helpers.fully_connect(g, output_one_hot, [output_char])

helpers.add_label(g, 'current\ncharacter', 0.5, 2, weight='bold')
helpers.add_label(g, 'next\ncharacter', 8.5, 2, weight='bold')
