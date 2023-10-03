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
    Reads metadata and channels from an Agilent .D directory.

    Args:
        path (str): Path of the directory.

    Returns:
        Dictionary representing metadata in the Agilent .D directory.

    """
    datafiles = []
    metadata = chemstation.parse_metadata(path, datafiles)
    if len(metadata) != 1:
        for name in map(str.lower, os.listdir(path)):
            if name.endswith('ch'):
                metadata["Agilent .ch"] = True
            elif name.endswith('uv'):
                metadata["Agilent .uv"] = True
            elif name.endswith('1.ms'):
                metadata["Agilent .ms 1"] = True
            elif name.endswith('2.ms'):
                metadata["Agilent .ms 2"] = True
    if len(metadata) == 1:
        datadir = read(path)
        if not datadir:
            return None
        metadata = datadir.metadata
        for name in [datafile.name.lower() for datafile in datadir.datafiles]:
            if name.endswith('ch'):
                metadata["Agilent .ch"] = True
            elif name.endswith('uv'):
                metadata["Agilent .uv"] = True
            elif name.endswith('1.ms'):
                metadata["Agilent .ms 1"] = True
            elif name.endswith('2.ms'):
                metadata["Agilent .ms 2"] = True
    return metadata
