#!/bin/bash

time (
	set -euo pipefail

	FRIDA_ROOT=$(pwd)/openai-chat-gpt

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
		FRIDA_PYENV=$BIN/pyenv
		FRIDA_PYTHON=$BIN/python
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

		cat > $FRIDA_PYENV <<-END
			#!/bin/bash
			set -euo pipefail
			source $ACTIVATE
			echo "# Using python from \$VIRTUAL_ENV"
			echo "# running: \$@"
			exec \$@
		END
		cat > $FRIDA_PYTHON <<-END
			#!/bin/bash
			set -euo pipefail
			exec $FRIDA_PYENV python \$@
		END
		chmod -v +x $FRIDA_PYENV $FRIDA_PYTHON
		echo @@ FRIDA PYTHON
		cat $FRIDA_PYTHON
		echo @@ FRIDA PYENV
		cat $FRIDA_PYENV
	}
	make_pyenv $FRIDA_ROOT python "PyQt6 PyQt6-NetworkAuth PyQt6-WebEngine"

	true
)
# CudaText: lexer_file="Bash script"; tab_size=2; tab_spaces=Yes; newline=LF;
