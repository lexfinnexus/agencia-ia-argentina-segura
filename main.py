#!/usr/bin/env python3
"""
Agencia IA Argentina Segura - Punto de Entrada Principal
Propietario: Humberto Patricio Castro

Este archivo orquesta los módulos del sistema y demuestra su ejecución real.
Incluye el Motor de Optimización de Tokens para minimizar consumo de API.

Uso:
    python main.py --demo
    python main.py --verify --archivo contrato.md --hash <hash_esperado>
    python main.py --prompt
    python main.py --cache-stats
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
from src.token_optimizer import TokenOptimizer


# ==============================================================================
# CONFIGURACIÓN
# ==============================================================================
OWNER_NAME = "Humberto Patricio Castro"
OWNER_ROLE = "Director General y Propietario"
VERSION = "1.1.0"


# ==============================================================================
# SYSTEM PROMPT DE RUNTIME (Conciso - optimizado para tokens)
# ==============================================================================
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
# FUNCIONES DE DEMOSTRACIÓN
# ==============================================================================
def banner():
    """Imprime el banner de inicio del sistema."""
    print("=" * 70)
    print("  AGENCIA IA ARGENTINA SEGURA - v" + VERSION)
    print("  Propietario: " + OWNER_NAME)
    print("  Cumplimiento: Ley 25.326 | Ley 25.506 | Ley 24.240")
    print("  Motor de Optimización de Tokens: ACTIVO")
    print("=" * 70)
    print()


def demo_completo():
    """
    Ejecuta una demostración completa del sistema con optimización de tokens.
    """
    banner()
    print("🚀 INICIANDO DEMOSTRACIÓN COMPLETA\n")

    # Paso 1: Inicializar componentes
    print("📦 [1/7] Inicializando módulos...")
    auditor = AuditLogger(log_file_path="demo_audit.log")
    generator = ContractGenerator(audit_logger=auditor)
    supervisor = HumanSupervisor(audit_logger=auditor)
    token_optimizer = TokenOptimizer(cache_file="demo_token_cache.json")
    print("   ✅ AuditLogger inicializado")
    print("   ✅ ContractGenerator inicializado")
    print("   ✅ HumanSupervisor inicializado")
    print("   ✅ TokenOptimizer inicializado\n")

    # Paso 2: Preparar datos del contrato
    print("📝 [2/7] Preparando datos del contrato...")
    contract_type = "servicios"
    parties = ["Consultora ABC S.A.", "Cliente XYZ S.R.L."]
    conditions = [
        "Servicio de consultoría en transformación digital",
        "Plazo: 6 meses",
        "Monto: $500.000 ARS mensuales"
    ]
    
    # Serializar para validación de tokens
    input_data = json.dumps({
        "type": contract_type,
        "parties": parties,
        "conditions": conditions
    }, ensure_ascii=False)
    
    print(f"   ✅ Datos preparados")
    print(f"   📊 Tipo: {contract_type}")
    print(f"   👥 Partes: {len(parties)}\n")

    # Paso 3: Validación de tokens (Pre-flight check)
    print("⚡ [3/7] Validación de tokens (Pre-flight)...")
    validation = token_optimizer.validate_and_optimize(
        prompt=SYSTEM_PROMPT_RUNTIME,
        input_data=input_data,
        max_allowed_tokens=2000
    )
    
    if not validation.is_allowed:
        print(f"   ❌ Solicitud RECHAZADA: {validation.rejection_reason}")
        print("   💡 Ajusta los datos y vuelve a intentar.")
        return
    
    if validation.is_cached:
        print(f"   ⚡ RESPUESTA EN CACHÉ - Tokens consumidos: 0")
        print(f"   💰 Ahorro: 100% de tokens en esta operación\n")
        # En producción, aquí se devolvería validation.cached_response
    else:
        print(f"   ✅ Solicitud APROBADA")
        print(f"   📊 Tokens estimados: {validation.estimated_tokens}")
        print(f"   📡 Se realizará llamada a API de IA\n")

    # Paso 4: Generar borrador (simulado)
    print("📄 [4/7] Generando borrador de contrato...")
    draft = generator.create_contract(
        contract_type=contract_type,
        parties=parties,
        conditions=conditions
    )
    print(f"   ✅ Contrato generado")
    print(f"   🆔 ID: {draft.contract_id}")
    print(f"   🔐 Hash SHA-256: {draft.hash_sha256}")
    print(f"   ⚖️  Cumplimiento legal: {draft.legal_compliance}\n")

    # Guardar en caché para futuras consultas idénticas
    token_optimizer.save_to_cache(
        prompt=SYSTEM_PROMPT_RUNTIME,
        input_data=input_data,
        response={
            "contract_id": draft.contract_id,
            "hash": draft.hash_sha256,
            "status": "draft"
        }
    )
    print("   💾 Respuesta guardada en caché criptográfica\n")

    # Paso 5: Enviar a supervisión
    print("👁️  [5/7] Enviando a supervisión humana...")
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

    # Paso 6: Aprobación humana
    print(f"✍️  [6/7] Aprobación de {OWNER_NAME}...")
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

    # Paso 7: Verificación e informe
    print("🔍 [7/7] Verificación e informe final...")
    is_valid = supervisor.verify_document_integrity(
        document_id=draft.contract_id,
        content=draft.content
    )
    print(f"   ✅ Integridad: {'VÁLIDA' if is_valid else 'COMPROMETIDA'}")
    
    report = auditor.generate_compliance_report()
    print(f"   📊 Total eventos: {report['total_events']}")
    print(f"   ⚠️  Eventos críticos: {report['critical_events']}")
    print(f"   ⚖️  Cumplimiento Ley 25.326: {report['compliance_summary']['ley_25326']}")
    print(f"   ⚖️  Cumplimiento Ley 25.506: {report['compliance_summary']['ley_25506']}")
    print(f"   ⚖️  Cumplimiento Ley 24.240: {report['compliance_summary']['ley_24240']}")
    
    # Estadísticas de optimización de tokens
    cache_stats = token_optimizer.get_cache_stats()
    print(f"\n   💰 ESTADÍSTICAS DE OPTIMIZACIÓN:")
    print(f"   📦 Respuestas en caché: {cache_stats['total_cached_responses']}")
    print(f"   ⚡ Tokens ahorrados (estimado): {cache_stats['estimated_tokens_saved']}")
    print()

    print("=" * 70)
    print("  ✅ DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
    print("  📁 Logs guardados en: demo_audit.log")
    print("  💾 Caché de tokens: demo_token_cache.json")
    print("=" * 70)


def verify_file(filepath: str, expected_hash: str):
    """
    Verifica la integridad de un archivo comparando su hash SHA-256.
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


def show_cache_stats():
    """Muestra estadísticas de la caché de tokens."""
    optimizer = TokenOptimizer(cache_file="demo_token_cache.json")
    stats = optimizer.get_cache_stats()
    
    print("📊 ESTADÍSTICAS DE CACHÉ DE TOKENS")
    print("=" * 50)
    print(f"   Respuestas almacenadas: {stats['total_cached_responses']}")
    print(f"   Tokens ahorrados (est.): {stats['estimated_tokens_saved']}")
    print(f"   Costo evitado (USD est.): ${stats['estimated_tokens_saved'] * 0.00001:.4f}")
    print("=" * 50)


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
    parser.add_argument(
        "--cache-stats",
        action="store_true",
        help="Muestra estadísticas de la caché de tokens"
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
    elif args.cache_stats:
        show_cache_stats()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
