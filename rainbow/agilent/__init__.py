from rainbow.agilent import chemstation
from rainbow.datadirectory import DataDirectory
import os 


def read(path, prec=0, hrms=False):
    """
    Reads an Agilent .D directory. 

    Args:
        path (str): Path of the directory.
        prec (int, optional): Number of decimals to round masses.
        hrms (bool, optional): Flag for HRMS parsing. 

    Returns:
        DataDirectory representing the Agilent .D directory. 

    """
    datafiles = []
    datafiles.extend(chemstation.parse_allfiles(path, prec))
    if hrms: 
        from rainbow.agilent import masshunter 
        datafiles.extend(masshunter.parse_allfiles(path))

    metadata = chemstation.parse_metadata(path, datafiles)

    return DataDirectory(path, datafiles, metadata)

def read_metadata(path):
    """
    Reads metadata from an Agilent .D directory.

    Args:
        path (str): Path of the directory.

    Returns:
        Dictionary representing metadata in the Agilent .D directory.

    """
    datafiles = []
    metadata = chemstation.parse_metadata(path, datafiles)
    if len(metadata) == 1:
        datadir = read(path)
        return datadir.metadata if datadir else None
    return metadata



def read_metadata_and_agilent(path):
    """
    Reads metadata and finds Agilent files from an Agilent .D directory.

    Args:
        path (str): Path of the directory.

    Returns:
        Dictionary representing metadata and agilent files present in the Agilent .D directory.

    """
    
    agilent_files = {}
    agilent_files.update(read_metadata(path))
    for name in os.listdir(path):
        filePath = os.path.join(path, name)
        ext = os.path.splitext(filePath)[1].lower()

        # Check if the file has a valid extension
        if ext == '.ch':
            agilent_files ["Agilent .ch"] = True
        elif ext == '.uv':
            agilent_files ["Agilent .uv"] = True
        elif ext == '.ms':
            if os.path.splitext(filePath)[0][-1] == '1':
                agilent_files ["Agilent .ms 1"] = True
            elif os.path.splitext(filePath)[0][-1] == '2':
                agilent_files ["Agilent .ms 2"] = True
            
    

    return agilent_files