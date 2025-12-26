from typing import Protocol, Dict, Any, Callable

from .providers.openai import OpenAIImageProvider
# from .providers.flux import FluxImageProvider  # sonra eklenecek


class ImageProvider(Protocol):
    """Contract for all image generation providers.

    Each provider must:
    - expose a unique `name`
    - implement `generate`
    - return a normalized response dict
    """

    name: str

    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Generate image(s) from a prompt.

        Must return a normalized dict with at least:
        {
            "images": [...],
            "provider": str,
            "raw": dict,
            "content_type": "url" | "base64"
        }
        """


ProviderFactory = Callable[[], ImageProvider]


def _openai_provider() -> ImageProvider:
    return OpenAIImageProvider()


# Registry is intentionally simple.
# Adding a new provider should be a one-line change here.
# Note: We register factories (lazy init) to avoid import-time failures when
# provider-specific environment variables (e.g. OPENAI_API_KEY) aren't set.
PROVIDERS: Dict[str, ProviderFactory] = {
    "openai:gpt-image-1": _openai_provider,
    # "flux:flux-schnell": lambda: FluxImageProvider(),
}


def get_provider(name: str) -> ImageProvider:
    """Return a provider instance by registry name."""

    try:
        factory = PROVIDERS[name]
    except KeyError as exc:
        raise KeyError(f"Unknown image provider: {name}") from exc
    return factory()
