import pickle
from os import path


class CachedLetterDict:
    letter_dict = None
    training_file_names = None
    letter_dict_depth = None

    def __init__(self, new_letter_dict: dict, new_training_file_name: str, new_letter_dict_depth: int):
        self.letter_dict = new_letter_dict
        self.training_file_names = new_training_file_name
        self.letter_dict_depth = new_letter_dict_depth

    def serialize(self, file_path):
        with open(file_path, "wb") as file:
            file.write(pickle.dumps((self.letter_dict, self.training_file_names, self.letter_dict_depth)))

    @staticmethod
    def deserialize(file_path):
        if path.exists(file_path):
            with open(file_path, "rb") as file:
                data = pickle.loads(file.read())
                return CachedLetterDict(data[0], data[1], data[2])
        return None
