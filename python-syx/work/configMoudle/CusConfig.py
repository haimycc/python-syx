import configparser
import os


def getConfig(configDir, configName):
    if (configDir):
        cf = configparser.ConfigParser()
        configDir = os.getcwd()
    cf.read(configDir + configName, encoding='utf-8')


if __name__ == "__main__":
    cf = configparser.ConfigParser()
    configDir = os.getcwd()
    cf.read(configDir + r"\cusconfig.txt", encoding='utf-8')
    sections = cf.sections()
    print(sections)
    moduleRoot = str(cf.get("config", "moduleRoot")).strip()
    print(moduleRoot)
