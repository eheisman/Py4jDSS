from py4j.java_gateway import JavaGateway, get_field
import pandas as pd
import numpy as np
import matplotlib.pylab as pylab
%matplotlib inline
gateway = JavaGateway() # connect to the JVM
jhec = gateway.jvm.hec
#dssFile = jhec.heclib.dss.HecDss.open("C:/crt/test.dss")
#pathnames = dssFile.getCatalogedPathnames(True)

# myRecord = dssFile.get("/BRANDYWINE CREEK/WILMINGTON, DE/FLOW/01JAN1996/1DAY/USGS/")
# pathTable = pd.DataFrame([i.split("/")[1:-1] for i in pathnames], columns=[i for i in "ABCDEF"])
# myRecord.getClass().toString()
# for m in dssfile.getClass().getMethods():
    # print(m.toString())


HEC_EPOCH_TIME = -2209046400
def extractTSC(dssfile, path, tz_offset=8, ignoreDPart=True):
    record = dssfile.get(path, ignoreDPart) #.getData()
    def convert_time(t):
        return np.datetime64(int(t)*60+HEC_EPOCH_TIME-tz_offset*3600, 's', )
    times = pd.DatetimeIndex(data=[convert_time(t) for t in get_field(record, "times")], name="DateTime")
    values = [v for v in get_field(record,"values")]
    return pd.TimeSeries(values, index=times) #, columns=get_field(myRecord, "parameter"))


# incomplete
def extractPDC(dssfile, path):
    return pd.DataFrame(data, index=xOrds, columns=colNames)

def openDSSFile(fname):
    return jhec.heclib.dss.HecDss.open(fname)

dssFile = openDSSFile("C:/crt/test.dss")
ts = extractTSC(dssFile, "/BRANDYWINE CREEK/WILMINGTON, DE/FLOW/01JAN1996/1DAY/USGS/")
ts.plot()