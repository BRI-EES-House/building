import pandas as pd

class MasterTables:
    def __init__(self):
        self.m_BURU = pd.read_csv('master/m_BURU.csv', encoding='cp932')
        self.m_CP = pd.read_csv('master/m_CP.csv', encoding='cp932')
        self.m_HWU = pd.read_csv('master/m_HWU.csv', encoding='cp932')
        self.m_RSUR = pd.read_csv('master/m_RSUR.csv', encoding='cp932')
        self.m_LHGDR = pd.read_csv('master/m_LHGDR.csv', encoding='cp932')
        self.m_HHGDR = pd.read_csv('master/m_HHGDR.csv', encoding='cp932')
        self.m_AHGDR = pd.read_csv('master/m_AHGDR.csv', encoding='cp932')
        self.m_CAL = pd.read_csv('master/m_CAL.csv', encoding='cp932')

def get_master_tables():
    return MasterTables()
