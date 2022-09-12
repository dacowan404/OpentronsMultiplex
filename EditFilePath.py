import pandas as pd
from datetime import datetime
import os

#dirname = os.path.dirname(__file__)
inputFile = '/Users/gencore/Desktop/MultiplexingOpentrons/CSVs/21130_Hybird_redo_Sample.csv'
#filename = os.path.join(dirname, 'relative/path/to/file/you/want')

inputTable = pd.read_csv(inputFile, header=None, names= ['Volume', 'StartPlate', 'StartPosition', 'EndPosition'])
inputString = inputTable.to_string()

currentTime = datetime.now()
timeString = currentTime.strftime("%m/%d/%Y %I:%M:%S %p")

s = f'#file created: {timeString}\n\nimport pandas as pd\nfrom io import StringIO\n\n#dataframe String\ninputString = """{inputString}"""\n'

scriptFilePath = '/Users/gencore/Desktop/MultiplexingOpentrons/unfinishedScript.py'
with open(scriptFilePath, 'r') as scriptFile:
    script = scriptFile.read()

outputFilePath = '/Users/gencore/Desktop/MultiplexingOpentrons/Multiplex.py'
with open(outputFilePath, 'w') as outputFile:
    outputFile.write(s)
    outputFile.write(script)