import os
from typing import Dict, Any, List


class OpenAIImageProvider:
    """OpenAI image generation provider using gpt-image-1."""

    name = "openai:gpt-image-1"

    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. "
                "Please configure it as an environment variable."
            )

    def generate(
        self,
        prompt: str,
        num_images: int = 1,
        size: str = "1024x1024",
        **kwargs,
    ) -> Dict[str, Any]:
        """Generate images via OpenAI Images API.

        NOTE:
        - This method intentionally keeps the surface small.
        - Advanced parameters (seed, guidance, etc.) can be added later.
        """

        if not prompt or not prompt.strip():
            raise ValueError("Prompt must be a non-empty string.")

        # --- PLACEHOLDER IMPLEMENTATION ---
        # We are intentionally not calling the real API yet.
        # This allows:
        # - fast iteration
        # - testability
        # - clear separation of concerns

        fake_images: List[str] = [
            f"https://example.com/fake-image-{i}.png" for i in range(num_images)
        ]

        return {
            "images": fake_images,
            "provider": self.name,
            "raw": {
                "prompt": prompt,
                "size": size,
                "num_images": num_images,
                "note": "Stubbed OpenAI response",
            },
            "content_type": "url",
        }
