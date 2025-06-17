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
    def __init__(self, id, periodo_mkt, mes_ano, in_ativo, observacao, user, dt_insert):
        self.id              = id
        self.periodo_mkt     = periodo_mkt
        self.mes_ano         = mes_ano
        self.in_ativo        = in_ativo
        self.observacao      = observacao
        self.user            = user
        self.dt_insert       = dt_insert

class empreendimento_class:
    def __init__(self, id, empreendimento):
        self.id              = id
        self.empreendimento  = empreendimento

class user:
    def __init__(self, email, area_acesso, perfil, user_insert, dt_insert):
        self.email       = email
        self.area_acesso = area_acesso
        self.perfil      = perfil
        self.user_insert = user_insert
        self.dt_insert   = dt_insert


class suprimentos_contratos:
    def __init__(self, id, cd_empresa, nu_contrato, vl_orcamento, vl_primeira_proposta, user_insert, dt_insert):
        self.id                   = id
        self.cd_empresa           = cd_empresa
        self.nu_contrato          = nu_contrato
        self.vl_orcamento         = vl_orcamento
        self.vl_primeira_proposta = vl_primeira_proposta
        self.user_insert          = user_insert
        self.dt_insert            = dt_insert

    
class comercial_metas:
    def __init__(self, id, empreendimento, periodo, agrupamento_empreendimento, meta, considera_bi, dt_insert, user):
        self.id                         = id
        self.empreendimento             = empreendimento
        self.periodo                    = periodo
        self.agrupamento_empreendimento = agrupamento_empreendimento
        self.meta                       = meta
        self.considera_bi               = considera_bi
        self.dt_insert                  = dt_insert
        self.user                       = user

class eventos_auten:
    def __init__(self, id, nm_evento, nm_projeto, id_fila, id_empreendimento):
        self.id                 = id
        self.nm_evento          = nm_evento
        self.nm_projeto         = nm_projeto
        self.id_fila            = id_fila
        self.id_empreendimento  = id_empreendimento