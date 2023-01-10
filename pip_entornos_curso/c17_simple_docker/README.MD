# Simple structured data type convertor

This easy python code allows the user to convert a file from a structured data type to other one, currently this are the extensions suppoprted:

* json
* csv
* xml
* xlsx

### Set Up 

Make a new virtual env
```bash
python3 -m venv env
source env/bin/activate
```

Install all the libraries for this project
```bash
pip install -r requirements.txt
```

How to run the program?
```
python main.py <file_to_convert> <new_extension> -n <optional_output_name>
```
Examples:
```
python main.py test.csv json -n output_in_json_format
```

```
python main.py test.json xlsx
```

To stop the virtual environment

```bash
deactivate
```
