# Ollama Setup

## Install (Windows PowerShell)

```powershell
irm https://ollama.com/install.ps1 | iex
```

## Pull Models

```bash
ollama pull llama3.2:1b
ollama pull gemma3:4b
ollama pull qwen3:8b
ollama pull ministral-3:8b
ollama pull embeddinggemma
```

## Manage Models

```bash
ollama ls                  # list downloaded models
ollama run <model_name>    # run a model interactively
ollama rm <model_name>     # remove a model
ollama show <model_name>   # show model details
```

## Notes

- `ollama serve` runs in the background automatically after install; API available at `http://localhost:11434`.
- macOS/Linux install: `curl -fsSL https://ollama.com/install.sh | sh`