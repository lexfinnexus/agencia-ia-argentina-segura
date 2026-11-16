"""
Pruebas Unitarias para el Módulo de Auditoría
Agencia IA Argentina Segura
Propietario: Humberto Patricio Castro
"""

import os
import json
import pytest
import sys

# Agregar el directorio src al path para importar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from audit_log import AuditLogger, SeverityLevel


@pytest.fixture
def temp_log_file(tmp_path):
    """Crea un archivo de log temporal para las pruebas."""
    return str(tmp_path / "test_audit.log")


@pytest.fixture
def auditor(temp_log_file):
    """Instancia del AuditLogger usando el archivo temporal."""
    return AuditLogger(log_file_path=temp_log_file)


def test_log_event_creation(auditor, temp_log_file):
    """Prueba la creación básica de un evento de auditoría."""
    record = auditor.log_event(
        agent_name="TestAgent",
        action_description="Prueba de generación de evento",
        severity=SeverityLevel.INFO,
        raw_data={"test_key": "test_value"},
        legal_checks={"ley_25326_datos_personales": True}
    )
    
    assert record.transaction_id is not None
    assert len(record.transaction_id) == 16
    assert record.agent_name == "TestAgent"
    assert record.severity == "INFO"
    assert record.supervisor_human == "Humberto Patricio Castro"
    assert record.data_hash is not None
    assert record.legal_compliance["ley_25326_datos_personales"] is True
    
    # Verificar que se escribió en el archivo
    assert os.path.exists(temp_log_file)
    with open(temp_log_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        assert len(lines) == 1
        log_entry = json.loads(lines[0])
        assert log_entry["agent_name"] == "TestAgent"
        assert "record_hash_sha256" in log_entry


def test_log_event_critical_triggers_alert(auditor, capsys):
    """Prueba que un evento CRITICAL genera la alerta en consola."""
    auditor.log_event(
        agent_name="SecurityModule",
        action_description="INTENTO DE ACCESO NO AUTORIZADO",
        severity=SeverityLevel.CRITICAL,
        raw_data={"ip": "192.168.1.100"}
    )
    
    captured = capsys.readouterr()
    assert "🚨 ALERTA CRÍTICA DE AUDITORÍA 🚨" in captured.out
    assert "Humberto Patricio Castro" in captured.out


def test_verify_log_integrity_valid(auditor, temp_log_file):
    """Prueba la verificación de integridad de un log válido."""
    auditor.log_event(
        agent_name="TestAgent",
        action_description="Evento válido",
        severity=SeverityLevel.INFO
    )
    
    is_valid = auditor.verify_log_integrity()
    assert is_valid is True


def test_verify_log_integrity_invalid(auditor, temp_log_file):
    """Prueba la verificación de integridad cuando falta el hash del registro."""
    with open(temp_log_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps({"agent_name": "TestAgent", "severity": "INFO"}) + "\n")
    
    is_valid = auditor.verify_log_integrity()
    assert is_valid is False


def test_generate_compliance_report(auditor):
    """Prueba la generación del informe de cumplimiento."""
    auditor.log_event(
        agent_name="ContractGenerator",
        action_description="Generación de contrato",
        severity=SeverityLevel.INFO,
        legal_checks={
            "ley_25326_datos_personales": True,
            "ley_25506_firma_digital": True,
            "ley_24240_defensa_consumidor": True
        }
    )
    
    auditor.log_event(
        agent_name="DataProcessor",
        action_description="Procesamiento de datos",
        severity=SeverityLevel.INFO,
        legal_checks={
            "ley_25326_datos_personales": True,
            "ley_25506_firma_digital": False,
            "ley_24240_defensa_consumidor": False
        }
    )
    
    report = auditor.generate_compliance_report()
    
    assert report["total_events"] == 2
    assert report["critical_events"] == 0
    assert report["compliance_summary"]["ley_25326"] == 2
    assert report["compliance_summary"]["ley_25506"] == 1
    assert report["compliance_summary"]["ley_24240"] == 1
    assert report["supervisor"] == "Humberto Patricio Castro"
  
