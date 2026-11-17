#!/usr/bin/env python3
"""
Agencia IA Argentina Segura - Punto de Entrada Principal
Propietario: Humberto Patricio Castro

Este archivo orquesta los módulos del sistema y demuestra su ejecución real.
Separa la DOCUMENTACIÓN (completa, sin límite de palabras) del SYSTEM PROMPT
de runtime (conciso, optimizado para consumo de tokens).

Uso:
    python main.py --demo
    python main.py --generate --tipo servicios --partes "Empresa A" "Cliente B"
    python main.py --verify --archivo contrato.md --hash <hash_esperado>
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone, timedelta

# Importar módulos del paquete src
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from src.audit_log import AuditLogger, SeverityLevel
from src.contract_generator import ContractGenerator
from src.human_supervisor import HumanSupervisor, DocumentType, SupervisionAction


# ==============================================================================
# CONFIGURACIÓN
# ==============================================================================
OWNER_NAME = "Humberto Patricio Castro"
OWNER_ROLE = "Director General y Propietario"
VERSION = "1.0.0"


# ==============================================================================
# SYSTEM PROMPT DE RUNTIME (Conciso - aplica consejo 5)
# ==============================================================================
# Este es el prompt que se enviaría a la API de Claude en cada llamada.
# Es CONCISO porque consume tokens por cada request.
# La documentación completa vive en /prompts/*.md (sin límite de palabras).
SYSTEM_PROMPT_RUNTIME = """
Eres el Asistente Legal de Agencia IA Argentina Segura.
Reglas inquebrantables:
1. Toda salida incluye contexto humanizado (limitaciones + recomendaciones).
2. Solo generas BORRADORES. Nunca ejecutas acciones legales autónomas.
3. Cumplimiento obligatorio: Ley 25.326, Ley 25.506, Ley 24.240.
4. Toda decisión crítica requiere aprobación de Humberto Patricio Castro.
5. Calcula hash SHA-256 de cada documento generado.
Responde en español, lenguaje claro, sin tecnicismos innecesarios.
"""


# ==============================================================================
# FUNCIONES DE DEMOSTRACIÓN (Aplican consejo 6: pruebas visibles)
# ==============================================================================
def banner():
    """Imprime el banner de inicio del sistema."""
    print("=" * 70)
    print("  AGENCIA IA ARGENTINA SEGURA - v" + VERSION)
    print("  Propietario: " + OWNER_NAME)
    print("  Cumplimiento: Ley 25.326 | Ley 25.506 | Ley 24.240")
    print("=" * 70)
    print()


def demo_completo():
    """
    Ejecuta una demostración completa del sistema con pruebas visibles.
    Aplica consejo 6: cada paso muestra evidencia criptográfica.
    """
    banner()
    print("🚀 INICIANDO DEMOSTRACIÓN COMPLETA\n")

    # Paso 1: Inicializar componentes
    print("📦 [1/6] Inicializando módulos...")
    auditor = AuditLogger(log_file_path="demo_audit.log")
    generator = ContractGenerator(audit_logger=auditor)
    supervisor = HumanSupervisor(audit_logger=auditor)
    print("   ✅ AuditLogger inicializado")
    print("   ✅ ContractGenerator inicializado")
    print("   ✅ HumanSupervisor inicializado\n")

    # Paso 2: Generar borrador
    print("📝 [2/6] Generando borrador de contrato...")
    draft = generator.create_contract(
        contract_type="servicios",
        parties=["Consultora ABC S.A.", "Cliente XYZ S.R.L."],
        conditions=[
            "Servicio de consultoría en transformación digital",
            "Plazo: 6 meses",
            "Monto: $500.000 ARS mensuales"
        ]
    )
    print(f"   ✅ Contrato generado")
    print(f"   🆔 ID: {draft.contract_id}")
    print(f"   🔐 Hash SHA-256: {draft.hash_sha256}")
    print(f"   📊 Tipo: {draft.contract_type}")
    print(f"   ⚖️  Cumplimiento legal: {draft.legal_compliance}\n")

    # Paso 3: Enviar a supervisión
    print("👁️  [3/6] Enviando a supervisión humana...")
    review_id = supervisor.submit_for_review(
        document_id=draft.contract_id,
        document_type=DocumentType.CONTRACT,
        content=draft.content,
        metadata={
            "hash": draft.hash_sha256,
            "parties": draft.parties
        }
    )
    print(f"   ✅ Revisión registrada")
    print(f"   🆔 Review ID: {review_id}")
    print(f"   📋 Pendientes: {len(supervisor.get_pending_reviews())}\n")

    # Paso 4: Aprobación humana (simulación)
    print(f"✍️  [4/6] Aprobación de {OWNER_NAME}...")
    decision = supervisor.review_and_decide(
        review_id=review_id,
        supervisor_name=OWNER_NAME,
        action=SupervisionAction.APPROVED,
        comments="Contrato revisado y aprobado. Cumple con Ley 25.326, 25.506 y 24.240."
    )
    print(f"   ✅ Decisión registrada")
    print(f"   🆔 Supervision ID: {decision.supervision_id}")
    print(f"   ⚖️  Acción: {decision.action}")
    print(f"   🔐 Hash final: {decision.new_hash}\n")

    # Paso 5: Verificación de integridad
    print("🔍 [5/6] Verificando integridad del documento...")
    is_valid = supervisor.verify_document_integrity(
        document_id=draft.contract_id,
        content=draft.content
    )
    print(f"   ✅ Integridad: {'VÁLIDA' if is_valid else 'COMPROMETIDA'}\n")

    # Paso 6: Informe final
    print("📊 [6/6] Informe de auditoría...")
    report = auditor.generate_compliance_report()
    print(f"   Total eventos: {report['total_events']}")
    print(f"   Eventos críticos: {report['critical_events']}")
    print(f"   Cumplimiento Ley 25.326: {report['compliance_summary']['ley_25326']}")
    print(f"   Cumplimiento Ley 25.506: {report['compliance_summary']['ley_25506']}")
    print(f"   Cumplimiento Ley 24.240: {report['compliance_summary']['ley_24240']}")
    print()

    print("=" * 70)
    print("  ✅ DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
    print("  📁 Logs guardados en: demo_audit.log")
    print("=" * 70)


def verify_file(filepath: str, expected_hash: str):
    """
    Verifica la integridad de un archivo comparando su hash SHA-256.
    Aplica consejo 6: prueba criptográfica visible.
    """
    if not os.path.exists(filepath):
        print(f"❌ Error: el archivo '{filepath}' no existe.")
        sys.exit(1)

    with open(filepath, 'rb') as f:
        actual_hash = hashlib.sha256(f.read()).hexdigest()

    print(f"🔍 Verificación de integridad:")
    print(f"   Archivo: {filepath}")
    print(f"   Hash esperado: {expected_hash}")
    print(f"   Hash calculado: {actual_hash}")
    print(f"   Estado: {'✅ ÍNTEGRO' if actual_hash == expected_hash else '❌ MODIFICADO'}")


def show_runtime_prompt():
    """Muestra el system prompt de runtime (conciso)."""
    print("📋 SYSTEM PROMPT DE RUNTIME (conciso, optimizado para tokens):")
    print("-" * 70)
    print(SYSTEM_PROMPT_RUNTIME)
    print("-" * 70)
    print(f"\n📚 Documentación completa disponible en: /prompts/*.md")
    print(f"   (Sin límite de palabras - es documentación, no runtime)")


# ==============================================================================
# CLI
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="Agencia IA Argentina Segura - Sistema de contratos legales con IA"
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Ejecuta la demostración completa del sistema"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verifica la integridad de un archivo"
    )
    parser.add_argument(
        "--archivo",
        type=str,
        help="Ruta del archivo a verificar (requiere --verify)"
    )
    parser.add_argument(
        "--hash",
        type=str,
        help="Hash SHA-256 esperado (requiere --verify)"
    )
    parser.add_argument(
        "--prompt",
        action="store_true",
        help="Muestra el system prompt de runtime"
    )

    args = parser.parse_args()

    if args.demo:
        demo_completo()
    elif args.verify:
        if not args.archivo or not args.hash:
            print("❌ Error: --verify requiere --archivo y --hash")
            sys.exit(1)
        verify_file(args.archivo, args.hash)
    elif args.prompt:
        show_runtime_prompt()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
  
