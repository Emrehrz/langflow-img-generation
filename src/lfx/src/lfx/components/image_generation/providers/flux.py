from typing import Dict, Any


class FluxImageProvider:
    """Stub FLUX provider. Will be implemented in a later step."""

    name = "flux:flux-schnell"

    def __init__(self) -> None:
        # Intentionally empty for now.
        # Later we may require REPLICATE_API_TOKEN or FAL_KEY etc.
        pass

    def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError(
            "FluxImageProvider is a stub. Implement hosted API call in a later step."
        )
