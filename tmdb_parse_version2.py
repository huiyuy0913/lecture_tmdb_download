import pandas
from bs4 import BeautifulSoup

import os
import re
import glob

if not os.path.exists("parsed_files_version2"):
	os.mkdir("parsed_files_version2")


df = pandas.DataFrame()


for file_name in glob.glob("json_files/*.json"):

	base_name = os.path.basename(file_name)

