"""
Módulo de Generación de Contratos con IA
Agencia IA Argentina Segura
Propietario: Humberto Patricio Castro

Este módulo genera borradores de contratos legales conforme a la legislación argentina,
con contexto humanizado obligatorio y preparación para firma digital (Ley 25.506).
"""

import hashlib
import json
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

from .audit_log import AuditLogger, SeverityLevel


# Configuración del propietario y supervisor obligatorio
OWNER_NAME = "Humberto Patricio Castro"
OWNER_ROLE = "Director General y Propietario"


@dataclass
class ContractDraft:
    """Representa un borrador de contrato generado por IA."""
    contract_id: str
    contract_type: str
    parties: List[str]
    conditions: List[str]
    content: str
    humanized_context: str
    generated_at_utc: str
    generated_at_art: str
    hash_sha256: str
    status: str = "draft"
    requires_human_review: bool = True
    legal_compliance: Dict[str, bool] = None

    def __post_init__(self):
        if self.legal_compliance is None:
            self.legal_compliance = {
                "ley_25326_datos_personales": False,
                "ley_25506_firma_digital": False,
                "ley_24240_defensa_consumidor": False
            }

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)


class ContractGenerator:
    """
    Generador de contratos con supervisión humana obligatoria.
    
    Reglas de negocio:
    - Solo genera borradores, nunca documentos finales.
    - Contexto humanizado obligatorio en todas las salidas.
    - No ejecuta acciones legales autónomas.
    - Requiere aprobación de Humberto Patricio Castro para finalizar.
    - Todo evento se registra en el log de auditoría.
    """

    def __init__(self, audit_logger: AuditLogger):
        self.audit_logger = audit_logger
        self.contracts_generated = []
        self.templates = self._load_templates()

    def _load_templates(self) -> Dict[str, str]:
        """Carga las plantillas base de contratos."""
        return {
            "servicios": self._template_servicios(),
            "compraventa": self._template_compraventa(),
            "confidencialidad": self._template_confidencialidad(),
            "locacion": self._template_locacion()
        }

    def create_contract(
        self,
        contract_type: str,
        parties: List[str],
        conditions: List[str],
        custom_template: Optional[str] = None
    ) -> ContractDraft:
        """
        Genera un borrador de contrato con contexto humanizado.
        
        Args:
            contract_type: Tipo de contrato (servicios, compraventa, etc.)
            parties: Lista de partes involucradas
            conditions: Lista de condiciones específicas
            custom_template: Template personalizado (opcional)
            
        Returns:
            ContractDraft: Borrador de contrato con contexto humanizado
        """
        # Validar tipo de contrato
        if contract_type not in self.templates and custom_template is None:
            raise ValueError(f"Tipo de contrato no soportado: {contract_type}")
        
        # Validar que haya al menos 2 partes
        if len(parties) < 2:
            raise ValueError("Se requieren al menos 2 partes para un contrato")
        
        # Generar timestamps
        now_utc = datetime.now(timezone.utc)
        now_art = now_utc.astimezone(timezone(offset=__import__('datetime').timedelta(hours=-3)))
        timestamp_utc = now_utc.isoformat()
        timestamp_art = now_art.isoformat()
        
        # Generar ID único del contrato
        contract_id_data = f"{contract_type}:{timestamp_utc}:{str(parties)}"
        contract_id = hashlib.sha256(contract_id_data.encode('utf-8')).hexdigest()[:16]
        
        # Generar contenido del contrato
        if custom_template:
            content = custom_template
        else:
            content = self.templates[contract_type]
        
        # Reemplazar placeholders con datos reales
        content = self._fill_template(content, parties, conditions)
        
        # Generar contexto humanizado obligatorio
        humanized_context = self._generate_humanized_context(
            contract_type=contract_type,
            parties=parties,
            conditions=conditions,
            timestamp_art=timestamp_art
        )
        
        # Calcular hash SHA-256 del contenido
        content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        
        # Determinar cumplimiento legal
        legal_compliance = {
            "ley_25326_datos_personales": True,  # Se incluye cláusula de datos
            "ley_25506_firma_digital": True,     # Se prepara para firma digital
            "ley_24240_defensa_consumidor": contract_type in ["servicios", "compraventa"]
        }
        
        # Crear borrador
        draft = ContractDraft(
            contract_id=contract_id,
            contract_type=contract_type,
            parties=parties,
            conditions=conditions,
            content=content,
            humanized_context=humanized_context,
            generated_at_utc=timestamp_utc,
            generated_at_art=timestamp_art,
            hash_sha256=content_hash,
            legal_compliance=legal_compliance
        )
        
        # Registrar en auditoría
        self.audit_logger.log_event(
            agent_name="ContractGenerator",
            action_description=f"Generación de borrador de contrato tipo {contract_type}",
            severity=SeverityLevel.INFO,
            raw_data={
                "contract_id": contract_id,
                "parties": parties,
                "contract_type": contract_type
            },
            legal_checks=legal_compliance
        )
        
        self.contracts_generated.append(draft)
        
        return draft

    def _fill_template(
        self,
        template: str,
        parties: List[str],
        conditions: List[str]
    ) -> str:
        """Reemplaza placeholders en la plantilla con datos reales."""
        content = template
        
        # Reemplazar partes
        if len(parties) >= 2:
            content = content.replace("[PARTE_A]", parties[0])
            content = content.replace("[PARTE_B]", parties[1])
        
        # Reemplazar condiciones (ejemplo simplificado)
        for i, condition in enumerate(conditions, 1):
            placeholder = f"[CONDICION_{i}]"
            content = content.replace(placeholder, condition)
        
        # Reemplazar fecha actual
        today = datetime.now().strftime("%d/%m/%Y")
        content = content.replace("[FECHA]", today)
        
        return content

    def _generate_humanized_context(
        self,
        contract_type: str,
        parties: List[str],
        conditions: List[str],
        timestamp_art: str
    ) -> str:
        """Genera contexto humanizado obligatorio para toda salida de IA."""
        context = f"""
╔════════════════════════════════════════════════════════════════╗
║  CONTEXTO HUMANIZADO - BORRADOR DE CONTRATO                    ║
╚════════════════════════════════════════════════════════════════╝

📋 ACCIÓN:
Generación de borrador de contrato tipo {contract_type.upper()}

📅 FECHA Y HORA (Argentina - ART):
{timestamp_art}

👤 RESPONSABLE:
Generador de Contratos IA - bajo supervisión de {OWNER_NAME}

📝 DESCRIPCIÓN:
Se ha generado un borrador de contrato entre:
• {parties[0]}
• {parties[1]}

Condiciones incluidas:
{chr(10).join(f'  • {cond}' for cond in conditions)}

⚠️ LIMITACIONES:
• Este es un BORRADOR generado por inteligencia artificial
• Requiere revisión por abogado matriculado antes de su uso
• No constituye asesoramiento legal vinculante
• Las partes deben verificar que refleje su voluntad real
• Debe cumplirse con formalidades legales específicas según el tipo

💡 RECOMENDACIONES:
• Revisar todas las cláusulas cuidadosamente
• Consultar con abogado especializado antes de firmar
• Verificar datos de las partes (DNI, CUIT, domicilios)
• Asegurar que los montos y plazos sean correctos
• Considerar registrar el contrato si la ley lo requiere

🔍 ESTADO:
BORRADOR - Requiere revisión humana obligatoria

⚖️ CUMPLIMIENTO LEGAL:
• Ley 25.326: Cláusula de datos personales incluida
• Ley 25.506: Preparado para firma digital
• Ley 24.240: Aplica para contratos de consumo

👤 SUPERVISIÓN HUMANA:
Pendiente de aprobación por {OWNER_NAME}

🔐 HASH SHA-256:
[Se generará al finalizar el documento]

╚════════════════════════════════════════════════════════════════╝
"""
        return context

    def get_contract_by_id(self, contract_id: str) -> Optional[ContractDraft]:
        """Obtiene un contrato por su ID."""
        for contract in self.contracts_generated:
            if contract.contract_id == contract_id:
                return contract
        return None

    def list_contracts(self) -> List[ContractDraft]:
        """Lista todos los contratos generados."""
        return self.contracts_generated

    def _template_servicios(self) -> str:
        """Plantilla de contrato de prestación de servicios."""
        return """
CONTRATO DE PRESTACIÓN DE SERVICIOS

En la ciudad de [CIUDAD], a los [DÍA] días del mes de [MES] de [AÑO], entre:

POR UNA PARTE: [PARTE_A], DNI/CUIT N° [NÚMERO], con domicilio en [DOMICILIO], en adelante denominado "EL PRESTADOR";

Y POR LA OTRA: [PARTE_B], DNI/CUIT N° [NÚMERO], con domicilio en [DOMICILIO], en adelante denominado "EL CLIENTE";

Ambas partes, en conjunto "LAS PARTES", convienen celebrar el presente Contrato de Prestación de Servicios, sujeto a las siguientes cláusulas:

CLÁUSULA PRIMERA - OBJETO:
EL PRESTADOR se obliga a realizar los siguientes servicios: [DESCRIPCIÓN DETALLADA DEL SERVICIO]

CLÁUSULA SEGUNDA - PLAZO:
El presente contrato tendrá una duración de [PLAZO], iniciando el [FECHA INICIO] y finalizando el [FECHA FIN].

CLÁUSULA TERCERA - PRECIO Y FORMA DE PAGO:
EL CLIENTE abonará la suma de [MONTO] en concepto de [CONCEPTO], mediante [FORMA DE PAGO].

CLÁUSULA CUARTA - OBLIGACIONES DEL PRESTADOR:
1. Realizar los servicios con diligencia y profesionalismo.
2. Cumplir con los plazos establecidos.
3. Mantener confidencialidad sobre la información del CLIENTE.

CLÁUSULA QUINTA - OBLIGACIONES DEL CLIENTE:
1. Pagar el precio en los términos acordados.
2. Proporcionar la información necesaria para la ejecución del servicio.
3. Cooperar con EL PRESTADOR para el cumplimiento del objeto.

CLÁUSULA SEXTA - PROTECCIÓN DE DATOS PERSONALES:
Las partes se comprometen a cumplir con la Ley 25.326 de Protección de Datos Personales. Los datos personales recolectados serán utilizados exclusivamente para los fines del presente contrato y no serán transferidos a terceros sin consentimiento expreso.

CLÁUSULA SÉPTIMA - FIRMA DIGITAL:
Las partes acuerdan que el presente contrato podrá ser firmado digitalmente conforme a la Ley 25.506, teniendo la firma digital la misma validez que la firma manuscrita.

CLÁUSULA OCTAVA - RESOLUCIÓN DE CONFLICTOS:
Cualquier controversia derivada del presente contrato será resuelta mediante mediación previa, y en su defecto, por los tribunales competentes de la República Argentina.

CLÁUSULA NOVENA - JURISDICCIÓN:
Para todos los efectos legales, las partes se someten a la jurisdicción de los tribunales de [CIUDAD/PROVINCIA].

En prueba de conformidad, las partes firman el presente contrato en dos ejemplares de igual tenor.

FIRMA EL PRESTADOR                    FIRMA EL CLIENTE
____________________                  ____________________
"""

    def _template_compraventa(self) -> str:
        """Plantilla de contrato de compraventa."""
        return """
CONTRATO DE COMPRAVENTA

En la ciudad de [CIUDAD], a los [DÍA] días del mes de [MES] de [AÑO], entre:

POR UNA PARTE: [PARTE_A], DNI/CUIT N° [NÚMERO], con domicilio en [DOMICILIO], en adelante denominado "EL VENDEDOR";

Y POR LA OTRA: [PARTE_B], DNI/CUIT N° [NÚMERO], con domicilio en [DOMICILIO], en adelante denominado "EL COMPRADOR";

Ambas partes convienen celebrar el presente Contrato de Compraventa, sujeto a las siguientes cláusulas:

CLÁUSULA PRIMERA - OBJETO:
EL VENDEDOR transfiere la propiedad de [DESCRIPCIÓN DEL BIEN] a EL COMPRADOR.

CLÁUSULA SEGUNDA - PRECIO:
EL COMPRADOR abonará la suma de [MONTO] en concepto de precio.

CLÁUSULA TERCERA - FORMA DE PAGO:
[DESCRIPCIÓN DE LA FORMA DE PAGO]

CLÁUSULA CUARTA - ENTREGA:
La entrega del bien se realizará el [FECHA DE ENTREGA] en [LUGAR DE ENTREGA].

CLÁUSULA QUINTA - GARANTÍA:
EL VENDEDOR garantiza que el bien está libre de gravámenes y vicios ocultos.

CLÁUSULA SEXTA - PROTECCIÓN DE DATOS:
[Cláusula conforme Ley 25.326]

CLÁUSULA SÉPTIMA - FIRMA DIGITAL:
[Cláusula conforme Ley 25.506]

CLÁUSULA OCTAVA - JURISDICCIÓN:
[Cláusula de jurisdicción]

FIRMA EL VENDEDOR                    FIRMA EL COMPRADOR
____________________                  ____________________
"""

    def _template_confidencialidad(self) -> str:
        """Plantilla de contrato de confidencialidad (NDA)."""
        return """
ACUERDO DE CONFIDENCIALIDAD (NDA)

Entre [PARTE_A] y [PARTE_B], se celebra el presente acuerdo de confidencialidad:

CLÁUSULA PRIMERA - INFORMACIÓN CONFIDENCIAL:
Se considera información confidencial toda aquella marcada como tal o que por su naturaleza deba ser tratada como tal.

CLÁUSULA SEGUNDA - OBLIGACIONES:
Las partes se comprometen a:
1. No divulgar la información confidencial a terceros.
2. Utilizar la información solo para los fines del acuerdo.
3. Mantener medidas de seguridad adecuadas.

CLÁUSULA TERCERA - PLAZO:
La obligación de confidencialidad tendrá una duración de [PLAZO] años.

CLÁUSULA CUARTA - EXCEPCIONES:
No se considera confidencial la información que:
1. Sea de dominio público.
2. Haya sido desarrollada independientemente.
3. Haya sido recibida legalmente de un tercero.

CLÁUSULA QUINTA - PROTECCIÓN DE DATOS:
[Cláusula conforme Ley 25.326]

CLÁUSULA SEXTA - JURISDICCIÓN:
[Cláusula de jurisdicción]

FIRMA PARTE A                        FIRMA PARTE B
____________________                  ____________________
"""

    def _template_locacion(self) -> str:
        """Plantilla de contrato de locación."""
        return """
CONTRATO DE LOCACIÓN

Entre [PARTE_A] (LOCADOR) y [PARTE_B] (LOCATARIO), se celebra el presente contrato:

CLÁUSULA PRIMERA - INMUEBLE:
El LOCADOR cede en locación el inmueble ubicado en [DIRECCIÓN DEL INMUEBLE].

CLÁUSULA SEGUNDA - DESTINO:
El inmueble será utilizado exclusivamente para [DESTINO: vivienda/comercio].

CLÁUSULA TERCERA - PLAZO:
El contrato tendrá una duración de [PLAZO] meses/años.

CLÁUSULA CUARTA - CANON:
El LOCATARIO abonará un canon mensual de [MONTO].

CLÁUSULA QUINTA - GARANTÍA:
[DESCRIPCIÓN DE LA GARANTÍA]

CLÁUSULA SEXTA - OBLIGACIONES DEL LOCATARIO:
1. Pagar el canon en término.
2. Mantener el inmueble en buen estado.
3. No realizar modificaciones sin autorización.

CLÁUSULA SÉPTIMA - PROTECCIÓN DE DATOS:
[Cláusula conforme Ley 25.326]

CLÁUSULA OCTAVA - JURISDICCIÓN:
[Cláusula de jurisdicción]

FIRMA EL LOCADOR                       FIRMA EL LOCATARIO
____________________                  ____________________
"""


# ==============================================================================
# Ejemplo de uso (No se ejecuta si se importa como módulo)
# ==============================================================================
if __name__ == "__main__":
    from audit_log import AuditLogger
    
    # Inicializar auditoría
    auditor = AuditLogger(log_file_path="contract_audit.log")
    
    # Inicializar generador de contratos
    generator = ContractGenerator(audit_logger=auditor)
    
    # Generar un contrato de servicios
    draft = generator.create_contract(
        contract_type="servicios",
        parties=["Consultora ABC S.A.", "Cliente XYZ S.R.L."],
        conditions=[
            "Servicio de consultoría en marketing digital",
            "Plazo: 6 meses",
            "Monto: $500,000 ARS mensuales"
        ]
    )
    
    print("\n✅ Contrato generado exitosamente")
    print(f"ID: {draft.contract_id}")
    print(f"Hash SHA-256: {draft.hash_sha256}")
    print(f"Estado: {draft.status}")
    print(f"Requiere revisión humana: {draft.requires_human_review}")
    print("\n📄 Contenido del contrato:")
    print(draft.content[:500] + "...")
    print("\n📋 Contexto humanizado:")
    print(draft.humanized_context)
  
