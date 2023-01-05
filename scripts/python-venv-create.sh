#!/usr/bin/bash

time (
	set -euo pipefail

	CHAT_GPT_ROOT=$(pwd)/openai-chat-gpt.venv

	function make_pyenv () {
		PACKAGES='pip wheel '
		ROOT=$1
		PYTHON=$2

		PACKAGES+=${3:-}

		BIN=$ROOT/bin
		VENV=$ROOT/venv
		VBIN=$VENV/bin
		PROMPT='python-venv'
		ACTIVATE=$VBIN/activate
		CHAT_GPT_PYENV=$BIN/pyenv
		CHAT_GPT_PYTHON=$BIN/python
		VENV_ARGS="--system-site-packages --symlinks --clear --prompt $PROMPT"

		rm -rf $ROOT
		mkdir -pv $BIN

		$PYTHON -m venv $VENV_ARGS $VENV

		source $ACTIVATE
		which python
		which pip
		for pkg in $PACKAGES; do
			pip install --upgrade $pkg
		done
		deactivate

		cat > $CHAT_GPT_PYENV <<-END
			#!/bin/bash
			set -euo pipefail
			source $ACTIVATE
			echo "# Using python from \$VIRTUAL_ENV"
			echo "# running: \$@"
			exec \$@
		END
		cat > $CHAT_GPT_PYTHON <<-END
			#!/bin/bash
			set -euo pipefail
			exec $CHAT_GPT_PYENV python \$@
		END
		chmod -v +x $CHAT_GPT_PYENV $CHAT_GPT_PYTHON
		echo @@ CHAT_GPT PYTHON
		cat $CHAT_GPT_PYTHON
		echo @@ CHAT_GPT PYENV
		cat $CHAT_GPT_PYENV
	}
	make_pyenv $CHAT_GPT_ROOT python3 "PyQt6 PyQt6-NetworkAuth PyQt6-WebEngine pyqtdarktheme"

	true
)
# CudaText: lexer_file="Bash script"; tab_size=2; tab_spaces=Yes; newline=LF;
