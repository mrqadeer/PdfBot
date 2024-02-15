import os

class Helper:
    def get_file_name(self,pdf_file):
        file_name=os.path.splitext(pdf_file.name)[0]

        return file_name
