from flask import Flask #, request
import traceback
import ast
from utils import get_attributes

import torch
from torch_geometric.data import Data

from network import Net

app = Flask(__name__)

@app.route('/<string:graph>/')
def test2(graph):
    try:
        device = torch.device('cuda:0')
        model = Net().to(device)
        model.load_state_dict(torch.load('model.pt', map_location=torch.device('cpu')))

        graph = ast.literal_eval(graph)
        get_attributes(graph)
        node_feats, edge_index = get_attributes(graph)

        edge_index = torch.LongTensor(edge_index)
        node_feats = torch.LongTensor(node_feats)
        y = torch.FloatTensor([1])

        data = Data(x=node_feats, edge_index=edge_index, y=y, graph=None, batch=torch.zeros_like(node_feats)).to(device)

        output, embed = model(data)

        return str(embed.data.cpu().numpy())
    except Exception  as ex:
    	return traceback.print_exc()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
