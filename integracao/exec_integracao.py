import integracao_contratos
import integracao_empreendimento
import integracao_usuario


print('Iniciando integração')
integracao_usuario.integracaoUsuario()
integracao_contratos.integracaoContratosSuprimentos()
integracao_empreendimento.integracaoEmpreendimento()
print('Integração finalizada!')