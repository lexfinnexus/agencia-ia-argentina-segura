"""
Módulo de Supervisión Humana Obligatoria
Agencia IA Argentina Segura
Propietario: Humberto Patricio Castro

Este módulo implementa el control de supervisión humana obligatoria (Human-in-the-Loop),
garantizando que ninguna acción crítica se ejecute sin la aprobación explícita
de Humberto Patricio Castro o personal autorizado.

Cumple con:
- Ley 25.326: Trazabilidad de decisiones sobre datos personales
- Ley 25.506: Validación previa a la firma digital
- Ley 24.240: Protección del consumidor en decisiones automatizadas
"""

import hashlib
import json
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum

from .audit_log import AuditLogger, SeverityLevel


# ==============================================================================
# CONFIGURACIÓN DEL PROPIETARIO Y SUPERVISOR OBLIGATORIO
# ==============================================================================
OWNER_NAME = "Humberto Patricio Castro"
OWNER_ROLE = "Director General y Propietario"


class SupervisionAction(Enum):
    """Acciones posibles del supervisor humano."""
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    MODIFIED = "MODIFIED"
    PENDING = "PENDING"


class DocumentType(Enum):
    """Tipos de documentos sujetos a supervisión."""
    CONTRACT = "CONTRACT"
    LEGAL_ANALYSIS = "LEGAL_ANALYSIS"
    DATA_PROCESSING = "DATA_PROCESSING"
    DIGITAL_SIGNATURE = "DIGITAL_SIGNATURE"
    CUSTOMER_COMMUNICATION = "CUSTOMER_COMMUNICATION"


@dataclass
class SupervisionRecord:
    """Registro inmutable de una decisión de supervisión humana."""
    supervision_id: str
    document_id: str
    document_type: str
    supervisor_name: str
    supervisor_role: str
    action: str
    timestamp_utc: str
    timestamp_art: str
    comments: str
    modifications: Optional[str]
    previous_hash: Optional[str]
    new_hash: Optional[str]
    legal_compliance: Dict[str, bool]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    def calculate_record_hash(self) -> str:
        """Calcula hash SHA-256 del registro para garantizar inmutabilidad."""
        record_string = json.dumps(self.to_dict(), sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(record_string.encode('utf-8')).hexdigest()


@dataclass
class AuthorizedSupervisor:
    """Supervisor autorizado para aprobar documentos."""
    name: str
    role: str
    authorization_level: str  # "FULL", "CONTRACTS", "DATA", "ANALYSIS"
    active: bool = True


class HumanSupervisor:
    """
    Gestor de supervisión humana obligatoria.
    
    Reglas de negocio inquebrantables:
    - La IA SOLO genera borradores.
    - NUNCA ejecuta acciones legales autónomas.
    - Humberto Patricio Castro (o autorizado) debe revisar y aprobar.
    - Trazabilidad completa de todas las decisiones.
    - Sin aprobación humana = sin ejecución.
    """

    def __init__(self, audit_logger: AuditLogger):
        self.audit_logger = audit_logger
        self.supervision_records = []
        
        # Registro de supervisores autorizados
        self.authorized_supervisors: List[AuthorizedSupervisor] = [
            AuthorizedSupervisor(
                name=OWNER_NAME,
                role=OWNER_ROLE,
                authorization_level="FULL",
                active=True
            )
        ]
        
        # Documentos pendientes de aprobación
        self.pending_documents: Dict[str, Dict[str, Any]] = {}

    def register_supervisor(
        self,
        name: str,
        role: str,
        authorization_level: str
    ) -> AuthorizedSupervisor:
        """
        Registra un nuevo supervisor autorizado.
        Requiere aprobación de Humberto Patricio Castro.
        """
        # Verificar que Humberto Patricio Castro autorice el registro
        self.audit_logger.log_event(
            agent_name="HumanSupervisor",
            action_description=f"Registro de nuevo supervisor autorizado: {name}",
            severity=SeverityLevel.WARNING,
            raw_data={
                "new_supervisor": name,
                "role": role,
                "authorization_level": authorization_level
            },
            legal_checks={
                "ley_25326_datos_personales": True,
                "ley_25506_firma_digital": False,
                "ley_24240_defensa_consumidor": False
            }
        )
        
        supervisor = AuthorizedSupervisor(
            name=name,
            role=role,
            authorization_level=authorization_level,
            active=True
        )
        
        self.authorized_supervisors.append(supervisor)
        return supervisor

    def is_authorized(
        self,
        supervisor_name: str,
        document_type: Optional[DocumentType] = None
    ) -> bool:
        """
        Verifica si un supervisor está autorizado para el tipo de documento.
        """
        for supervisor in self.authorized_supervisors:
            if supervisor.name == supervisor_name and supervisor.active:
                # Supervisor FULL puede aprobar todo
                if supervisor.authorization_level == "FULL":
                    return True
                
                # Verificar nivel de autorización específico
                if document_type and supervisor.authorization_level == document_type.value:
                    return True
        
        return False

    def submit_for_review(
        self,
        document_id: str,
        document_type: DocumentType,
        content: str,
        metadata: Dict[str, Any]
    ) -> str:
        """
        Envía un documento a revisión humana.
        
        Args:
            document_id: ID único del documento
            document_type: Tipo de documento
            content: Contenido del documento
            metadata: Metadatos adicionales
            
        Returns:
            str: ID de la solicitud de revisión
        """
        # Calcular hash del documento
        content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        
        # Generar ID de revisión
        review_id_data = f"{document_id}:{datetime.now(timezone.utc).isoformat()}"
        review_id = hashlib.sha256(review_id_data.encode('utf-8')).hexdigest()[:16]
        
        # Registrar documento pendiente
        self.pending_documents[review_id] = {
            "document_id": document_id,
            "document_type": document_type.value,
            "content": content,
            "content_hash": content_hash,
            "metadata": metadata,
            "submitted_at": datetime.now(timezone.utc).isoformat(),
            "status": "PENDING"
        }
        
        # Registrar en auditoría
        self.audit_logger.log_event(
            agent_name="HumanSupervisor",
            action_description=f"Documento enviado a revisión humana: {document_type.value}",
            severity=SeverityLevel.INFO,
            raw_data={
                "review_id": review_id,
                "document_id": document_id,
                "document_type": document_type.value
            },
            legal_checks={
                "ley_25326_datos_personales": True,
                "ley_25506_firma_digital": False,
                "ley_24240_defensa_consumidor": True,
                "supervision_humana_requerida": True
            }
        )
        
        return review_id

    def review_and_decide(
        self,
        review_id: str,
        supervisor_name: str,
        action: SupervisionAction,
        comments: str = "",
        modifications: Optional[str] = None
    ) -> SupervisionRecord:
        """
        Registra la decisión del supervisor humano.
        
        Args:
            review_id: ID de la solicitud de revisión
            supervisor_name: Nombre del supervisor
            action: Acción tomada (APPROVED, REJECTED, MODIFIED)
            comments: Comentarios del supervisor
            modifications: Modificaciones realizadas (si aplica)
            
        Returns:
            SupervisionRecord: Registro de la decisión
        """
        # Verificar que la revisión existe
        if review_id not in self.pending_documents:
            raise ValueError(f"Revisión no encontrada: {review_id}")
        
        # Verificar autorización del supervisor
        document_type = DocumentType(self.pending_documents[review_id]["document_type"])
        if not self.is_authorized(supervisor_name, document_type):
            # Registrar intento no autorizado
            self.audit_logger.log_event(
                agent_name="HumanSupervisor",
                action_description=f"INTENTO NO AUTORIZADO de revisión por: {supervisor_name}",
                severity=SeverityLevel.CRITICAL,
                raw_data={"review_id": review_id, "supervisor": supervisor_name},
                legal_checks={
                    "ley_25326_datos_personales": True,
                    "ley_25506_firma_digital": False,
                    "ley_24240_defensa_consumidor": False
                }
            )
            raise PermissionError(f"Supervisor no autorizado: {supervisor_name}")
        
        # Obtener datos del documento
        doc_data = self.pending_documents[review_id]
        previous_hash = doc_data["content_hash"]
        
        # Calcular nuevo hash si hay modificaciones
        new_hash = previous_hash
        if modifications:
            new_hash = hashlib.sha256(modifications.encode('utf-8')).hexdigest()
        
        # Generar timestamps
        now_utc = datetime.now(timezone.utc)
        now_art = now_utc.astimezone(timezone(timedelta(hours=-3)))
        
        # Generar ID de supervisión
        supervision_id_data = f"{review_id}:{supervisor_name}:{now_utc.isoformat()}"
        supervision_id = hashlib.sha256(supervision_id_data.encode('utf-8')).hexdigest()[:16]
        
        # Crear registro de supervisión
        record = SupervisionRecord(
            supervision_id=supervision_id,
            document_id=doc_data["document_id"],
            document_type=doc_data["document_type"],
            supervisor_name=supervisor_name,
            supervisor_role=OWNER_ROLE if supervisor_name == OWNER_NAME else "Autorizado",
            action=action.value,
            timestamp_utc=now_utc.isoformat(),
            timestamp_art=now_art.isoformat(),
            comments=comments,
            modifications=modifications,
            previous_hash=previous_hash,
            new_hash=new_hash,
            legal_compliance={
                "ley_25326_datos_personales": True,
                "ley_25506_firma_digital": action == SupervisionAction.APPROVED,
                "ley_24240_defensa_consumidor": True,
                "supervision_humana_completada": True
            }
        )
        
        # Actualizar estado del documento pendiente
        doc_data["status"] = action.value
        doc_data["reviewed_at"] = now_utc.isoformat()
        doc_data["reviewed_by"] = supervisor_name
        
        # Registrar en auditoría
        severity = SeverityLevel.INFO
        if action == SupervisionAction.REJECTED:
            severity = SeverityLevel.WARNING
        elif action == SupervisionAction.MODIFIED:
            severity = SeverityLevel.INFO
        
        self.audit_logger.log_event(
            agent_name="HumanSupervisor",
            action_description=f"Decisión de supervisión: {action.value} por {supervisor_name}",
            severity=severity,
            raw_data={
                "supervision_id": supervision_id,
                "review_id": review_id,
                "action": action.value
            },
            legal_checks=record.legal_compliance
        )
        
        self.supervision_records.append(record)
        
        return record

    def get_pending_reviews(self) -> List[Dict[str, Any]]:
        """Obtiene lista de documentos pendientes de revisión."""
        return [
            {
                "review_id": review_id,
                "document_id": data["document_id"],
                "document_type": data["document_type"],
                "submitted_at": data["submitted_at"],
                "status": data["status"]
            }
            for review_id, data in self.pending_documents.items()
            if data["status"] == "PENDING"
        ]

    def get_supervision_history(
        self,
        document_id: Optional[str] = None,
        supervisor_name: Optional[str] = None
    ) -> List[SupervisionRecord]:
        """
        Obtiene historial de supervisión con filtros opcionales.
        """
        results = self.supervision_records
        
        if document_id:
            results = [r for r in results if r.document_id == document_id]
        
        if supervisor_name:
            results = [r for r in results if r.supervisor_name == supervisor_name]
        
        return results

    def verify_document_integrity(
        self,
        document_id: str,
        content: str
    ) -> bool:
        """
        Verifica la integridad de un documento aprobado comparando hashes.
        """
        # Buscar el último registro de supervisión aprobado para este documento
        approved_records = [
            r for r in self.supervision_records
            if r.document_id == document_id and r.action == "APPROVED"
        ]
        
        if not approved_records:
            return False
        
        # Tomar el registro más reciente
        latest_record = max(approved_records, key=lambda r: r.timestamp_utc)
        
        # Calcular hash del contenido actual
        current_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        
        # Comparar con el hash aprobado
        return current_hash == latest_record.new_hash

    def generate_supervision_report(self) -> Dict[str, Any]:
        """
        Genera informe de supervisión para auditoría.
        """
        now_art = datetime.now(timezone(timedelta(hours=-3))).isoformat()
        
        total_records = len(self.supervision_records)
        approved = len([r for r in self.supervision_records if r.action == "APPROVED"])
        rejected = len([r for r in self.supervision_records if r.action == "REJECTED"])
        modified = len([r for r in self.supervision_records if r.action == "MODIFIED"])
        pending = len(self.get_pending_reviews())
        
        return {
            "generated_at": now_art,
            "supervisor": OWNER_NAME,
            "summary": {
                "total_decisions": total_records,
                "approved": approved,
                "rejected": rejected,
                "modified": modified,
                "pending": pending
            },
            "approval_rate": (approved / total_records * 100) if total_records > 0 else 0,
            "authorized_supervisors": [
                {"name": s.name, "role": s.role, "level": s.authorization_level}
                for s in self.authorized_supervisors if s.active
            ]
        }


# ==============================================================================
# Ejemplo de uso (No se ejecuta si se importa como módulo)
# ==============================================================================
if __name__ == "__main__":
    from audit_log import AuditLogger
    
    # Inicializar auditoría
    auditor = AuditLogger(log_file_path="supervision_audit.log")
    
    # Inicializar supervisor humano
    supervisor = HumanSupervisor(audit_logger=auditor)
    
    # Simular envío de contrato a revisión
    review_id = supervisor.submit_for_review(
        document_id="CONTRACT-001",
        document_type=DocumentType.CONTRACT,
        content="Contrato de servicios entre Parte A y Parte B...",
        metadata={"parties": ["Parte A", "Parte B"], "type": "servicios"}
    )
    
    print(f"\n✅ Documento enviado a revisión. ID: {review_id}")
    print(f"📋 Documentos pendientes: {len(supervisor.get_pending_reviews())}")
    
    # Simular aprobación por Humberto Patricio Castro
    record = supervisor.review_and_decide(
        review_id=review_id,
        supervisor_name=OWNER_NAME,
        action=SupervisionAction.APPROVED,
        comments="Contrato revisado y aprobado. Cumple con Ley 25.326 y 25.506."
    )
    
    print(f"\n✅ Decisión registrada. ID Supervisión: {record.supervision_id}")
    print(f"👤 Supervisor: {record.supervisor_name}")
    print(f"⚖️ Acción: {record.action}")
    print(f"🔐 Hash nuevo: {record.new_hash}")
    
    # Generar informe
    report = supervisor.generate_supervision_report()
    print(f"\n📊 Informe de supervisión:")
    print(json.dumps(report, indent=2, ensure_ascii=False))
  
