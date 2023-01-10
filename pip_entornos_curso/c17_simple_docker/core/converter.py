import pandas as pd


def convert_file(file_dir: str = ".csv", output_type: str = "csv", name: str = "") -> None:
    """
    Functions to converts different structured data types among which are: csv, json, xml, xlsx.
    It saves the original file with the same name but with the new output_type extension and format

    :param file_dir: name file to be converted with its extension
    :param output_type: file type to convert
    :param name: Optional, name of the new generated file

    :return: None
    """

    # First step: get the original file type from the file dir
    input_type = file_dir.split(".")[-1]
    file_name = file_dir.split(".")[0]
    assert input_type in ["csv", "json", "xml", "xlsx"], f"{input_type} is not a valid input type"
    assert input_type in ["csv", "json", "xml", "xlsx"], f"{output_type} is not a valid output type"
    if input_type == "csv":
        data = pd.read_csv(file_dir)
    elif input_type == "json":
        data = pd.read_json(file_dir)
    elif input_type == "xml":
        data = pd.read_xml(file_dir)
    elif input_type == "xlsx":
        data = pd.read_excel(file_dir)
    else:
        return None
    if name != "" and name is not None:
        file_name = name
    if output_type == "csv":
        data.to_csv(f"{file_name}.{output_type}", index=False)
    elif output_type == "json":
        data.to_json(f"{file_name}.{output_type}", index=True)
    elif output_type == "xml":
        data.to_xml(f"{file_name}.{output_type}", index=False)
    elif output_type == "xlsx":
        data.to_excel(f"{file_name}.{output_type}", index=False)
    else:
        return None
