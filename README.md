# 🛡️ Agencia IA Argentina Segura

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Compliance](https://img.shields.io/badge/Compliance-Ley_25.326_|_25.506_|_24.240-green.svg)](docs/legal/cumplimiento_legal.md)

Sistema modular de inteligencia artificial para la generación, análisis y gestión de documentos legales con estricto cumplimiento de la legislación de la República Argentina.

> **⚠️ ADVERTENCIA LEGAL:** Este sistema genera exclusivamente **BORRADORES**. Toda acción crítica requiere supervisión humana obligatoria. No reemplaza el asesoramiento de un abogado matriculado.

---

## 👤 Propietario y Responsable Legal

- **Nombre:** Humberto Patricio Castro
- **Cargo:** Director General y Propietario
- **Jurisdicción:** República Argentina

---

## 🎯 Objetivo del Proyecto

Proporcionar una infraestructura de código abierto, segura y auditable para:
1. Automatizar la creación de borradores de contratos con contexto humanizado.
2. Garantizar el cumplimiento de la Ley 25.326 (Datos Personales), Ley 25.506 (Firma Digital) y Ley 24.240 (Defensa del Consumidor).
3. Implementar un sistema de *Human-in-the-Loop* (HITL) donde la IA nunca ejecuta acciones legales autónomas.
4. Proveer trazabilidad inmutable mediante hashing criptográfico (SHA-256) y auditoría estructurada.

---

## 🏗️ Arquitectura del Sistema

```text
┌─────────────────────────────────────────────────────────────────┐
│                    CAPA DE PRESENTACIÓN                          │
│         (Interfaces de usuario, APIs, Webhooks)                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                  CAPA DE ORQUESTACIÓN                            │
│         (Grok Coordinador - Control maestro del sistema)         │
└────────────────────────────┬────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼───────┐  ┌────────▼────────┐  ┌───────▼───────┐
│  CAPA DE IA   │  │  CAPA LEGAL     │  │  CAPA DE      │
│  (Generación) │  │  (Análisis)     │  │  SEGURIDAD    │
│ • Contratos   │  │ • Analista      │  │ • Tokenizador │
│ • Chatbot     │  │ • Compliance    │  │ • Firmante    │
│ • Asistentes  │  │ • DPO           │  │ • Auditor     │
└───────┬───────┘  └────────┬────────┘  └───────┬───────┘
        │                   │                    │
        └───────────────────┼────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────────────┐
│              CAPA DE SUPERVISIÓN HUMANA                          │
│   (Human-in-the-Loop - Humberto Patricio Castro)                 │
└───────────────────────────┬────────────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────────────┐
│              CAPA DE PERSISTENCIA Y AUDITORÍA                    │
│   (Logs inmutables, hashes SHA-256, registros legales)           │
└─────────────────────────────────────────────────────────────────┘
📂 Estructura del Repositorio
agencia-ia-argentina-segura/
├── docs/
│   ├── legal/                  # Documentación de cumplimiento normativo
│   │   ├── politica_privacidad.md
│   │   ├── terminos_uso.md
│   │   ├── cumplimiento_legal.md
│   │   └── ...
│   └── technical/              # Documentación técnica
│       └── arquitectura.md
├── prompts/                    # Prompts maestros de cada agente de IA
│   ├── prompt-grok-coordinador.md
│   ├── prompt-generador-contratos.md
│   ├── prompt-analista-legal.md
│   ├── prompt-tokenizador.md
│   ├── prompt-firmante-digital.md
│   ├── prompt-protector-datos.md
│   └── prompt-auditor.md
├── src/                        # Implementación en Python
│   ├── __init__.py
│   ├── audit_log.py            # Registro inmutable de eventos
│   ├── contract_generator.py   # Generación de borradores
│   └── human_supervisor.py     # Control de aprobación humana (HITL)
├── templates/                  # Plantillas base de contratos
├── config.example.py           # Configuración base (copiar a config.py)
├── requirements.txt            # Dependencias de Python
├── LICENSE                     # Licencia MIT
└── README.md                   # Este archivo
⚖️ Marco Legal de Cumplimiento
Este proyecto está diseñado para operar bajo las siguientes normativas:
Ley
Descripción
Implementación en el Sistema
Ley 25.326
Protección de Datos Personales
Módulo prompt-protector-datos.md, encriptación AES-256, minimización de datos.
Ley 25.506
Firma Digital
Módulo prompt-firmante-digital.md, hashing SHA-256, preparación para certificados autorizados.
Ley 24.240
Defensa del Consumidor
Módulo prompt-analista-legal.md, detección de cláusulas abusivas, derecho de arrepentimiento.
CCyC (Ley 26.994)
Código Civil y Comercial
Plantillas basadas en principios de buena fe, objeto cierto y jurisdicción argentina.
🚀 Instalación y Uso
1. Clonar el repositorio
git clone https://github.com/TU-USUARIO/agencia-ia-argentina-segura.git
cd agencia-ia-argentina-segura
2. Configurar el entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
3. Instalar dependencias
pip install -r requirements.txt
4. Configurar variables de entorno
cp config.example.py config.py
# Edita config.py con tus rutas de certificados y claves de API
5. Ejemplo de uso (Python)
from src.audit_log import AuditLogger, SeverityLevel
from src.contract_generator import ContractGenerator
from src.human_supervisor import HumanSupervisor, DocumentType, SupervisionAction

# 1. Inicializar componentes
auditor = AuditLogger(log_file_path="audit.log")
generator = ContractGenerator(audit_logger=auditor)
supervisor = HumanSupervisor(audit_logger=auditor)

# 2. Generar borrador
draft = generator.create_contract(
    contract_type="servicios",
    parties=["Consultora ABC S.A.", "Cliente XYZ S.R.L."],
    conditions=["Plazo: 6 meses", "Monto: $500,000 ARS"]
)

# 3. Enviar a supervisión humana
review_id = supervisor.submit_for_review(
    document_id=draft.contract_id,
    document_type=DocumentType.CONTRACT,
    content=draft.content,
    metadata={"hash": draft.hash_sha256}
)

# 4. Aprobar (Simulación de acción de Humberto Patricio Castro)
decision = supervisor.review_and_decide(
    review_id=review_id,
    supervisor_name="Humberto Patricio Castro",
    action=SupervisionAction.APPROVED,
    comments="Revisado y aprobado conforme a la legislación vigente."
)

print(f"✅ Contrato aprobado. Hash final: {decision.new_hash}")
🔒 Seguridad y Auditoría
Trazabilidad: Cada acción genera un AuditRecord con hash SHA-256 inmutable.
No Repudio: Los registros de supervisión humana vinculan criptográficamente la decisión al supervisor.
Minimización: Los datos sensibles nunca se almacenan en texto plano en los logs de auditoría.
🤝 Contribuciones
Las contribuciones son bienvenidas bajo los siguientes principios:
Todo cambio debe mantener o mejorar el cumplimiento legal argentino.
Ningún cambio puede eliminar la supervisión humana obligatoria.
Los nuevos agentes de IA deben incluir su propio prompt maestro en /prompts.
📄 Licencia
Distribuido bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
Este proyecto es propiedad de Humberto Patricio Castro. República Argentina, 2026.

## 🎯 PASO 4: Guardar (Commit)
1. Haz clic en **"Commit changes..."**.
2. Escribe: `Actualizar README.md con arquitectura, instalación y marco legal completo`
3. Clic en **"Commit changes"**.

---

# 📄 ARCHIVO 19: `templates/contrato_servicios.md`

## 🎯 PASO 1: Crear el archivo
1. Haz clic en **"Add file"** → **"Create new file"**.
2. Escribe exactamente:
```text
templates/contrato_servicios.md
# CONTRATO DE PRESTACIÓN DE SERVICIOS PROFESIONALES

**Fecha:** [FECHA]  
**Lugar:** [CIUDAD], República Argentina

---

## ENTRE LAS PARTES

Por una parte, **[NOMBRE COMPLETO O RAZÓN SOCIAL DEL PRESTADOR]**, DNI/CUIT N° [NÚMERO], con domicilio legal en [DOMICILIO COMPLETO], en adelante denominado "**EL PRESTADOR**";

Y por la otra, **[NOMBRE COMPLETO O RAZÓN SOCIAL DEL CLIENTE]**, DNI/CUIT N° [NÚMERO], con domicilio legal en [DOMICILIO COMPLETO], en adelante denominado "**EL CLIENTE**";

Ambas partes, en conjunto "LAS PARTES", convienen celebrar el presente Contrato de Prestación de Servicios, sujeto a las siguientes cláusulas:

---

## CLÁUSULAS

### PRIMERA: OBJETO
EL PRESTADOR se obliga a realizar a favor de EL CLIENTE los siguientes servicios:  
[DESCRIPCIÓN DETALLADA, CLARA Y ESPECÍFICA DE LOS SERVICIOS A PRESTAR].

### SEGUNDA: PLAZO DE EJECUCIÓN
El presente contrato tendrá una duración de [PLAZO, ej: seis (6) meses], iniciando el [FECHA DE INICIO] y finalizando el [FECHA DE FINALIZACIÓN], salvo rescisión anticipada conforme a la Cláusula Séptima.

### TERCERA: HONORARIOS Y FORMA DE PAGO
EL CLIENTE abonará a EL PRESTADOR la suma total de [MONTO EN NÚMEROS] ([MONTO EN LETRAS] PESOS ARGENTINOS) en concepto de contraprestación por los servicios.  
El pago se realizará de la siguiente manera: [DESCRIBIR FORMA DE PAGO, ej: 50% al inicio y 50% contra entrega final, mediante transferencia bancaria a la CBU N° XXX].

### CUARTA: OBLIGACIONES DE EL PRESTADOR
1. Realizar los servicios con la diligencia, profesionalismo y estándar de cuidado propios de su actividad.
2. Cumplir con los plazos establecidos en la Cláusula Segunda.
3. Mantener estricta confidencialidad sobre la información de EL CLIENTE a la que tenga acceso.
4. Emitir los comprobantes fiscales correspondientes (Factura) por los pagos recibidos.

### QUINTA: OBLIGACIONES DE EL CLIENTE
1. Abonar los honorarios en los términos y plazos pactados.
2. Proporcionar a EL PRESTADOR toda la información, documentación y acceso necesario para la ejecución de los servicios.
3. Designar un interlocutor válido para la toma de decisiones durante la vigencia del contrato.

### SEXTA: PROTECCIÓN DE DATOS PERSONALES (Ley 25.326)
LAS PARTES declaran que cumplirán estrictamente con la Ley 25.326 de Protección de Datos Personales y las disposiciones de la Agencia de Acceso a la Información Pública (AAIP). Los datos personales intercambiados serán utilizados exclusivamente para el cumplimiento de este contrato, no serán cedidos a terceros sin consentimiento expreso, y se implementarán las medidas de seguridad técnicas y organizativas adecuadas para protegerlos.

### SÉPTIMA: RESCISIÓN
Cualquiera de LAS PARTES podrá rescindir el presente contrato de manera anticipada, notificando a la otra parte por escrito con una antelación mínima de [ej: treinta (30)] días corridos. En caso de rescisión, EL CLIENTE abonará a EL PRESTADOR la parte proporcional de los servicios efectivamente prestados hasta la fecha de finalización.

### OCTAVA: INDEPENDENCIA CONTRACTUAL
EL PRESTADOR actúa como un contratista independiente. Nada en este contrato se interpretará como la creación de una relación laboral, sociedad o joint venture entre LAS PARTES.

### NOVENA: PROPIEDAD INTELECTUAL
[Seleccionar una opción:]  
- Opción A: Todos los derechos de propiedad intelectual sobre los entregables finales serán transferidos a EL CLIENTE una vez abonado el total de los honorarios.  
- Opción B: EL PRESTADOR retiene la propiedad intelectual de sus metodologías y herramientas preexistentes, otorgando a EL CLIENTE una licencia de uso no exclusiva y perpetua para los fines del proyecto.

### DÉCIMA: FIRMA DIGITAL (Ley 25.506)
LAS PARTES acuerdan que el presente contrato podrá ser firmado mediante firma digital, la cual tendrá la misma validez y eficacia probatoria que la firma ológrafa, conforme al artículo 2 de la Ley 25.506 y sus normas reglamentarias. El documento final será protegido mediante hash SHA-256 para garantizar su integridad.

### UNDÉCIMA: LEY APLICABLE Y JURISDICCIÓN
Para todos los efectos legales derivados del presente contrato, LAS PARTES se someten a las leyes de la República Argentina y a la jurisdicción de los tribunales ordinarios en lo Comercial de la Ciudad Autónoma de Buenos Aires, renunciando a cualquier otro fuero o jurisdicción que pudiera corresponderles.

---

En prueba de conformidad, LAS PARTES firman el presente contrato en dos (2) ejemplares de un mismo tenor y a un solo efecto, en la fecha y lugar indicados en el encabezado.

<br>
<br>

_____________________________  
**FIRMA EL PRESTADOR**  
Nombre:  
DNI/CUIT:  

<br>
<br>

_____________________________  
**FIRMA EL CLIENTE**  
Nombre:  
DNI/CUIT:  

---
*Documento generado como borrador por Agencia IA Argentina Segura. Requiere revisión y aprobación final por Humberto Patricio Castro antes de su ejecución.*

---

## 🧪 Ejecución y Pruebas (Demo en Vivo)

El proyecto es **100% ejecutable**. Para verificarlo:

### Demo completa del sistema
```bash
python main.py --demo
Esto ejecuta el flujo completo: generación de contrato → supervisión humana → verificación de integridad → informe de cumplimiento.
Verificar integridad de un archivo
python main.py --verify --archivo templates/contrato_servicios.md --hash <hash_sha256>
Ver el system prompt de runtime (conciso)
python main.py --prompt
Ejecutar pruebas unitarias
pytest tests/ -v
Separación documentación vs. runtime (Consejo 5)
Documentación completa (sin límite de palabras): /prompts/*.md, /docs/
System prompt de runtime (conciso, optimizado para tokens): definido en main.py como SYSTEM_PROMPT_RUNTIME
Memoria unificada y evolución (Consejos 2, 3, 4)
Segundo cerebro: docs/memoria-agentes.md
Registro de cambios: CHANGELOG.md
Auditoría semestral: Sección 9 de docs/legal/cumplimiento_legal.md
📈 Roadmap y Contribuciones
Próximas versiones
Integración con API de Anthropic Claude
Interfaz web con Streamlit
Módulo de firma digital con certificados reales
Soporte multi-jurisdicción (LATAM)
Cómo contribuir
Fork el repositorio.
Crea una rama: git checkout -b feature/tu-feature.
Abre un Issue describiendo el cambio.
Envía un Pull Request con pruebas.
Proyecto desarrollado y mantenido por Humberto Patricio Castro. República Argentina, 2026.
Licensed under MIT License.
