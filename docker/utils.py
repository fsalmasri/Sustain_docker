import numpy as np


def nodes_names_remapping(g):
    nodes_embed = {
        "pumpHead": 0,
        "asepticDisconnector": 1,
        "mechanicDisconnector": 2,
        "quickCoupler": 3,
        "triclampConnector": 4,
        "bioreactorBag": 5,
        "twoDimensionalBag": 6,
        "threeDimensionalBag": 7,
        "mixerBag": 8,
        "bottle": 9,
        "plug": 10,
        "sensor": 11,
        "couplerReducer": 12,
        "straightFitting": 13,
        "lConnector": 14,
        "tConnector": 15,
        "yConnector": 16,
        "xConnector": 17,
        "asepticConnector": 18,
        "sipConnector": 19,
        "pinchClamp": 20,
        "hydrophobicFilter": 21,
        "hydrophilicFilter": 22,
        "tubing": 23,
        "lConnector": 24,
        "tConnector": 25,
        "twoDimensionalBag": 26,
        "threeDimensionalBag": 27,
        "triclampConnector": 28,
        "sipConnector": 29,
        "bottle": 30,
        "mechanicDisconnector": 31,
        "Add_W": 32

    }

    node_feats = []
    for node in g:
        if 'B' in node:
            node_feats.append(nodes_embed['bioreactorBag'])
        elif 'H' in node:
            node_feats.append(nodes_embed['hydrophobicFilter'])
        elif 'F' in node:
            node_feats.append(nodes_embed['hydrophilicFilter'])
        elif 'Q' in node:
            node_feats.append(nodes_embed['quickCoupler'])
        elif 'Y' in node:
            node_feats.append(nodes_embed['yConnector'])
        elif 'X' in node:
            node_feats.append(nodes_embed['xConnector'])
        elif 'P' in node:
            node_feats.append(nodes_embed['plug'])
        elif 'A' in node:
            node_feats.append(nodes_embed['asepticConnector'])
        elif 'D' in node:
            node_feats.append(nodes_embed['asepticDisconnector'])
        elif 'S' in node:
            node_feats.append(nodes_embed['straightFitting'])
        elif 'M' in node:
            node_feats.append(nodes_embed['mixerBag'])
        elif 'R' in node:
            node_feats.append(nodes_embed['couplerReducer'])
        elif 'T' in node:
            node_feats.append(nodes_embed['triclampConnector'])
        elif 'N' in node:
            node_feats.append(nodes_embed['tConnector'])
        elif 'G' in node:
            node_feats.append(nodes_embed['twoDimensionalBag'])
        elif 'I' in node:
            node_feats.append(nodes_embed['threeDimensionalBag'])
        elif 'E' in node:
            node_feats.append(nodes_embed['triclampConnector'])
        elif 'O' in node:
            node_feats.append(nodes_embed['sipConnector'])
        elif 'J' in node:
            node_feats.append(nodes_embed['bottle'])
        elif 'C' in node:
            node_feats.append(nodes_embed['mechanicDisconnector'])
        elif 'Z' in node:
            node_feats.append(nodes_embed['lConnector'])
        elif 'W' in node:
            node_feats.append(nodes_embed['Add_W'])

        else:
            print('Error', node)
            exit()

    return node_feats

def get_attributes(g):
    dict_nodes = {}
    edge_index = []
    counter = 0

    for edge in g:
        for node in edge:
            if not node in dict_nodes:
                dict_nodes[node] = counter
                counter += 1

        edge_index.append([dict_nodes[edge[0]], dict_nodes[edge[1]]])

    node_feats = nodes_names_remapping(dict_nodes.keys())

    return node_feats, np.array(edge_index).T