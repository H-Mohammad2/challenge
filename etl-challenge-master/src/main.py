import csv
import logging

from database import Database

logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__name__)


class EtlScript:
    def __init__(self):
        self.database_conn = Database("acme")
        self.header_file = "./headers.txt"
        self.data_file = "./data.csv"
        self.out_file = "./output.csv"

    def load_file_to_database(self, file_path: str):
        self.database_conn.load_file(file_path)

    def run(self):
        # Your code starts here.
        #read headers from header file

        csv.register_dialect('customdelimiter', delimiter='|')
        with open('final_output.csv', 'wt', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            with open('headers.txt') as csv_file:
                csv_reader = csv.reader(csv_file)
                header = []
                for row in csv_reader:
                    header.append(row[0])
                writer.writerow(header)


            with open('data.csv') as csv_file:
                csv_reader = csv.reader(csv_file,"customdelimiter")

                for row in csv_reader:
                    writer.writerow(row)

            self.load_file_to_database("final_output.csv")


if __name__ == "__main__":
    EtlScript().run()
    header = []
