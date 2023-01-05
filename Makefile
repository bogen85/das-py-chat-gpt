# We are not using any builtins
MAKEFLAGS:= \
	--warn-undefined-variables \
	--no-builtin-rules \
	--no-builtin-variables \
	--silent

.ONESHELL:

SHELL := /usr/bin/bash
PROJECT_ROOT := $(PWD)
_ = echo "[$@]"; set -euo pipefail

default:; $_

TMP := $(PROJECT_ROOT)/.tmp
tmp_cache := $(TMP)/cache
SCRIPTS := $(PROJECT_ROOT)/scripts
INSTANTFPCCACHE := $(tmp_cache)/instantfpc
instantfpc := $(shell which instantfpc)

dot_vars := $(instantfpc) $(SCRIPTS)/dot_vars.pas

VENV := openai-chat-gpt.venv
VENV_PYTHON := $(VENV)/bin/python

project_vars := \
	SHELL PROJECT_ROOT SCRIPTS INSTANTFPCCACHE TMP tmp_cache instantfpc dot_vars VENV VENV_PYTHON


export $(project_vars)

.vars:; $_; $(dot_vars) $(project_vars)

clean:
	$_
	rm -rvf .tmp/*
	rm -rf */__pycache__

clean-all: clean
	$_
	rm -rf $(VENV)

$(VENV_PYTHON):
	$_
	$(SCRIPTS)/python-venv-create.sh

run: $(VENV_PYTHON)
	$_
	$(VENV_PYTHON)  $(PROJECT_ROOT)/ChatGPT/main.py

# CudaText: lexer_file=Makefile; tab_size=2; tab_spaces=No; newline=LF;
