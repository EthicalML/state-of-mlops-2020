g = PGM([5.1, 3.9], origin=[0.5, 0.4])

input_layer = helpers.layer(
    g,
    [0, 1, 0, 0, 0],
    1, 4, spacing=0.75)
hidden_layers = [
    helpers.layer(
        g,
        [f'$h_{{{i},{j}}}$' for j in range(3)],
        2 + (1 * i), 3.25,
        spacing=0.75, observed=True)
    for i in range(3)
]
output_layer = helpers.layer(
    g,
    [1, 0, 0, 0, 0],
    5, 4, spacing=0.75)

helpers.fully_connect(g, input_layer, hidden_layers[0])
helpers.fully_connect(g, hidden_layers[0], hidden_layers[1])
helpers.fully_connect(g, hidden_layers[1], hidden_layers[2])
helpers.fully_connect(g, hidden_layers[2], output_layer)

helpers.add_label_range(
    g,
    ['a', 'b', 'c', 'd', 'e'],
    0.6, 4, spacing=0.75, direction='V',
    color='blue', size='medium', weight='bold',
    overrides={'b': {'color': 'red'}})
helpers.add_label_range(
    g,
    ['a', 'b', 'c', 'd', 'e'],
    5.4, 4, spacing=0.75, direction='V',
    color='blue', size='medium', weight='bold',
    overrides={'a': {'color': 'red'}})

helpers.add_label(g, '...etc.', 1, 0.5, weight='bold')
helpers.add_label(g, '...etc.', 5, 0.5, weight='bold')
