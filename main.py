import utils

if __name__ == "__main__":
    filename = "operations.json"
    operations = utils.read_file(filename)
    last_operation = utils.last_operations(operations)
    print(utils.information_output(last_operation))
