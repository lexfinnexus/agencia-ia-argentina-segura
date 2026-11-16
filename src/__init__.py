"""
Agencia IA Argentina Segura - Paquete Principal
Propietario: Humberto Patricio Castro

Este paquete orquesta los módulos de auditoría, generación de contratos
y supervisión humana, garantizando el cumplimiento de las Leyes 25.326,
25.506 y 24.240 de la República Argentina.
"""

__version__ = "1.0.0"
__author__ = "Humberto Patricio Castro"
__license__ = "MIT"

# Importación de módulos principales para facilitar el acceso
from .audit_log import AuditLogger, SeverityLevel
from .contract_generator import ContractGenerator, ContractDraft
from .human_supervisor import HumanSupervisor, SupervisionAction, DocumentType

__all__ = [
    "AuditLogger",
    "SeverityLevel",
    "ContractGenerator",
    "ContractDraft",
    "HumanSupervisor",
    "SupervisionAction",
    "DocumentType",
]
