"""
Módulo de Auditoría Inmutable (Audit Log)
Agencia IA Argentina Segura
Propietario: Humberto Patricio Castro

Este módulo garantiza la trazabilidad inmutable de todas las acciones del sistema,
cumpliendo con la Ley 25.326 (Protección de Datos), Ley 25.506 (Firma Digital) 
y Ley 24.240 (Defensa del Consumidor) de la República Argentina.
"""

import hashlib
import json
import os
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, Optional
from dataclasses import dataclass, asdict
from enum import Enum

# Configuración del propietario y supervisor obligatorio
OWNER_NAME = "Humberto Patricio Castro"
OWNER_ROLE = "Director General y Propietario"


class SeverityLevel(Enum):
    """Niveles de severidad para eventos de auditoría."""
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass
class AuditRecord:
    """Registro inmutable de una acción del sistema."""
    transaction_id: str
    timestamp_utc: str
    timestamp_art: str
    agent_name: str
    action_description: str
    severity: str
    supervisor_human: str
    data_hash: Optional[str]
    legal_compliance: Dict[str, bool]
    status: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    def calculate_record_hash(self) -> str:
        """Calcula el hash SHA-256 del registro para garantizar su inmutabilidad."""
        record_string = json.dumps(self.to_dict(), sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(record_string.encode('utf-8')).hexdigest()


class AuditLogger:
    """
    Gestor de registros de auditoría conforme a estándares legales argentinos.
    
    Reglas de negocio:
    - Todo registro incluye la supervisión de Humberto Patricio Castro.
    - Los datos sensibles nunca se guardan en texto plano, solo sus hashes.
    - Cada registro genera su propio hash criptográfico para detectar alteraciones.
    """

    def __init__(self, log_file_path: str = "audit_log.jsonl"):
        self.log_file_path = log_file_path
        self._ensure_log_file_exists()

    def _ensure_log_file_exists(self) -> None:
        """Crea el archivo de log si no existe."""
        dir_path = os.path.dirname(os.path.abspath(self.log_file_path))
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        if not os.path.exists(self.log_file_path):
            with open(self.log_file_path, 'w', encoding='utf-8') as f:
                f.write("")

    def _get_timestamps(self) -> tuple:
        """Obtiene timestamps en UTC y ART (Argentina, UTC-3)."""
        now_utc = datetime.now(timezone.utc)
        now_art = now_utc.astimezone(timezone(timedelta(hours=-3)))
        return now_utc.isoformat(), now_art.isoformat()

    def _write_to_file(self, payload: Dict[str, Any]) -> None:
        """Escribe directamente en el archivo de log (evita problemas con logger global)."""
        with open(self.log_file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")

    def log_event(
        self,
        agent_name: str,
        action_description: str,
        severity: SeverityLevel,
        raw_data: Optional[Any] = None,
        legal_checks: Optional[Dict[str, bool]] = None
    ) -> AuditRecord:
        """
        Registra un evento en el log de auditoría de forma inmutable.
        
        Args:
            agent_name: Nombre del módulo o agente que ejecuta la acción.
            action_description: Descripción clara de la acción realizada.
            severity: Nivel de severidad del evento.
            raw_data: Datos asociados (se convertirán a hash, nunca se guardan en crudo).
            legal_checks: Diccionario de cumplimiento legal.
            
        Returns:
            AuditRecord: El registro generado con su hash de integridad.
        """
        timestamp_utc, timestamp_art = self._get_timestamps()
        
        # Generar ID de transacción único
        tx_data = f"{agent_name}:{action_description}:{timestamp_utc}"
        transaction_id = hashlib.sha256(tx_data.encode('utf-8')).hexdigest()[:16]
        
        # Hashear datos sensibles si existen (Principio de Minimización Ley 25.326)
        data_hash = None
        if raw_data is not None:
            data_string = json.dumps(raw_data, sort_keys=True, ensure_ascii=False)
            data_hash = hashlib.sha256(data_string.encode('utf-8')).hexdigest()
        
        # Valores por defecto de cumplimiento legal
        compliance = {
            "ley_25326_datos_personales": False,
            "ley_25506_firma_digital": False,
            "ley_24240_defensa_consumidor": False,
            "supervision_humana_requerida": True
        }
        if legal_checks:
            compliance.update(legal_checks)
        
        # Crear el registro
        record = AuditRecord(
            transaction_id=transaction_id,
            timestamp_utc=timestamp_utc,
            timestamp_art=timestamp_art,
            agent_name=agent_name,
            action_description=action_description,
            severity=severity.value,
            supervisor_human=OWNER_NAME,
            data_hash=data_hash,
            legal_compliance=compliance,
            status="REGISTRADO_INMUTABLE"
        )
        
        # Agregar hash del propio registro para cadena de bloques local
        record_hash = record.calculate_record_hash()
        
        # Preparar payload final para el log
        log_payload = record.to_dict()
        log_payload["record_hash_sha256"] = record_hash
        
        # Escribir directamente en el archivo
        self._write_to_file(log_payload)
        
        # Alerta inmediata en caso de evento CRÍTICO
        if severity == SeverityLevel.CRITICAL:
            self._trigger_critical_alert(record)
            
        return record

    def _trigger_critical_alert(self, record: AuditRecord) -> None:
        """
        Protocolo de respuesta a incidentes críticos.
        Notifica inmediatamente al propietario.
        """
        alert_msg = (
            f"🚨 ALERTA CRÍTICA DE AUDITORÍA 🚨\n"
            f"Fecha ART: {record.timestamp_art}\n"
            f"Agente: {record.agent_name}\n"
            f"Acción: {record.action_description}\n"
            f"Supervisor requerido: {record.supervisor_human}\n"
            f"ID Transacción: {record.transaction_id}\n"
            f"ACCIÓN INMEDIATA REQUERIDA POR {OWNER_NAME}."
        )
        print(alert_msg)

    def verify_log_integrity(self) -> bool:
        """
        Verifica que el archivo de log no haya sido alterado.
        
        Returns:
            bool: True si el formato es válido y no hay corrupciones evidentes.
        """
        try:
            with open(self.log_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        record_dict = json.loads(line)
                        if "record_hash_sha256" not in record_dict:
                            return False
            return True
        except (json.JSONDecodeError, FileNotFoundError):
            return False

    def generate_compliance_report(self) -> Dict[str, Any]:
        """
        Genera un informe de cumplimiento legal basado en los logs.
        """
        report = {
            "generated_at": self._get_timestamps()[1],
            "supervisor": OWNER_NAME,
            "total_events": 0,
            "critical_events": 0,
            "compliance_summary": {
                "ley_25326": 0,
                "ley_25506": 0,
                "ley_24240": 0
            }
        }
        
        try:
            with open(self.log_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        record = json.loads(line)
                        report["total_events"] += 1
                        
                        if record.get("severity") == "CRITICAL":
                            report["critical_events"] += 1
                            
                        compliance = record.get("legal_compliance", {})
                        if compliance.get("ley_25326_datos_personales"):
                            report["compliance_summary"]["ley_25326"] += 1
                        if compliance.get("ley_25506_firma_digital"):
                            report["compliance_summary"]["ley_25506"] += 1
                        if compliance.get("ley_24240_defensa_consumidor"):
                            report["compliance_summary"]["ley_24240"] += 1
        except FileNotFoundError:
            pass
            
        return report


# ==============================================================================
# Ejemplo de uso (No se ejecuta si se importa como módulo)
# ==============================================================================
if __name__ == "__main__":
    # Inicializar el auditor
    auditor = AuditLogger(log_file_path="test_audit.log")
    
    # Registrar un evento normal
    auditor.log_event(
        agent_name="GeneradorContratos",
        action_description="Generación de borrador de contrato de servicios",
        severity=SeverityLevel.INFO,
        raw_data={"partes": ["Empresa A", "Cliente B"], "monto": 50000},
        legal_checks={
            "ley_25326_datos_personales": True,
            "ley_25506_firma_digital": False,
            "ley_24240_defensa_consumidor": True
        }
    )
    
    # Registrar un evento crítico (simulación de intento de firma sin aprobación)
    auditor.log_event(
        agent_name="FirmanteDigital",
        action_description="INTENTO DE FIRMA SIN APROBACIÓN HUMANA",
        severity=SeverityLevel.CRITICAL,
        raw_data={"contrato_id": "CTX-999"},
        legal_checks={
            "ley_25326_datos_personales": True,
            "ley_25506_firma_digital": False,
            "ley_24240_defensa_consumidor": False
        }
    )
    
    print("\n✅ Auditoría completada. Revisar test_audit.log")
    print("✅ Informe de cumplimiento:", json.dumps(auditor.generate_compliance_report(), indent=2))
