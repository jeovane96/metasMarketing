class metas:
    def __init__(self, id, empreendimento, mes_ano, meta, observacao, user, dt_insert):
        self.id              = id
        self.empreendimento  = empreendimento
        self.mes_ano         = mes_ano
        self.meta            = meta
        self.observacao      = observacao
        self.user            = user
        self.dt_insert       = dt_insert

class periodo:
    def __init__(self, id, periodo_mkt, mes_ano, observacao, user, dt_insert):
        self.id              = id
        self.periodo_mkt     = periodo_mkt
        self.mes_ano         = mes_ano
        self.observacao      = observacao
        self.user            = user
        self.dt_insert       = dt_insert