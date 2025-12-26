"""Image Generation component (Langflow/LFX minimal stub).

This repository only contains the image_generation component package, not the full
Langflow/LFX runtime. To keep the code importable in isolation, this component
tries to import real LFX base classes if they exist, and otherwise falls back to
lightweight local stubs.

When you drop this folder into a real Langflow install, the real imports will be
used and the node will show up in the palette (assuming Langflow's component
discovery scans this package).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .provider_registry import PROVIDERS, get_provider


# --- Optional LFX imports (preferred) ---------------------------------------
try:
    from lfx.components.base import Component  # type: ignore
    from lfx.components.inputs import DropdownInput, TextInput, IntInput  # type: ignore
    from lfx.types import Data, Output  # type: ignore
except Exception:  # pragma: no cover

    class Component:  # minimal stub
        pass

    @dataclass
    class Data:  # minimal stub
        data: Any

    @dataclass
    class Output:  # minimal stub
        display_name: str
        name: str
        method: str

    @dataclass
    class _BaseInput:  # minimal stub
        name: str
        display_name: str
        required: bool = False

    @dataclass
    class DropdownInput(_BaseInput):
        options: List[str] = None  # type: ignore
        default: Optional[str] = None

    @dataclass
    class TextInput(_BaseInput):
        multiline: bool = False

    @dataclass
    class IntInput(_BaseInput):
        default: int = 1
        min: Optional[int] = None
        max: Optional[int] = None


class ImageGenerationComponent(Component):
    """Image Generation node supporting multiple providers via a registry."""

    display_name = "Image Generation"
    description = "Generate images using OpenAI or FLUX-based models."
    icon = "Image"

    inputs = [
        DropdownInput(
            name="model",
            display_name="Model",
            options=list(PROVIDERS.keys()),
            default="openai:gpt-image-1",
        ),
        TextInput(
            name="prompt",
            display_name="Prompt",
            required=True,
            multiline=True,
        ),
        IntInput(
            name="num_images",
            display_name="Number of Images",
            default=1,
            min=1,
            max=4,
        ),
    ]

    outputs = [
        Output(
            display_name="Images",
            name="images",
            method="generate",
        )
    ]

    # Real LFX will set these attributes based on inputs.
    model: str
    prompt: str
    num_images: int

    def generate(self) -> Data:
        provider = get_provider(self.model)

        result: Dict[str, Any] = provider.generate(
            prompt=self.prompt,
            num_images=self.num_images,
        )

        return Data(data=result)
