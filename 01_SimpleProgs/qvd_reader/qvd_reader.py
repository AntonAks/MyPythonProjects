from tempfile import TemporaryDirectory
from pathlib import Path
from win32com.client import Dispatch
import pandas as pd


file_path = '<file path>'


def qvd_to_pandas(src_qvd):

    with TemporaryDirectory(dir='.') as tmp_dir:
        tmp_csv = Path(tmp_dir).absolute() / 'tmp.csv'
        tmp_qvw = Path(tmp_dir).absolute() / 'tmp.qvw'

        script = f'''    
        ExportTable: REPLACE LOAD * FROM {Path(src_qvd).absolute()} (qvd);
        STORE ExportTable INTO {tmp_csv} (txt);
        DROP TABLE ExportTable;
        '''

        qv = Dispatch('QlikTech.QlikView')
        active_doc = qv.CreateDoc()

        doc_properties = active_doc.GetProperties()
        doc_properties.script = doc_properties.script + script

        active_doc.SetProperties(doc_properties)
        active_doc.SaveAs(tmp_qvw)
        active_doc.ReloadEx(0, 1)

        active_doc.CloseDoc()
        qv.Quit()

        df = pd.read_csv(open(tmp_csv, encoding='utf8'), dtype=str)

    return df

df = qvd_to_pandas(file_path)

print(df)
