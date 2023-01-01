'''
Author: Sylvain Dec 2022
'''

from ast import arg
from html import entities
import os
import networkx as nx
import matplotlib.pyplot as plt
import argparse
from transformers import BertTokenizer

class Prepare:

    def __init__(self, folder_path, folder_path_entities_relations) -> None:
        self.folder_path = folder_path
        self.folder_path_entities_relations = folder_path_entities_relations

    def build_graph_from_file(self, file_path):
        graph = nx.MultiDiGraph()
        with open(file_path, 'r') as file:
            for l in file:
                e1, r, e2 = l.strip().split('\t')
                # Bidirectionnal
                graph.add_edges_from([(e1, e2, dict(relation=r))])
                graph.add_edges_from([(e2, e1, dict(relation='inv-'+r))])

        return graph
    
    def get_relations_entities(self, ):

        relation2text, entity2text = {}, {}
        for root, _, files in os.walk(self.folder_path_entities_relations):
            for file in files:
                file_path = root + '/' + file
                if 'relation' in file:
                    with open(file_path, 'r', encoding="utf8") as file_relation:
                        for l in file_relation:
                            relation, text = l.strip().split('\t')
                            relation2text[relation] = text
                elif 'entity' in file:
                    with open(file_path, 'r', encoding="utf8") as file_entity:
                        for l in file_entity:
                            entity, text = l.strip().split('\t')
                            name = text.split(',')[0]
                            entity2text[entity] = name
        return relation2text, entity2text

    def read_folders(self,):
        for root, _ , files in os.walk(self.folder_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = root + '/' + file
                    data = self.build_graph_from_file(file_path)
                    relations, entities = self.get_relations_entities()


    def prepare_inputs_to_bert(self,):
        pass



if __name__ == '__main__':

    parser = argparse.ArgumentParser(' Loader Data BERTRL')
    parser.add_argument('--folder_data', default=r'C:\\Users\\verdy\Desktop\\github_repos\BERTRL\data\\fb237', help='path from text data')
    parser.add_argument('--folder_relations_entities', default=r'C:\\Users\\verdy\Desktop\\github_repos\BERTRL\data\\text\\FB237', help='path to get the relations and entities')

    params = parser.parse_args()

    prepare = Prepare(params.folder_data, params.folder_relations_entities)
    prepare.read_folders()
