# Arquitectura del Sistema
# Agencia IA Argentina Segura
# Propietario: Humberto Patricio Castro

**Versión**: 1.0.0  
**Última actualización**: 17 de noviembre de 2026

---

## 1. Visión General

"Agencia IA Argentina Segura" es un sistema modular de inteligencia artificial diseñado para la generación, análisis y gestión de documentos legales con estricto cumplimiento de la legislación argentina.

**Principio fundamental**: La IA actúa únicamente como asistente. Toda decisión crítica requiere supervisión humana obligatoria de Humberto Patricio Castro.

---

## 2. Arquitectura de Capas

─────────────────────────────────────────────────────────────────┐
│ CAPA DE PRESENTACIÓN │
│ (Interfaces de usuario, APIs, Webhooks) │
└────────────────────────────┬────────────────────────────────────┘
│
┌────────────────────────────▼────────────────────────────────────┐
│ CAPA DE ORQUESTACIÓN │
│ (Grok Coordinador - Control maestro del sistema) │
└────────────────────────────┬────────────────────────────────────┘
│
┌────────────────────┼────────────────────┐
│ │ │
┌───────▼───────┐ ┌────────▼────────┐ ┌───────▼───────┐
│ CAPA DE IA │ │ CAPA LEGAL │ │ CAPA DE │
│ (Generación) │ │ (Análisis) │ │ SEGURIDAD │
│ │ │ │ │ │
│ • Contratos │ │ • Analista │ │ • Tokenizador │
│ • Chatbot │ │ • Compliance │ │ • Firmante │
│ • Asistentes │ │ • DPO │ │ • Auditor │
└───────┬───────┘ └────────┬────────┘ └───────┬───────┘
│ │ │
└───────────────────┼────────────────────┘
│
┌───────────────────────────▼────────────────────────────────────┐
│ CAPA DE SUPERVISIÓN HUMANA │
│ (Human-in-the-Loop - Humberto Patricio Castro) │
└───────────────────────────┬────────────────────────────────────┘
│
┌───────────────────────────▼────────────────────────────────────┐
│ CAPA DE PERSISTENCIA Y AUDITORÍA │
│ (Logs inmutables, hashes SHA-256, registros legales) │
└─────────────────────────────────────────────────────────────────┘


---

## 3. Módulos del Sistema

### 3.1 Capa de Prompts (`/prompts`)

Cada agente de IA está definido por un prompt maestro que establece su identidad, reglas y límites.

| Archivo | Rol | Responsabilidad Principal |
|---|---|---|
| `prompt-grok-coordinador.md` | Coordinador General | Orquestar todos los agentes |
| `prompt-generador-contratos.md` | Generador | Crear borradores de contratos |
| `prompt-analista-legal.md` | Analista | Validar cumplimiento normativo |
| `prompt-tokenizador.md` | Tokenizador | Generar hashes y tokens únicos |
| `prompt-firmante-digital.md` | Firmante | Gestionar firma digital (Ley 25.506) |
| `prompt-protector-datos.md` | DPO | Protección de datos (Ley 25.326) |
| `prompt-auditor.md` | Auditor | Trazabilidad inmutable |
| `prompt-chatbot-whatsapp.md` | Chatbot | Interfaz conversacional |

### 3.2 Capa de Código (`/src`)

Implementación Python de los módulos críticos:

| Módulo | Función |
|---|---|
| `audit_log.py` | Registro inmutable de eventos con hash SHA-256 |
| `contract_generator.py` | Generación de borradores con plantillas |
| `human_supervisor.py` | Control de aprobación humana obligatoria |
| `__init__.py` | Paquete principal del sistema |

### 3.3 Capa Legal (`/docs/legal`)

Documentación de cumplimiento normativo:

| Documento | Ley Aplicable |
|---|---|
| `politica_privacidad.md` | Ley 25.326 |
| `terminos_uso.md` | Ley 24.240 |
| `cumplimiento_legal.md` | Marco integral |
| `escudo-legal-y-descargo.md` | Limitación de responsabilidad |
| `organigrama-agentes-y-pdca.md` | Estructura organizacional |

---

## 4. Flujo de Datos Principal

### 4.1 Generación de Contrato (Caso de Uso Principal)
USUARIO solicita generación de contrato
│
▼
GROK COORDINADOR recibe la solicitud
│
▼
GENERADOR DE CONTRATOS crea borrador
├── Aplica plantilla legal
├── Incluye cláusulas Ley 25.326, 25.506, 24.240
└── Agrega contexto humanizado obligatorio
│
▼
ANALISTA LEGAL revisa el borrador
├── Verifica cumplimiento normativo
├── Detecta riesgos (Alto/Medio/Bajo)
└── Genera informe de análisis
│
▼
TOKENIZADOR calcula hash SHA-256
├── Genera token único
└── Registra marca de tiempo
│
▼
SUPERVISOR HUMANO (Humberto Patricio Castro)
├── Revisa borrador + análisis + hash
├── Aprueba, rechaza o modifica
└── Firma digital (Ley 25.506)
│
▼
AUDITOR registra toda la trazabilidad
├── Log inmutable con hash
└── Certificado de existencia
│
▼
DOCUMENTO FINAL firmado y almacenado

---

## 5. Modelo de Seguridad

### 5.1 Principios de Diseño

1. **Supervisión Humana Obligatoria (HITL)**: Ninguna acción crítica se ejecuta sin aprobación.
2. **Defensa en Profundidad**: Múltiples capas de validación.
3. **Mínimo Privilegio**: Cada agente solo accede a lo necesario.
4. **Trazabilidad Total**: Todo evento queda registrado con hash.
5. **No Repudio**: Firmas digitales garantizan autoría.

### 5.2 Criptografía Aplicada

| Componente | Algoritmo | Uso |
|---|---|---|
| Integridad de documentos | SHA-256 | Hash de contratos y logs |
| Encriptación en reposo | AES-256-GCM | Datos sensibles |
| Encriptación en tránsito | TLS 1.3 | Comunicaciones |
| Firma digital | RSA-2048 + SHA-256 | Validez legal (Ley 25.506) |
| Tokens únicos | UUID v4 | Identificación sin revelar datos |

### 5.3 Control de Acceso

┌─────────────────────────────────────┐
│ Humberto Patricio Castro │ ← Nivel FULL (Propietario)
│ (Director General y Propietario) │
└──────────────────┬──────────────────┘
│
┌──────────────┼──────────────┐
▼ ▼ ▼
┌────────┐ ┌──────────┐ ┌──────────┐
│Agente 1│ │ Agente 2 │ │ Agente N │ ← Solo generan borradores
└────────┘ └──────────┘ └──────────┘

---

## 6. Cumplimiento Normativo por Módulo

### Ley 25.326 - Protección de Datos Personales
- **Módulo responsable**: `prompt-protector-datos.md`
- **Controles**: Consentimiento, minimización, derechos ARCO, encriptación

### Ley 25.506 - Firma Digital
- **Módulo responsable**: `prompt-firmante-digital.md`
- **Controles**: Certificado autorizado, hash SHA-256, timestamp

### Ley 24.240 - Defensa del Consumidor
- **Módulo responsable**: `prompt-analista-legal.md`
- **Controles**: Cláusulas no abusivas, derecho de arrepentimiento, información clara

---

## 7. Diagrama de Componentes

                ┌─────────────────┐
                │   USUARIO FINAL  │
                └────────┬────────┘
                         │
                ┌────────▼────────┐
                │  API / INTERFAZ  │
                └────────┬────────┘
                         │
                ┌────────▼────────┐
                │  GROK COORDINADOR│
                └──┬─────┬─────┬──┘
                   │     │     │
      ┌────────────┘     │     └────────────┐
      ▼                  ▼                  ▼
      ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ GENERADOR │ │ ANALISTA │ │ TOKENIZ. │
│ CONTRATOS │ │ LEGAL │ │ │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
│ │ │
└─────────────────┼──────────────────┘
│
┌────────▼────────┐
│ SUPERVISOR │
│ HUMANO (HPC) │
└────────┬────────┘
│
┌────────▼────────┐
│ AUDITOR │
│ (Log Inmutable)│
└────────┬────────┘
│
┌────────▼────────┐
│ ALMACENAMIENTO │
│ SEGURO │
└─────────────────┘

---

## 8. Decisiones de Diseño Clave

### 8.1 ¿Por qué prompts en lugar de código para la IA?
- **Flexibilidad**: Los prompts se pueden actualizar sin redeploy.
- **Transparencia**: Cualquiera puede auditar el comportamiento de la IA.
- **Cumplimiento**: Las reglas legales están explícitas y versionadas.

### 8.2 ¿Por qué logs inmutables con hash?
- **Validez legal**: Cumple requisitos de prueba digital.
- **No repudio**: Imposible alterar registros sin detectarlo.
- **Auditoría**: Trazabilidad completa para autoridades.

### 8.3 ¿Por qué supervisión humana obligatoria?
- **Responsabilidad legal**: Evita que la IA tome decisiones autónomas.
- **Calidad**: Revisión profesional de cada documento.
- **Ética**: Alineación con principios de IA responsable.

---

## 9. Roadmap Técnico

### Fase 1 (Completada) ✅
- [x] Definición de prompts de agentes
- [x] Documentación legal base
- [x] Módulos core de Python
- [x] Sistema de auditoría

### Fase 2 (En progreso) 🔄
- [ ] Integración con API de Anthropic Claude
- [ ] Módulo de firma digital completo
- [ ] Interfaz web de usuario
- [ ] Tests unitarios y de integración

### Fase 3 (Planificada) 📋
- [ ] Despliegue en producción
- [ ] Certificación de seguridad
- [ ] Auditoría externa
- [ ] Escalado a múltiples jurisdicciones

---

## 10. Referencias Técnicas

- **Python**: 3.10+
- **Dependencias**: Ver `requirements.txt`
- **Configuración**: Ver `config.example.py`
- **Licencia**: MIT (ver `LICENSE`)

---

*Este documento forma parte del sistema "Agencia IA Argentina Segura" y está sujeto a las leyes de la República Argentina.*

*Propiedad de Humberto Patricio Castro. 2026.*
