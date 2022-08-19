import csv
import json
from xml.etree import ElementTree as ET

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def read_csv(path, type):
        data = []

        with open(path, 'r') as file:
            data_file = csv.DictReader(file)
            for i in data_file:
                data.append(i)

        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)

    @staticmethod
    def read_json(path, type):
        data = []

        with open(path, 'r') as file:
            data_file = json.load(file)
            for i in data_file:
                data.append(i)

        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)

    @staticmethod
    def read_xml(path, type):
        data = []

        with open(path, 'r') as file:
            tree = ET.parse(file)
            root = list(tree.getroot())

            info_dict = {}

            for i in range(len(root)):
                for info in root[i]:
                    info_dict[info.tag] = info.text
                data.append(info_dict)
                info_dict = {}

        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)

    @staticmethod
    def import_data(path, type):
        if ".csv" in path:
            return Inventory.read_csv(path, type)
        if ".json" in path:
            return Inventory.read_json(path, type)
        if ".xml" in path:
            return Inventory.read_xml(path, type)
