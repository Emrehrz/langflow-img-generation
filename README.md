# Langflow / LFX Image Generation Component (Standalone)

## What This Is

This repository contains a standalone **Image Generation** component designed for **Langflow/LFX**.

Since no reference implementation or full Langflow repo was provided, **reasonable assumptions** were made based on the challenge description and typical Langflow component conventions.

## Design Decisions

- **Providers are resolved via a lazy factory-based registry** to avoid import-time failures when environment variables (like API keys) are missing.
- **Provider-specific logic is isolated** inside `providers/` to make it easy to add new providers without touching component code.
- **Output is normalized** to a single schema so the UI can remain provider-agnostic.
- **Minimal validation** is enforced at the provider level (e.g., prompt must be non-empty).

## Environment Variables

- `OPENAI_API_KEY` (required to instantiate the OpenAI provider)
- `FLUX_API_KEY` (not yet enabled; future work)

## How to Add a New Provider

1. Create a provider class in `src/lfx/src/lfx/components/image_generation/providers/`.
2. Implement `generate(prompt: str, **kwargs) -> dict` and return a **normalized** response:

   - `images`: list of url/base64 image payloads
   - `provider`: provider id string
   - `raw`: provider-native response or metadata
   - `content_type`: `"url"` or `"base64"`

3. Register the provider via a **factory** in `PROVIDERS` inside `provider_registry.py`.
4. Ensure the `model` dropdown options include the provider key (this happens automatically since `component.py` uses `list(PROVIDERS.keys())`).

## Limitations / Next Steps

- **FLUX provider is stubbed** but not enabled.
- **No real Langflow palette verification** was possible in this repository because the full Langflow/LFX runtime and component discovery system were not provided.
- Advanced image parameters (negative prompt / seed / guidance / size choices) are intentionally omitted for clarity at this stage.

### Palette visibility note (important)

Palette visibility could not be verified in this repository because the full Langflow/LFX runtime and component discovery system were not provided.
However, the component follows Langflow’s documented conventions:

- exported via `__init__.py`
- uses `Component`, `Input`, and `Output` contracts (with safe local fallbacks)
- resolves providers dynamically via a registry

## Running tests

```bash
pip install -r requirements.txt
pytest
```