#!/usr/bin/env bash
# Instala tudo que o sistema de estudos precisa. Roda 1x.
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "==> 1/3  Instalando ffmpeg (precisa de sudo)…"
if ! command -v ffmpeg >/dev/null 2>&1; then
  sudo apt-get update && sudo apt-get install -y ffmpeg
else
  echo "    ffmpeg já instalado ✓"
fi

echo "==> 2/3  Criando ambiente virtual Python (.venv)…"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

echo "==> 3/3  Instalando dependências Python…"
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Pronto! Para usar, ative o ambiente e rode o estudo.py:"
echo "     cd \"$DIR\""
echo "     source .venv/bin/activate"
echo "     python estudo.py listar"
echo ""
echo "   (dica: o comando 'estudar' no README facilita isso)"
