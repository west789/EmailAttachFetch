from configparser import ConfigParser
from loggingModule import logger

class InitConfig(object):
    def __init__(self, cfgPath):
        # print(cfgPath)
        self.cfgPath = cfgPath
        self.config = ConfigParser()
        self.config.read(cfgPath)
        self.emailIP = self.config.get('email', 'emailIP')
        self.emailPort = self.config.getint('email', 'emailPort')
        self.emailUser = self.config.get('email', 'emailUser')
        self.emailPass = self.config.get('email', 'emailPass')
        self.emailSavePath = self.config.get('path', 'fileSavePath')
        self.cutOff = self.config.get('threshold', 'cutOff')
    
    def setCutOff(self, value):
        try:
            self.config.set('threshold', 'cutoff', str(value))
            with open(self.cfgPath, 'w+') as f:
                self.config.write(f)
        except Exception:
            logger.error("Error on update cutOFF to %s" %value)

if __name__ == "__main__":
    import os
    import sys
    if getattr(sys, 'frozen', False):
        module_path = os.path.dirname(sys.executable)
    elif __file__:
        module_path = os.path.dirname(__file__)
    # cfg = InitConfig(os.path.join(os.path.dirname(__file__), 'config.ini'))
    cfg = InitConfig(os.path.join(module_path, 'config.ini'))
    print (cfg.config.sections())
    