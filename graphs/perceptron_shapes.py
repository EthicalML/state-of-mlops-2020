g = PGM([7, 5], origin=[-0.5, 0])

g.add_node(Node('feature_0', '$x_0$', 1, 2))
g.add_node(Node('feature_1', '$x_1$', 1, 1))
g.add_node(Node('bias', '$b$', 2, 0.5))
g.add_node(Node('weighted_sum', 'Σ', 2, 1.5, observed=True))
g.add_node(Node('activation_function', '$f(x)$', 3, 1.5, observed=True))
g.add_node(Node('output', '$y$', 4, 1.5))

g.add_edge('feature_0', 'weighted_sum')
g.add_edge('feature_1', 'weighted_sum')
g.add_edge('bias', 'weighted_sum')
g.add_edge('weighted_sum', 'activation_function')
g.add_edge('activation_function', 'output')

helpers.add_label(g, '$w_0$', 1.5, 2)
helpers.add_label(g, '$w_1$', 1.5, 1)
helpers.add_label(g, '1', 2.2, 1)

helpers.add_label(g, 'Area', 0.2, 2,
    color='blue', size='medium', weight='bold')
helpers.add_label(g, 'Perimeter', 0.2, 1,
    color='blue', size='medium', weight='bold')
helpers.add_label(g, 'Square OR Triangle', 5.3, 1.5,
    color='red', size='medium', weight='bold')
