# Registro de Cambios (Changelog)
# Agencia IA Argentina Segura
# Propietario: Humberto Patricio Castro

Este archivo documenta todos los cambios notables del proyecto, siguiendo el formato [Keep a Changelog](https://keepachangelog.com/es/).

---

## [1.0.0] - 2026-11-17

### 🎉 Lanzamiento inicial

#### Agregado
- **Capa de Prompts (8 agentes)**:
  - `prompt-grok-coordinador.md`: Coordinador maestro del sistema.
  - `prompt-generador-contratos.md`: Generación de borradores legales.
  - `prompt-analista-legal.md`: Análisis de cumplimiento normativo.
  - `prompt-tokenizador.md`: Hash SHA-256 y tokens únicos.
  - `prompt-firmante-digital.md`: Gestión de firma digital (Ley 25.506).
  - `prompt-protector-datos.md`: DPO conforme Ley 25.326.
  - `prompt-auditor.md`: Trazabilidad inmutable.
  - `prompt-chatbot-whatsapp.md`: Interfaz conversacional.

- **Capa de Código Python (`src/`)**:
  - `audit_log.py`: Registro inmutable con hash SHA-256.
  - `contract_generator.py`: Generador de borradores con plantillas.
  - `human_supervisor.py`: Control HITL obligatorio.
  - `__init__.py`: Paquete principal.

- **Capa Legal (`docs/legal/`)**:
  - `politica_privacidad.md`: Conforme Ley 25.326.
  - `terminos_uso.md`: Conforme Ley 24.240.
  - `cumplimiento_legal.md`: Matriz de cumplimiento integral.
  - `escudo-legal-y-descargo.md`: Limitación de responsabilidad.
  - `organigrama-agentes-y-pdca.md`: Modelo de gobierno.
  - `protocolo-humanizacion-y-contratos-tokenizados.md`: Protocolo operativo.

- **Capa Técnica (`docs/technical/`)**:
  - `arquitectura.md`: Diagramas y decisiones de diseño.

- **Memoria y Evolución**:
  - `docs/memoria-agentes.md`: Segundo cerebro del sistema.
  - `CHANGELOG.md`: Este archivo.

- **Plantillas (`templates/`)**:
  - `contrato_servicios.md`: Plantilla base conforme legislación argentina.

- **Pruebas (`tests/`)**:
  - `test_audit_log.py`: Pruebas unitarias del módulo de auditoría.

- **Configuración**:
  - `config.example.py`: Configuración base.
  - `requirements.txt`: Dependencias Python.
  - `LICENSE`: Licencia MIT.
  - `README.md`: Documentación principal.
  - `registro-de-auditoria.md`: Log histórico.

#### Cumplimiento Legal
- Ley 25.326 (Protección de Datos Personales): ✅ Implementado.
- Ley 25.506 (Firma Digital): ✅ Implementado.
- Ley 24.240 (Defensa del Consumidor): ✅ Implementado.
- Código Civil y Comercial (Ley 26.994): ✅ Referenciado.

#### Arquitectura
- Patrón Human-in-the-Loop (HITL) obligatorio.
- Supervisor humano: Humberto Patricio Castro (único aprobador final).
- Hash SHA-256 en todos los documentos críticos.
- Logs inmutables en formato JSONL.

---

## Plantilla para futuras versiones

[X.Y.Z] - YYYY-MM-DD
Agregado
[Nuevas funcionalidades]
Modificado
[Cambios en funcionalidades existentes]
Corregido
[Bugs resueltos, referenciando Issue #]
Eliminado
[Funcionalidades removidas]
Seguridad
[Parches o mejoras de seguridad]

---

*Este archivo es parte del sistema "Agencia IA Argentina Segura".*
*Propiedad de Humberto Patricio Castro. 2026.*
