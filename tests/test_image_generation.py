import pytest


def test_openai_provider_normalized_output(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    from lfx.components.image_generation.providers.openai import OpenAIImageProvider

    provider = OpenAIImageProvider()
    result = provider.generate(prompt="a cat", num_images=2)

    assert "images" in result
    assert len(result["images"]) == 2
    assert result["provider"] == "openai:gpt-image-1"
    assert result["content_type"] == "url"


def test_get_provider_returns_openai(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    from lfx.components.image_generation.provider_registry import get_provider

    provider = get_provider("openai:gpt-image-1")
    assert provider.name == "openai:gpt-image-1"


def test_openai_provider_empty_prompt(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    from lfx.components.image_generation.providers.openai import OpenAIImageProvider

    provider = OpenAIImageProvider()

    with pytest.raises(ValueError):
        provider.generate(prompt="")
