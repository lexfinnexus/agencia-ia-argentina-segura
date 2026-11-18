"""
Motor de Optimización y Validación de Tokens
Agencia IA Argentina Segura
Propietario: Humberto Patricio Castro

Objetivo: Minimizar el consumo de tokens de principio a fin mediante:
1. Caché criptográfica (respuesta inmediata si el input ya fue procesado).
2. Validación pre-vuelo (rechazar payloads que excedan límites antes de llamar a la API).
"""

import hashlib
import json
import os
from typing import Any, Dict, Optional
from dataclasses import dataclass

# Configuración de límites (ajustable según el modelo de IA)
MAX_INPUT_CHARS = 8000  # Equivalente aprox. a 2000-2500 tokens (seguridad pre-vuelo)
CACHE_FILE = "token_cache.json"


@dataclass
class TokenValidationResult:
    is_allowed: bool
    estimated_tokens: int
    is_cached: bool
    cached_response: Optional[Any]
    rejection_reason: Optional[str]


class TokenOptimizer:
    """
    Gestor de eficiencia de tokens.
    Intercepta solicitudes para evitar llamadas innecesarias a la API de IA.
    """

    def __init__(self, cache_file: str = CACHE_FILE):
        self.cache_file = cache_file
        self._ensure_cache_exists()

    def _ensure_cache_exists(self) -> None:
        if not os.path.exists(self.cache_file):
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def _get_cache(self) -> Dict[str, Any]:
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save_cache(self, cache_data: Dict[str, Any]) -> None:
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, indent=2, ensure_ascii=False)

    def _calculate_input_hash(self, prompt: str, input_data: str) -> str:
        """Genera un hash único de la combinación prompt + datos de entrada."""
        combined = f"{prompt}::{input_data}"
        return hashlib.sha256(combined.encode('utf-8')).hexdigest()

    def _estimate_tokens(self, text: str) -> int:
        """
        Estimación conservadora de tokens (1 token ≈ 4 caracteres en español).
        En producción, se puede reemplazar por la librería 'tiktoken' de OpenAI/Anthropic.
        """
        return max(1, len(text) // 4)

    def validate_and_optimize(
        self, 
        prompt: str, 
        input_data: str, 
        max_allowed_tokens: int = 2000
    ) -> TokenValidationResult:
        """
        Valida la solicitud antes de enviarla a la IA.
        
        Returns:
            TokenValidationResult: Indica si se permite, si está en caché, y la razón si es rechazado.
        """
        input_hash = self._calculate_input_hash(prompt, input_data)
        estimated_tokens = self._estimate_tokens(prompt + input_data)
        
        # 1. Validación Pre-vuelo (Límite de seguridad)
        if len(input_data) > MAX_INPUT_CHARS:
            return TokenValidationResult(
                is_allowed=False,
                estimated_tokens=estimated_tokens,
                is_cached=False,
                cached_response=None,
                rejection_reason=f"Input excede el límite de seguridad de {MAX_INPUT_CHARS} caracteres."
            )
            
        if estimated_tokens > max_allowed_tokens:
            return TokenValidationResult(
                is_allowed=False,
                estimated_tokens=estimated_tokens,
                is_cached=False,
                cached_response=None,
                rejection_reason=f"Tokens estimados ({estimated_tokens}) exceden el límite de {max_allowed_tokens}."
            )

        # 2. Verificación de Caché (Ahorro del 100% de tokens si existe)
        cache_data = self._get_cache()
        if input_hash in cache_data:
            return TokenValidationResult(
                is_allowed=True,
                estimated_tokens=0,  # No se consumen tokens reales
                is_cached=True,
                cached_response=cache_data[input_hash],
                rejection_reason=None
            )

        # 3. Aprobado para llamada a la API
        return TokenValidationResult(
            is_allowed=True,
            estimated_tokens=estimated_tokens,
            is_cached=False,
            cached_response=None,
            rejection_reason=None
        )

    def save_to_cache(self, prompt: str, input_data: str, response: Any) -> None:
        """Guarda la respuesta de la IA en la caché para futuras consultas idénticas."""
        input_hash = self._calculate_input_hash(prompt, input_data)
        cache_data = self._get_cache()
        
        cache_data[input_hash] = response
        self._save_cache(cache_data)

    def get_cache_stats(self) -> Dict[str, int]:
        """Devuelve estadísticas de eficiencia (cuántas llamadas se ahorraron)."""
        cache_data = self._get_cache()
        return {
            "total_cached_responses": len(cache_data),
            "estimated_tokens_saved": len(cache_data) * 500  # Estimación conservadora por respuesta
        }
