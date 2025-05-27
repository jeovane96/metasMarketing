class metas:
    def __init__(self, id, nm_meta, empreendimento, mes_ano, tp_meta, meta, observacao, user, dt_insert):
        self.id              = id
        self.nm_meta         = nm_meta
        self.empreendimento  = empreendimento
        self.mes_ano         = mes_ano
        self.tp_meta         = tp_meta
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

class empreendimento_class:
    def __init__(self, id, empreendimento):
        self.id              = id
        self.empreendimento  = empreendimento