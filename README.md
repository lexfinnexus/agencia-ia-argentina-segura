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
│   ├── technical/              # Documentación técnica
│   │   └── arquitectura.md
│   └── memoria-agentes.md      # Segundo cerebro del sistema
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
│   └── contrato_servicios.md
├── tests/                      # Pruebas unitarias
│   └── test_audit_log.py
├── config.example.py           # Configuración base (copiar a config.py)
├── main.py                     # Punto de entrada ejecutable
├── requirements.txt            # Dependencias de Python
├── CHANGELOG.md                # Registro de cambios
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
🧪 Ejecución y Pruebas (Demo en Vivo)
El proyecto es 100% ejecutable. Para verificarlo:
Demo completa del sistema
python main.py --demo
Esto ejecuta el flujo completo: generación de contrato → supervisión humana → verificación de integridad → informe de cumplimiento.
Verificar integridad de un archivo
Ver el system prompt de runtime (conciso)
python main.py --prompt
Ejecutar pruebas unitarias
pytest tests/ -v
Separación documentación vs. runtime
Documentación completa (sin límite de palabras): /prompts/*.md, /docs/
System prompt de runtime (conciso, optimizado para tokens): definido en main.py como SYSTEM_PROMPT_RUNTIME
Memoria unificada y evolución
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
📄 Licencia
Distribuido bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
Proyecto desarrollado y mantenido por Humberto Patricio Castro. República Argentina, 2026.
Licensed under MIT License.
