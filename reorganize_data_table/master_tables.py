import pandas as pd

class MasterTables:

    def __init__(self, m_BURU, m_CP, m_T, m_HWU, m_RSUR, m_LHGDR, m_HHGDR, m_AHGDR, m_CAL):
        self.m_BURU = m_BURU
        self.m_CP = m_CP
        self.m_T = m_T
        self.m_HWU = m_HWU
        self.m_RSUR = m_RSUR
        self.m_LHGDR = m_LHGDR
        self.m_HHGDR = m_HHGDR
        self.m_AHGDR = m_AHGDR
        self.m_CAL = m_CAL

    @classmethod
    def read(cls):
    
        m_BURU = pd.read_csv('master/m_BURU.csv', encoding='cp932')
        m_CP = pd.read_csv('master/m_CP.csv', encoding='cp932')
        m_T = pd.read_csv('master/m_T.csv', encoding='cp932')
        m_HWU = pd.read_csv('master/m_HWU.csv', encoding='cp932')
        m_RSUR = pd.read_csv('master/m_RSUR.csv', encoding='cp932')
        m_LHGDR = pd.read_csv('master/m_LHGDR.csv', encoding='cp932')
        m_HHGDR = pd.read_csv('master/m_HHGDR.csv', encoding='cp932')
        m_AHGDR = pd.read_csv('master/m_AHGDR.csv', encoding='cp932')
        m_CAL = pd.read_csv('master/m_CAL.csv', encoding='cp932')
    
        return cls(m_BURU, m_CP, m_T, m_HWU, m_RSUR, m_LHGDR, m_HHGDR, m_AHGDR, m_CAL)
    
    def write(self):

        for df, file_name in [
            (self.m_BURU, 'master/m_BURU'),
            (self.m_CP, 'master/m_CP'),
            (self.m_T, 'master/m_T'),
            (self.m_HWU, 'master/m_HWU'),
            (self.m_RSUR, 'master/m_RSUR'),
            (self.m_LHGDR, 'master/m_LHGDR'),
            (self.m_HHGDR, 'master/m_HHGDR'),
            (self.m_AHGDR, 'master/m_AHGDR'),
            (self.m_CAL, 'master/m_CAL')
        ]:
            df.to_csv(file_name + '.csv', encoding='cp932')


