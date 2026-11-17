# Declaración de Cumplimiento Legal y Ético
# Agencia IA Argentina Segura
# Propietario: Humberto Patricio Castro

**Última actualización**: 17 de noviembre de 2026  
**Versión**: 1.0.0  
**Estado**: Vigente y de cumplimiento obligatorio para todos los módulos del sistema.

---

## 1. IDENTIFICACIÓN DEL RESPONSABLE

El presente documento certifica el compromiso de cumplimiento normativo del proyecto "Agencia IA Argentina Segura".

- **Responsable Legal y Técnico**: Humberto Patricio Castro
- **Cargo**: Director General y Propietario
- **Jurisdicción**: República Argentina
- **Correo de contacto oficial**: [hp.funes.castro@gmail.com]

---

## 2. MARCO NORMATIVO APLICABLE

El sistema ha sido diseñado, desarrollado y operado en estricto cumplimiento de las siguientes normas de la República Argentina:

1. **Ley 25.326**: Protección de los Datos Personales y sus normas reglamentarias (Disposiciones de la AAIP).
2. **Ley 25.506**: Régimen de Firma Digital y Certificados Digitales.
3. **Ley 24.240**: Ley de Defensa del Consumidor y sus modificatorias.
4. **Código Civil y Comercial de la Nación (Ley 26.994)**: Principios generales de los contratos, buena fe y responsabilidad civil.
5. **Constitución Nacional Argentina**: Artículo 43 (Habeas Data) y Artículo 42 (Derechos del consumidor).

---

## 3. MATRIZ DE CUMPLIMIENTO POR MÓDULO

### 3.1 Módulo de Generación de Contratos (IA)
| Requisito Legal | Implementación en el Sistema |
|---|---|
| **Transparencia (Ley 24.240)** | Toda salida de IA incluye un bloque de "Contexto Humanizado" que explica limitaciones y recomienda revisión profesional. |
| **No automatización de decisiones críticas** | El sistema genera exclusivamente **borradores**. La ejecución o firma requiere aprobación explícita de Humberto Patricio Castro. |
| **Validez probatoria** | Los documentos se preparan con estructura apta para firma digital (Ley 25.506), incluyendo hash SHA-256 y marca de tiempo. |

### 3.2 Módulo de Protección de Datos (DPO IA)
| Requisito Legal | Implementación en el Sistema |
|---|---|
| **Consentimiento (Art. 5, Ley 25.326)** | El sistema exige registro de consentimiento expreso antes de procesar datos personales. |
| **Principio de Minimización** | Los agentes de IA están programados para solicitar y procesar solo los datos estrictamente necesarios para la finalidad del contrato. |
| **Derechos ARCO (Art. 14, Ley 25.326)** | Se proveen mecanismos documentados para que los titulares soliciten Acceso, Rectificación, Cancelación u Oposición. |
| **Datos Sensibles (Art. 7, Ley 25.326)** | Requieren un nivel de seguridad crítico y consentimiento expreso y por escrito. El sistema alerta si se detectan sin el protocolo adecuado. |

### 3.3 Módulo de Tokenización y Firma Digital
| Requisito Legal | Implementación en el Sistema |
|---|---|
| **Integridad del documento (Ley 25.506)** | Cálculo automático de hash SHA-256 antes y después de la firma para garantizar que el documento no fue alterado. |
| **Autenticidad** | Vinculación de la firma a un certificado digital emitido por un Certificador Autorizado en Argentina. |
| **Trazabilidad** | Registro inmutable en el log de auditoría de cada paso del proceso de firma. |

### 3.4 Módulo de Auditoría y Trazabilidad
| Requisito Legal | Implementación en el Sistema |
|---|---|
| **Registro de accesos (Disposición AAIP 11/2006)** | Todo acceso, modificación o generación de documento queda registrado con timestamp, agente responsable y supervisor humano. |
| **Conservación de datos** | Los logs de auditoría se conservan por un plazo de 5 años, cumpliendo con los plazos de prescripción comercial y de responsabilidad civil. |

---

## 4. PRINCIPIOS DE IA ÉTICA Y SEGURA

El proyecto adhiere a los principios emergentes de gobernanza de Inteligencia Artificial, garantizando:

1. **Supervisión Humana en el Bucle (Human-in-the-Loop)**: Ningún agente de IA tiene capacidad de ejecución autónoma sobre contratos, firmas o transferencias de datos. Humberto Patricio Castro mantiene el control final.
2. **No Discriminación Algorítmica**: Los prompts y plantillas están diseñados para evitar sesgos en la generación de cláusulas contractuales.
3. **Explicabilidad**: Cada resultado de IA se entrega acompañado de su razonamiento, fuentes (cuando aplica) y limitaciones conocidas.
4. **Seguridad por Diseño**: La encriptación (AES-256) y el hashing (SHA-256) son componentes nativos, no añadidos posteriores.

---

## 5. PROTOCOLO DE RESPUESTA A INCIDENTES

En caso de detectar una vulnerabilidad, brecha de datos o incumplimiento normativo, el sistema activa el siguiente protocolo:

1. **Contención inmediata**: Bloqueo automático de la operación sospechosa.
2. **Notificación interna**: Alerta prioritaria a Humberto Patricio Castro en un plazo máximo de 1 hora.
3. **Evaluación de impacto**: Análisis del alcance de la brecha por el módulo de Auditoría y DPO IA.
4. **Notificación a autoridad**: Si existe riesgo para los derechos de los titulares, se notificará a la Agencia de Acceso a la Información Pública (AAIP) dentro de las 72 horas, conforme a las mejores prácticas internacionales y la normativa local.
5. **Notificación a afectados**: Comunicación clara y sin tecnicismos a los usuarios impactados.

---

## 6. LIMITACIÓN DE RESPONSABILIDAD DEL SOFTWARE OPEN SOURCE

Este proyecto se distribuye bajo licencia **MIT**. Si bien el diseño del sistema cumple con las leyes argentinas:

- El código se proporciona "tal cual" (as-is), sin garantías de ningún tipo.
- Los desarrolladores, colaboradores y el propietario (Humberto Patricio Castro) no se hacen responsables por el uso indebido, ilegal o no supervisado que terceros puedan dar al software una vez desplegado en sus propios entornos.
- Es responsabilidad de quien despliegue el sistema garantizar que su configuración local (certificados digitales, políticas de seguridad) cumpla con la ley.

---

## 7. AUDITORÍA Y VERIFICACIÓN

El cumplimiento de esta declaración está sujeto a:

- Revisiones periódicas del código fuente por parte de la comunidad open source.
- Auditorías internas de los logs del sistema.
- Actualizaciones del marco legal argentino (ej. reglamentación futura de IA).

---

## 8. AUTORIDAD DE APLICACIÓN Y RECLAMOS

Para cualquier consulta, reclamo o ejercicio de derechos relacionados con el cumplimiento legal de este proyecto, el canal oficial es:

- **Responsable**: Humberto Patricio Castro
- **Correo electrónico**: [hp.funes.castro@gmail.com]
- **Autoridad de Control en Protección de Datos**: Agencia de Acceso a la Información Pública (AAIP), www.argentina.gob.ar/aaip
- **Autoridad de Aplicación en Defensa del Consumidor**: Secretaría de Comercio Interior, www.argentina.gob.ar/produccion/defensadelconsumidor

---

*Este documento es una declaración formal de cumplimiento del sistema "Agencia IA Argentina Segura". Su violación por parte de operadores del sistema constituye una falta grave y potencialmente ilegal.*

---

*Propiedad de Humberto Patricio Castro. República Argentina, 2026.*

---

## 9. PROTOCOLO DE AUDITORÍA SEMESTRAL (Ciclo PDCA)

En cumplimiento del principio de mejora continua y para evitar el "hobbling" (sobrerrestricción innecesaria del modelo), el sistema se somete a una auditoría cada **6 meses** con la siguiente metodología:

### 9.1 Categorización de Reglas

| Categoría | Ejemplo | ¿Se puede modificar en auditoría? |
|-----------|---------|-----------------------------------|
| **A. Ley Inmutable** | Supervisión humana obligatoria, hash SHA-256, cláusulas Ley 25.326/25.506/24.240 | ❌ NO. Son requisitos legales argentinos. |
| **B. Regla Operativa** | Temperatura de IA, formato de contexto humanizado, límite de tokens | ✅ SÍ. Se optimizan según evolución del modelo. |
| **C. Regla de Seguridad** | Encriptación AES-256, logs inmutables | ⚠️ Solo para fortalecer, nunca para debilitar. |

### 9.2 Cronograma de Auditoría

| Fecha programada | Responsable | Alcance |
|------------------|-------------|---------|
| 17/05/2027 | Humberto Patricio Castro | Revisión de SECCIÓN 5 de `docs/memoria-agentes.md` |
| 17/11/2027 | Humberto Patricio Castro | Revisión integral + actualización de normativa |
| 17/05/2028 | Humberto Patricio Castro | Revisión de SECCIÓN 5 de `docs/memoria-agentes.md` |

### 9.3 Criterios de Eliminación de Reglas Operativas

Una regla operativa (Categoría B) solo se elimina si cumple **TODOS** estos criterios:
1. El modelo actual ya la cumple por diseño (verificado con pruebas).
2. Su eliminación no afecta ninguna regla de Categoría A o C.
3. La eliminación se documenta en `CHANGELOG.md` y en `docs/memoria-agentes.md`.
4. Humberto Patricio Castro aprueba la eliminación por escrito.

### 9.4 Registro de Auditorías

| Fecha | Tipo | Reglas revisadas | Reglas eliminadas | Aprobación |
|-------|------|------------------|-------------------|------------|
| - | Inaugural | 0 | 0 | Pendiente 17/05/2027 |

---

*Protocolo de auditoría semestral establecido conforme a principios de mejora continua (PDCA) y respetando la inmutabilidad de las obligaciones legales argentinas.*
