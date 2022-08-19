import csv
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
    def import_data(path, type):
        if ".csv" in path:
            return Inventory.read_csv(path, type)
