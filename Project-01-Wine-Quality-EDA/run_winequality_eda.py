import nbformat
from nbclient import NotebookClient
nb_path = 'WineQuality_EDA_MehraliHub.ipynb'
nb = nbformat.read(nb_path, as_version=4)
client = NotebookClient(nb, timeout=600)
print('Executing', nb_path)
client.execute()
nbformat.write(nb, nb_path)
print('Executed and saved', nb_path)
