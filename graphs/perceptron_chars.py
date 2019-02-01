g = PGM([5.7, 4.1], origin=[0.5, 0.2])

perceptron = Node('weighted_sum', 'Σ', 2, 2.5, observed=True)
g.add_node(perceptron)

activation = Node('activation_function', '$f(Σ)$', 3, 2.5, observed=True)
g.add_node(activation)

g.add_node(Node('bias', '$b$', 2, 1))
g.add_edge('bias', 'weighted_sum')
g.add_edge('weighted_sum', 'activation_function')

helpers.add_label(g, 'next character', 5.4, 2.5,
    color='red', size='medium', weight='bold')

input_layer = helpers.layer(
    g,
    [f'$x_{i}$' for i in range(5)],
    1, 4, spacing=0.75)
helpers.fully_connect(g, input_layer, [perceptron])

output_layer = helpers.layer(
    g,
    [f'$y_{i}$' for i in range(5)],
    4, 4, spacing=0.75)
helpers.fully_connect(g, [activation], output_layer)

weight_label_y_offsets = [0.5, 0.975, 1.4, 1.724, 2.05]
for i in range(5):
    helpers.add_label(
        g, f'$w_{i}$', 1.5, 4 - weight_label_y_offsets[i])

helpers.add_label(g, '1', 2.2, 1.5)

helpers.add_label_range(
    g,
    ['a', 'b', 'c', 'd', 'e'],
    0.6, 4, spacing=0.75, direction='V',
    color='blue', size='medium', weight='bold')
helpers.add_label_range(
    g,
    ['a', 'b', 'c', 'd', 'e'],
    4.4, 4, spacing=0.75, direction='V',
    color='blue', size='medium', weight='bold')

helpers.add_label(g, '...etc.', 1, 0.5, weight='bold')
