"""
Configuración del Sistema - Agencia IA Argentina Segura
Propietario: Humberto Patricio Castro

INSTRUCCIONES:
1. Copiar este archivo como 'config.py' (no subir a Git).
2. Completar las credenciales y rutas.
3. Nunca compartir el archivo 'config.py' real.
"""

# ==============================================================================
# 1. IDENTIDAD Y PROPIEDAD
# ==============================================================================
OWNER_NAME = "Humberto Patricio Castro"
OWNER_ROLE = "Director General y Propietario"
PROJECT_NAME = "Agencia IA Argentina Segura"
VERSION = "1.0.0"

# ==============================================================================
# 2. CONFIGURACIÓN LEGAL (Leyes Argentinas)
# ==============================================================================
LEGAL_FRAMEWORK = {
    "data_protection": "Ley 25.326",
    "digital_signature": "Ley 25.506",
    "consumer_defense": "Ley 24.240",
    "civil_code": "Ley 26.994 (CCyC)"
}

# Jurisdicción por defecto
DEFAULT_JURISDICTION = "Ciudad Autónoma de Buenos Aires, Argentina"

# ==============================================================================
# 3. SEGURIDAD Y CRIPTOGRAFÍA
# ==============================================================================
# Algoritmos aprobados
HASH_ALGORITHM = "SHA-256"
ENCRYPTION_ALGORITHM = "AES-256-GCM"
SIGNATURE_ALGORITHM = "RSA-2048"

# Rutas de certificados (Ley 25.506)
# IMPORTANTE: Usar solo certificadores autorizados por la Secretaría de Gobierno
DIGITAL_CERTIFICATE_PATH = "./certs/certificate.p12"
PRIVATE_KEY_PATH = "./certs/private_key.pem"
CERTIFICATE_PASSWORD_ENV_VAR = "CERT_PASSWORD"  # No hardcodear contraseñas

# ==============================================================================
# 4. PROTECCIÓN DE DATOS (Ley 25.326)
# ==============================================================================
DATA_RETENTION_DAYS = 365 * 5  # 5 años para auditoría legal
DATA_ENCRYPTION_AT_REST = True
DATA_ENCRYPTION_IN_TRANSIT = True
REQUIRE_EXPLICIT_CONSENT = True

# Contacto para ejercicios de derechos ARCO
DPO_EMAIL = "dpo@agencia-ia-argentina-segura.com.ar"

# ==============================================================================
# 5. IA Y SUPERVISIÓN HUMANA
# ==============================================================================
# La IA nunca actúa autónomamente en decisiones críticas
HUMAN_IN_THE_LOOP_REQUIRED = True
AUTHORIZED_SUPERVISORS = [
    "Humberto Patricio Castro"
]

# Configuración del modelo de IA (ej. Anthropic Claude)
AI_PROVIDER = "anthropic"
AI_MODEL = "claude-3-sonnet-20240229"
AI_MAX_TOKENS = 4096
AI_TEMPERATURE = 0.2  # Baja temperatura para mayor precisión legal

# ==============================================================================
# 6. AUDITORÍA Y LOGS
# ==============================================================================
AUDIT_LOG_ENABLED = True
AUDIT_LOG_FILE = "logs/audit_log.jsonl"
AUDIT_LOG_RETENTION_DAYS = 1825  # 5 años
ALERT_CRITICAL_EVENTS = True  # Notificar inmediatamente al propietario

# ==============================================================================
# 7. ENTORNO
# ==============================================================================
ENVIRONMENT = "development"  # development, staging, production
DEBUG = False
SECRET_KEY_ENV_VAR = "APP_SECRET_KEY"
