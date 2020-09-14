# import sys
# sys.path.append('../')
class read_mca_file:
    def __init__(self, File, encode='utf-8'):
        self.fileD=open(File,encoding=encode)
        self.state='<<root>>'

    def set_state(self,line):
        if line.find('<<PMCA SPECTRUM>>')>=0:
            self.state='<<PMCA SPECTRUM>>'
        elif line.find('<<CALIBRATION>>')>=0:
            self.state='<<CALIBRATION>>'
            self.cal=[]
        elif line.find('<<DATA>>')>=0:
            self.state='<<DATA>>'
            self.data=[]
        elif line.find('<<DP5 CONFIGURATION>>')>=0:
            self.state='<<DP5 CONFIGURATION>>'
            self.conf={}
        elif line.find('<<DPP STATUS>>')>=0:
            self.state='<<DPP STATUS>>'
            self.status={}
        else:
            return -1
        return 1

    def read_info_value(self,line):
        offset=line.find('- ')+2
        return line[offset:]
            
    def read_info(self,line):
        if line.find('REAL_TIME')>=0:
            self.liveTime=float(self.read_info_value(line))
        if line.find('REAL_TIME')>=0:
             self.realTime=float(self.read_info_value(line))
        if line.find('START_TIME')>=0:
            self.date=self.read_info_value(line)

    def read_cal(self,line):
        if line.find('LABEL')>=0:
            return 0
        self.cal.append(line)

    def read_data(self,line):
        if line.find('<<END>>')>=0:
            return
        self.data.append(int(line))

    def read_conf(self,line):
        if line.find('<<DP5 CONFIGURATION END>>')>=0:
            return
        split=line.split(sep='=')
        key=split[0]
        value=split[1].split(sep=';')[0]
        self.conf[key]=value

    def read_status(self,line):
        if line.find('<<DPP STATUS END>>')>=0:
            return
        split=line.split(sep=':')
        key=split[0]
        value=split[1]
        self.status[key]=value
        
    def process_line(self,line):
        if self.state == '<<PMCA SPECTRUM>>':
            self.read_info(line)
        elif self.state == '<<CALIBRATION>>':
            self.read_cal(line)
        elif self.state == '<<DATA>>':
            self.read_data(line)
        elif self.state =='<<DP5 CONFIGURATION>>':
            self.read_conf(line)
        elif self.state =='<<DPP STATUS>>':
            self.read_status(line)
        
    def read_file(self):
        lines=self.fileD.readlines()
        for line in lines:
            #print(line,'ps:',self.state)
            #if state=='<<root>>':
            if self.set_state(line) < 0:
                self.process_line(line)

if __name__ == '__main__':
    mca=read_mca_file('Data/NaI2x2_old/mca/Cal_Co1.mca','latin-1')
    mca.read_file()
