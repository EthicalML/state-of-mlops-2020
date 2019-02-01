g = PGM([5.1, 4.1], origin=[0.5, 0.2])

input_layer = helpers.layer(
    g,
    [0, 1, 0, 0, 0],
    1, 4, spacing=0.75)
hidden_layer = helpers.layer(
    g,
    [f'$h_{i}$' for i in range(3)],
    3, 3.25, spacing=0.75, observed=True)
output_layer = helpers.layer(
    g,
    [1, 0, 0, 0, 0],
    5, 4, spacing=0.75)

helpers.fully_connect(g, input_layer, hidden_layer)
helpers.fully_connect(g, hidden_layer, output_layer)

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
